"""
Generate medication schedule markdown from med_schedule.json
This script reads the JSON file and generates the markdown section
for inclusion in index.qmd
"""

import json
import sys
from pathlib import Path


def generate_schedule_markdown(json_file):
    """Generate markdown from med_schedule.json"""
    with open(json_file) as f:
        data = json.load(f)

    # Group items by time
    by_time = {}
    for item in data["items"]:
        time = item["time"]
        if time not in by_time:
            by_time[time] = []
        by_time[time].append(item)

    # Generate markdown
    lines = []
    for time in data["time_order"]:
        if time in by_time:
            # Time headers with emoji
            headers = {
                "Morning": "🕗 Morning",
                "Lunch": "🍽 Lunch",
                "Afternoon": "🌇 Afternoon",
                "Dinner": "🌙 Dinner",
                "Bedtime": "🌃 Bedtime",
            }

            lines.append(f"### {headers.get(time, time)}\n")
            for item in by_time[time]:
                lines.append(f"* {item['compound']} — {item['dosage']}")
            lines.append("")  # blank line between sections

    return "\n".join(lines)


def update_qmd_section(qmd_file, new_content):
    """Update the medication schedule section in index.qmd"""
    with open(qmd_file) as f:
        content = f.read()

    # Find and replace the section between markers
    start_marker = "## 💡 Meds and Supplements Schedule\n"
    end_marker = "\n## ⚖️ Strategic Observations"

    if start_marker not in content or end_marker not in content:
        print(
            f"Error: Could not find schedule section markers in {qmd_file}",
            file=sys.stderr,
        )
        return False

    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)

    new_qmd = content[:start_idx] + new_content + "\n" + content[end_idx:]

    with open(qmd_file, "w") as f:
        f.write(new_qmd)

    return True


if __name__ == "__main__":
    json_file = Path(__file__).parent / "med_schedule.json"
    qmd_file = Path(__file__).parent / "index.qmd"

    if not json_file.exists():
        print(f"Error: {json_file} not found", file=sys.stderr)
        sys.exit(1)

    if not qmd_file.exists():
        print(f"Error: {qmd_file} not found", file=sys.stderr)
        sys.exit(1)

    # Generate markdown
    markdown = generate_schedule_markdown(json_file)

    # Update qmd file
    if update_qmd_section(qmd_file, markdown):
        print(f"✓ Updated {qmd_file} with generated schedule")
        sys.exit(0)
    else:
        sys.exit(1)
