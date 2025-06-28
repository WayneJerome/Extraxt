# extract_svg_points.py
from svgpathtools import svg2paths
import numpy as np
import json

paths, _ = svg2paths("MicroEng.svg")

points = []
for segment in paths[0]:  # Could loop through all paths
    for t in np.linspace(0, 1, 50):
        pt = segment.point(t)
        points.append([pt.real, pt.imag])

# Normalize and center (optional)
points = np.array(points)
points -= points.mean(axis=0)

# Save to JSON
with open("svg_points.json", "w") as f:
    json.dump(points.tolist(), f)
