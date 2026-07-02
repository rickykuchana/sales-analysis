def safe_divide(numerator, denominator):
    try:
        return numerator/denominator
    except ZeroDivisionError: 
        return "cannot divide by zero"

print(safe_divide(10,0))
print(safe_divide(10,100))
