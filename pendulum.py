from manim import *

class SimplePendulum(Scene):
    def construct(self):
        origin = ORIGIN
        length = 2
        theta_max = 30 * DEGREES
        t_tracker = ValueTracker(0)  # ✅ Keeps track of time

        # Pendulum line updated based on t_tracker
        pendulum_line = always_redraw(lambda: Line(
            origin,
            origin + length * rotate_vector(DOWN, theta_max * np.cos(2 * t_tracker.get_value())),
            stroke_width=4
        ))

        bob = always_redraw(lambda: Dot(
            pendulum_line.get_end(), radius=0.1, color=BLUE
        ))

        self.add(pendulum_line, bob)

        # Animate the time tracker value over 4 seconds
        self.play(t_tracker.animate.increment_value(4), run_time=4, rate_func=linear)
