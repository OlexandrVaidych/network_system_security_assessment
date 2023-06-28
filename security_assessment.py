import math


class SecurityAssessment:

    def calculate_x(self, value, term):

        if ((value >= 0) & (value <= 0.5)):
            x = math.sqrt(value / 2) * (term[1] - term[0]) + term[0]
        else:
            x = term[1] - math.sqrt((1 - value) / 2) * (term[1] - term[0])

        return round(x, 2)

    def assess_security(self, values, weight_coefficients, terms):
        T1 = [0, 20]
        T2 = [20, 40]
        T3 = [40, 60]
        T4 = [60, 80]
        T5 = [80, 100]

        x1 = self.calculate_x(values[0], T2)
        x2 = self.calculate_x(values[1], T2)
        x3 = self.calculate_x(values[2], T4)
        x4 = self.calculate_x(values[3], T3)
        x5 = self.calculate_x(values[4], T1)
        x6 = self.calculate_x(values[5], T1)

        x = [x1, x2, x3, x4, x5, x6]

        print(x)