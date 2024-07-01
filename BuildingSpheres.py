


from math import pi
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = 4*pi * self.radius**3 / 3
        self.surface = 4*pi* self.radius**2
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(self.volume,5)
    def get_surface_area(self):
        return round(self.surface,5)
    def get_density(self):
        return round(self.mass/self.volume, 5)
    

    import codewars_test as test
from solution import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        ball = Sphere(2,50)

        test.assert_approx_equals(ball.get_radius(),2, margin=1e-5, message="Check radius")
        test.assert_approx_equals(ball.get_mass(),50, margin=1e-5, message="Check mass")
        test.assert_approx_equals(ball.get_volume(), 33.51032, margin=1e-5, message="Check volume")
        test.assert_approx_equals(ball.get_surface_area(),50.26548, margin=1e-5, message="Check area")
        test.assert_approx_equals(ball.get_density(),1.49208, margin=1e-5, message="Check density")