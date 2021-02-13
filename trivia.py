# Python file
# Save this with extension .py


print("Welcome To The Trivia!!")


# Scoring
total_q = 4
def question_1():
    global score
    score = int(0)

# Question1
question1 = str(raw_input("1. What's the best programming language? "))
ans1 = "Python"
if question1 == ans1:
    print("Correct!!")
    question_1()
    score = score + 1
    print("Your Updated Score Is: ", score)
else:
    print("Wrong, the correct answer is: ", ans1)


    
# Question2
question2 = str(raw_input("2. What's 2+2? "))
ans2 = "4"
if question2 == ans2:
    print("Correct!!")
    score = score + 1
    print("Your Updated Score Is: ", score)
else:
    print("Wrong, the correct answer is: ", ans2)

# Question3
question3 = str(raw_input("3. What's 4-5? "))
ans3 = "-1"
if question3 == ans3:
    print("Correct!!")
    score = score + 1
    print("Your Updated Score Is: ", score)
else:
    print("Wrong, the correct answer is: ", ans3)    
    
# Question4
question4 = str(raw_input("4. What's Java-Script? "))
ans4 = "Programming Language"
if question4 == ans4:
    print("Correct!!")
    score = score + 1
    print("Your Updated Score Is: ", score)
else:
    print("Wrong, the correct answer is: ", ans4)
 
print("Thank You For Playing! You Scored: ", score)
print("Credits:","/n", "Arnav Naik")
print("Check Out My GitHub: https://code643/")
