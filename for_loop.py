
# To print the sum of array integer 
number_arrays = [5, 3, 7, 2, 32, 59, 99]
array_sum = 0
for num in number_arrays:
    array_sum += num
print(array_sum)

ar = [232, 34, 73, 2, 32, 59, 99]
def simpleArray(ar):
    Total = 0
    for x in ar:
        try:
            Total += int(x)
        except ValueError:
            pass
    return Total

sum = simpleArray(ar)
print(sum)


# creating a dictionary that will sum the content of array
def SimpleArrayForm(n, ar):
    sumArray = 0
    for i in SimpleArrayForm:
        sumArray += i
    return sumArray

# if you want to ilterat through an array and sum them
def simpleArraysum(ar):
    # initailizing the valiable that keep track of the sum
    Total = 0
    for i in range(len(ar)):
        Total += ar[i]
    # return the sum
    return Total

# To raise an exeption if the value type of the array is not an integer 
def simpleArraysum(ar):
    Total = 0
    for i in ar:
        if not isinstance(ar, int):
            raise TypeError("The value you entered is not an integer type \n input array must be an integer value type")
        Total += i
    return Total

# if the array contain a missed datatype we can sum only the int values and pass others using try and except function  
def simpleArray(ar):
    Total = 0
    for x in ar:
        try:
            Total += int(x)
        except ValueError:
            pass
    return Total

ar = [5, 3, 7, 2, 32, 59, 99]
def simpleArray(ar):
    Total = 0
    for x in ar:
        try:
            Total += int(x)
        except ValueError:
            pass
    return Total

sum = simpleArray(ar)
print(sum)