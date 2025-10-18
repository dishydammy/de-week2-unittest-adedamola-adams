# Artificial Pancreas System

## Overview

This project is a simplified model of an Artificial Pancreas System (APS). It simulates how the glucose level in a human body is affected by meals and exercise, and how insulin can be administered to regulate the glucose level. The system can also recommend actions to take based on the current glucose level.

## Implemented Features

*   **Meal Simulation:** The `meal` function simulates the effect of eating a meal by increasing the glucose level based on the number of carbohydrates consumed.
*   **Exercise Simulation:** The `exercise` function simulates the effect of physical activity by decreasing the glucose level based on the duration of the exercise.
*   **Insulin Delivery:** The `deliver_insulin` function simulates the delivery of insulin, which lowers the glucose level.
*   **Action Recommendation:** The `recommend_action` function provides recommendations on whether to eat, take insulin, or do nothing, based on the current glucose level. It can also automatically apply the recommended action.
*   **Unit Tests:** The project includes a suite of unit tests written using `pytest` to ensure the correctness of the system's logic.

## Project Structure

```
.
├── main
│   ├── __init__.py
│   └── artificial_pancreas.py
├── tests
│   ├── __init__.py
│   └── test_artificial_pancreas.py
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

*   Python 3.7+
*   pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/dishydammy/de-week2-unittest-adedamola-adams.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd de-week2-unittest-adedamola-adams
    ```
3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The main logic is in the `ArtificialPancreasSystem` class in `main/artificial_pancreas.py`. You can create an instance of this class and use its methods to simulate the system.

```python
from main.artificial_pancreas import ArtificialPancreasSystem

# Create a new APS instance
aps = ArtificialPancreasSystem(glucose_level=120)

# Simulate a meal
aps.meal(carbs=50)
print(f"Glucose after meal: {aps.glucose_level}")

# Simulate exercise
aps.exercise(duration=30)
print(f"Glucose after exercise: {aps.glucose_level}")

# Get a recommendation
message, action = aps.recommend_action()
print(f"Recommendation: {message}, {action}")

# Get a recommendation and auto-apply it
message, action = aps.recommend_action(auto_apply=True)
print(f"Recommendation: {message}, {action}")
print(f"Glucose after auto-apply: {aps.glucose_level}")
```

## Running Tests

To run the tests, navigate to the project's root directory and run the following command:

```bash
pytest -v
```