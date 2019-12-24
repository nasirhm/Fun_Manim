from manimlib.imports import *

class LightSourcePhoton(Scene):
    def construct(self):

        Amplitude = 0.4
        freq = 3
        angular_freq = (2*np.pi)*freq
        equation = lambda t: Amplitude*np.sin(t*angular_freq)

        photon = FunctionGraph(equation,x_min=-5,x_max=-4)
        light_source = Dot(photon.points[0], radius=0.5, color=YELLOW)

        tip = Arrow(photon.points[-1],photon.points[-1]+RIGHT*0.4)
        self.play(GrowFromCenter(light_source))
        self.play(ShowCreation(photon))
        self.play(ShowCreation(tip))
        photon.add(tip)

        animation = ApplyMethod(photon.shift, (6,0,0))
        self.play(animation)

