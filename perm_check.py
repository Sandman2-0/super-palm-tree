#Permutation check problem
def solution(A):
    N = len(A)  #Getting the number of elements in the array
    seenVals = set()    #Creating a set to store values already encountered

    for i in range(len(A)):         #Looping through every element in the array
        if A[i] < 1 or A[i] > N:    #Checking if the value is outside the required range
            return 0    #Returning 0 if the value is invalid

        if A[i] in seenVals:    #Checking if the value has already appeared
            return 0    #Returning 0 if a duplicate is found

        seenVals.add(A[i])      #Adding the current value to the set

    return 1    #Returning 1 if all values are valid and unique

print(solution([4, 1, 3, 2]))