height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(int(weight)/int(height*height))
if bmi >= 35:
    print('\033[1m'+f"your BMI is {bmi} ,You are clinically obese")
elif bmi <= 18.5:
    print('\033[1m'+f"your BMI is {bmi} ,You are underweight")
elif bmi in range(19,25) :
    print('\033[1m'+f"your BMI is {bmi},you have a normal weight")
elif bmi in range(25,30) :
    print('\033[1m'+f"your BMI is {bmi},you are slightly overweight")
elif bmi >= 30:
    print('\033[1m'+f"your BMI is {bmi} ,you are obese")
else:
    print('\033[1m'+f"your BMI is {bmi} ,you are obese")    