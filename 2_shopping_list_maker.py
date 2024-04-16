# Task 1: Write a functional list where user can add items until user replies "stop" and then returns the shopping list

def create_shopping_list():
    create_shopping_list = ["eggs", "yogurt", "bread","cheese", "jelly", "peanut butter", "waffles"]
    print("Welcome to what is on my shopping list!")

while True:
    item = input ("ice cream (or type 'stop'to finish):")

    if item.lower() == 'stop':
        break
    else:
        create_shopping_list.append('ice cream')

# Task 2: Include a feature to remove items from the list:

def create_shopping_list():
   create_shopping_list = ["eggs", "yogurt", "bread","cheese", "jelly", "peanut butter", "waffles"]
if item in create_shopping_list:
    create_shopping_list.remove('waffles')
else:
    print("Item not found in the shopping list.")


#Dylan I forgot how to stop the other funcation from running for ex my task 1 is still giving output whole I am not working on Task 2?

#Task 3: Add a feature that prints out the entire list in a formatted way.

def create_shopping_list():
    shopping_list = ["eggs", "yogurt", "bread","cheese", "jelly", "peanut butter", "waffles"]
    print("welcome to the shoppng list!")
while true:
    print("current shopping list:")
    for item in (create_shopping_list, start==1):
        print(f"{item}, {item}")

#Dylan even with this one I am still getting the reponse from Task 1, in this case would I just start a new window? How do I comment out the previous funciton isnt it Ctrl[] and if that is correct how do undo?
