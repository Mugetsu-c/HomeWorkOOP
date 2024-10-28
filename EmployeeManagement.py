from abc import ABC


class Employee(ABC):
    """
    Base class for all employees.
    """

    
    def __init__(self, first_name: str, last_name: str, position: str, salary: float, bonus: float):
        """
        Initialize an Employee object with the given parameters.

        Parameters:
        first_name (str): The first name of the employee.
        last_name (str): The last name of the employee.
        position (str): The position of the employee.
        salary (float): The salary of the employee. Must be a non-negative float.
        bonus (float): The bonus percentage of the employee. Must be a non-negative

        Raises:
        ValueError: If the salary is a negative integer.
        """
        if salary < 0:
            raise ValueError("Salary must be a non-negative number.")
        if bonus < 0:
            raise ValueError("Bonus percentage must be a non-negative number.")
        self._first_name = first_name
        self._last_name = last_name
        self._position = position
        self._salary = salary
        self._bonus = bonus

    def __repr__(self) -> str:
        """
        Return a string representation of the Employee object.

        The string representation includes the class name, first name, last name, position, and salary.

        Returns:
        str: A string representation of the Employee object.
        """
        return f"""{self.__class__.__name__}: 
        Имя: {self._first_name}, 
        Фамилия: {self._last_name}, 
        Должность: {self._position}, 
        Зарплата: {self._salary}"""

    def get_bonus(self) -> float:
        """
        Calculate and return the bonus amount for the employee based on their position.
        
        The bonus is calculated as a percentage of the employee's salary.
        - Manager: 20% of the salary
        - Developer: 15% of the salary
        - Designer: 10% of the salary

        Returns:
        float: The bonus amount for the employee.
        """
        return self._salary * self._bonus


class Manager(Employee):
    def __init__(self, first_name, last_name, position, salary):
        super().__init__(first_name, last_name, position, salary, 0.20)


class Developer(Employee):
    def __init__(self, first_name, last_name, position, salary):
        super().__init__(first_name, last_name, position, salary, 0.15)


class Designer(Employee):
    def __init__(self, first_name, last_name, position, salary):
        super().__init__(first_name, last_name, position, salary, 0.10)


def main():
    # Пример использования
    employees = [
        Manager("Иван", "Иванов", "Менеджер", 100000),
        Developer("Петр", "Петров", "Разработчик", 80000),
        Designer("Анна", "Смирнова", "Дизайнер", 70000)
    ]

    for employee in employees:
        print(employee.get_bonus())
        
if __name__ == '__main__':
    main()