class AttendanceCalculator:
    def __init__(self, strategy, n):
        self.strategy = strategy
        self.n = n

    def get_number_of_ways_to_attend(self):
        return self.strategy.calculate_ways(self.n)

    def probability_to_miss_gradution_ceremony(self):
        return self.strategy.calculate_number_of_invalid_attendance_patterns(self.n)
