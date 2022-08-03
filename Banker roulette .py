import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#names_ln = len(names)
#random_names = random.randint(0,names_ln-1)
#print(names[random_names] + " is going to buy the meal today!")
x = random.choice(names)
print(x + " is going to buy the meal today!")