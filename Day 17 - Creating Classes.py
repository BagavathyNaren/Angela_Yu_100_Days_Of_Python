class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Leonardo Dicaprio")



print(f'{user_1.id}\n{user_1.name}')

user_2 = User("67",'Jil')

print(f'{user_2.id}\n{user_2.name}')




user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


"""
# Attributes are variables associated with an object.  

# def __init__(self): is the special function in python

The attributes are the things that the object has and the methods are the things that the object does.



############################ METHOD ############################################################
class Car():
   def enter_race_mode():
       self.seats = 2

my_car = Car()

my_car.enter_race_mode()

But remember when a function is attached to an object then it's called a method

"""

