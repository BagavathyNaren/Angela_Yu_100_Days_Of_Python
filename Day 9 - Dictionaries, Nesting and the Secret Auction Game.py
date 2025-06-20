# programming_dictionary = {
#     "Bug": "An error in the program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."  
# }


# print(f'Calling the bug key from the programming_dictionary: {programming_dictionary["Bug"]}')

# programming_dictionary["Loop"] =  "The action of doing something over and over again."

# print(programming_dictionary)

# empty_dictionary = {}

# # programming_dictionary = {}

# # print(programming_dictionary)

# programming_dictionary["Bug"] = "A moth in your computer."

# print(programming_dictionary)

# for key in programming_dictionary:
#     print(f'Key in a dictionary: {key}')
#     print(f'Value in a dictionary: {programming_dictionary[key]}')
#     print(f'Key and value in a dictionary: {key}: {programming_dictionary[key]}')

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for key_student_name in student_scores:
#     if ( 91 <=  student_scores[key_student_name] <= 100 ):
#         student_grades[key_student_name] = "Outstanding"
#     elif ( 81 <= student_scores[key_student_name] <= 90 ):
#         student_grades[key_student_name] = "Exceeds Expectations"
#     elif ( 71 <= student_scores[key_student_name] <= 80 ):
#         student_grades[key_student_name] = "Acceptable"
#     else:
#         student_grades[key_student_name] = "Fail"
    
# print(student_grades)

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# # Nested List In Dictionary

# travel_log = {
#     "France": ["Paris","Lille","Dijon"],
#     "Germany": ["Stuttgart","Berlin"]
# }

# # Print Lille from the travel_log

# print(travel_log["France"][1])
        
# nested_list = ["A","B",["C","D"]]

# # Pull out D from the nested_list

# print(nested_list[2][1])


# travel_log_dictionary = {
#     "France": {
#         "cities_visited": ["Paris","Lille","Dijon"],
#          "total_visits": 8
#     },
#     "Germany": {
#         "cities_visited": ["Berlin","Hamburg","Stuttgart"],
#         "total_visits": 5
#     }
# }

# print(travel_log_dictionary["Germany"]["cities_visited"][2])


# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# print(order["main"][2][0])


"""                Auction Bidding Game                                            """
import os
from Private_Bidding_Auction_Art import logo

print(logo)

isBiddingOn = True

bidders_dict = {}

while isBiddingOn:

    print("Welcome to the secret auction program.")
    user_input = input("What is your name?: ")
    bid_input = int(input("What's your bid?: "))
    bidders_input = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if "yes" in bidders_input:
        os.system('cls')
        bidders_dict[user_input] = bid_input      
    else:
        bidders_dict[user_input] = bid_input
        max_bid = 0
        for bidder_name in bidders_dict:
            if ( bidders_dict[bidder_name] >= max_bid ):
                max_bid = bidders_dict[bidder_name]
        biddig_people_list = dict( (value,key) for key , value in bidders_dict.items())
        # max_bidding_person = biddig_people_list[max_bid]
        max_bidding_person = biddig_people_list.get(max_bid)
        print(f"The winner is {max_bidding_person} with a bid of ${max_bid}.")
        isBiddingOn = False