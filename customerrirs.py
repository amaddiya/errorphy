def check_positive_number(num):
    num = int (input("Enter a number:"))
    if num < 0:
        raise ValueError("Only positive numbers are allowed")
    return num
try:

    check_positive_number(-5)
    print ("Input is positive")

except ValueError as e:
    print(f"Please enter a valid number.Error: {e}")
  
    
