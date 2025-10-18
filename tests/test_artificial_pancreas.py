import pytest
from main.artificial_pancreas import ArtificialPancreasSystem

@pytest.fixture
def artificial_pancreas_system():
    """Creates this instance for all tests"""
    return ArtificialPancreasSystem(100, 1.0, 100, 10)

def test_meal(artificial_pancreas_system):
    """Tests that a meal correctly increases glucose level"""
    initial_glucose_level = artificial_pancreas_system.glucose_level
    artificial_pancreas_system.meal(40)
    assert artificial_pancreas_system.glucose_level == initial_glucose_level + 40 * artificial_pancreas_system.GLUCOSE_PER_CARB

def test_exercise(artificial_pancreas_system):
    """Tests that an exercise reduces glucose level"""
    initial_glucose_level = artificial_pancreas_system.glucose_level
    artificial_pancreas_system.exercise(50)
    assert artificial_pancreas_system.glucose_level == initial_glucose_level - 50 * artificial_pancreas_system.GLUCOSE_BURN_PER_MIN

def test_deliver_insulin_high(artificial_pancreas_system):
    """Tests that insulin reduces glucose level when it is too high"""
    artificial_pancreas_system.glucose_level = 120
    initial_glucose_level = artificial_pancreas_system.glucose_level
    artificial_pancreas_system.deliver_insulin(10)
    assert artificial_pancreas_system.glucose_level == initial_glucose_level - 10 * artificial_pancreas_system.insulin_sensitivity

def test_deliver_insulin_normal(artificial_pancreas_system):
    """Tests that insulin is not administered when it is not needed"""
    initial_glucose_level = artificial_pancreas_system.glucose_level
    message = artificial_pancreas_system.deliver_insulin(10)
    assert message == "Glucose level is okay, no need for insulin"

def test_recommend_action_high_glucose(artificial_pancreas_system):
    """Test that the system recommends insulin when glucose is high."""
    artificial_pancreas_system.glucose_level = 130
    message, action = artificial_pancreas_system.recommend_action()
    assert "too high" in message
    assert "Deliver insulin" in action

def test_recommend_action_low_glucose(artificial_pancreas_system):
    """Test that the system recommends carbs when glucose is low."""
    artificial_pancreas_system.glucose_level = 70
    message, action = artificial_pancreas_system.recommend_action()
    assert "too low" in message
    assert "Eat carbs" in action

def test_recommend_action_normal_glucose(artificial_pancreas_system):
    """Test that the system gives an okay when glucose is normal."""
    message, action = artificial_pancreas_system.recommend_action()
    assert "okay" in message
    assert "Maintain" in action

def test_auto_apply_insulin(artificial_pancreas_system):
    """Test that the system auto applies insulin when glucose is high"""
    artificial_pancreas_system.glucose_level = 130
    message, action = artificial_pancreas_system.recommend_action(auto_apply=True)
    assert artificial_pancreas_system.glucose_level <= 120

def test_auto_apply_meal(artificial_pancreas_system):
    """Test that the system auto applies meals when glucose is low"""
    artificial_pancreas_system.glucose_level = 70
    message, action = artificial_pancreas_system.recommend_action(auto_apply=True)
    assert artificial_pancreas_system.glucose_level >= 90

def test_negative_carbs_raise_error(artificial_pancreas_system):
    """Test negative carbs raise ValueError."""
    with pytest.raises(ValueError):
        artificial_pancreas_system.meal(-10)

def test_negative_exercise_raise_error(artificial_pancreas_system):
    """Test negative exercise duration raises ValueError."""
    with pytest.raises(ValueError):
        artificial_pancreas_system.exercise(-20)

def test_invalid_parameters_error():
    """Test that invalid sensitivity or carb values raise a ValueError."""
    system = ArtificialPancreasSystem(glucose_level=100, insulin_sensitivity=0)
    with pytest.raises(ValueError):
        system.recommend_action()