#!/usr/bin/env python3
"""Assembles the PCP Nexus Manual from parts into a single self-contained index.html."""
import os

DIR = os.path.dirname(os.path.abspath(__file__))
PARTS_DIR = os.path.join(DIR, "parts")

# Read the CSS skeleton from template.html
with open(os.path.join(DIR, "template.html"), "r", encoding="utf-8") as f:
    skeleton = f.read()

# Read all body parts in order
part_files = [
    "body_part1.txt",    # Header, nav, hero, quick start, roles
    "part2_system.txt",  # What is PCP Nexus, architecture, pipelines
    "part3_interface.txt", # Requirements, main window, console, settings
    "part4_operations.txt", # Daily procedures, Phase 1/2, dashboard
    "part5_advanced.txt",   # Dedup, CSV handoff, backfill, keywords
    "part6_support.txt",    # Troubleshooting, checklists, revision, footer, JS
]

body_content = ""
for pf in part_files:
    path = os.path.join(PARTS_DIR, pf)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            body_content += f.read()
    else:
        print(f"WARNING: Missing part file: {pf}")

# Replace the placeholder with actual body content
final_html = skeleton.replace(
    "<!-- PLACEHOLDER_SPLIT -->",
    body_content.strip()
)

# Write the final assembled file
with open(os.path.join(DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"SUCCESS: index.html assembled ({len(final_html):,} characters)")
