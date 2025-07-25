import random
from typing import List

from CSP.Problem import Problem
from CSP.Variable import Variable
from crossmathConstraint import CrossMathConstraint

class CrossMathProblem(Problem):
    def __init__(self):
        super().__init__([], [])

        variables = {
            'A': Variable[int]([20, 17, 12, 10, 9, 5], 'A'),
            'A1': Variable[int]([7], 'A1'),
            'A2': Variable[int]([17], 'A2'),
            'B': Variable[int]([20, 17, 12, 10, 9, 5], 'B'),
            'B2': Variable[int]([19], 'B2'),
            'C': Variable[int]([20, 17, 12, 10, 9, 5], 'C'),
            'D': Variable[int]([20, 17, 12, 10, 9, 5], 'D'),
            'E': Variable[int]([20, 17, 12, 10, 9, 5], 'E'),
            'E2': Variable[int]([10], 'E2'),
            'F': Variable[int]([20, 17, 12, 10, 9, 5], 'F'),
            'F1': Variable[int]([3], 'F1')
        }

        # Set fixed values
        variables['A1'].value = 7
        variables['A2'].value = 17
        variables['B2'].value = 19
        variables['E2'].value = 10
        variables['F1'].value = 3

        # Define constraints
        constraints = [
            CrossMathConstraint([variables['A'], variables['A1'], variables['A2']]),
            CrossMathConstraint([variables['A'], variables['B'], variables['B2']]),
            CrossMathConstraint([variables['B2'], variables['C'], variables['A1']]),
            CrossMathConstraint([variables['A1'], variables['D'], variables['C']]),
            CrossMathConstraint([variables['E'], variables['A1'], variables['E2']]),
            CrossMathConstraint([variables['E'], variables['F1'], variables['F']])
        ]

        self.constraints = constraints
        self.variables = list(variables.values())

    def print_assignments(self):
        for variable in self.variables:
            if variable.name in ['A', 'B', 'C', 'D', 'E', 'F']:
                print(f"{variable.name} is set to {variable.value}")


problem = CrossMathProblem()
