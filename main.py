print("hello world")

print("/_____|")
print("/_____|")
print("/_____|")
print("/_____|")

Person_name = "John Doe"
Person_income = "4"
print(Person_name + " is a fine man with several income sources, " + Person_income + " of which comes from IT")
person_name = "Habeeb Hand"
# person_Income = "44";
person_Income = 4
# is_right = True
print("here is another man, you mean " + person_name + " with " + str(person_Income) + " sources of income from IT??")

# string manipulation
print("let\"s")
first_String = "Machine Learning ENGINEER"
print(first_String)
print(first_String.upper())
print(first_String.islower())
print(first_String.lower().islower())
print(len(first_String))
print(len('first_String'))
print(first_String[24])
print('first_String'[4])
print(first_String.index("l".upper()))
print(first_String.replace("Machine Learning", "AI"))
print(first_String.replace(" ", " TEST -- SEE "))
print(first_String.replace("e", "y"))

# number manipulation
print("2")
print(+2)
print(-2.2142058)
print(14 - 4.8822)
print(2 * 50 + 41)
my_Num = 14
print(my_Num % 3) 
boyAge = -5
print("Boy is " + str(boyAge))
print(pow(5, 3))
print(abs(boyAge))
print(max(45,785), min(822,759,522,4878))

from math import *
print(floor(2.998))
print(ceil(2.221))
print(sqrt(144))

# getting user input
# name = input("Enter your name: ")
# age = input("How old are you? ")
# print("Hello " + name +". What does been " + age + " feels like?")

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# print(number1 + number2)

# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
# print(number1 + number2)

# mad libs game 
# color = input("Enter your fav. color: ")
# color = color.replace(color[0], "\"" + color[0].upper()) + "\""
# # color[1] = color[1].upper()
# SOF = input("Enter your state of origin: ")
# SOF = SOF.replace(SOF[0], "*" + SOF[0].upper()) + "*"
# print("You seem to like " + color + ". You must be from " + SOF + ". Right?")

# lists
friends = ["Habeeb", "Ade", "Arnold", 1, False, "Tope", "Khair"]
print(friends[2], friends[-2], friends[-1], friends[2:], friends[2: 5])
friends[2] = "Billal Bn Rabba"
family = ["Abu", "Ummuh", "Taiye", "Kenny"]
# list functions
family.extend(friends)  
print(family)
friends.append("Idris")
friends.insert(2, "Barakat")
friends.insert(2, ("Barakat","Aisha"))
print(friends)
friends.remove("Habeeb")
# friends.clear()
print(friends)
friends.pop()
print(friends)
print(friends.index("Ade"))
family.append(77)
print(family, family.index(77), friends.count("Barakat"))
numbers = [788, 0, 895, 89, 7823, 12, 13, 14, 25]
# numbers.sort()
numbers.reverse()
print(numbers)
# friends.sort()
friends.reverse()
print(friends)
# friends = ["Tade", "Bayo", "Tobi"]
print(friends)
friendsTwo = friends.copy()
print(friendsTwo)

# Tuples
priorities = ("Deen", "success")
# priorities[1] = "good"  // throws error. tuple not mutable
priorities1 = ["anything else?", (74, "boy"), (7, 110)]
priorities1[2] = (744, "boy")
print(priorities1)

# function
def say_hello(user, age):
    return ("Hello " + user + ". You're " + str(age) + ".")
    # print("Hello " + user + ". You're " + str(age) + ".")

# say_hello("Tolani")   // throws error because argument is not 2
print(say_hello("OlohunTower", 74))
# say_hello("OluwaTowa", "20")
def cube_number(num):
    # return pow(num, 3)
    return num * num * num
print(cube_number(3))

# if statement
# numb1 = int(input("Enter a number: "))
# numb2 = int(input("Enter a number: "))
# if numb1 > 0 and numb2 > 0:
#      print(str(numb1) + " and " + str(numb2) + "      are positive numbers.")
# elif numb1 > 0 or numb2 > 0:
#    print("Either " + str(numb1) + " or " + str(numb2) + " is a positive number.")
# elif numb1 > 0 and numb2 < 0:
#      print(str(numb1) + " is a positive number while " + str(numb2) + " is a negative number.")
# elif numb1 < 0 and numb2 > 0:
#      print(str(numb1) + " is a negative number while " + str(numb2) + " is a positive number.")
# elif not(numb1 > 0 or numb2 > 0):
#    print(str(numb1) + " and " + str(numb2) + " are negative numbers.")

def max_num(num1, num2, num3):
         if num1 > num2 and num1 > num3:
           return num1
         elif num2 > num3 and num2 > num3:
            return num2
         else:
            return num3
print(max_num(40, 58, 99))

# calculator
# first_num = int(input("Enter your first number: "))
# second_num = int(input("Enter your second number: "))
# ope = input("Enter your operator: ")
# def calculator(fnum1, ope, fnum2):
#     if ope == "+":
#        return fnum1 + fnum2
#     elif ope == "-":
#        return fnum1 - fnum2
#     elif ope == "/":
#        return fnum1 / fnum2
#     elif ope == "*":
#        return fnum1 * fnum2
#     else:
#        return "Operator is invalid"

# print(calculator(first_num, ope, second_num))

# Dictionaries
first_dico = {
   "Jan": "January",
   "Feb": "February",
   "Mar": "March",
   'Jany': "April",
   # LaFamilia: "babe",  //error because a string has to be defined with a parentheses
   True : "Yes",
   45: "na no",
}
print(first_dico["Jany"])
print(first_dico.get("mar"))
print(first_dico.get("mar", "This key is not existent on this dictionary! Please check your spelling or include it in the dictionary with the value to assess its value."))
print(first_dico[45])
print(first_dico.get(True))

# while loop
i = 1
while i < 5:
      print(i)
      i += 1

# Guess Game
# guess_word = "cat"
# user_input = ""
# while user_input != guess_word:
#    user_input = input("enter what you think the guess word is: ")
   
# print("Yaay, you guessed right. The guess word is " + user_input)

# 
the_guess_word = "Jannah"
user_guess = ""
guess_count = 0
guess_status = False

# while user_guess != the_guess_word and not(guess_status):
#       if guess_count != 3:
#          user_guess = input("enter what you think the guess word is: ")
#          guess_count += 1
#       else:
#          guess_status = True
# if guess_status:
#    print("You just ran out of guesses dear!")
#    print("Try again later!")
# else:
#    print("Yaay, you guessed right. The guess word is " + user_guess)
#    print("You win!")

   # For Loop
for j in "JANNAH":
    print(j)
for i in range(4):
    print(i)
states = ["Kwara", "Lagos", "Kaduna"]
for state in range(len(states)):
    print(states[state])
for i in range(3, 9):
    print(i)
for state in range(3):
    if state == 0:
       print("This is the first state in the lits. Looks like you are from here. The state is " + states[state])
    else:
       print(states[state] + ": Other states")
       
# exponential function
print(2**3) 

def power_num(base, power):
    result = 1
    for i in range(power):
        result = result*base 
    return result

print(power_num(2, 4)) 

# nested List
nested_num = [
   [4, 8],
   [7, 9, 81],
   [0] 
]
for i in nested_num: 
    for j in i:
         #  for k in j:
         print(j)

# vowel translator
def translate(phrase):
    phrase = phrase.lower()
    vowel = "aeiou"
    translated = ""
    for i in phrase:
        if i in "aeiou":
           translated += "g"
        else:
           translated += i 
    return translated.replace(translated[0], translated[0].upper())

# print(translate(input("Enter a phrase: ")))

# number = int(input("enter a number: "))
# print(number)
# print(10/0)
try:
   value = 10/0
   number = int(input("enter a number: "))
   print(number)
   
except ValueError as error:
   print(error)
except ZeroDivisionError:
   print("not divisle by 0")

guess_word = "cat"
user_input = ""
# while user_input != guess_word:
#    user_input = input("enter what you think the guess word is: ")
#    print(user_input)
   
# print("Yaay, you guessed right. The guess word is " + user_input)

myName = "Abass"
userGuess = ""
userGuessCount = 0
userGuessStatus = True

while userGuess != myName and userGuessStatus:
      if(userGuessCount != 3):
         # userGuess = input("Enter what you think my name is: ")
         # userGuessFirstLetter = userGuess[0].upper()  //this converts the first letter of the user input into a capital letter.
         # userGuess = userGuess.replace(userGuess[0], userGuess[0].upper())    // I'm trying to convert only the first letter to a capital letter here. the replace method converts the first letter in all places where it occurs. I believe a "splice or slice" method would work fine here.
         print(userGuess)
         userGuessCount +=1
      else:
         userGuessStatus = False

# if userGuess == myName:
#    print("Heyy! You got the name right. You Win!")
# else:
#    print("You ran out of guess count. Sorry, You lose.")
   
   # Reading the contents of a file
fileUsage = open("test.txt", "r+")
print(fileUsage.writable())
print(fileUsage.readable())
# print(fileUsage.readlines()[9])

# print(len(fileUsage.readlines()))    // not understood, how can be length of a non-empty list be returning zero.

for i in fileUsage.readlines():
    print(i)

# print(fileUsage.read())
# print(fileUsage.readline())

fileUsage.close()

# Adding to the contents of a file --- writing a file
# fileUsage2 = open("test.txt2", "w")
fileUsage2 = open("test.txt2", "a")
print(fileUsage2.write("\nThis is a new line added to the file through the append mode with the line break character."))
fileUsage2.write("<h1>Let's convert all to a one line word. </h1>")

fileUsage3 = open("test.html", "w")
# fileUsage3.write("<h1>Welcome to the HTML zone. </h1>")
# fileUsage3.write("<h1>Welcome Back to the HTML zone. </h1>")
# overwriting the contents of a file.
fileUsage3.write("Well, is anything still here")
fileUsage3.close()

# classes and objects
from student import Student
student1 = Student("Abass", 25, "male", False)
student2 = Student("Salmah", 20, "female", True)
print(student1.age)
print(student2.name)

# multiple choice quiz
from Question import Question

question_prompts = [
   "what colors are apples?? \n (a) Red \n (b) Grey \n (c) Yellow \n (d) Indigo \n \n",
"what colors are bananas?? \n (a) Red \n (b) Green \n (c) Yellow \n (d) Indigo \n \n",
"what colors are berries?? \n (a) Red \n (b) Blue \n (c) Yellow \n (d) Indigo \n \n"
]

questions = [
   Question(question_prompts[0], "a"),
   Question(question_prompts[1], "b"),
   Question(question_prompts[2], "a")
]

def askQuestion(questions):
    score = 0
    for i in questions:
        userAnswer = input(i.prompt)
        if userAnswer == i.answer:
           score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " right.")

askQuestion(questions)