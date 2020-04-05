###Notes
'''
equating a string can be done with eval()
e.g. cat = '3+4*7'; eval(cat); 31

Remove answer after answering question
Added sounds
'''



###IMPORTS
from tkinter import *
from winsound import *
import random
import math

###DEFINE FUNCTIONS
def round_number(answer):
    answer = answer + 0.005
    return (math.floor(answer*100)) / 100

def style1_make_answers():
    ###Making answers for buddy code
    global questionAnswer, num2, num1, questionvar
    restart = 0
    if style1_level >= 4:
        num2 = random.randint(10, 101)
        num1 = random.randint(1, num2)  # generating two numbers for fraction
        questionAnswer = (num1 / num2) * 100  # answer to check
        questionAnswer = round_number(questionAnswer)
    elif style1_level >= 3:
        num2 = random.randint(3, 21)
        num1 = random.randint(1, num2)  # generating two numbers for fraction
        questionAnswer = (num1 / num2) * 100  # answer to check
        questionAnswer = round_number(questionAnswer)
    elif style1_level >= 2:
        while restart == 0:  # keep looping until answer = whole number
            num2 = random.randint(10, 101)
            num1 = random.randint(1, num2)
            questionAnswer = (num1 / num2) * 100
            if float(questionAnswer) == int(questionAnswer):
                restart = 1
                if float(questionAnswer) == float(100):
                    restart = 0
    elif style1_level >= 1:
        while restart == 0:  # keep looping until answer = whole number
            num2 = random.randint(3, 21)
            num1 = random.randint(1, num2)
            questionAnswer = (num1 / num2) * 100
            if float(questionAnswer) == int(questionAnswer):
                restart = 1
                if float(questionAnswer) == float(100):
                    restart = 0
        questionAnswer = (num1 / num2) * 100  # answer to check
    elif style1_level <= 1:
        num2 = 10
        num1 = random.randint(1, num2)  # generating two numbers for fraction
        questionAnswer = (num1 / num2) * 100  # answer to check
    #also sets question title and changes the correct or wrong label
    questionTxt2 = str(num1) + " divided by " + str(num2)
    questionvar.set(questionTxt2)

def submit_button(event):
    global userEntry, answerInputBox, style1_level
    userEntry = (answerInputBox.get())  # gets the input from entry box
    global answers, questionAnswer, answer_check_var, labels
    try:
        float(userEntry)
    except ValueError:
        answer_check_var.set('Incorrect Format, only include numbers in your answer')
    if float(userEntry) == float(questionAnswer):
        answerInputBox.delete(0, 'end')
        play_correct()
        answer_check_var.set('Correct, Good Job!')
        style1_level += 0.2
        reset_question()
    else:
        answer_check_var.set('Incorrect, Try Again!')
        play_wrong()
        style1_level -= 0.2



def reset_question():
    global labels, answerInputBox, submitButton, answers
    c = 0
    for null in labels:
        labels[c].grid_forget()
        c += 1
    style1_make_answers()
    answers = ['null']

def play_correct():
    return PlaySound("ding.wav", SND_FILENAME | SND_ASYNC)

def play_wrong():
    return PlaySound("incorrect.wav", SND_FILENAME | SND_ASYNC)



###DEFINE VARIABLES
labels = []
answers = ['null']
###Grab variables from file

###Start up
try:
    style1_level
except NameError:    #if style1_level is undefined set to 0
    style1_level = 0
if style1_level < 0: #if style1_level is below 0 set to 0
    style1_level = 0


##DEBUG

### INTERFACE
root = Tk()

questionvar = StringVar()
questionLabel = Label(root, textvariable=questionvar, anchor=CENTER, font="Times 20 bold")
questionLabel.grid(row=2, column=2)


answer_check_var = StringVar()
answer_check_label = Label(root, textvariable=answer_check_var, anchor=CENTER, font="Times 20 bold")
answer_check_label.grid(row=3, column=2)

#creating titlte
questionTxt = "Convert the fraction to a percentage (round to two decimal places)"
titleText = StringVar()
title2 = Label(root, textvariable=titleText, anchor=CENTER, font="Times 30 bold")
title2.grid(row=1, column=2)
titleText.set(questionTxt)

#creating entry
answerInputBox = Entry(root)
answerInputBox.grid(row=2, column=1, sticky=W, pady=4)

#changing default text
answerInputBox.delete(0, END)
answerInputBox.insert(0, "insert answer")
answerInputBox.bind('<Return>', submit_button)


#submit (checking answer) button
submitButton = Button(root, text='Submit')
submitButton.bind('<Button-1>', submit_button)
submitButton.grid(row=2, column=2, sticky=W, pady=4)

#later exit button that saves levels to text file
style1_make_answers()

root.state('zoomed')
root.mainloop()