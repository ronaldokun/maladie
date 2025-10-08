## How to use the Medication & Supplementation Timeline

### JavaScript-based (Current - Recommended)

The visualization now runs entirely in the browser using native JavaScript!

* **Interactive HTML**: `meds.html` - Open this file directly in your browser
* **Config JSON**: `med_schedule.json` - Edit this file to update your medications/supplements

**Usage:**

*Option 1: Using a local web server (Recommended)*
```bash
# From the meds_and_supplements directory
./serve.sh
# Or manually:
python3 -m http.server 8000
# Then open: http://localhost:8000/meds.html
```

*Option 2: Direct file opening (Manual file selection)*
1. Open `meds.html` directly in your browser
2. When prompted, select the `med_schedule.json` file from the file picker
3. The visualization will load

**Note:** Modern browsers block JavaScript from loading local files for security reasons when opened via `file://`. The manual file picker is a workaround, but using a local web server (Option 1) provides the best experience.

**Benefits:**
- No Python dependencies to install (unless using the local server)
- Edit JSON → Refresh browser → See changes instantly!
- Works exactly like `index.html` in the parent directory
- All configuration in one JSON file

### Python-based (Legacy - Optional)

You can still generate a static HTML file using Python if needed:

```bash
pip install plotly pandas
python plot_meds.py --json med_schedule.json --out meds_static.html
```

### What you can tweak in `med_schedule.json`

* **Bucket rules & order**

  * `settings.bucket_order`: order of legend and filter buttons.
  * `settings.bucket_rules`: map fine-grained `function` strings → a bucket.
    Any function not listed falls back to **"Gut/Other"** automatically.
* **Legend placement**

  * `settings.legend`: `x`, `y`, `xanchor`, `yanchor`, `orientation`, background/border.
* **Figure size**

  * `settings.figure.height` and `settings.figure.margin` (l/r/t/b).
* **Labels & styling**

  * `settings.labels.title`, `xaxis_title`, `yaxis_title`.
  * `settings.traces.marker_size`, `textfont_size`, `textposition`.
* **Buttons bar**

  * `settings.buttons_bar`: position (`x`,`y`), anchors, colors, padding.

