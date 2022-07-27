print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_Case_name=name1.lower()
LcnC1 =lower_Case_name.count("t")
LcnC2 =lower_Case_name.count("r")
LcnC3 =lower_Case_name.count("u")
LcnC4 =lower_Case_name.count("e")
LcnC5 =lower_Case_name.count("l")
LcnC6 =lower_Case_name.count("o")
LcnC7 =lower_Case_name.count("v")
LcnC8 =lower_Case_name.count("e")
LcnC_sum = LcnC1+LcnC2+LcnC3+LcnC4+LcnC5+LcnC6+LcnC7+LcnC8
#name2 calculation
lower_Case_name2=name2.lower()
Lcn2C1 =lower_Case_name2.count("t")
Lcn2C2 =lower_Case_name2.count("r")
Lcn2C3 =lower_Case_name2.count("u")
Lcn2C4 =lower_Case_name2.count("e")
Lcn2C5 =lower_Case_name2.count("l")
Lcn2C6 =lower_Case_name2.count("o")
Lcn2C7 =lower_Case_name2.count("v")
Lcn2C8 =lower_Case_name2.count("e")
Lcn2C_sum = Lcn2C1+Lcn2C2+Lcn2C3+Lcn2C4+Lcn2C5+Lcn2C6+Lcn2C7+Lcn2C8
loveScore=(str(LcnC_sum)+str(Lcn2C_sum))
if int(loveScore) <10 or int(loveScore)>90:
  print(f"your score is {loveScore},you go together like coke and mentos")
elif int(loveScore) in range(40,50):
      print(f"your score is {loveScore},you are alright together")
else:
    print(f"your score is {loveScore}.")        






