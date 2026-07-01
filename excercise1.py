#excercise 1 
#calculate_average take a list and provide the average of all numbers in the list 

def calculate_average(numbers):
    average = sum(numbers)/len(numbers)
    return average

calculate_average([12,20,30,40])