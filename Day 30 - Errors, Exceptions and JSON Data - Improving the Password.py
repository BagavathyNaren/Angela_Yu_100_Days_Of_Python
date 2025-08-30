"""

try:
  Soemthing that might cause an exception
except:
  Do this if there was an exception
else:
  Do this if there were no exceptions
finally:
  Do this no matter what happens

  
  Handling Errors & Exceptions 

# FileNotFound Error
with open("a_file.txt") as file:
    file.read()

# KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

#IndexError
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

#TypeError
text = "abc"
print(text + 5)

"""

# FileNotFound #



  #Exception Handling

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

# #BMI Example

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

 # 229. Raising your own Exceptions


# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Fruit pie")

# make_pie(4)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            # If 'Likes' key doesn't exist, treat it as 0 likes
            total_likes = total_likes + 0
    
    return total_likes

# Test the function
result = count_likes(facebook_posts)
print(f"Total likes: {result}")


