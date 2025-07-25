from CSP.Constraint import Constraint

class CrossMathConstraint(Constraint):
    def __init__(self, variables):
        super().__init__(variables)

    def is_satisfied(self):
        values = [var.value for var in self.variables]
        if None in values:
            return True
        a, b, c = values
        return a + b == c or a - b == c
