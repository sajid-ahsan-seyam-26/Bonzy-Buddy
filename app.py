import datetime
import os
import random
import webbrowser
import tkinter as tk
from tkinter import messagebox
APP_NAME="BuddyPy Begineer Assistant"
NOTES_FILE="note.txt"
TASKS_FILE="task.txt"
reminder_list=[]
def add_line_to_file(file_name,text):
    file=open(file_name,"a",encoding="utf-8")
    file.write(text+"\n")
    file.close()
def read_lines_from_file(file_name):
    if not os.path.exists(file_name):
     return []
    file = open(file_name, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    clean_lines = []
    for line in lines:
       clean_lines.append(line.strip())
       return clean_lines
def clean_file(file_name):
    file=open(file_name,"w",encoding="uft-8")
    file.write("")
    file.close()
def get_help_text():
     return (
        "You can type these commands:\n\n"
        "1. hi\n"
        "2. time\n"
        "3. date\n"
        "4. calc 10 + 5 * 2\n"
        "5. open youtube\n"
        "6. search python tutorial\n"
        "7. note buy milk\n"
        "8. show notes\n"
        "9. clear notes\n"
        "10. add task finish homework\n"
        "11. tasks\n"
        "12. done task 1\n"
        "13. clear tasks\n"
        "14. remind me to drink water in 10 minutes\n"
        "15. reminders\n"
        "16. joke\n"
        "17. exit"
    )
def calculate_answer(expression):

    allowed_characters = "0123456789+-*/(). "

    for letter in expression:
        if letter not in allowed_characters:
            return "Calculator e sudhu number and + - * / use koro."

    try:
        answer = eval(expression)
        return "Answer: " + str(answer)
    except Exception:
        return "Sorry, calculation bujhte pari nai. Example: calc 10 + 5"
def open_website(website_name):
    websites={
        "google":"http://www.google.com",
        "youtube":"http://www.youtube.com",
        "facebook":"http://www.chagpt.com",
        "chatgpt":"http://chatgpt.com",
        "gamil":"http://mail.google.com"
    }
    if website_name in websites:
        webbrowser.open(websites[website_name])
        return"opening" +website_name
    return "I know google,youtube,facebook,chatgpt,gamil"

    
    
