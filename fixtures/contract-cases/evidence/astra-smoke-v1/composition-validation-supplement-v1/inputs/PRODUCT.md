# Fieldlight Rentals — Product

Revision: 1 (fixed)

Purpose: compare three independent equipment rental options and choose one for a local preview. No checkout, payment, account, inventory update or reservation exists. No option is recommended over another.

Required visible page copy:
- Fieldlight Rentals
- Choose your field kit
- Compare day-hire equipment for a small recording session.
- One-day hire · Collection only
- Included equipment
- Availability
- Selection preview

| ID | Name | Price | Included equipment | Availability | Selection action |
| --- | --- | --- | --- | --- | --- |
| pocket | Pocket Audio Kit | $24 / day | Portable recorder; Lavalier microphone; Headphones | Available today | Choose Pocket Audio Kit |
| interview | Interview Kit | $42 / day | Two wireless microphones; Portable recorder; Table stands | Available today | Choose Interview Kit |
| room | Room Recording Kit | $58 / day | Stereo microphone pair; Audio interface; Monitor headphones | Available tomorrow | Choose Room Recording Kit |

Each item owns its name, price, three included-equipment facts, availability and selection action. Availability is informational; all three options may be selected for preview. Do not merge these distinct options or invent recommendation, stock counts, savings, ratings or urgency.

Initial local state: no selection; visible output is `No kit selected.` Each selection sets only the selected option ID in local page memory, makes exactly that action aria-pressed=true and the others false, and updates output to `<Name> selected. Local preview only — no reservation made.` Selecting another item replaces the previous selection. Reload resets to no selection. All three choices remain usable. No network request, persistent storage or external write is part of selection.

Keep all required copy, item fields, options and selection semantics. Markup and visual presentation may change within these meanings.
