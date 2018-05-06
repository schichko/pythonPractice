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
    for x in myList:
        ans.append(math.factorial(x))
    return ans
q2 = [3,4,5,6,7,8,9,10]
print(factorial(q2))