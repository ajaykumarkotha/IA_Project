import sys
from attendance import AttendanceCalculator
from strategies.ConsecutiveAbsenceStrategy import ConsecutiveAbsenceStrategy


def main():
    try:
        days = int(sys.argv[1])
        strategy = ConsecutiveAbsenceStrategy()
        attendance_calculator = AttendanceCalculator(strategy, days)
        number_of_valid_ways = attendance_calculator.get_number_of_ways_to_attend()
        number_of_invalid_attendance_patterns = (
            attendance_calculator.probability_to_miss_gradution_ceremony()
        )

        print(f"{number_of_invalid_attendance_patterns}/{number_of_valid_ways}")
    except IndexError:
        print("Please pass 'days' argument in command line")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
