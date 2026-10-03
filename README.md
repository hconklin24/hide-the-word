# Hide the Word

A typing-based Bible memorization app. Make lists of passages, then practice by typing first letters or whole words, with optional reference practice.

- **WEB** (World English Bible, public domain, from eBible.org) is built in and works offline.
- **NIV, NASB, NLT** are copyrighted and not included: paste text per passage, or fetch with an [API.Bible](https://scripture.api.bible) key.

Lists are saved in your browser. Use Settings → Export/Import to back up or share them.

## Files
- `index.html`: the app
- `web.js`: WEB text data
- `build.py`: bundles both into a single shareable file at `dist/hide-the-word.html`
