
from hypothesis import given, strategies as st
from gym_membership import parse_plan, calculate_bmi, average_workout


@given(st.text() | st.none())
def test_parse_plan_no_crash(s):
    try:
        parse_plan(s)
    except Exception as e:
        assert False, f"parse_plan crashed with input {s!r}: {e}"


@given(st.text() | st.none())
def test_calculate_bmi_no_crash(s):
    try:
        calculate_bmi(s)
    except Exception as e:
        assert False, f"calculate_bmi crashed with input {s!r}: {e}"


@given(st.text() | st.none())
def test_average_workout_no_crash(s):
    try:
        average_workout(s)
    except Exception as e:
        assert False, f"average_workout crashed with input {s!r}: {e}"
