from manim import *
from manim.utils.rate_functions import ease_in_sine
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService as SpeechService


class MedialTriangleToPyramid(ThreeDScene, VoiceoverScene):
    def construct(self):
        self.set_speech_service(SpeechService())

        axes = Axes(
            x_range=[-3, 77, 8],
            y_range=[-3, 53, 8],
            x_length=0.95 * 10,
            y_length=0.95 * 7,
            x_axis_config={
                "numbers_to_include": [64, 72],
            },
            y_axis_config={
                "numbers_to_include": [48],
            },
        )

        triangle_bl = axes.c2p(0, 0)
        triangle_br = axes.c2p(68, 0)
        triangle_t = axes.c2p(32, 48)

        triangle_bl_point = Dot(triangle_bl, color=RED)
        triangle_br_point = Dot(triangle_br, color=RED)
        triangle_t_point = Dot(triangle_t, color=RED)

        triangle_bl_label = MathTex("(0, 0)").next_to(triangle_bl_point, DOWN)
        triangle_br_label = MathTex("(68, 0)").next_to(triangle_br_point, UR, buff=0.2)
        triangle_t_label = MathTex("(32, 48)").next_to(triangle_t_point, UP)

        triangle = Polygon(triangle_bl, triangle_br, triangle_t, color=BLUE)

        with self.voiceover(
            "To start solving the question, let's plot the given triangle."
        ) as tracker:
            self.play(Write(axes), run_time=tracker.duration / 3)
            self.play(
                Create(triangle),
                Create(triangle_bl_point),
                Create(triangle_br_point),
                Create(triangle_t_point),
                run_time=tracker.duration / 3,
            )
            self.play(
                Write(triangle_bl_label),
                Write(triangle_br_label),
                Write(triangle_t_label),
                run_time=tracker.duration / 3,
            )

        self.wait(1)

        mid_tl = axes.c2p(16, 24)
        mid_tr = axes.c2p(50, 24)
        mid_b = axes.c2p(34, 0)

        mid_tl_point = Dot(mid_tl, color=GREEN)
        mid_tr_point = Dot(mid_tr, color=GREEN)
        mid_b_point = Dot(mid_b, color=GREEN)

        mid_tl_label = MathTex("(", "16", ",", "24", ")").next_to(mid_tl_point, LEFT)
        mid_tr_label = MathTex("(", "50", ",", "24", ")").next_to(mid_tr_point, RIGHT)
        mid_b_label = MathTex("(", "34", ",", "0", ")").next_to(mid_b_point, DOWN)

        medial_triangle = Polygon(mid_tl, mid_tr, mid_b, color=GREEN)

        with self.voiceover("Now we can plot the medial triangle.") as tracker:
            self.play(
                Create(medial_triangle),
                Create(mid_tl_point),
                Create(mid_tr_point),
                Create(mid_b_point),
                run_time=tracker.duration / 2,
            )
            self.play(
                Write(mid_tl_label),
                Write(mid_tr_label),
                Write(mid_b_label),
                run_time=tracker.duration / 2,
            )

        self.wait(1)

        medial_base_length = BraceBetweenPoints(mid_tr, mid_tl)
        medial_base_length_label = MathTex("34").next_to(
            medial_base_length, UP, buff=0.2
        )

        medial_height_length = BraceBetweenPoints(axes.c2p(16, 0), mid_tl)
        medial_height_label = MathTex("24").next_to(
            medial_height_length, RIGHT, buff=0.2
        )

        with self.voiceover(
            "We can trivially compute the base and height of the medial triangle by comparing x and y values."
        ) as tracker:
            self.play(
                Create(medial_base_length),
                Write(medial_base_length_label),
                mid_tl_label[1].animate.set_color(RED),
                mid_tr_label[1].animate.set_color(RED),
                run_time=tracker.duration / 2,
            )
            self.play(
                Create(medial_height_length),
                Write(medial_height_label),
                mid_tl_label[3].animate.set_color(RED),
                mid_b_label[3].animate.set_color(RED),
                mid_tl_label[1].animate.set_color(WHITE),
                mid_tr_label[1].animate.set_color(WHITE),
                run_time=tracker.duration / 2,
            )

        self.wait(1)

        pyramid_base_formula = MathTex(
            "A_{\\text{base}} = \\frac{1}{2} \\times 34 \\times 24"
        ).to_corner(UR)

        pyramid_base_formula_new = MathTex("A_{\\text{base}} = 408").move_to(
            pyramid_base_formula
        )

        with self.voiceover(
            "The area of the medial triangle is then trivial to compute."
        ) as tracker:
            self.play(Write(pyramid_base_formula), run_time=tracker.duration / 2)
            self.play(
                Transform(pyramid_base_formula, pyramid_base_formula_new),
                run_time=tracker.duration / 2,
            )

        self.wait(1)

        non_medial_triangles_t = Polygon(
            mid_tl, mid_tr, triangle_t, fill_color=GREEN, fill_opacity=1, color=RED
        )
        non_medial_triangles_bl = Polygon(
            triangle_bl, mid_tl, mid_b, fill_color=GREEN, fill_opacity=1, color=RED
        )
        non_medial_triangles_br = Polygon(
            mid_tr, triangle_br, mid_b, fill_color=GREEN, fill_opacity=1, color=RED
        )

        with self.voiceover(
            "We can now look at the three walls of the pyramid and where they intersect."
        ) as tracker:
            self.play(
                Create(non_medial_triangles_t),
                Create(non_medial_triangles_bl),
                Create(non_medial_triangles_br),
                run_time=tracker.duration,
            )

        self.move_camera(phi=60 * DEGREES)

        self.play(
            Rotate(
                non_medial_triangles_bl,
                angle=118.1 * DEGREES,  # Wolfram Alpha magic
                axis=mid_tl - mid_b,
                rate=linear,
                about_point=mid_b,
            ),
            Rotate(
                non_medial_triangles_br,
                angle=122 * DEGREES,  # Wolfram Alpha magic
                axis=mid_b - mid_tr,
                rate=linear,
                about_point=mid_b,
            ),
            Rotate(
                non_medial_triangles_t,
                angle=90 * DEGREES,
                axis=RIGHT,
                rate=linear,
                about_point=axes.c2p(34, 24),
            ),
            run_time=4,
        )

        with self.voiceover(
            "The pyramid forms at a clear point, but the best way of finding that point is to view the bending from the top."
        ) as tracker:
            self.begin_ambient_camera_rotation(rate=2 * PI / tracker.duration)
            self.wait(tracker.duration)
            self.stop_ambient_camera_rotation()

        self.wait(1)

        self.play(
            Rotate(
                non_medial_triangles_bl,
                angle=-118.1 * DEGREES,  # Wolfram Alpha magic
                axis=mid_tl - mid_b,
                rate=linear,
                about_point=mid_b,
            ),
            Rotate(
                non_medial_triangles_br,
                angle=-122 * DEGREES,  # Wolfram Alpha magic
                axis=mid_b - mid_tr,
                rate=linear,
                about_point=mid_b,
            ),
            Rotate(
                non_medial_triangles_t,
                angle=-90 * DEGREES,
                axis=RIGHT,
                rate=linear,
                about_point=axes.c2p(34, 24),
            ),
            run_time=1,
        )

        self.move_camera(phi=0 * DEGREES)

        line_1 = Line(triangle_bl, axes.c2p(32, 24) + OUT * 2.85)
        line_2 = Line(triangle_br, axes.c2p(32, 24) + OUT * 2.85)
        line_3 = Line(
            triangle_t, axes.c2p(32, 24) + OUT * 2.85
        )  # 2.85 is from the z of the apex of pyramid

        with self.voiceover(
            "Notice how, as the sides of the pyramid rotate upward, a line is roughly tracing them."
        ) as tracker:
            self.play(
                Rotate(
                    non_medial_triangles_bl,
                    angle=118.1 * DEGREES,  # Wolfram Alpha magic
                    axis=mid_tl - mid_b,
                    rate_func=linear,
                    about_point=mid_b,
                ),
                Rotate(
                    non_medial_triangles_br,
                    angle=122 * DEGREES,  # Wolfram Alpha magic
                    axis=mid_b - mid_tr,
                    rate_func=linear,
                    about_point=mid_b,
                ),
                Rotate(
                    non_medial_triangles_t,
                    angle=90 * DEGREES,
                    axis=RIGHT,
                    rate_func=linear,
                    about_point=axes.c2p(34, 24),
                ),
                Create(line_1, rate_func=ease_in_sine),
                Create(line_2, rate_func=ease_in_sine),
                Create(line_3, rate_func=ease_in_sine),
                run_time=tracker.duration + 0.5,
            )

        self.wait(1)

        self.play(
            FadeOut(non_medial_triangles_t),
            FadeOut(non_medial_triangles_bl),
            FadeOut(non_medial_triangles_br),
        )

        extended_line_1 = Line(triangle_bl, axes.c2p(32 * 4, 24 * 4), color=YELLOW)
        extended_line_2 = Line(
            triangle_br,
            triangle_br - 4 * (triangle_br - axes.c2p(32, 24)),
            color=YELLOW,
        )
        extended_line_3 = Line(
            triangle_t, triangle_t - 4 * (triangle_t - axes.c2p(32, 24)), color=YELLOW
        )

        with self.voiceover(
            "Upon extending these lines, we see that they are the altitudes of the triangle. Thus, the orthocenter of a pyramid's net is that pyramid's apex."
        ) as tracker:
            self.play(
                FadeOut(line_1),
                FadeOut(line_2),
                FadeOut(line_3),
                run_time=0.1,
            )
            self.play(
                Create(extended_line_1),
                Create(extended_line_2),
                Create(extended_line_3),
                FadeOut(medial_base_length),
                FadeOut(medial_height_length),
                FadeOut(medial_base_length_label),
                FadeOut(medial_height_label),
                run_time=tracker.get_remaining_duration(),
            )

        pyramid_height = BraceBetweenPoints(axes.c2p(32, 48), axes.c2p(32, 24))
        pyramid_height_label = MathTex("24").next_to(pyramid_height, LEFT, buff=0.2)

        with self.voiceover(
            "The orthocenter sits on one of the sides of the medial triangle, which means the non-medial triangle adjacent to that will be up 90 degrees when the pyramid is constructed. Thus, the pyramid's height is equal to the distance between the triangle's uppermost vertex and the orthocenter. "
        ) as tracker:
            self.play(
                Create(pyramid_height),
                Write(pyramid_height_label),
                run_time=tracker.duration,
            )

        volume_formula = MathTex("V = \\frac{1}{3} \\times 408 \\times 24").next_to(
            pyramid_base_formula, DOWN
        )

        volume_formula_new = MathTex("V = 3264").move_to(volume_formula)

        with self.voiceover(
            "Finally, we can compute the volume of the pyramid by multiplying the base area and height and dividing by 3."
        ) as tracker:
            self.play(Write(volume_formula), run_time=tracker.duration * 2 / 3)
            self.play(Transform(volume_formula, volume_formula_new), run_time=tracker.duration / 3)

        self.wait(0.2)

        with self.voiceover("So three thousand two hundred sixty-four is the solution to the problem.") as tracker:
            self.play(Circumscribe(volume_formula_new), run_time=tracker.duration)
