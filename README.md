# The TypeWriter

A free, open-source screenplay editor that runs entirely in your browser. No accounts, no installs, no cloud — just open the HTML file and start writing.

## What it does

The TypeWriter gives you a structured screenplay writing environment with an **Act > Scene > Line** hierarchy. You write using four line types — Setting, Direction, Dialogue, and Action — and the app handles formatting, numbering, and continuity for you.

Scripts are saved as lightweight JSON files on your machine. When you're ready to share, export to a properly formatted screenplay PDF with a title page, character list, and table of contents.

## Quick start

Open `script_maker_setup_fix.html` in any modern browser. That's it.

You can also try it live at the [GitHub Pages demo](https://yashmahtani.github.io/The-TypeWriter/) if one is configured via the `docs/` folder.

## Features

**Writing**
- Four line types with keyboard shortcuts (`` ` ``+1 through `` ` ``+4) and smart auto-advance between types
- Character management with autocomplete, ghost text, scene filtering, and archiving
- Direction cues that track character entrances and exits per scene with visual toggle chips
- Automatic `(cont.)` detection for consecutive dialogue from the same character
- Auto-numbered acts and scenes ("Act One", "Scene Three") with optional custom names

**Editing**
- Inline editing — double-click any line to edit in place, or use the Edit button
- Drag-and-drop reordering for acts, scenes, and lines with validation against character presence
- 50-level undo/redo (Ctrl+Z / Ctrl+Shift+Z) with full state snapshots
- Insert cursor — click a line to insert new content after it

**Organization**
- Collapsible side panel with table of contents and character list
- Summaries tab with script statistics
- Read-only View tab for distraction-free reading
- Settings tab for font size, indicator styles, and colors

**File handling**
- Save/load as JSON — your data stays on your machine
- Autosave after first manual save (toggleable)
- Visual save indicator (gray/orange/red/green) so you always know where you stand
- PDF export with professional screenplay formatting
- Unsaved-changes warning on page close

## Project structure

```
The-TypeWriter/
  script_maker_setup_fix.html   # The app (open this)
  docs/index.html               # GitHub Pages entry point
  TODO.md                       # Feature roadmap
  CLAUDE.md                     # Dev notes and project memory
  archive/                      # Older versions kept for reference
    script_maker.py             # Original Python CLI
    script_maker_ui.html        # First web UI
    script_maker_ui_v6.html     # Early standalone version
    script_maker_ui_v9.html     # Host-app CSS variable version
    script_maker_ui_v10.html    # Inline editing + undo/redo version
    Script-Writer/              # Separate early text editor prototype
    fonts/                      # Custom fonts from earlier iterations
```

## How it works under the hood

The entire app is a single HTML file — no build step, no framework, no dependencies. All state lives in a global JavaScript object (`S`) that maps directly to the JSON save format. The UI re-renders from that object on every change, with undo snapshots captured before each mutation.

Dark mode follows your system preference automatically.

## Roadmap

See [TODO.md](TODO.md) for the full list. The highlights:

- FDX export (Final Draft format)
- Find and replace across the script
- Auto-formatting for screenplay conventions
- Beat board / index card view
- Notes and comments on lines and scenes

## License

This project is provided as-is for personal and educational use.
