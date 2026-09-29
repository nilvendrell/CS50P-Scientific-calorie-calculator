# Scientific calorie calculator
THIS IS MY FINAL PROJECT FOR CS50P HARVARD COURSE!
#### Video Demo:  https://youtu.be/bHTOdpZcZfo
#### Description:

The Caloric Needs Calculator is a Python application designed to help users calculate their Basal Metabolic Rate (BMR), Total Daily Energy Expenditure (TDEE), and daily caloric needs based on personal characteristics and activity level. The application offers a user-friendly command-line interface and supports customizable activity levels and objectives to tailor the calorie intake recommendations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [project.py](#projectpy)
  - [test_project.py](#test_projectpy)
  - [activity.csv](#activitycsv)
- [Contributing](#contributing)

## Features

- *Calculate BMR*: Estimate the number of calories your body requires at rest using the Mifflin-St Jeor equation.
- *Calculate TDEE*: Adjust calorie needs based on your activity level.
- *Determine Daily Caloric Intake*: Set dietary goals to lose, maintain, or gain weight, and receive personalized daily caloric intake recommendations.
- *Nutritional Breakdown*: Get a macronutrient breakdown for protein, carbohydrates, and fats.
- *Hydration Recommendation*: Receive daily water intake suggestions based on body weight.
- *User-friendly Interface*: Navigate through clear prompts and interactive elements.
- *Automated Testing*: Verify the accuracy of calculations using unit tests with pytest.

## Installation

1. *Clone the Repository*:
    bash
    git clone https://github.com/your-username/caloric-needs-calculator.git
    cd caloric-needs-calculator


2. *Install Dependencies*:
    Make sure you have Python installed. Then install the required Python packages:
    bash
    pip install -r requirements.txt


3. *Run the Program*:
    Execute the main script to start the application:
    bash
    python project.py


4. *Run Tests*:
    Use pytest to ensure everything is working correctly:
    bash
    pytest test_project.py


## Usage

When you run the program, you'll be prompted to input your weight, height, age, and gender. Then, select your activity level and dietary goal to get personalized recommendations.

### Example Usage

1. *Input Personal Information*:
   - Enter your weight (in kg).
   - Enter your height (in cm).
   - Enter your age.
   - Specify your gender (m for male, f for female).

2. *Select Activity Level*:
   Choose from the list provided in activity.csv:
[5:58 p. m., 7/8/2024] Noah Vendrell: 3. *Choose Dietary Goal*:
Select your objective:
[5:58 p. m., 7/8/2024] Noah Vendrell: 4. *View Results*:
- *BMR*: Your Basal Metabolic Rate.
- *TDEE*: Your Total Daily Energy Expenditure.
- *Daily Caloric Needs*: Calories to achieve your selected goal.
- *Macros*: Breakdown of protein, carbohydrates, and fat.
- *Water Intake*: Recommended daily water intake.

## Code Overview

### project.py

The main script includes the following functions:

- main(): Orchestrates the workflow, prompting the user for inputs and calculating BMR, TDEE, and daily caloric needs.
- Get_Properties(): Collects user information such as weight, height, age, and gender.
- BMR(weight, height, age, gender): Computes the Basal Metabolic Rate.
- TDEE(bmr): Calculates Total Daily Energy Expenditure using the activity level.
- Calories(tdee): Adjusts caloric needs based on the user's objective.
- Macros(weight, calories): Provides macronutrient breakdown.
- Water(weight): Suggests daily water intake.
- Clear(): Clears the console for a clean interface.

### test_project.py

Contains unit tests for validating the core functions:

- test_BMR(): Tests BMR calculations for different genders.
- test_totalexpenditure(): Verifies TDEE calculations across activity levels.
- test_Water(): Checks the accuracy of water intake recommendations.

### activity.csv

The CSV file lists various activity levels with corresponding multipliers and descriptions. It's used to calculate TDEE based on user input.

| Level              | Multiplier | Description                          |
|--------------------|------------|--------------------------------------|
| Sedentary          | 1.2        | Desk job, minimal exercise           |
| Lightly active     | 1.375      | Exercise 1-3 days/week               |
| Moderately active  | 1.55       | Exercise 3-5 days/week               |
| Very active        | 1.725      | Exercise 6-7 days/week               |
| Excessively active | 1.9        | Intense double daily workouts        |

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/your-feature-name)
3. Commit your changes (git commit -m 'Add some feature')
4. Push to the branch (git push origin feature/your-feature-name)
5. Open a pull request

