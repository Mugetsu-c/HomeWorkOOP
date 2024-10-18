
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first_name: str, last_name: str, position: str, salary: float):
        """
        Initialize an Employee object with the given parameters.

        Parameters:
        first_name (str): The first name of the employee.
        last_name (str): The last name of the employee.
        position (str): The position of the employee.
        salary (int): The salary of the employee. Must be a non-negative integer.

        Raises:
        ValueError: If the salary is a negative integer.
        """
        if salary < 0:
            raise ValueError("Salary must be a non-negative integer.")
        self._first_name = first_name
        self._last_name = last_name
        self._position = position
        self._salary = salary

    def __repr__(self) -> str:
        """
        Return a string representation of the Employee object.

        The string representation includes the class name, first name, last name, position, and salary.

        Returns:
        str: A string representation of the Employee object.
        """
        return f"""{self.__class__.__name__}: 
        Имя: {self._first_name}, 
        Фамилие: {self._last_name}, 
        Должность: {self._position}, 
        Зарплата: {self._salary}"""

    @abstractmethod
    def get_bonus(self) -> float:
        pass

class Manager(Employee):
    def get_bonus(self) -> float:
        """
        Calculate and return the bonus amount for the employee based on their position.

        The bonus is calculated as a percentage of the employee's salary.
        - Manager: 20% of the salary

        Parameters:
        self (Employee): The instance of the Employee class.

        Returns:
        float: The bonus amount for the employee.
        """
        return self._salary * 0.20

class Developer(Employee):
    def get_bonus(self):
        """
        Calculate and return the bonus amount for the employee based on their position.

        The bonus is calculated as a percentage of the employee's salary.
        - Developer: 15% of the salary

        Parameters:
        self (Employee): The instance of the Employee class.

        Returns:
        float: The bonus amount for the employee.
        """
        return self._salary * 0.15

class Designer(Employee):
    def get_bonus(self) -> float:
        """
        Calculate and return the bonus amount for the employee based on their position.

        The bonus is calculated as a percentage of the employee's salary.
        - Designer: 10% of the salary

        Parameters:
        self (Employee): The instance of the Employee class.

        Returns:
        float: The bonus amount for the employee.
        """
        return self._salary * 0.10

# Пример использования
employees = [
    Manager("Иван", "Иванов", "Менеджер", 100000),
    Developer("Петр", "Петров", "Разработчик", 80000),
    Designer("Анна", "Смирнова", "Дизайнер", 70000)
]

for employee in employees:
    print(employee.get_bonus())
