from strategies.BaseStrategy import BaseStrategy


class ConsecutiveAbsenceStrategy(BaseStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.cache = {}

    def _get_number_of_ways(self, n, consecA):
        """
        Calculate the number of valid ways to attend classes over a given number of days,
        considering the consecutive absence restriction.

        Args:
            n (int): The remaining number of days to calculate ways for.
            consecA (int): The count of consecutive absent days.

        Returns:
            int: The number of valid ways to attend classes.
        """

        # Check if the result is already in the cache
        if (n, consecA) in self.cache:
            return self.cache[(n, consecA)]

        # Base case: no more days left
        if n == 0:
            return 1

        ways = 0

        # Recursively calculate ways considering consecutive absence limit
        if consecA < 3:
            ways += self._get_number_of_ways(n - 1, consecA + 1)
        ways += self._get_number_of_ways(n - 1, 0)

        self.cache[(n, consecA)] = ways
        return ways

    def calculate_ways(self, n):
        # calculate all the valid ways
        return self._get_number_of_ways(n, 0)

    def calculate_number_of_invalid_attendance_patterns(self, n):
        """
        Calculate the probability of missing the graduation ceremony based on the number of days and
        the allowed consecutive absence limit.

        By considering the last day as absent by default (to account for missing the graduation ceremony),
        this method calculates the valid ways for the remaining days.

        Returns:
            int: The probability of missing the graduation ceremony.
        """
        return self._get_number_of_ways(n - 1, 1)
