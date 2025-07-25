from abc import ABC, abstractmethod

from CSP.Variable import Variable
from typing import List


class Constraint(ABC):

    def __init__(self, variables: List[Variable]):
        self.variables = variables

    @abstractmethod
    def is_satisfied(self) -> bool:
        return True
