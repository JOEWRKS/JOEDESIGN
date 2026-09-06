# Operations Status Console — Visual Direction

Status: APPROVED
Revision: 1

## Direction

Quiet operational clarity. Use a warm neutral canvas, one compact summary band, and three directly scannable status rows. The action area should feel decisive without making the status rows decorative cards.

## Approved semantic values

- `surface.page`: `#F6F7F4`
- `surface.panel`: `#FFFFFF`
- `text.primary`: `#1E2520`
- `text.muted`: `#66706A`
- `border.subtle`: `#D7DDD8`
- `action.primary`: `#205C4A`
- `status.healthy`: `#207A55`
- `status.monitoring`: `#8A6418`
- `status.attention`: `#A33A32`
- `space.section`: `32px`
- `radius.panel`: `18px`

`status.attention.icon` is intentionally unspecified. Do not invent or infer an icon token.

## Existing-role intent

Map these semantic roles onto equivalent healthy project-native roles when they already exist. The project does not need token renames merely to copy the names above.

## Visual Flow

The eye should move from heading and summary to the ordered status rows, then to the primary action and secondary detail link. Status meaning must remain available in text and not rely on color alone.

## Bridge Rationale

The green action value is exact authority, not permission to rename the project's established `--commit-action` role. The intentionally missing icon value stays unresolved because text, dot, and border treatments already preserve the Product status meaning.

## Responsive intent

On desktop, keep heading context and the compact summary band visually paired while status rows use the available width. On mobile, stack the header context, keep all three rows in order, and make the primary action comfortably reachable. This relationship remains prose; do not force it into a token schema.

## Approved Visual Evidence

Smoke F requires actual browser observation at desktop `1440×1000` and mobile `390×844`. Approval of this direction is not User Acceptance of a produced render.

## Open Visual Decisions

- `status.attention.icon`: unresolved by design; no value is approved in Revision 1.

