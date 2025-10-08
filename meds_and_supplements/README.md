## How to use the Medication & Supplementation Timeline

### JavaScript-based (Current - Recommended)

The visualization now runs entirely in the browser using native JavaScript!

* **Interactive HTML**: `meds.html` - Open this file directly in your browser
* **Config JSON**: `med_schedule.json` - Edit this file to update your medications/supplements

**Usage:**
1. Edit `med_schedule.json` with your medication schedule
2. Open `meds.html` in any modern web browser
3. The plot will automatically reload data from the JSON file

**Benefits:**
- No Python required!
- Just refresh the browser to see updates after editing the JSON
- Works exactly like `index.html` in the parent directory

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

