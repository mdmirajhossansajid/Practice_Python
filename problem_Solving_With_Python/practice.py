print("Hello! This program will help you scale a number using min-max scaling.")
print("Please enter the minimum value of the range:")
min_value = float(input())
print("Please enter the maximum value of the range:")
max_value = float(input())
print("Please enter the number you want to scale:")
number = float(input())
def min_max_scaling(num, min_val, max_val):
    scaled_value = (num - min_val) / (max_val - min_val)
    return scaled_value
scaled_number = min_max_scaling(number, min_value, max_value)
print(f"The scaled value of {number} in the range [{min_value}, {max_value}] is: {scaled_number}")  
 