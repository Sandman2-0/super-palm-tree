#Odd occurrences in array problem
def solution(A):
    countDict = {}  #Dictionary to store how many times each value appears

    for i in range(len(A)): #Looping through every element in the array
        if A[i] in countDict:       #Checking if the value already exists in the dictionary
            countDict[A[i]] += 1    #Increasing the count if it already exists
        else:
            countDict[A[i]] = 1     #Adding the value to the dictionary if it doesn't exist

    for num in countDict:   #Looping through every unique number in the dictionary
        if countDict[num] % 2 != 0: #Checking if the number appears an odd number of times
            return num      #Returning the unpaired value

print(solution([9, 3, 9, 3, 9, 7, 9]))