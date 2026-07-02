#type hints
def calculate_average(number:list) -> float: 
   average= sum(number)/len(number)
   return average

print(calculate_average([10, 20, 30, 40]))