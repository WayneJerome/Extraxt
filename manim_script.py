from manim import *
import numpy as np
import json

class ContinuousMotion(Scene):
    def construct(self):
        # Load the points
        with open("svg_points.json", "r") as f:
            raw_points = np.array(json.load(f))

        # Optional: scale to fit the screen
        scale_factor = 0.05
        raw_points *= scale_factor

        # Convert to Manim vectors
        vector_field_points = [np.array([x, y, 0]) for x, y in raw_points]

        # Vector field function pulling toward nearest path point
        def func(pos):
            closest = min(vector_field_points, key=lambda p: np.linalg.norm(p - pos))
            direction = (closest - pos)
            return direction / (np.linalg.norm(direction) + 1e-3)

        # Create stream lines without deprecated args
        stream_lines = StreamLines(
            func,
            stroke_width=1.5,
            max_anchors_per_line=25,
            padding=0.5,
        )

        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
