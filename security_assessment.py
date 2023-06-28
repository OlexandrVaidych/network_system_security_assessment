import math


class SecurityAssessment:

    def determine_security_assessment(self, security_assessment):
        if (security_assessment > 0.8) & (security_assessment <= 1):
            security_assessment_str = "low"
        elif (security_assessment > 0.6) & (security_assessment <= 0.8):
            security_assessment_str = "below average"
        elif (security_assessment > 0.4) & (security_assessment <= 0.6):
            security_assessment_str = "middle"
        elif (security_assessment > 0.2) & (security_assessment <= 0.4):
            security_assessment_str = "above average"
        else:
            security_assessment_str = "high"

        return f"Security assessment is {security_assessment} - {security_assessment_str}"

    def calculate_security_assessment(self, norm_weight_coeffs, x_norm):
        assessment = 0

        for i in range(len(x_norm)):
            assessment += norm_weight_coeffs[i] * (1 - x_norm[i])

        return round(assessment, 3)

    def calculate_norm_weight_coeffs(self, weight_coeffs):
        norm_weight_coeffs = []

        sum_weight_coeffs = sum(weight_coeffs)

        for weight_coeff in weight_coeffs:
            norm_weight_coeffs.append(round(weight_coeff / sum_weight_coeffs, 3))

        return norm_weight_coeffs

    def calculate_x_normalized(self, x):
        normalized = []

        for i in x:
            normalized.append(round(i / 100, 2))

        return normalized

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

        x_normalized = self.calculate_x_normalized(x)

        normalized_weight_coeffs = self.calculate_norm_weight_coeffs(weight_coefficients)

        security_assessment = self.calculate_security_assessment(normalized_weight_coeffs, x_normalized)

        security_assessment_str = self.determine_security_assessment(security_assessment)
        print(security_assessment_str)
