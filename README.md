# The Scriptwriter

A free, open-source screenplay editor that runs entirely in your browser. No accounts, no installs, no cloud — just open the HTML file and start writing.

**[Try it live →](https://yashmahtani.github.io/The-TypeWriter/)**

## What it does

The Scriptwriter gives you a structured screenplay writing environment with an **Act > Scene > Line** hierarchy. You write using four line types — Setting, Direction, Dialogue, and Action — and the app handles formatting, numbering, and continuity for you.

Scripts auto-save to your browser's localStorage and can be linked to a file on disk via the File System Access API. When you're ready to share, export to a formatted screenplay PDF or download a metadata ZIP containing the raw JSON for later editing.

## Quick start

Open `script_maker.html` in any modern browser. That's it. You can start a new script, open a saved JSON file, or try the built-in sample script.

## Features

**Writing**
- Four line types (Setting, Direction, Dialogue, Action) with customizable keyboard shortcuts (default: backtick + 1/2/3/4) and smart auto-advance between types
- Character management with autocomplete, ghost text, scene filtering, and archiving
- Direction cues that track character entrances and exits per scene with visual toggle chips
- Automatic `(cont.)` detection for consecutive dialogue from the same character
- Auto-numbered acts and scenes ("Act One", "Scene Three") with optional custom names

**Editing**
- Inline editing — double-click any line to edit in place, or use the Edit button
- Drag-and-drop reordering for acts, scenes, and lines with validation against character presence
- 50-level undo/redo (Ctrl+Z / Ctrl+Shift+Z) with full state snapshots
- Insert cursor — click a line to insert new content after it
- Find and replace across the script with line-type filter chips (Ctrl+F)

**Organization**
- Collapsible side panel with table of contents and expandable character list
- Click a character to see their full description and searchable dialogue history; click any dialogue line to jump to it in the editor
- Summaries tab with script statistics
- Read-only View tab with act/scene separators for distraction-free reading
- Settings tab for font size, indicator styles, line-type colors, theme override, and pill hotkey customization

**File handling**
- localStorage auto-persistence — your work is saved in the browser automatically
- File System Access API — link to a file on disk and overwrite on each save (no repeated downloads)
- Fallback JSON download for browsers without File System Access API
- Visual save indicator: gray (no file), blue (browser-only), green (linked to disk file)
- PDF export with title page, character list, table of contents, and formatted script pages
- Metadata ZIP download — exports the raw JSON and a manifest for re-importing later
- PDF + metadata export — bundles the print-ready PDF with metadata in a single ZIP

**Appearance**
- Dark mode follows your system preference, or override with light/dark in Settings
- Customizable line-type accent colors with per-type enable/disable toggles
- Configurable selected-line indicator (barrier or highlight) with color options

## Project structure

```
The-TypeWriter/
  script_maker.html             # The app (open this)
  docs/
    index.html                  # GitHub Pages copy
    describe.html               # Feature guide / manual
  TODO.md                       # Feature roadmap
  CLAUDE.md                     # Dev notes and project memory
  README.md                     # This file
  archive/                      # Older versions kept for reference
```

## How it works under the hood

The entire app is a single HTML file with one external dependency (JSZip via CDN for ZIP export). No build step, no framework. All state lives in a global JavaScript object (`S`) that maps directly to the JSON save format. The UI re-renders from that object on every change, with undo snapshots captured before each mutation.

## Roadmap

See [TODO.md](TODO.md) for the full list. Up next:

- FDX export (Final Draft format)
- Auto-formatting for screenplay conventions
- Beat board / index card view
- Notes and comments on lines and scenes
- Revision tracking / version history

## License

This project is provided as-is for personal and educational use.
