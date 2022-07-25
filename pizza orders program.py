print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print("your final bill is: $18.")

if size == "S":
    if add_pepperoni == "N":
        if extra_cheese == "N":
            print("your final bill is: $15.")

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "N":
            print("your final bill is: $17.")
if size == "S":
    if add_pepperoni == "N":
        if extra_cheese == "Y":
            print("your final bill is: $16.")
#Medium pizza
if size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print("your final bill is: $24.")

if size == "M":
    if add_pepperoni == "N":
        if extra_cheese == "N":
            print("your final bill is: $20.")

if size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "N":
            print("your final bill is: $23.")
if size == "M":
    if add_pepperoni == "N":
        if extra_cheese == "Y":
            print("your final bill is: $21.")
#Large pizza
if size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print("your final bill is: $29.")
if size == "L":
    if add_pepperoni == "N":
        if extra_cheese == "N":
            print("your final bill is: $25.")            
if size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "N":
            print("your final bill is: $28.")
if size == "L":
    if add_pepperoni == "N":
        if extra_cheese == "Y":
            print("your final bill is: $26.")


            














