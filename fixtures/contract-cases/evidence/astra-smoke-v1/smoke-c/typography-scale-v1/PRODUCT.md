# Waypoint Product Authority
Status: APPROVED. Revision: 1.

Waypoint is a read-only team briefing for a community workshop coordinator. The page helps the coordinator review preparation first, then the handover plan. It is not a ticketing system and has no editing or completion controls.

The only state in scope is the populated static briefing. Brand: Waypoint. Page title: A shared plan for workshop day. Supporting sentence: Prepare the room, welcome the group, and leave a clear handover.
Primary action: Review handover. It navigates within this page to #handover, never creating or changing a record.

Locked semantic structure and copy:

- SECTION A: Preparation. Section purpose: Everything the team needs before doors open.
  - MAJOR GROUP A1: People and materials. Purpose: Brief the hosts and prepare the shared resources.
    - SUBGROUP A1-a: Host briefings. Purpose: Two briefings, one consistent welcome.
      - ITEM GROUP A1-a-1: Welcome desk. Description: Greet participants and explain the room layout. Owner: Maya. Time: 09:00.
      - ITEM GROUP A1-a-2: Room host. Description: Introduce the session and show the shared materials. Owner: Theo. Time: 09:15.
    - SUBGROUP A1-b: Shared resources. Purpose: Keep the two reference packs within reach.
      - ITEM GROUP A1-b-1: Participant pack. Description: Agenda, room map, and printed exercises. Owner: Inez. Time: 08:45.
      - ITEM GROUP A1-b-2: Facilitator pack. Description: Session notes and discussion prompts. Owner: Jules. Time: 08:45.
  - MAJOR GROUP A2: Room readiness. Purpose: Check the space before the first arrival.
    - SUBGROUP A2-a: Opening checks. Purpose: Confirm the two physical essentials.
      - ITEM GROUP A2-a-1: Seating plan. Description: Arrange the chairs around the shared tables. Owner: Noor. Time: 08:30.
      - ITEM GROUP A2-a-2: Materials table. Description: Place the reference packs near the entrance. Owner: Eli. Time: 08:40.
- SECTION B: Handover. Section purpose: Leave the next team with useful context.
  - MAJOR GROUP B1: Follow-up and ownership. Purpose: Keep the recap and open questions distinct.
    - SUBGROUP B1-a: Team handover. Purpose: Two records for a clear next step.
      - ITEM GROUP B1-a-1: Session recap. Description: Summarize the topics discussed during the workshop. Owner: Maya. Time: 16:00.
      - ITEM GROUP B1-a-2: Open questions. Description: List the questions that need a later response. Owner: Theo. Time: 16:15.
    - SUBGROUP B1-b: Resource return. Purpose: Make the reference packs available again.
      - ITEM GROUP B1-b-1: Printed packs. Description: Return reusable pages to the shared shelf. Owner: Inez. Time: 16:30.
      - ITEM GROUP B1-b-2: Room notes. Description: Leave the room arrangement note for the next host. Owner: Jules. Time: 16:30.

The A1-a and B1-a item-group sibling relationships have the same meaning even where implementation wrappers differ. Owner labels and values, and time labels and values, are tightly bound local information, not additional structural groups.
All group titles, descriptions, owner/time pairs, and the anchor action must remain available and in the same semantic order at both viewports. Footer: Local briefing · Example content.
No new roles, routes, status meanings, tasks, state transitions, features, policies, or integrations are authorized. Visual presentation and spatial refinement may change without changing these facts.
