


# #                      Advanced Python Arguments                    #



# import turtle

# tim = turtle.Turtle()

# screen = turtle.Screen()

# tim.write("Some text", font=("Times New Roman", 80, "bold"))

# " tim.write() method takes 5 inputs => (self, arg, move, align, font) => self is the method associated with Turtle Class"

# screen.exitonclick()

# def foo(a, b=4, c=6): 
#     print(a, b, c)
 
# foo(1, 7, 9)


# def add(*args):
#     print(args)
#     print(type(args))
#     print(args[2])
#     #loop_through_args = [arg for arg in args]
#     #print(loop_through_args)
#     for n in args:
#         print(n)
    
#     return sum(args)


# sum = add(1, 2, 3, 4, 5)
# print(sum)


# #


# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.year = kwargs.get("year")
#         self.seats = kwargs.get("seats")

# my_car = Car(make="Rolls Royce")
# print(my_car.make)
# print(my_car.model)
# print(my_car.year)


# def test(*args):
#     print(args)

# test(1,2,3,5)


from tkinter import * # type: ignore

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial",24,"bold"))
#my_label.pack(side="left")

#my_label.pack(expand=True)

my_label["text"] = "New Label Text"
my_label.config(text="New Label Text")
#my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
#input.pack(side="left")
print(input.get())
input.grid(column=2, row=2)

window.mainloop()