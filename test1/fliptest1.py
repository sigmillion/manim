from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class FontsExample(Scene):
    def construct(self):
        ft = Text("Noto Sans", font="Marker Felt")
        self.add(ft)


class FlipTest1(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5],
            y_range=[-1, 1],
        )
        labels = ax.get_axis_labels()
        gauss_curve = ax.plot(lambda t: np.exp(-0.5*(t**2)), color=BLUE_C)
        colors = color_gradient([BLUE, GREEN], 100)
        gauss_shade = ax.get_area(gauss_curve,color=(ManimColor('#58C4DD'),RED),opacity=0.9)

        self.add(ax, gauss_shade, gauss_curve)


class FlipTest2(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range=[-5, 5],
            y_range=[-1, 1],
            z_range=[-5, 5],
        )
        labels = ax.get_axis_labels()
        gauss_curve = ax.plot(lambda t: np.exp(-0.5*(t**2)), color=BLUE_C)
        colors = color_gradient([BLUE, GREEN], 100)
        gauss_shade = ax.get_area(gauss_curve,color=(ManimColor('#58C4DD'),RED),opacity=0.9)

        self.set_camera_orientation(zoom=0.5)
        self.add(ax, gauss_shade, gauss_curve)
        self.move_camera(phi=-10*DEGREES, theta=-90*DEGREES, run_time=2)
