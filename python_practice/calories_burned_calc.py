import csv


class CalorieCalculator:
    def __init__(self):
        self.exercise = None
        self.weight = None
        self.exerciseHours = None
        self.exerciseMin = None
        self.exerciseSec = None

    def metVals(self):
        metSports = "01 Participating in Sports, Exercise, or Recreation"
        sportsMetVals = {}
        metFile = "atus-met_table3.csv"

        with open(metFile, newline='') as metFile:
            metReaderDict = csv.DictReader(metFile)
            sportsMetVals = {row['Specific Category']: row['Summary MET value']
                             for row in metReaderDict if row['General Category'] == metSports}
        return sportsMetVals

    def fuzzyMatch(self, pattern, string):
        return pattern.lower() in string.lower()

    def findExercise(self):
        metVals = self.metVals()
        validExercises = list(metVals.keys())
        while True:
            self.exercise = input("Enter your exercise: ").strip()
            matchingExercises = [
                exercise for exercise in validExercises if self.fuzzyMatch(self.exercise, exercise)]

            if matchingExercises:
                break
            else:
                print("Invalid exercise. Please try again.")

        if len(matchingExercises) > 1:
            print("Multiple matching exercises found. Please choose one:")
            for i, exercise in enumerate(matchingExercises):
                print(f"{i+1}. {exercise}")

            choice = int(input("Enter your exercise choice: "))
            self.exercise = matchingExercises[choice - 1]
        else:
            self.exercise = matchingExercises[0]

        metVal = metVals[self.exercise]
        return float(metVal)

    def calcWeight(self):
        while True:
            try:
                self.weight = float(input("Enter Your Weight (in lbs): "))
                break
            except ValueError:
                print("Invalid Weight, please try again.")

        kgs = self.weight * 0.45359237
        return kgs

    def validTime(self, prompt, minVal, maxVal):
        while True:
            try:
                value = (int(input(prompt)))
                if minVal <= value <= maxVal:
                    return value
                else:
                    print(
                        f"Invalid value. Please enter a number between {minVal} and {maxVal}.")
            except ValueError:
                print("Invalid Value. Please Enter a Valid Integer")

    def calcTime(self):
        self.exerciseHours = self.validTime(
            "Enter the number of hours exercised: ", 0, 24)
        self.exerciseMin = self.validTime(
            "Enter the number of minutes exercised: ", 0, 60)
        self.exerciseSec = self.validTime(
            "Enter the number of seconds exercised: ", 0, 60)

        timeExercising = float(
            self.exerciseHours) + float(self.exerciseMin / 60) + float(self.exerciseSec / 360)
        return timeExercising

    def calcCalories(self):
        calories = self.findExercise() * self.calcWeight() * self.calcTime()
        return calories


findCalories = CalorieCalculator()
calories = findCalories.calcCalories()
print("Exercise Calories: ", round(calories, 2))
