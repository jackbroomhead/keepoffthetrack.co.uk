# keepoffthetrack.co.uk

The Keep Off The Track studio website, hosted with GitHub Pages at <https://keepoffthetrack.co.uk>.

- `index.html`: the studio homepage.
- `synecdoche/index.html`: the hosted Synecdoche game design document. **Don't edit it here.** It is generated from the Unity repo's `Docs/GDD/index.html` by `tools/build_site.py`, which also adds the studio credit.
- `assets/`: the Keep Off The Track masthead, exported from the Aseprite source.
- `CNAME`: tells GitHub Pages to serve the site at keepoffthetrack.co.uk.

## Updating the GDD

```bash
python tools/build_site.py
git add -A && git commit -m "Update Synecdoche GDD" && git push
```
