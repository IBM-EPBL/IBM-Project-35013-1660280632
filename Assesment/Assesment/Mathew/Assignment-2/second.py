#variables
a=10
b=20
print(a)
print(id(a))
print(a+b)
print(a*b)


a=20.5
print (a)
print(type(a))

#multiple variable 
a,b,c =10,3,20

print(a)
print(b)
print(c)

del b
print(b)

#tuple
tpl ={1,2,3,4,5}
print(tpl)
print(type(tpl))

#ifelse
n=int(input("enter a num:"))
if n%2==0:
    print("even")
else :
    print("odd")


#sample pgm

a=5
b=6
c=7
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of the triangle is %0.2f" %area)
    
