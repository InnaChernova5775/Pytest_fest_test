from app.calculator import Calculator
class TestCaLc:
    def setup (self):
        self.calc= Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 2)== 6

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2)== 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 2)== 3

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 4, 3)== 7





