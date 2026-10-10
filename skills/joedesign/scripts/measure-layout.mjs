// Executed in the actual browser after state assertions. Values are rendered box
// relationships, including the effects of margin, padding, gap and control height.
export async function measureLayout(page, checks) {
  return page.evaluate(checks => {
    const rect = el => {
      const r = el.getBoundingClientRect(), s = getComputedStyle(el);
      if (!r.width || !r.height || s.visibility === 'hidden' || s.display === 'none') throw Error('Unobserved/hidden element');
      return {top:r.top,bottom:r.bottom,left:r.left,right:r.right,width:r.width,height:r.height,
        margin:[s.marginTop,s.marginRight,s.marginBottom,s.marginLeft],
        padding:[s.paddingTop,s.paddingRight,s.paddingBottom,s.paddingLeft],gap:s.gap,lineHeight:s.lineHeight};
    };
    const select = (root, selector) => {
      const nodes = [...root.querySelectorAll(selector)];
      if (!nodes.length) throw Error('Selector has no matches: '+selector);
      return nodes;
    };
    return checks.filter(c=>c.method==='geometry').map(check=>{
      const row={check_id:check.check_id,criterion_sha256:check.criterion_sha256,values:[],boxes:[]};
      try {
        const c=check.criterion;
        if (c.kind==='pair') {
          const a=select(document,c.from), b=select(document,c.to);
          if(a.length!==b.length) throw Error('Unpaired selectors');
          if(!['top','bottom','left','right'].includes(c.from_edge)||!['top','bottom','left','right'].includes(c.to_edge)) throw Error('Invalid edge');
          for(let i=0;i<a.length;i++){const x=rect(a[i]),y=rect(b[i]);row.boxes.push([x,y]);row.values.push(y[c.to_edge]-x[c.from_edge]);}
        } else {
          for(const parent of select(document,c.container)) {
            const box=rect(parent), children=select(parent,c.items).map(rect);
            row.boxes.push({container:box,children});
            if(c.kind==='gap') {
              if(!['x','y'].includes(c.axis)||children.length<2) throw Error('Gap requires consecutive observed elements and axis');
              const start=c.axis==='y'?'top':'left',end=c.axis==='y'?'bottom':'right';
              for(let i=1;i<children.length;i++) row.values.push(children[i][start]-children[i-1][end]);
            } else if(c.kind==='inset') {
              if(!['top','bottom','left','right'].includes(c.edge)) throw Error('Invalid inset edge');
              const first=['top','left'].includes(c.edge);
              const edge=(first?Math.min:Math.max)(...children.map(r=>r[c.edge]));
              row.values.push(first?edge-box[c.edge]:box[c.edge]-edge);
            } else throw Error('Unsupported geometry');
          }
        }
      } catch(error){row.error=String(error);}
      return row;
    });
  }, checks);
}
