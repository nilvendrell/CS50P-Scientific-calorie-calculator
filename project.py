import csv
from tabulate import tabulate
import os


def main():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    name = input("What's your name?: ")
    weight, height, age, gender = Get_Properties()
    bmr = BMR(weight, height, age, gender)
    print()
    print(f"Your Basal Metabolic Rate is {bmr:.1f} calories.")
    Clear()
    print("For calculating your calories of maintenance we need to know your level of activity:")
    tdee=TDEE(bmr)
    print()
    print(f"Your Total Daily Energy Expenditure is {tdee:.1f} calories.")
    Clear()
    print("For calculating your calories we need to know your objective:")
    kcal=Calories(tdee)
    print()
    print(f"You need to eat {kcal:.1f} calories every day!")
    Clear()
    print(f"DASHBOARD: {name}")
    print()
    print(Macros(weight,kcal))
    print()
    print(f"{kcal:.1f} calories")
    print(f"And everyday you must drink {Water(weight)}")
    print("\n\n\n")


def Get_Properties():
    while True:
        try:
            weight = float(input("How much do you weight? (in kg): "))
            height = float(input("How tall are you? (in cm): "))
            age = float(input("How old are you?: "))
            break
        except ValueError:
            print()
            print("Please enter the correct format (Only the number, can be a decimal number)")
    while True:
        try:
            gender = input("If you consider male press m, if you consider female press f: ")
            if gender not in ["f","m"]:
                raise ValueError
            break
        except ValueError:
            print()
            print("Please enter the correct format (f or m)")
    if gender == "f":
        gender = -161
    else:
        gender = 5

    return weight, height, age, gender

def BMR(weight, height, age, gender):
    return 10 * weight + 6.25 * height - 5 * age + gender


def TDEE(BMR):
    with open("activity.csv") as file:
        reader = csv.reader(file)
        header=next(reader)
        print(tabulate(reader,header,tablefmt="pretty",showindex=True))
    print("What is your level of exercise?")
    while True:
        try:
            level_of_activity = int(input("Press 0,1,2,3 or 4: "))
            if level_of_activity not in [0,1,2,3,4]:
                raise ValueError
            break
        except ValueError:
            pass
    match level_of_activity:
        case 0:
            level_of_activity = 1.2
        case 1:
            level_of_activity = 1.375
        case 2:
            level_of_activity = 1.55
        case 3:
            level_of_activity = 1.725
        case 4:
            level_of_activity = 1.9
    return BMR * level_of_activity

def totalexpenditure(BMR,level_of_activity):
    match level_of_activity:
        case 0:
            level_of_activity = 1.2
        case 1:
            level_of_activity = 1.375
        case 2:
            level_of_activity = 1.55
        case 3:
            level_of_activity = 1.725
        case 4:
            level_of_activity = 1.9
    return BMR * level_of_activity

def Calories(TDEE):
    print(tabulate(([["Lose weight fastly"],["Lose weight softly"],["Maintain my weight"],["Gain weight softly"],["Gain weight fastly"]]),tablefmt="grid",showindex=True))
    print("What is your objective?")
    while True:
        try:
            deficit = int(input("Press 0,1,2,3 or 4: "))
            if deficit not in [0,1,2,3,4]:
                raise ValueError
            break
        except ValueError:
            pass
    match deficit:
        case 0:
            deficit = -500
        case 1:
            deficit = -300
        case 2:
            deficit = 0
        case 3:
            deficit = 300
        case 4:
            deficit = 500
    return TDEE + deficit

def Clear():
    _=input("Press enter to continue")
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def Macros(weight, calories):
    protein_g = round(1.6 * weight, 1)
    protein_kcal = round(protein_g * 4, 1)
    protein_percent = round(protein_kcal / calories * 100, 1)
    fat_kcal = round(calories * 0.3, 1)
    fat_g = round(fat_kcal / 9, 1)
    fat_percent = round(fat_kcal / calories * 100, 1)
    carbohydrates_kcal = round(calories - protein_kcal - fat_kcal, 1)
    carbohydrates_g = round(carbohydrates_kcal / 4, 1)
    carbohydrates_percent = round(carbohydrates_kcal / calories * 100, 1)
    table = [
        [f"{protein_percent}%", f"{carbohydrates_percent}%", f"{fat_percent}%"],
        [f"{protein_kcal} kcal", f"{carbohydrates_kcal} kcal", f"{fat_kcal} kcal"],
        [f"{protein_g} g", f"{carbohydrates_g} g", f"{fat_g} g"],
    ]
    return tabulate(table, headers=["protein", "carbohydrates", "fat"], tablefmt="grid")


def Water(weight):
    return f"{weight*0.035:.3f} l"


if __name__ == "__main__":
    main()
