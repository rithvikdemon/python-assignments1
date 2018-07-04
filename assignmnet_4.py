#Question1

tup1= (1,2,3,'x','y','z')
print(tup1)
print(len(tup1))

#Question2

tup2= (1,2,3)
tup3= ('x','y','z')
print('Max element in tupel 1 is=', (max(tup2)))
print('Min element in tupel 1 is=', (min(tup2)))
print('Max element in tupel 2 is=', (max(tup3)))
print('Min element in tupel 2 is=', (min(tup3)))

#Question3

tup4= (1,2,3,10,20,30)
print(tup4)
x=1
for i in tup4:
    x=x*i
print(x)

#Question4

seta={input("Enter elements") for i in range (4)}
print (seta)
setb={input("Enter elements") for i in range (4)}
print(setb)

setc= seta & setb
print("Intersection= ", setc)

setd= seta - setb
print("Difference= ", setd)

sete= seta<=setb
print("Compare= ", sete)

#Question5

dict = {}
for i in range (3):
    name=input("Enter the name")
    marks=int(input ("Enter marks"))
    dict [name]=marks
print (dict)

#Question6

print (sorted(dict.items(),key=lambda x:x[1]))

#Question7

dict1= {}
str= "MISSISSIPPI"
m = str.count('M')
i = str.count('I')
s = str.count('S')
p = str.count('P')

dict1['M']=m
dict1['I']=i
dict1['S']=s
dict1['P']=p

print(dict1)
