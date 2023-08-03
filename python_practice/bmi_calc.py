height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(float(weight) / float(height)**2)

bmi_statement = f"Your BMI is {bmi},"

if bmi < 19:
    print(bmi_statement + " you are underweight.")
elif 18 <= bmi < 25:
    print(bmi_statement + " you have a normal weight.")
elif 25 <= bmi < 30:
    print(bmi_statement + " you are slightly obese.")
elif 30 <= bmi < 35:
    print(bmi_statement + " you are obese.")
else:
    print(bmi_statement + " you are clinically obese.")
