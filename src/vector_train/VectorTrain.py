from manimlib import *


class VectorTrain(Scene):
	def construct(self):
		title = Title("Scalar Multiplication")
		self.play(Write(title))
		scalar_def = Text("A scalar is another name for a real number.", t2c={' scalar': RED})
		self.play(Write(scalar_def, run_time=2))
		self.wait()
		self.remove(scalar_def, title)

		scalar_explanation = Text("When we mutliply a vector by a scalar,")
		scalar_explanation2 = Text("we multiply both coordinate values by the scalar.").next_to(scalar_explanation, DOWN)
		scalar_group = VGroup(scalar_explanation, scalar_explanation2).scale(0.8)
		self.play(Write(scalar_group))
		self.wait(3)
		self.remove(scalar_group)
		

		plane = NumberPlane(x_range=[-1,7,1], y_range=[-6,3,1], 
			x_length=8, y_length=8, axis_config={"unit_size":0.5}).to_edge(LEFT)
		

		self.play(ShowCreation(plane))
		

		

		a_vec = Line(plane.c2p(0,0), plane.c2p(3,-2), color=YELLOW).add_tip()
		
		a_vec_name = Tex(r'\vec{a}', color=YELLOW).next_to(a_vec, RIGHT)
		

		a_vec_lbl = Tex(r"\vec{a} = \begin{bmatrix} 3 \\ -2 \end{bmatrix}", color=YELLOW).shift(3*RIGHT)
		

		a_group = VGroup(a_vec, a_vec_name, a_vec_lbl)
		
		dbl_vec = Line(plane.c2p(0,0), plane.c2p(6,-4), color=RED).add_tip()
		
		dbl_vec_name = Tex(r"2\vec{a}", color=ORANGE).next_to(a_vec, RIGHT)
		
		dbl_vec_lbl = Tex(r"2\vec{a} = \begin{bmatrix} 6 \\ -4 \end{bmatrix}", color=ORANGE).shift(3*RIGHT)
		
		dbl_group = VGroup(dbl_vec, dbl_vec_name, dbl_vec_lbl)
		
		

		self.play(ShowCreation(a_vec))
		
		self.play(Write(a_vec_name))
		
		self.wait()
		
		self.play(Write(a_vec_lbl))
		
		self.wait()
		
		self.play(Transform(a_group, dbl_group, run_time=2))
		
		self.wait(2)
		
		self.remove(a_group, dbl_group, plane)
		
		self.wait()
		

		plane2 = NumberPlane(x_range=[-5,4,1], y_range=[-3,3,1]).to_edge(LEFT)
		
		self.play(ShowCreation(plane2))
		

		a_vec = Line(plane2.c2p(0,0), plane2.c2p(3,-2), color=YELLOW).add_tip()
		
		a_vec_name = Tex(r"\vec{a}", color=YELLOW).next_to(a_vec, RIGHT)
		
		a_vec_lbl = Tex(r"\vec{a} = \begin{bmatrix} 3 \\ -2 \end{bmatrix}", 
			color=YELLOW).shift(4*RIGHT)
		
		a_group = VGroup(a_vec, a_vec_name, a_vec_lbl)
		
		neg_vec = Line(plane2.c2p(0,0), plane2.c2p(-3,2), 
			color=RED).add_tip()
		
		neg_vec_name = Tex(r"-\vec{a}", color=ORANGE).next_to(neg_vec, LEFT)
		
		neg_vec_lbl = Tex(r"-1\vec{a} = \begin{bmatrix} -3 \\ 2 \end{bmatrix}", 
			color=ORANGE).shift(4*RIGHT)
		
		neg_group = VGroup(neg_vec, neg_vec_name, neg_vec_lbl)
		

		self.play(ShowCreation(a_group))
		
		self.wait()
		

		self.play(Transform(a_group, neg_group))
		
		self.wait(3)
		
		self.remove(a_group, neg_group, plane2)
		
		self.wait()

		
		example_text = Tex("Given",r"\ \vec{v}=\begin{bmatrix} 1 \\ -1 \end{bmatrix} , ", r"\vec{w}=\begin{bmatrix} -2 \\ 0 \end{bmatrix} .\ ","find ",r"\ 3\vec{v} + \vec{w}.")
		
		self.play(Write(example_text))
		
		self.wait(3)
		
		self.remove(example_text)
		
		self.wait()

		example_plane = NumberPlane(x_range=[-4,4,1], 
			y_range=[-4,4,1]).to_edge(LEFT)
		v_example = Line(start=example_plane.c2p(0,0), 
			end=example_plane.c2p(1,-1), color=YELLOW).add_tip()
		v_example_lbl = Tex(r"\vec{v}", color=YELLOW).next_to(v_example, RIGHT)
		

		v_example_tex = Tex(r"\vec{v}=\begin{bmatrix} 1 \\ -1 \end{bmatrix}", color=YELLOW).shift(3.5*RIGHT + 2*UP)
		
		self.play(ShowCreation(example_plane))
		
		self.play(ShowCreation(v_example))
		
		self.play(Write(v_example_lbl))
		
		self.play(Write(v_example_tex))
		

		w_example = Line(start=example_plane.c2p(0,0), end=example_plane.c2p(-2,0),
			color=BLUE).add_tip()
		
		w_example_lbl = Tex(r"\vec{w}", color=BLUE).next_to(w_example, UP)
		
		w_example_tex = Tex(r"\vec{w}=\begin{bmatrix} -2 \\ 0 \end{bmatrix}", color=BLUE).next_to(v_example_tex, RIGHT)
		
		self.play(ShowCreation(w_example))
		
		self.play(Write(w_example_lbl))
		
		self.play(Write(w_example_tex))
		

		w_example_lbl.add_updater(lambda x: x.next_to(w_example, UP))
		
		scale_v_example = Line(start=example_plane.c2p(0,0), 
			end=example_plane.c2p(3,-3), color=YELLOW).add_tip()
		
		scale_v_lbl = Tex(r"3\vec{v}", color=YELLOW).next_to(scale_v_example)
		
		scale_v_tex = Tex(r"3\vec{v} = \begin{bmatrix} 3 \\ -3 \end{bmatrix}", color=YELLOW).next_to(w_example_tex, LEFT)
		
		self.play(Transform(v_example, scale_v_example))
		
		self.play(Transform(v_example_lbl, scale_v_lbl))
		
		self.play(Transform(v_example_tex, scale_v_tex))
		
		example_resultant = Line(start=example_plane.c2p(3,-3), end=example_plane.c2p(1,-3),
			color=BLUE).add_tip()
		
		self.play(Transform(w_example, example_resultant))
		
		self.wait()
		

		vec_sum = Line(start=example_plane.c2p(0,0), end=example_plane.c2p(1,-3),
			color=PURPLE).add_tip()
		vec_sum_lbl = Tex(r"3\vec{v}+\vec{w}", color=PURPLE).next_to(vec_sum, LEFT)
		vec_sum_tex = Tex(r"3\vec{v} + \vec{w} = \begin{bmatrix} 1 \\ -3 \end{bmatrix}", color=PURPLE).next_to(scale_v_tex, 2*DOWN)
		self.wait()
		self.play(ShowCreation(vec_sum))
		self.play(Write(vec_sum_lbl))
		self.play(Write(vec_sum_tex))
		self.wait()
		self.remove(vec_sum, vec_sum_lbl, vec_sum_tex, v_example, v_example_lbl, v_example_tex,
		w_example, scale_v_lbl, scale_v_tex, example_plane,
		example_resultant, scale_v_example, w_example_lbl, w_example_tex)

		
		example_text = Tex("Given",r"\ \vec{v}=\begin{bmatrix} 1 \\ -1 \end{bmatrix} , ", r"\vec{w}=\begin{bmatrix} -2 \\ 0 \end{bmatrix} .\ ","find ",r"\ 3\vec{v} - \vec{w}.")

		self.play(Write(example_text))
		self.wait()
		self.remove(example_text)
		self.wait()

		example_plane = NumberPlane(x_range=[-3,5.5,1], 
			y_range=[-4,4,1]).to_edge(LEFT)
		v_example = Line(start=example_plane.c2p(0,0), 
			end=example_plane.c2p(1,-1), color=YELLOW).add_tip()
		v_example_lbl = Tex(r"\vec{v}", color=YELLOW).next_to(v_example, RIGHT)
		v_example_tex = Tex(r"\vec{v}=\begin{bmatrix} 1 \\ -1 \end{bmatrix}", color=YELLOW).shift(3.5*RIGHT + 2*UP)
		self.play(ShowCreation(example_plane))
		self.play(ShowCreation(v_example))
		self.play(Write(v_example_lbl))
		self.play(Write(v_example_tex))

		w_example = Line(start=example_plane.c2p(0,0), end=example_plane.c2p(-2,0),
			color=BLUE).add_tip()
		w_example_lbl = Tex(r"\vec{w}", color=BLUE).next_to(w_example, DOWN)
		w_example_tex = Tex(r"\vec{w}=\begin{bmatrix} -2 \\ 0 \end{bmatrix}", color=BLUE).next_to(v_example_tex, RIGHT)
		self.play(ShowCreation(w_example))
		self.play(Write(w_example_lbl))
		self.play(Write(w_example_tex))
		w_example_lbl.add_updater(lambda x: x.next_to(w_example, DOWN))
		scale_v_example = Line(start=example_plane.c2p(0,0), 
			end=example_plane.c2p(3,-3), color=YELLOW).add_tip()
		scale_v_lbl = Tex(r"3\vec{v}", color=YELLOW).next_to(scale_v_example.get_center())
		scale_v_tex = Tex(r"3\vec{v} = \begin{bmatrix} 3 \\ -3 \end{bmatrix}", color=YELLOW).next_to(w_example_tex, LEFT)
		self.play(Transform(v_example, scale_v_example))
		self.play(Transform(v_example_lbl, scale_v_lbl))
		self.play(Transform(v_example_tex, scale_v_tex))
		self.remove(v_example_lbl)
		scale_w_example = Line(start=example_plane.c2p(0,0),
		end=example_plane.c2p(2,0), color=BLUE).add_tip()
		self.play(Transform(w_example, scale_w_example))
		self.wait()
		example_resultant = Line(start=example_plane.c2p(3,-3), end=example_plane.c2p(5,-3),
			color=BLUE).add_tip()
		self.play(Transform(w_example, example_resultant))
		self.remove(w_example_lbl)
		self.wait()

		vec_sum = Line(start=example_plane.c2p(0,0), end=example_plane.c2p(5,-3),
			color=PURPLE).add_tip()
		vec_sum_lbl = Tex(r"3\vec{v} - \vec{w}", color=PURPLE).next_to(vec_sum.get_center(), 1.25*RIGHT)
		vec_sum_tex = Tex(r"3\vec{v} - \vec{w} = \begin{bmatrix} 5 \\ -3 \end{bmatrix}", color=PURPLE).to_edge(RIGHT)
		self.wait()
		self.play(ShowCreation(vec_sum))
		self.play(Write(vec_sum_lbl))
		self.play(Write(vec_sum_tex))
		self.wait()

		self.clear()
		final_text = Text("Made By S.Mahdi Mirfendereski",font="Noto Sans")
		self.play(Write(final_text, run_time=2))
		self.wait()