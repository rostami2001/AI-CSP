import os
import subprocess
import time
from collections import deque
from copy import deepcopy
from typing import Optional, List

from CSP.Problem import Problem
from CSP.Variable import Variable


class Solver:

    def __init__(self, problem: Problem, use_mrv: bool = False, use_lcv: bool = False, use_forward_check: bool = False):
        """
                Initializes the Solver object with the given problem instance and optional parameters.

                Args:
                    problem (Problem): The problem instance to be solved.
                    use_mrv (bool, optional): A boolean indicating whether to use the Minimum Remaining Values heuristic.
                                              Defaults to False.
                    use_lcv (bool, optional): A boolean indicating whether to use the Least Constraining Values heuristic.
                                              Defaults to False.
                    use_forward_check (bool, optional): A boolean indicating whether to use the Forward Checking algorithm.
                                                        Defaults to False.
        """
        self.problem = problem
        self.use_lcv = use_lcv
        self.use_mrv = use_mrv
        self.use_forward_check = use_forward_check
        self.back_up = deque()

    def is_finished(self) -> bool:
        """
                Determines if the problem has been solved.

                Returns:
                    bool: True if the problem has been solved, False otherwise.
        """
        return all([x.is_satisfied() for x in self.problem.constraints]) and len(
            self.problem.get_unassigned_variables()) == 0

    def solve(self):
        """
                Solves the problem instance using the backtracking algorithm with optional heuristics.
        """
        self.problem.calculate_neighbors()
        start = time.time()
        for var in self.problem.variables:
            if not self.forward_check(var):
                print("Problem Unsolvable")
                return
        result = self.backtracking()
        end = time.time()
        time_elapsed = (end - start) * 1000
        if result:
            print(f'Solved after {time_elapsed} ms')
        else:
            print(f'Failed to solve after {time_elapsed} ms')

    def backtracking(self) -> bool:
        """
                Implements the backtracking algorithm.

                Returns:
                    bool: True if the problem has been solved, False otherwise.
        """
        if self.is_finished():
            return True
        var = self.select_unassigned_variable()
        if var is None:  # Add this check
            return False
        original_domain = var.domain.copy()
        ordered_values = self.order_domain_values(var)
        for value in ordered_values:
            self.save_domain(self.problem.variables)
            var.value = value
            if self.forward_check(var):
                result = self.backtracking()
                if result:
                    return True
            var.value = None
            var.domain = original_domain
            self.load_domain(self.problem)
        return False

    def forward_check(self, var: Variable) -> bool:
        """
                Implements the Forward Checking algorithm.

                Args:
                    var (Variable): The variable to be checked.

                Returns:
                    bool: True if the variable is consistent with all constraints, False otherwise.
        """
        "-----------CoMPLETE FROM HERE---"
        for neighbor in var.neighbors:
            if not neighbor.has_value:
                original_domain = neighbor.domain.copy()
                for neighbour_value in original_domain:
                    neighbor.value = neighbour_value
                    if not self.is_consistent(neighbor):
                        neighbor.domain.remove(neighbour_value)
                    neighbor.value = None
                    if len(neighbor.domain) == 0:
                        return False
        return True

    def select_unassigned_variable(self) -> Optional[Variable]:
        """
                Selects an unassigned variable from the problem instance.

                Returns:
                    Optional[Variable]: The selected variable or None if all variables have been assigned.
        """
        if self.use_mrv:
            return self.mrv()
        unassigned_variables = self.problem.get_unassigned_variables()
        return unassigned_variables[0] if unassigned_variables else None

    def order_domain_values(self, var: Variable):
        """
                Orders the domain values of the given variable according to the selected heuristic.

                Args:
                    var (Variable): The variable whose domain values are to be ordered.

                Returns:
                    List: The ordered domain values of the variable.
        """
        if self.use_lcv:
            return self.lcv(var)
        return var.domain

    def mrv(self) -> Optional[Variable]:
        """
                Implements the Minimum Remaining Values heuristic.

                Returns:
                    Optional[Variable]: The variable with the smallest domain or None if all variables have been assigned.
        """
        "-----------CoMPLETE FROM HERE---"
        min_remaining_values = float('inf')
        selected_variable = None
        unassigned_var = self.problem.get_unassigned_variables()
        for var in unassigned_var:
            if len(var.domain) < min_remaining_values:
                selected_variable = var
                min_remaining_values = len(var.domain)
        return selected_variable

    def is_consistent(self, var: Variable) -> bool:
        """
                Determines ifthe given variable is consistent with all constraints.

                Args:
                    var (Variable): The variable to be checked for consistency.

                Returns:
                    bool: True if the variable is consistent with all constraints, False otherwise.
        """
        return all(constraint.is_satisfied() for constraint in self.problem.constraints if var in constraint.variables)

    def lcv(self, var: Variable):
        """
                Implements the Least Constraining Values heuristic.

                Args:
                    var (Variable): The variable whose domain values are to be ordered.

                Returns:
                    List: The domain values of the variable ordered according to the number of conflicts they cause.
        """
        domain_values = var.domain
        constraints = self.problem.get_neighbor_constraints(var)
        conflicts_count = {}
        for value in domain_values:
            var.value = value
            conflicts_count[value] = 0
            for constraint in constraints:
                if not constraint.is_satisfied():
                    conflicts_count[value] += 1
            var.value = None
        ordered_values = sorted(domain_values, key=lambda value: conflicts_count[value])
        return ordered_values

    def save_domain(self, vars: List[Variable]):
        self.back_up.append([var.domain.copy() for var in vars])

    def load_domain(self, problem: Problem):
        domains = self.back_up.pop()
        for i in range(len(problem.variables)):
            problem.variables[i].domain = domains[i]
