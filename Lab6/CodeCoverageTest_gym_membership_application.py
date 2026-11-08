
import pytest

from gym_membership import membership_cost, can_enter, bmi_category


# 1. Membership cost tests

def test_invalid_plan():
    with pytest.raises(ValueError):
        membership_cost("weekly", 25, False, False)


def test_age_below_14():
    with pytest.raises(ValueError):
        membership_cost("monthly", 12, False, False)


def test_senior_with_yearly_trainer():
    result = membership_cost("yearly", 65, False, True)
    assert result == 10500


def test_student_membership():
    result = membership_cost("monthly", 20, True, False)
    assert result == 1350


# 2. Entry permission tests

def test_inactive_plan():
    assert can_enter(10, False, False, "M") is False


def test_entry_before_opening():
    assert can_enter(4, True, False, "M") is False


def test_women_only_slot():
    assert can_enter(10, True, True, "F") is True


def test_normal_slot():
    assert can_enter(10, True, False, "M") is True


# 3. BMI category tests

def test_invalid_height():
    with pytest.raises(ValueError):
        bmi_category(60, 0)


def test_underweight():
    assert bmi_category(17, 1) == "underweight"


def test_normal_bmi():
    assert bmi_category(22, 1) == "normal"


def test_overweight():
    assert bmi_category(27, 1) == "overweight"


def test_obese():
    assert bmi_category(32, 1) == "obese"
