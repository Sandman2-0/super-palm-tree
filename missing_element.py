#Missing element in array problem
def solution(A):
    N = len(A)  #Getting the number of elements in the array

    expectedSum = (N+1)*(N+2)//2    #Calculating the sum of all numbers from 1 to N+1 
                                    #(adds up 1 + 2 + 3... +n based on the size of the array)
                                    
    actualSum = 0   #Variable to store the actual sum of the existing elements

    for i in range(len(A)): #Looping through every element in the array
        actualSum += A[i]   #Adding the current element to the total sum

    missingVal = expectedSum - actualSum    #Finding the missing value by subtracting the sums

    return missingVal   #Returning the missing value

print(solution([2, 3, 1, 5]))