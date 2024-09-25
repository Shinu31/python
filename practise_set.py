
#Sum of 2 no by taking input

'''a = int(input("enter first number:"))
b = int(input ("enter second number:"))
 
print("sum =",a + b)


------------------------------------------------------



#WAP to input side of a square and print its area
side =int (input("Enter side:"))

print("area = ",side * side )  #or side ** 2 
---------------------------------------------


#WAP to check if number entered by the user is odd or even
nm = int(input("Enter ur number :"))
if nm % 2 ==0:
    print("Even")
else:
    print("Odd")

------------------------------------------------

#WAP to find greatest of 3 number entered by user


nm1 = int(input("Enter ur first number:"))
nm2 = int(input("Enter ur Second number:"))
nm3 = int(input("Enter ur Third number:"))
if (nm1 > nm2)and(nm1>nm3):      # or  (nm1 > nm2 > nm3):  
   
    print(nm1," is greatest ")
elif (nm2 >nm3):
    print(nm2,"is greatest")
else:
    print(nm3,"is greatest")

    ---------------------------------------------------------

#WAP to check if a number is a multiple of 7 or not

nm =int(input("Enter ur number :"))
if nm % 7 == 0:
    print("yes ",nm," it is divisible by 7")
else:
    print("sorry",nm," is not divisible by 7")

    -----------------------------------------------------------------
    #WAP to ask the user to enter names of their 3 favourite movies & store them in list.

l1 = input("Enter ur favourite movies : ")
l2 =input("Enter ur favourite movies : ")
l3 =input("Enter ur favourite movies : ")
l4 = [ l1 ,l2 ,l3]
print(l4) 

                        OR

 movies = []  
movies.append(input("Enter first movie:"))
movies.append(input("Enter Second movie:"))
movies.append(input("Enter Third movie:"))
print(movies)             

-----------------------------------------------------------------------  


#WAP to check if a list contains a palindrom of elelment

l1 = ['racecar']
l2 = l1.copy()
l2.reverse()
if (l1==l2):
    print("palindrom")
else:
    print("not palindrom")
-------------------------------------------------------------



#WAP to count yhe number of student with the "A grade in the following tuple"

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))
 ----------------------------------------------------------------------

 #Store the above values in list and sort them from "A" to "D"
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)

------------------------------------------------------------------------
#