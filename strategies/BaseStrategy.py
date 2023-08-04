from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    @abstractmethod
    def calculate_ways(self, n):
        pass

    @abstractmethod
    def calculate_number_of_invalid_attendance_patterns(self, n):
        pass
