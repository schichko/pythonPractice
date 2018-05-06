#imports
import math

print("Question 1")
#Creates a list
q1 = []
#similar to a for loop in java between 2000 and 3200
for x in range(2000,3200):
    #if statement uses the actual word and not &&
    if((x%7 == 0) and (x%5 != 0)):
        q1.append(str(x))

#So what this does is it takes a list of STRINGS and joins them with a comma sperating them, the , can be replaced with anything and then it will have that character between each string
print (','.join(q1))

print("Question 2")

#So in a python definination you do not need to define the data type of what you are passing in 
def factorial(myList):
    ans = []
    #Similar to the for range function from above but this is more like a for each loop in java, looking at each element in myList
    for x in myList:
        #appends the factorial to the list with the math import
        ans.append(math.factorial(x))
    return ans

q2 = [3,4,5,6,7,8,9,10]
print(factorial(q2))

print("Question 3")

n = 8
#How to initilize a dictonary ie {1 : 1, 2: 6} (Position and value) 
d = dict()
for x in range (1,n+1):
    #When we are working with a dictonary we must look at the postion by doing dictonary[] and then set that equal to something 
    d[x] = x*x
print(d)

print("Question 4")
#Here we are noticing the difference between a Tuple and a List
#a Tuple CANNOT be changed ulike lists and Tuples also use parentheses
#A List can be changed and uses square brackets
#This is how we do inputs in python, the string can be anything or nothing and it comes up as a message when we are inputing 

values = input("Enter Numbers in a comma seperate list: ")
#l becomes a list with 3 values seperated by ,
l = values.split(",")
#We create the tuple from the list because if we create the tuple off of raw input we will be adding the , to our tuple
#i.e, ('1',',','2',ect) but since we create it out of the list we dont get the ,'s
t = tuple(l)
print(values)
print(l)
print(t)
