# Week 2: Data Cleaning Script

# Sample data
data = [10, 20, 20, 30, 40, 40, 50, 60, 70, 70]

# 1. Remove duplicates
cleaned_data = list(set(data))
print("Data after removing duplicates:", cleaned_data)

# 2. Filter data (e.g., only numbers > 30)
filtered_data = [x for x in cleaned_data if x > 30]
print("Filtered data (numbers > 30):", filtered_data)

# 3. Example function: sum of squares
def sum_of_squares(lst):
    return sum([x**2 for x in lst])

print("Sum of squares of filtered data:", sum_of_squares(filtered_data))

# 4. Lambda example: double each number
doubled_data = list(map(lambda x: x*2, filtered_data))
print("Doubled data:", doubled_data)

# 5. Recursion example: factorial of 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))
