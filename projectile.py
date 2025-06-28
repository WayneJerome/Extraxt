from manim import *

class ProjectileMotion(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10], y_range=[0, 5, 1], axis_config={"include_numbers": True}
        ).add_coordinates()
        self.play(Create(axes))

        projectile = Dot(color=YELLOW)
        self.add(projectile)

        path = VMobject()
        path.set_color(RED)
        path.start_new_path(projectile.get_center())

        v0 = 5  # initial velocity
        angle = 45 * DEGREES
        g = 9.8

        def pos(t):
            x = v0 * np.cos(angle) * t
            y = v0 * np.sin(angle) * t - 0.5 * g * t**2
            return axes.c2p(x, y)

        def update_path(mob, dt):
            t = self.time
            point = pos(t)
            projectile.move_to(point)
            mob.add_line_to(point)
            self.time += dt

        self.time = 0
        path.add_updater(update_path)
        self.add(path)
        self.wait(2.5)
        path.remove_updater(update_path)
