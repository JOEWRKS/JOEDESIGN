# after: computed contrast

Actual Chrome computed colors; transparent ancestors composited to the opaque canvas. No gradients or images. Ratios use unrounded luminance; shown to 2 decimals.

sRGB c = channel / 255; linear = c / 12.92 when c ≤ 0.04045, otherwise ((c + 0.055) / 1.055)^2.4. L = 0.2126 R + 0.7152 G + 0.0722 B. Contrast = (Llighter + 0.05) / (Ldarker + 0.05).

Normal text ≥ 4.5:1; text ≥ 24px or bold ≥ 18.6667px ≥ 3:1. Meaningful action boundary / focus / supplemental priority rail evaluated at ≥ 3:1. Hidden content cannot pass visibility through a ratio. Decorative separators are not state or control boundaries.

## desktop: 1440×1000

Document: 1440×1000; horizontal overflow: false.

| Element / state / property | Foreground | Actual background | Ratio | Minimum | Result |
| --- | --- | --- | ---: | ---: | --- |
| .eyebrow / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| h1 / base / color | #30334a | #fafbfe | 11.95 | 3 | PASS |
| .lead / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| .primary-action / base / color | #ffffff | #285d8f | 6.88 | 4.5 | PASS |
| h2 / base / color | #30334a | #fafbfe | 11.95 | 3 | PASS |
| .count / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| footer / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| .priority-label / base / color | #285d8f | #fafbfe | 6.65 | 4.5 | PASS |
| #review-r-01 .record-id / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-01 h3 / base / color | #30334a | #fafbfe | 11.95 | 3 | PASS |
| #review-r-01 .description / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-01 .source / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-01 time / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-01 .status / base / color | #14633d | #d1f4df | 6.15 | 4.5 | PASS |
| #review-r-02 .record-id / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-02 h3 / base / color | #30334a | #fafbfe | 11.95 | 3 | PASS |
| #review-r-02 .description / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-02 .source / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-02 time / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-02 .status / base / color | #785514 | #fff0be | 5.94 | 4.5 | PASS |
| #review-r-03 .record-id / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-03 h3 / base / color | #30334a | #fafbfe | 11.95 | 3 | PASS |
| #review-r-03 .description / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-03 .source / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-03 time / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-03 .status / base / color | #a12f36 | #ffdcdc | 5.55 | 4.5 | PASS |
| .primary-action / base boundary / backgroundColor | #285d8f | #fafbfe | 6.65 | 3 | PASS |
| .primary-action / base outer boundary / borderTopColor | #285d8f | #fafbfe | 6.65 | 3 | PASS |
| #review-r-02 / priority rail (supplemental) / borderLeftColor | #285d8f | #fafbfe | 6.65 | 3 | PASS |
| #review-r-02 / priority rail / inner surface / borderLeftColor | #285d8f | #fafbfe | 6.65 | 3 | PASS |
| .primary-action / hover / color | #ffffff | #204b73 | 9.07 | 4.5 | PASS |
| .primary-action / hover boundary / backgroundColor | #204b73 | #fafbfe | 8.77 | 3 | PASS |
| .primary-action / hover outer boundary / borderTopColor | #204b73 | #fafbfe | 8.77 | 3 | PASS |
| .primary-action / keyboard focus / outlineColor | #174f7b | #fafbfe | 8.31 | 3 | PASS |
| #review-r-02 / anchor target focus / outlineColor | #174f7b | #fafbfe | 8.31 | 3 | PASS |

## mobile: 390×844

Document: 390×985; horizontal overflow: false.

| Element / state / property | Foreground | Actual background | Ratio | Minimum | Result |
| --- | --- | --- | ---: | ---: | --- |
| .eyebrow / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| h1 / base / color | #30334a | #fafbfe | 11.95 | 3 | PASS |
| .lead / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| .primary-action / base / color | #ffffff | #285d8f | 6.88 | 4.5 | PASS |
| h2 / base / color | #30334a | #fafbfe | 11.95 | 4.5 | PASS |
| .count / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| footer / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| .priority-label / base / color | #285d8f | #fafbfe | 6.65 | 4.5 | PASS |
| #review-r-01 .record-id / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-01 h3 / base / color | #30334a | #fafbfe | 11.95 | 4.5 | PASS |
| #review-r-01 .description / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-01 .source / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-01 time / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-01 .status / base / color | #14633d | #d1f4df | 6.15 | 4.5 | PASS |
| #review-r-02 .record-id / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-02 h3 / base / color | #30334a | #fafbfe | 11.95 | 4.5 | PASS |
| #review-r-02 .description / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-02 .source / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-02 time / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-02 .status / base / color | #785514 | #fff0be | 5.94 | 4.5 | PASS |
| #review-r-03 .record-id / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-03 h3 / base / color | #30334a | #fafbfe | 11.95 | 4.5 | PASS |
| #review-r-03 .description / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-03 .source / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-03 time / base / color | #586174 | #fafbfe | 6.01 | 4.5 | PASS |
| #review-r-03 .status / base / color | #a12f36 | #ffdcdc | 5.55 | 4.5 | PASS |
| .primary-action / base boundary / backgroundColor | #285d8f | #fafbfe | 6.65 | 3 | PASS |
| .primary-action / base outer boundary / borderTopColor | #285d8f | #fafbfe | 6.65 | 3 | PASS |
| #review-r-02 / priority rail (supplemental) / borderLeftColor | #285d8f | #fafbfe | 6.65 | 3 | PASS |
| #review-r-02 / priority rail / inner surface / borderLeftColor | #285d8f | #fafbfe | 6.65 | 3 | PASS |
| .primary-action / hover / color | #ffffff | #204b73 | 9.07 | 4.5 | PASS |
| .primary-action / hover boundary / backgroundColor | #204b73 | #fafbfe | 8.77 | 3 | PASS |
| .primary-action / hover outer boundary / borderTopColor | #204b73 | #fafbfe | 8.77 | 3 | PASS |
| .primary-action / keyboard focus / outlineColor | #174f7b | #fafbfe | 8.31 | 3 | PASS |
| #review-r-02 / anchor target focus / outlineColor | #174f7b | #fafbfe | 8.31 | 3 | PASS |

