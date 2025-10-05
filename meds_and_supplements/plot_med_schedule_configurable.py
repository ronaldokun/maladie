#!/usr/bin/env python3
import json
import argparse
import pandas as pd
import plotly.graph_objects as go

def bucket_for_function(func: str, rules: dict) -> str:
    # Find the first bucket whose rules list contains func; else default "Gut/Other"
    for bucket, fn_list in rules.items():
        if func in set(fn_list or []):
            return bucket
    return "Gut/Other"

def build_dataframe(data: dict):
    time_order = data.get("time_order") or ["Morning", "Midday", "Evening", "Dinner", "Bedtime"]
    settings = data.get("settings", {})
    rules = settings.get("bucket_rules", {})
    items = data["items"]

    # compute order within each time slot
    order_map, rows = {}, []
    for item in items:
        t = item["time"]
        order_map[t] = order_map.get(t, 0) + 1
        func = item["function"]
        bucket = bucket_for_function(func, rules)
        rows.append({
            "time": t,
            "order_in_slot": order_map[t],
            "compound": item["compound"],
            "function": func,
            "dosage": item.get("dosage", ""),
            "bucket": bucket
        })
    return pd.DataFrame(rows), time_order, settings

def visible_mask(bucket_order, show_bucket: str):
    return [b == show_bucket or show_bucket == "All" for b in bucket_order]

def make_figure(df: pd.DataFrame, time_order, settings: dict):
    # pull settings + sane defaults
    bucket_order = settings.get("bucket_order") or ["Liver", "Sleep", "Anti-inflammatory", "Gut/Other"]

    legend_cfg = settings.get("legend", {})
    fig_cfg = settings.get("figure", {})
    labels = settings.get("labels", {})
    traces_cfg = settings.get("traces", {})
    buttons_bar = settings.get("buttons_bar", {})

    marker_size = traces_cfg.get("marker_size", 12)
    textfont_size = traces_cfg.get("textfont_size", 9)
    textposition = traces_cfg.get("textposition", "top center")

    fig = go.Figure()
    for bucket in bucket_order:
        sub = df[df["bucket"] == bucket]
        fig.add_trace(
            go.Scatter(
                x=sub["time"],
                y=sub["order_in_slot"],
                mode="markers+text",
                text=sub["compound"],
                textposition=textposition,
                textfont=dict(size=textfont_size),
                name=bucket,
                hovertemplate=(
                    "<b>%{text}</b><br>"
                    "Bucket: " + bucket + "<br>"
                    "Function: %{customdata[0]}<br>"
                    "Dosage: %{customdata[1]}<extra></extra>"
                ),
                customdata=sub[["function", "dosage"]],
                marker=dict(size=marker_size),
            )
        )

    buttons = [
        dict(label="All", method="update", args=[{"visible": visible_mask(bucket_order, "All")}]),
        dict(label="Liver only", method="update", args=[{"visible": visible_mask(bucket_order, "Liver")}]),
        dict(label="Sleep only", method="update", args=[{"visible": visible_mask(bucket_order, "Sleep")}]),
        dict(label="Anti-inflammatory only", method="update", args=[{"visible": visible_mask(bucket_order, "Anti-inflammatory")}]),
        dict(label="Gut/Other only", method="update", args=[{"visible": visible_mask(bucket_order, "Gut/Other")}]),
    ]

    # layout
    fig.update_layout(
        title=labels.get("title", "Medication & Supplementation — Interactive Timeline"),
        xaxis=dict(title=labels.get("xaxis_title", "Time of Day"),
                   categoryorder="array", categoryarray=time_order),
        yaxis=dict(title=labels.get("yaxis_title", "Order within Time Slot"), dtick=1, rangemode="tozero"),
        legend=dict(
            orientation=legend_cfg.get("orientation", "v"),
            x=legend_cfg.get("x", 1.02),
            y=legend_cfg.get("y", 1.0),
            xanchor=legend_cfg.get("xanchor", "left"),
            yanchor=legend_cfg.get("yanchor", "top"),
            bgcolor=legend_cfg.get("bgcolor", "rgba(255,255,255,0.9)"),
            bordercolor=legend_cfg.get("bordercolor", "rgba(0,0,0,0.2)"),
            borderwidth=legend_cfg.get("borderwidth", 1),
        ),
        margin=fig_cfg.get("margin", {"l": 60, "r": 200, "t": 80, "b": 60}),
        height=fig_cfg.get("height", 760),
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                buttons=buttons,
                x=buttons_bar.get("x", 0.5),
                y=buttons_bar.get("y", 1.12),
                xanchor=buttons_bar.get("xanchor", "center"),
                yanchor=buttons_bar.get("yanchor", "top"),
                bgcolor=buttons_bar.get("bgcolor", "rgba(255,255,255,0.8)"),
                bordercolor=buttons_bar.get("bordercolor", "rgba(0,0,0,0.25)"),
                borderwidth=buttons_bar.get("borderwidth", 1),
                pad=buttons_bar.get("pad", {"r": 5, "t": 2, "b": 2, "l": 5})
            )
        ]
    )
    return fig

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True, help="Path to the JSON config file")
    ap.add_argument("--out", default="med_schedule_plot_configurable.html", help="Output HTML path")
    args = ap.parse_args()

    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    df, time_order, settings = build_dataframe(data)
    fig = make_figure(df, time_order, settings)
    fig.write_html(args.out, include_plotlyjs="cdn", full_html=True)
    print(f"Wrote: {args.out}")

if __name__ == "__main__":
    main()
