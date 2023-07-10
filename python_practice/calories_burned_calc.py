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
            for row in metReaderDict:
                if row['General Category'] == metSports:
                    specCat = row['Specific Category']
                    metVal = row['Summary MET value']
                    sportsMetVals[specCat] = metVal
        return sportsMetVals

    def fuzzyMatch(self, pattern, string):
        pattern = pattern.lower()
        string = string.lower()
        return pattern in string

    def findExercise(self):
        metVals = self.metVals()
        validExercises = list(metVals.keys())

        self.exercise = input("Enter in your exercise: ")

        matchingExercises = [exercise for exercise in validExercises if self.fuzzyMatch(
            self.exercise, exercise)]
        print(matchingExercises)

        while not matchingExercises:
            print("invalid Exercise")
            self.exercise = input("Enter in your exercise: ")

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
                print("invalid Weight")

        kgs = float(self.weight) * 0.45359237
        return kgs

    def calcTime(self):
        while True:
            try:
                self.exerciseHours = int(
                    input("Enter in the number of hours exercised: "))
                break
            except ValueError:
                print("not a correct value. try again")
        while True:
            try:
                self.exerciseMin = int(
                    input("Enter in the number of minutes exercised: "))
                if 0 <= self.exerciseMin <= 60:
                    break
                else:
                    print("not a valid minute number, please enter between 0-60.")
            except ValueError:
                print("not a correct value. try again")
        while True:
            try:
                self.exerciseSec = int(
                    input("Enter in the number of seconds exercised: "))
                if 0 <= self.exerciseSec <= 60:
                    break
                else:
                    print("not between 0-60. please enter in again.")
            except ValueError:
                print("not a correct value. try again")

        timeExercising = float(
            self.exerciseHours) + float(self.exerciseMin / 60) + float(self.exerciseSec / 360)
        return timeExercising

    def calcCalories(self):
        calories = self.findExercise() * self.calcWeight() * self.calcTime()
        return calories


findCalories = CalorieCalculator()
calories = findCalories.calcCalories()
print("Exercise Calories: ", calories)
