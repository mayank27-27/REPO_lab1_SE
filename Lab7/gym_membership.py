
def parse_plan(code):
    try:
        if not isinstance(code, str):
            return "", 0

        parts = code.split('-')

        if len(parts) != 2:
            return "", 0

        plan, months = parts

        if not plan.strip() or not months.strip():
            return "", 0

        months = int(months)

        if months <= 0:
            return "", 0

        return plan.strip().upper(), months

    except (ValueError, TypeError):
        return "", 0


def calculate_bmi(data):
    try:
        if not isinstance(data, str):
            return 0.0

        parts = data.split(',')

        if len(parts) != 2:
            return 0.0

        weight, height = map(float, parts)

        if weight <= 0 or height <= 0:
            return 0.0

        return round(weight / (height ** 2), 1)

    except (ValueError, TypeError, OverflowError):
        return 0.0


def average_workout(minutes):
    try:
        if not isinstance(minutes, str) or not minutes.strip():
            return 0

        values = [int(m) for m in minutes.split()]

        if not values or any(m < 0 for m in values):
            return 0

        return sum(values) // len(values)

    except (ValueError, TypeError, OverflowError):
        return 0


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    print("Plan and Months:", result)

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    print("BMI:", result)

    print("\n==== Running average_workout ====")
    user_input = input("Enter workout minutes separated by spaces (e.g. 45 60 30): ")
    result = average_workout(user_input)
    print("Average Minutes:", result)


if __name__ == "__main__":
    main()
