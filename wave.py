from manim import *

class WaveFunction(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10], y_range=[-2, 2],
            tips=False,
            axis_config={"include_numbers": False}
        ).add_coordinates()

        self.play(Create(axes))

        k = 2 * PI / 4
        w = 2 * PI / 2
        A = 1

        wave = always_redraw(lambda: axes.plot(
            lambda x: A * np.sin(k * x - w * self.time),
            color=BLUE
        ))

        self.time = 0

        def updater(mob, dt):
            self.time += dt

        self.add_updater(updater)
        self.add(wave)
        self.wait(4)
 # type: ignore