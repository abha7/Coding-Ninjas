# taking input from the user
number = int(input("Enter any number: "))
isPrime= True #Boolean to store if number is prime or not
if number > 1: # prime number is always greater than 1
   i=2
   while i< number:
      if (number % i) == 0: # Checking for positive divisors
        isPrime= False
        break
      i=i+1
if(number<=1): # If number is less than or equal to 1
   print("Is Not Prime")
elif(isPrime): # If Boolean is true
   print("Is Prime")
else:
   print("Is Not Prime")



# num = int(input("Enter the number: "))
# prime=True

# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print("This number is Prime")
# else:
#     print("This number is not Prime")
hdjhjfhaldsjjn
sjdfjj