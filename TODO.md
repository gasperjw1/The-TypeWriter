# The Scriptwriter — Feature Roadmap

Based on comparison with WriterDuet, Arc Studio Pro, and WriterSolo (Session 1, 2026-04-30).

## Unique Strengths (keep and refine)

- **Direction cues** — Chip-based UI for tracking character entrances/exits per scene. No competitor does this natively.
- **Drag-and-drop validation** — Reordering lines validates against character presence state, preventing invalid cue sequences.
- **Character archiving** — Characters can be archived without deletion, preserving their lines and stats.

## Feature Gaps

### Completed

- [x] **Inline editing** — Edit any line in place (double-click or Edit button). Dialogue shows character dropdown, action, and text fields. Direction routes to the full cue modal. *(Session 1)*
- [x] **Undo/Redo** — 50-entry cursor-based undo stack with Redo button and Ctrl+Z / Ctrl+Shift+Z shortcuts. *(Session 1)*
- [x] **PDF export** — Generates formatted screenplay PDF with title page, character list, table of contents, and script pages. *(Pre-existing in setup_fix)*
- [x] **Auto-numbered acts and scenes** — "Act One", "Scene Three" with optional user names after an em dash. *(Session 3)*
- [x] **Standalone character creation** — "+ New character" button in side panel, no dialogue line required. *(Session 3)*
- [x] **Find & replace** — Search across the entire script with line-type filter chips (Setting, Direction, Dialogue, Action). Replace individually or in bulk. Ctrl+F to open, Escape to close. *(Session 4)*
- [x] **Persistent save system** — localStorage auto-persistence + File System Access API for linking to a disk file that gets overwritten on each save. No more repeated downloads. *(Session 4)*

### To Do

- [ ] **FDX export** — Export to Final Draft (.fdx) format, the industry standard for screenplay interchange. WriterDuet, Arc Studio, and WriterSolo all support this.
- [ ] **Auto-formatting** — Automatic enforcement of screenplay conventions: auto-capitalize character names in dialogue headers, enforce slugline format (INT./EXT.), smart period/dash handling in settings.
- [ ] **Real-time collaboration** — Multiple users editing the same script simultaneously with cursor presence and conflict resolution. Core feature of WriterDuet.
- [ ] **Revision tracking / version history** — Save named versions, compare diffs between revisions, mark revised pages. Standard in professional screenwriting tools.
- [ ] **Beat board / index card view** — Visual outlining mode where acts and scenes appear as movable cards on a corkboard. Offered by Arc Studio and WriterSolo.
- [ ] **Notes and comments** — Attach notes or comments to specific lines, scenes, or acts for collaborative feedback or personal reminders.
- [ ] **Cloud sync / account-based storage** — Save scripts to a server with user accounts so work persists across devices. Currently localStorage + optional disk file via File System Access API.

## Other Improvements (identified during development)

- [ ] **Keyboard shortcuts reference** — An in-app help panel listing all keyboard shortcuts (pill selection, undo/redo, submit, etc.)
- [ ] **Multi-line setting support** — Allow Shift+Enter for multi-line setting/action text in the input bar (currently Enter always submits)
- [ ] **Scene reordering across acts** — Drag-and-drop currently only works within the same act for scenes. Cross-act scene moves would be useful.
- [ ] **Line moving across scenes** — Same limitation as above for individual lines.
- [ ] **Print-friendly View tab** — Add print CSS or a dedicated print button to the View tab for quick paper output without PDF export.
