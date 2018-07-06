#Question1

year=(int(input("Enter the year")))
if (year%4==0 and year%100==0 and year%400==0):
    print ("Leap year")
else :
    print("Not a leap year")

#Question2

l= int(input("Enter the length"))
b= int(input("Enter the breadth"))

if (l==b):
    print("This is a Square")
else:
        print("This is a Rectangle")

#Question3

age1= int(input("Enter the first age"))
age2= int(input("Enter the second age"))
age3= int(input("Enter the third age"))

if (age1>age2 and age1>age3):
    if (age2>age3):
        print("First is oldest and Third is youngest")
    else:
         print("First is oldest and Second is youngest")
elif(age2>age3 and age1>age3):
    print("Second is oldest and Third is youngest")
elif(age2>age3 and age3>age1):
    print("Second is oldest and First is youngest")
elif(age2>age1 ):
    print("Third is oldest and First is youngest")
else:
    print("Third is oldest and Second is youngest")

#Question4

points=int(input("Enter the point"))
if (points>=1 and points<=50):
   print("No Prize")
elif (points>=51 and points<=150):
    print("You won a Wooden Dog")
elif (points>=151 and points<=180):
    print("You won a Book")
elif (points>=181 and points<=200):
    print("You won Chocolates")
else:
    print("Sorry! No prize this time")

#Question5

units=int(input("Enter the units"))
cost= units*100
if (cost>1000):
    disc=cost/10
    print("Total cost= ",cost-disc)
else:
    print("Total Cost= ",cost)
    


