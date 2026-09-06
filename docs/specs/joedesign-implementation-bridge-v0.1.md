# JOEDESIGN Implementation Bridge v0.1

**Status:** CANONICAL BRIDGE CONTRACT — IMPLEMENTATION CANDIDATE BASELINE  
**Scope:** approved visual truth → implementation mapping  
**Dependency policy:** no required Google design.md runtime, parser, CLI, vendor package, or external design engine

---

## 1. Purpose

The Implementation Bridge reduces loss between an approved visual decision and the code that implements it.

It does not create visual authority.

```text
APPROVED Project DESIGN.md
        ↓
Implementation Bridge
        ↓
Project-native tokens / components / styles
        ↓
Actual runtime
        ↓
Visual verification
```

The Bridge answers:

- Which approved visual values are exact enough to implement?
- Which project-native token or component role should receive them?
- Which values remain unresolved?
- What materially changed in the implementation mapping?
- Has the actual rendered result been observed?

---

## 2. Authority

Authority order does not change.

```text
Product Truth
→ APPROVED Project DESIGN.md
→ JOEDESIGN Craft Core
→ Selected Project References
→ JOE Default Taste
```

Implementation mappings are derivative artifacts. They cannot amend Product Truth or Project `DESIGN.md`.

A token existing in code does not make it approved visual truth.

A token exporter, linter, design-system file, or external schema does not become design authority merely because it is machine-readable.

---

## 3. Exact values vs intent

The Bridge separates two kinds of design information.

### Exact implementation values

Examples:

- approved color values;
- approved typography roles and exact properties;
- approved spacing roles;
- approved radius roles;
- approved component visual tokens.

These may be mapped into implementation tokens.

### Intent / rationale

Examples:

- visual hierarchy;
- visual flow;
- brand character;
- imagery ownership;
- responsive composition intent;
- anti-patterns.

These guide implementation and verification but are not converted into invented numeric tokens.

Do not manufacture exact values merely to make the implementation schema complete.

---

## 4. Unknown remains unresolved

If Project `DESIGN.md` does not contain an exact implementation value and current approved evidence does not prove one, the Bridge must preserve that absence.

```text
UNKNOWN
≠ infer a plausible value
≠ copy a reference value
≠ promote current code to authority
```

If implementation requires a new material visual value, JOEDESIGN must make a project-specific design decision and prove it before treating it as durable approved truth.

Local reversible implementation details that do not create material visual truth may remain implementation-level decisions.

---

## 5. Project-native mapping first

Do not replace an existing healthy project token system merely to match an external schema.

Preferred mapping order:

```text
approved semantic design role
→ existing equivalent project-native token/component role
→ new project-native semantic role only when required
→ raw local value only when truly local and justified
```

Equivalent existing roles should be reused.

Do not rename stable project tokens solely to match Google design.md naming examples, Tailwind defaults, or another reference system.

---

## 6. Structured token interoperability

Google `design.md` is an interoperability reference, not a JOEDESIGN dependency.

When a Project `DESIGN.md` already contains compatible structured YAML frontmatter, JOEDESIGN may consume exact values from compatible groups such as:

```text
colors
typography
spacing
rounded
components
```

Token values are implementation facts only when they are sourced from current approved project authority.

JOEDESIGN may also produce a compatible structured representation when a project explicitly benefits from machine-readable interchange.

Do not require all JOEDESIGN projects to adopt the Google schema.

Do not require the `@google/design.md` package, CLI, parser, or network service.

---

## 7. Preserve JOEDESIGN-specific content

Interoperability must not delete or downgrade JOEDESIGN-specific sections such as:

- Product Authority Pointer;
- Visual North Star;
- Visual Flow;
- Responsive Translation;
- Approved Visual Evidence;
- Open Visual Decisions;
- Reference Relationships.

Unknown/custom Markdown sections are preserved when translating or reviewing a structured DESIGN.md representation.

Machine compatibility must not erase human/agent design rationale.

---

## 8. Lint concept

A material bridge review should detect, when applicable:

- unresolved token references;
- duplicate semantic roles with conflicting values;
- mapped values that contradict approved Project `DESIGN.md`;
- unsupported or unexplained one-off values;
- implementation tokens that silently diverged from approved roles.

This is a behavioral contract in v0.1, not a required standalone CLI.

---

## 9. Diff concept

When implementation mappings change materially, compare the semantic role mapping rather than only raw file bytes.

Useful material diff fields include:

```text
role
before value / mapping
after value / mapping
source authority
reason
scope
```

A change in token naming without visual meaning may be implementation-only.

A change in approved visual value is a design-authority concern and must follow the applicable DESIGN.md revision/approval process.

---

## 10. Export concept

Approved structured tokens may be translated into project-native implementation forms such as:

- CSS custom properties;
- Tailwind theme values;
- DTCG-compatible token data;
- framework-specific theme objects.

An export is not automatically correct because it serialized successfully.

Do not claim format conformance without validating the produced format.

The Bridge does not require a universal exporter in v0.1.

---

## 11. Responsive boundary

Current external token schemas may not fully express JOEDESIGN responsive visual truth.

Do not force responsive hierarchy, composition, crop, information order, or interaction expression into unsupported token shapes.

Keep responsive intent in Project `DESIGN.md` prose/roles when structured representation would lose meaning.

Implementation agents translate responsive intent into project-native code and JOEDESIGN verifies the actual target render.

---

## 12. Verification boundary

Successful mapping does not prove the design.

```text
Token Mapping PASS
≠ Technical PASS
≠ Visual Conformance PASS
≠ User Acceptance
```

After material implementation:

```text
approved intent / exact values
→ mapped implementation
→ actual runtime
→ observed result
→ PASS / FAIL / UNVERIFIED
```

Visual PASS still requires actual rendered observation.

---

## 13. Ceremony boundary

Do not create a bridge manifest, lint report, or token diff for every tiny visual edit.

Use bounded bridge evidence when:

- a durable token system is being introduced or materially changed;
- an approved design system is being handed to another implementation agent;
- cross-tool interchange is material;
- token drift or authority conflict is suspected;
- a mapping change must be reviewed independently.

Small local refinements may map directly into existing project roles and proceed to actual rendered verification.

---

## 14. Non-goals

v0.1 does not include:

- Google design.md as a required runtime dependency;
- a YAML parser;
- a universal token CLI;
- a design-token database;
- Figma variable synchronization;
- automatic code generation from every DESIGN.md field;
- automatic mutation of approved DESIGN.md;
- a new public skill or command;
- replacement of existing project token systems;
- automatic visual PASS from lint/export success.

---

## 15. Canonical rule

> **The JOEDESIGN Implementation Bridge translates approved visual truth into project-native implementation roles without creating new authority. Exact approved values may be mapped; unknown values remain unresolved. Existing project token architecture is preferred over forced external naming. Structured DESIGN.md tokens may interoperate with compatible Google design.md concepts, but external schemas and tools remain optional. Custom JOEDESIGN rationale and responsive intent must be preserved. Token mapping, linting, diffing, or export success never replaces actual rendered visual verification or user acceptance.**
