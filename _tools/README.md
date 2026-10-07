# Care guides + label printer tooling

- `care_data.py`: the original care dataset (fish, inverts, plants). Add or edit entries here.
- `build_care.py`: regenerates `/care/**`, `/care/data.json`, the sitemap `/care` + `/labels` entries and the llms.txt "Care guides" section. Run from repo root: `python3 _tools/build_care.py`. Idempotent.
- `/labels/` is a client-side tool (labels.js, labels.css, qr.js = MIT qrcode-generator). It reads `/care/data.json`, so rebuild after any data change.
- Keep ranges conservative and written from general hobby knowledge; do not copy another site's database. Store details (addresses, phones, hours) live in `STORES` in `build_care.py`.
- Underscore folders are not published by GitHub Pages' Jekyll, so this folder stays off the live site.

Placeholder art: _tools/make_art.py draws original cartoon SVGs into care/art/ for species without a photo (run before build_care.py). Add a real photo to care/photos.json and it replaces the illustration.
