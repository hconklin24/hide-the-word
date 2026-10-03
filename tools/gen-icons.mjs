// Renders the app icons (gold book on green) used for Add to Home Screen / Add to Dock. Run: npm run icons
import sharp from 'sharp';
import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';

const book = readFileSync('node_modules/@material-symbols/svg-400/rounded/menu_book-fill.svg', 'utf8').match(/<path d="([^"]+)"/)[1];
// Full-bleed square (iOS and Android mask the corners themselves); the book sits in the central safe zone.
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" fill="#236b41"/>
  <g transform="translate(256 256) scale(0.30) translate(-480 480)"><path d="${book}" fill="#ebc248"/></g>
</svg>`;

mkdirSync('icons', { recursive: true });
writeFileSync('icons/icon.svg', svg);
for (const [file, size] of [['apple-touch-icon.png', 180], ['icon-192.png', 192], ['icon-512.png', 512]]) {
  await sharp(Buffer.from(svg)).resize(size, size).png().toFile(`icons/${file}`);
}
console.log('Wrote icons/');
