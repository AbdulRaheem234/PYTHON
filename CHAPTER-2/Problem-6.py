# Direct percentage calculation

# Input: total marks obtained
obtained_marks = float(input("Enter total marks obtained: "))

# Input: total maximum marks
maximum_marks = float(input("Enter total maximum marks: "))

# Calculate percentage
percentage = (obtained_marks / maximum_marks) * 100

# Print the percentage
print(f"Percentage = {percentage:.2f}%")
