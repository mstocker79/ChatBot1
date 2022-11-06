import re
import long_responses as long
from tkinter import *

# The first section creates the gui. I decided to comment that out, and I am working on a brand new gui.

# root = Tk()
#
# root.title('Chat Bot')
# root.geometry('400x500')
#
# #Create the menu
# main_menu = Menu(root)
#
# file_menu = Menu(root)
# file_menu.add_command(label='New...')
# file_menu.add_command(label='Save As ')
# file_menu.add_command(label='Exit')
#
# main_menu.add_cascade(label='file', menu=file_menu)
# main_menu.add_cascade(label='Edit', menu=file_menu)
# main_menu.add_cascade(label='Quit', menu=file_menu)
#
# root.config(menu=main_menu)
#
# #Create the chat window
# ChatWindow = Text(root, bd=1, bg='black', width=50, height=8)
# ChatWindow.place(x=6, y=6, height=385, width=390 )
#
# #Create the message window
# messageWindow = Text(root, bg='black', width=30, height=4)
# messageWindow.place(x=128, y=400, height=88, width=260)
#
# #Create the button to send the message
# Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font='Arial, 20')
# Button.place(x=6, y=400, height=88, width=120)
#
# #Add a Scroll bar
# scrollbar = Scrollbar(root, command=ChatWindow.yview())
# scrollbar.place(x=385, y=5, height=385)
#
# root.mainloop()

def message_probablity(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob_list
            highest_prob_list[bot_response] = message_probablity(message, list_of_words, single_response, required_words)

        # responses --------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup'], single_response=True)
    response("I'm doing fine, how are you?", ['how', 'are', 'you', 'doing'], required_words=['how'])
    response("I'm talking to you silly! Do you want to hear a riddle?", ['what', 'are', 'you', 'doing'], required_words=['what'])
    response("I wish I had feelings, but I am a bot.", ['ok', 'fine', 'good', 'great', 'okay'], single_response=True)
    response("The more you take, the more you leave behind. What am I?", ['yes', 'ya'], single_response=True)
    response("That's the correct answer", ['steps', 'footsteps'], single_response=True)
    response("The answer was footsteps", ["don't", 'know', 'not'], required_words=["don't"])

    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match



def get_response(user_input):
    split_message = re.split(r'\s+|[,:?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Response system

while True:
    print('Bot: ' + get_response(input('You: ')))

