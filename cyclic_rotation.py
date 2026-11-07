#Cyclic rotation problem
def solution(A, K):
    count = 0           #Setting a count variable to track current cycle count
    tempArr = A.copy()  #Creating a temporary array to store cycles
    tempVal = 0

    while count<K:  #while current cycles are under required cycles
        tempVal = tempArr[len(A)-1] #Saving the last value of the current array
        
        for i in range(len(A)-2, -1, -1):   #Nested loop to perform the cycling
            tempArr[i+1] = tempArr[i]       #Shifting every element to the right

        tempArr[0] = tempVal            #Moving the last value of the previous cycle to the first index to complete the new cycle
        count+=1    #Increasing the count value when a cycle has been performed

    return tempArr  #Returning the fully cycled array

print(solution([1, 2, 3, 4, 5], 3))
