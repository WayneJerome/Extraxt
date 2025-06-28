import json
import numpy as np
import matplotlib.pyplot as plt

# Load points from JSON
with open("svg_points.json", "r") as f:
    points = np.array(json.load(f))

# Optional: normalize and center
points -= points.mean(axis=0)

# Plot
plt.figure(figsize=(6, 6))
plt.plot(points[:, 0], points[:, 1], 'o-', markersize=2, linewidth=0.5)
plt.title("Extracted SVG Path Points")
plt.axis('equal')  # Maintain aspect ratio
plt.grid(True)
plt.show()
