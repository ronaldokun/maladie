## How to config and create plot locally

* **Config JSON** (edit settings here):
  [med_schedule_config.json](sandbox:/mnt/data/med_schedule_config.json)
* **Reusable script (reads JSON settings)**:
  [plot_med_schedule_configurable.py](sandbox:/mnt/data/plot_med_schedule_configurable.py)
* **Standalone interactive HTML (generated)**:
  [med_schedule_plot_configurable.html](sandbox:/mnt/data/med_schedule_plot_configurable.html)


```bash
pip install plotly pandas
python plot_med_schedule_configurable.py --json med_schedule_config.json --out med_schedule_plot_configurable.html
```

### What you can tweak in `med_schedule_config.json`

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

