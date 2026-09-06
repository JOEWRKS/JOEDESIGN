# before: computed contrast

Actual Chrome computed colors; transparent ancestors composited to the opaque canvas. No gradients or images. Ratios use unrounded luminance; shown to 2 decimals.

sRGB c = channel / 255; linear = c / 12.92 when c ≤ 0.04045, otherwise ((c + 0.055) / 1.055)^2.4. L = 0.2126 R + 0.7152 G + 0.0722 B. Contrast = (Llighter + 0.05) / (Ldarker + 0.05).

Normal text ≥ 4.5:1; text ≥ 24px or bold ≥ 18.6667px ≥ 3:1. Meaningful action boundary / focus / supplemental priority rail evaluated at ≥ 3:1. Hidden content cannot pass visibility through a ratio. Decorative separators are not state or control boundaries.

## desktop: 1440×1000

Document: 1440×1000; horizontal overflow: false.

| Element / state / property | Foreground | Actual background | Ratio | Minimum | Result |
| --- | --- | --- | ---: | ---: | --- |
| .eyebrow / base / color | #19ad57 | #fafbfe | 2.84 | 4.5 | FAIL |
| h1 / base / color | #d400b8 | #fafbfe | 4.52 | 3 | PASS |
| .lead / base / color | #a8adbb | #fafbfe | 2.17 | 4.5 | FAIL |
| .primary-action / base / color | #ffffff | #19bdd5 | 2.26 | 4.5 | FAIL |
| h2 / base / color | #593de0 | #edf7ef | 6.04 | 3 | PASS |
| .count / base / color | #e69131 | #edf7ef | 2.26 | 4.5 | FAIL |
| footer / base / color | #adb1bc | #fafbfe | 2.07 | 4.5 | FAIL |
| .priority-label / base / color | #30334a | #fff0f8 | 11.23 | 4.5 | HIDDEN |
| #review-r-01 .record-id / base / color | #9a78d6 | #eff5ff | 3.18 | 4.5 | FAIL |
| #review-r-01 h3 / base / color | #43356c | #eff5ff | 9.76 | 3 | PASS |
| #review-r-01 .description / base / color | #a5a9b5 | #eff5ff | 2.14 | 4.5 | FAIL |
| #review-r-01 .source / base / color | #e88d25 | #eff5ff | 2.32 | 4.5 | FAIL |
| #review-r-01 time / base / color | #e88d25 | #eff5ff | 2.32 | 4.5 | FAIL |
| #review-r-01 .status / base / color | #12834d | #d1f4df | 4.05 | 4.5 | FAIL |
| #review-r-02 .record-id / base / color | #9a78d6 | #fff0f8 | 3.16 | 4.5 | FAIL |
| #review-r-02 h3 / base / color | #43356c | #fff0f8 | 9.71 | 3 | PASS |
| #review-r-02 .description / base / color | #a5a9b5 | #fff0f8 | 2.13 | 4.5 | FAIL |
| #review-r-02 .source / base / color | #e88d25 | #fff0f8 | 2.31 | 4.5 | FAIL |
| #review-r-02 time / base / color | #e88d25 | #fff0f8 | 2.31 | 4.5 | FAIL |
| #review-r-02 .status / base / color | #d89e22 | #fff0be | 2.09 | 4.5 | FAIL |
| #review-r-03 .record-id / base / color | #9a78d6 | #e8faf5 | 3.22 | 4.5 | FAIL |
| #review-r-03 h3 / base / color | #43356c | #e8faf5 | 9.89 | 3 | PASS |
| #review-r-03 .description / base / color | #a5a9b5 | #e8faf5 | 2.17 | 4.5 | FAIL |
| #review-r-03 .source / base / color | #e88d25 | #e8faf5 | 2.35 | 4.5 | FAIL |
| #review-r-03 time / base / color | #e88d25 | #e8faf5 | 2.35 | 4.5 | FAIL |
| #review-r-03 .status / base / color | #ec6666 | #ffdcdc | 2.48 | 4.5 | FAIL |
| .primary-action / base boundary / backgroundColor | #19bdd5 | #fafbfe | 2.19 | 3 | FAIL |
| .primary-action / base outer boundary / borderTopColor | #14bba5 | #fafbfe | 2.34 | 3 | FAIL |
| #review-r-02 / priority rail (supplemental) / borderLeftColor | #f24d94 | #edf7ef | 3.06 | 3 | PASS |
| #review-r-02 / priority rail / inner surface / borderLeftColor | #f24d94 | #fff0f8 | 3.04 | 3 | PASS |
| .primary-action / hover / color | #ffffff | #f6a229 | 2.08 | 4.5 | FAIL |
| .primary-action / hover boundary / backgroundColor | #f6a229 | #fafbfe | 2.01 | 3 | FAIL |
| .primary-action / hover outer boundary / borderTopColor | #14bba5 | #fafbfe | 2.34 | 3 | FAIL |
| .primary-action / keyboard focus / outlineColor | #a2c9ef | #fafbfe | 1.67 | 3 | FAIL |
| #review-r-02 / anchor target focus / outlineColor | #a2c9ef | #edf7ef | 1.58 | 3 | FAIL |

## mobile: 390×844

Document: 390×985; horizontal overflow: false.

| Element / state / property | Foreground | Actual background | Ratio | Minimum | Result |
| --- | --- | --- | ---: | ---: | --- |
| .eyebrow / base / color | #19ad57 | #e3eaf4 | 2.42 | 4.5 | FAIL |
| h1 / base / color | #d400b8 | #e3eaf4 | 3.86 | 3 | PASS |
| .lead / base / color | #a8adbb | #e3eaf4 | 1.85 | 4.5 | FAIL |
| .primary-action / base / color | #ffffff | #19bdd5 | 2.26 | 4.5 | FAIL |
| h2 / base / color | #593de0 | #dce4ef | 5.17 | 4.5 | PASS |
| .count / base / color | #e69131 | #dce4ef | 1.94 | 4.5 | FAIL |
| footer / base / color | #adb1bc | #e3eaf4 | 1.77 | 4.5 | FAIL |
| .priority-label / base / color | #30334a | #fff0f8 | 11.23 | 4.5 | HIDDEN |
| #review-r-01 .record-id / base / color | #9a78d6 | #eff5ff | 3.18 | 4.5 | FAIL |
| #review-r-01 h3 / base / color | #43356c | #eff5ff | 9.76 | 4.5 | PASS |
| #review-r-01 .description / base / color | #a5a9b5 | #eff5ff | 2.14 | 4.5 | FAIL |
| #review-r-01 .source / base / color | #e88d25 | #eff5ff | 2.32 | 4.5 | FAIL |
| #review-r-01 time / base / color | #e88d25 | #eff5ff | 2.32 | 4.5 | FAIL |
| #review-r-01 .status / base / color | #12834d | #d1f4df | 4.05 | 4.5 | FAIL |
| #review-r-02 .record-id / base / color | #9a78d6 | #fff0f8 | 3.16 | 4.5 | FAIL |
| #review-r-02 h3 / base / color | #43356c | #fff0f8 | 9.71 | 4.5 | PASS |
| #review-r-02 .description / base / color | #a5a9b5 | #fff0f8 | 2.13 | 4.5 | FAIL |
| #review-r-02 .source / base / color | #e88d25 | #fff0f8 | 2.31 | 4.5 | FAIL |
| #review-r-02 time / base / color | #e88d25 | #fff0f8 | 2.31 | 4.5 | FAIL |
| #review-r-02 .status / base / color | #d89e22 | #fff0be | 2.09 | 4.5 | FAIL |
| #review-r-03 .record-id / base / color | #9a78d6 | #e8faf5 | 3.22 | 4.5 | FAIL |
| #review-r-03 h3 / base / color | #43356c | #e8faf5 | 9.89 | 4.5 | PASS |
| #review-r-03 .description / base / color | #a5a9b5 | #e8faf5 | 2.17 | 4.5 | FAIL |
| #review-r-03 .source / base / color | #e88d25 | #e8faf5 | 2.35 | 4.5 | FAIL |
| #review-r-03 time / base / color | #e88d25 | #e8faf5 | 2.35 | 4.5 | FAIL |
| #review-r-03 .status / base / color | #ec6666 | #ffdcdc | 2.48 | 4.5 | FAIL |
| .primary-action / base boundary / backgroundColor | #19bdd5 | #e3eaf4 | 1.87 | 3 | FAIL |
| .primary-action / base outer boundary / borderTopColor | #14bba5 | #e3eaf4 | 2.00 | 3 | FAIL |
| #review-r-02 / priority rail (supplemental) / borderLeftColor | #f24d94 | #dce4ef | 2.62 | 3 | FAIL |
| #review-r-02 / priority rail / inner surface / borderLeftColor | #f24d94 | #fff0f8 | 3.04 | 3 | PASS |
| .primary-action / hover / color | #ffffff | #f6a229 | 2.08 | 4.5 | FAIL |
| .primary-action / hover boundary / backgroundColor | #f6a229 | #e3eaf4 | 1.71 | 3 | FAIL |
| .primary-action / hover outer boundary / borderTopColor | #14bba5 | #e3eaf4 | 2.00 | 3 | FAIL |
| .primary-action / keyboard focus / outlineColor | #a2c9ef | #e3eaf4 | 1.43 | 3 | FAIL |
| #review-r-02 / anchor target focus / outlineColor | #a2c9ef | #dce4ef | 1.35 | 3 | FAIL |

