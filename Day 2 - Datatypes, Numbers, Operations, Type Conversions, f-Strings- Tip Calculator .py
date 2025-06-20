# print("Howdy"[1]) # Subscripting means pulling out a character from a string
# print("Howdy"[4])
# print("Howdy"[-2])

# String Concatenation
# print("123"+"356")

# Integer = Whole Number
# print(678+3)

# Large Integers
# print(4354_3593_048)

# Float = Floating Point Number
# float_number =3.145
# print(float_number)

# Boolean True or False
# print(True)
# print(False)

# print(len("12345"))

# Type Checking
# int_datatype = type(5)
# print(int_datatype)

# string_datatype = type("Bagavathy")
# print(string_datatype)

# float_datatype = type(45.78)
# print(float_datatype)

# bool_datatype = type(False)
# print(bool_datatype)

# print("Number of letters in your name: " + str(len(input("Enter your name"))))

# print("My age is " + str(10))
# print(2+2)
# print(3*3)
# print(4/4)
# print(type(4//4))
# print(90-23)
# print(4**4)

# PEMDAS (Paranthesis, Exponenets, Multiplication, Division, Addition, Subtraction) PEMDASLR
# print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + (3 / 3) - 3))

# height = 6.6
# weight = 79
# bmi = weight / height ** 2
# print(bmi)
# floor_bmi= int(bmi) # Floor down to the nearest whole number
# print(floor_bmi) 
# print(round(bmi)) # Round to the nearest whole number
# print(round(bmi,2))

# score = 0 

# score += 0
# score -= 0
# score *= 0
# score /= 0

# print((6 + 4 / 2 - (1 * 2)))
# a = int("5") / int(2.7)
# print(type(a))

print("Welcome to the tip calculator!")
bill_input = float(input("What was the total bill? $"))
tip_input = int(input("How much tip would you like to give? 10, 12, or 15?"))
split_bill_no = int(input("How many people to split the bill?"))
bill_per_individual = (bill_input + (bill_input * (tip_input / 100))) / (split_bill_no)
rounded_bill_per_individual = round(bill_per_individual,2)
print(f"Each person should pay: {rounded_bill_per_individual}")