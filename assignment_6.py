#Question1

num=[input("Enter the number") for i in range(1)]
print("Numbers entered are", num)


#Question3

num=[int(input("Enter the number")) for i in range(5)]
print("Numbers entered are", num)
num_sq= [i**2 for i in num]
print ("Squares of numbers are " ,num_sq)

#Question4

lst= [1,2,3,'a','b','c',1.0,2.0,3.0]
print("List contains= ", lst)
int_lst = [x for x in lst if isinstance(x, int)]
str_lst = [x for x in lst if isinstance(x, str)]
float_lst = [x for x in lst if isinstance(x, float)]
print (("list for integers = "),int_lst)
print (("list for string   = "),str_lst)
print (("list for float    = "),float_lst)

#Question5
a=[]
for i in range(1,102):
    a.append(i)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("Even list= ", even)
print("Odd list= ",odd)

#Question6

for i in range(0, 4):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")

#Question7

dict = {}
for i in range (5):
    name=input("Enter the name")
    marks=int(input ("Enter marks"))
    dict [name]=marks
    print(dict)

#Question8

lst=[]
for x in range(5):
    s=input("Enter elements")
    lst.append(s)
    print(lst)

d=input("Enter elements to be deleted")
for x in lst:
    if x==d:
        lst.remove(x)
else:
        print("Elements not present")
print("The list is", lst)
    




