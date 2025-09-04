# def greet():
#     print("Hi Naren")
#     print("Complete the python within 100 days")
#     print("Get into agentic ai automation as soon as possible")

# greet()


# def greet_with_name(name):
#      print(f"Hi, {name}")

# greet_with_name("Naren Bagavathy")

# def greet_with(name,location):
#     print(f"Hello, {name}")
#     print(f"What is it like to work in {location}?")

# #greet_with("Nana","Chennai")


# #greet_with("Chennai","Nana")

# greet_with(location="USA",name="Narendran")

"""             LOVE SCORE CALCULATOR         """
# def calculate_love_score(name1, name2):
#     concat_names = name1+name2
#     change_concat_names_to_uppercase = concat_names.upper()
#     No_of_T = 0
#     No_of_R = 0
#     No_of_U = 0
#     No_of_E = 0
#     No_of_L = 0
#     No_Of_O = 0
#     No_of_V = 0
#     for letter in change_concat_names_to_uppercase:
#         if "T" in letter:
#             No_of_T += 1
#         elif "R" in letter:
#             No_of_R += 1
#         elif "U" in letter:
#             No_of_U += 1
#         elif "E" in letter:
#             No_of_E += 1
#         elif "L" in letter:
#             No_of_L += 1
#         elif "O" in letter:
#             No_Of_O += 1
#         elif "V" in letter:
#             No_of_V += 1
    
#     You_True = No_of_T + No_of_R + No_of_U + No_of_E
#     Love = No_of_L + No_Of_O + No_of_V + No_of_E
#     Love_Score = str(You_True) + str(Love)
#     print(Love_Score)
            
# calculate_love_score("Kanye West", "Kim Kardashian")

"""                                CAESAR CIPHER                                                            """


from Caesar_Cipher_Art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
def caesar_cipher(original_text, shift_amount, encode_or_decode): 
         output_text = ""
         if "decode" in encode_or_decode:
                shift_amount *= -1
         for letter in original_text:
             if letter not in alphabet:
                 output_text += letter
             else:                 
                 shifted_position = alphabet.index(letter) + shift_amount
                 shifted_position %= len(alphabet)
                 output_text += alphabet[shifted_position]
         print(f"Here is the {encode_or_decode}d result: {output_text}")
 
isCipher = True

while (isCipher):
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(original_text=text,shift_amount=shift,encode_or_decode=direction)
    continue_game = input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()
    if continue_game == "no":
       isCipher = False
       print("Good-bye mamu!")



