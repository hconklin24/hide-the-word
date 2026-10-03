# Hide the Word

A typing-based Bible memorization app. Make lists of passages, then practice by typing first letters or whole words, with optional reference practice.

- **WEB** (World English Bible, public domain, from eBible.org) is built in and works offline.
- **NIV, NASB, NLT** are copyrighted and not included: paste text per passage, or fetch with an [API.Bible](https://scripture.api.bible) key.

Lists are saved in your browser. Use Settings → Export/Import to back up or share them.

Styled with [Material 3](https://m3.material.io) using [Material Web](https://material-web.dev) components, in a green / gold / white theme.

## Files
- `index.html`: the app
- `theme.css`: Material 3 color tokens (light + dark), generated
- `vendor/material.js`: bundled Material Web components + icons, generated
- `web.js`: WEB text data
- `build.py`: inlines everything into a single shareable file at `dist/hide-the-word.html`

## Development
The site needs no build step; `vendor/material.js` and `theme.css` are committed. To regenerate them:

```bash
npm install
npm run vendor   # after changing which components/icons tools/build-vendor.mjs includes
npm run theme    # after changing the seed colors in tools/gen-theme.mjs
npm run build    # single-file dist/hide-the-word.html
```
