def prime_checker(number):
  div1 = number / 1
  div2 = number / number
  if div1 == number and div2 ==1:
    print(f"{number} is a prime number.")
  else:
    print("the number is not a prime number")
    
n = int(input("Check this number: "))
prime_checker(number=n)



