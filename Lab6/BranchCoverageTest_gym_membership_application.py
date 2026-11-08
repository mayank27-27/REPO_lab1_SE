
import pytest

from gym_membership import membership_cost, can_enter, bmi_category


# 1. Membership cost - test all decision outcomes

def test_invalid_plan():
    with pytest.raises(ValueError):
        membership_cost("weekly", 25, False, False)


def test_age_below_14():
    with pytest.raises(ValueError):
        membership_cost("monthly", 12, False, False)


def test_senior_discount():
    assert membership_cost("yearly", 65, False, False) == 9000


def test_student_discount():
    assert membership_cost("quarterly", 20, True, False) == 3600


def test_regular_non_student():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_yearly_trainer():
    assert membership_cost("yearly", 30, False, True) == 13500


def test_non_yearly_trainer():
    assert membership_cost("monthly", 30, False, True) == 3500


# 2. Entry permission - test all decision outcomes

def test_inactive_plan():
    assert can_enter(10, False, False, "M") is False


def test_before_opening():
    assert can_enter(4, True, False, "M") is False


def test_after_closing():
    assert can_enter(23, True, False, "M") is False


def test_women_only_female():
    assert can_enter(10, True, True, "F") is True


def test_women_only_male():
    assert can_enter(10, True, True, "M") is False


def test_normal_slot():
    assert can_enter(10, True, False, "M") is True


# 3. BMI category - test all decision outcomes

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


# Boundary value tests

def test_bmi_boundary_18_5():
    assert bmi_category(18.5, 1) == "normal"


def test_bmi_boundary_25():
    assert bmi_category(25, 1) == "overweight"


def test_bmi_boundary_30():
    assert bmi_category(30, 1) == "obese"


def test_entry_at_opening_time():
    assert can_enter(5, True, False, "M") is True


def test_entry_at_closing_time():
    assert can_enter(22, True, False, "M") is True
