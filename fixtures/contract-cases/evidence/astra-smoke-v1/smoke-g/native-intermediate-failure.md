# Preserved native intermediate failure

At 2026-09-06T11:07:40.726Z the single native Smoke G run issued one command that read `PRODUCT.md` and then attempted to read a literal `APPROVED DESIGN.md`. The second path did not exist, so that command exited 1 after successfully printing `PRODUCT.md`.

Bounded original error:

```text
Get-Content: Cannot find path 'D:\JOEWRKS\joedesign-color-contrast-validation-20260906\runs\G\workspace\APPROVED DESIGN.md' because it does not exist.
```

The fixture's actual approved authority is `DESIGN.md` (`Status: APPROVED`). The runtime subsequently read it, recorded this distinction in `role-map-before.md`, and did not modify either authority file. This preserved diagnostic is not a final gate failure.
