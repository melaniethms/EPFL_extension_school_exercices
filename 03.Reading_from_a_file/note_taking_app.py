# I enter the programme 
# I get a message that let me choose between 2 options : 
#     option one : adding a note 
#     option two : searching for a note
# if I write "1" :
#   I get a message "Enter your note :" under which I can write a note. 
#     when clicking "enter" it saves the note in my file under some specials characteres "---" 
#     then either the programme quit or I get asked again what option I want (I can choose while writing the programme)
# if I select write "2" :
#   I get a message "Enter the text to search :" under which I can write a word to search.
#     when clicking "enter", the programme looks for this specific word in my notes and print notes (with their special characters) in which it did find the word
#     then quit or replay

file = open("notes.txt", "a")

first_choice = print(input("What do you want to do ?\nPress 1 for adding a note\nPress 2 for searching your notes\n"))

# def adding_note() :
#     note = print(input("Enter your note :\n"))
#     file.write("----\n" + note)
    
if first_choice == "1" :
    note = print(input("Enter your note :\n"))
    file.write("----\n" + note)
    
    


# elif question == "2" :
#     search = print(input("Enter the text to search :\n"))
#     file = open("notes.txt")
#     content = file.read()
#     file.find(search)
#     file.close()
#     print("Enter the text to search :\n")
file.close()