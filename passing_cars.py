#Passing cars problem
def solution(A):
    eastCars = 0    #Variable to track the number of eastbound cars encountered
    passingCars = 0 #Variable to track the total number of passing car pairs

    for i in range(len(A)): #Looping through every car in the array
        if A[i] == 0:       #Checking if the current car is traveling east
            eastCars+=1     #Increasing the number of eastbound cars encountered

        else:   #If the current car is traveling west
            passingCars+=eastCars #Adding all previously encountered eastbound cars to the total passing pairs

        if passingCars>1000000000: #Checking if the total number of pairs exceeds the limit
            return -1   #Returning -1 if the limit is exceeded

    return passingCars  #Returning the total number of passing car pairs

print(solution([0, 1, 0, 1, 1]))