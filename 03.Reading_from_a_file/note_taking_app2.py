# I enter the programme 
# I get a message that let me choose between 2 options : 
#     option one : adding a note 
#     option two : searching for a note
# if I write "1" :
#   I get a message "Enter your note :" under which I can write a note. 
#     when clicking "enter" it saves the note in my text file "notes.txt" under some specials characteres "---" 
#     then either the programme quit or I get asked again what option I want (I can choose while writing the programme)
# if I select write "2" :
#   I get a message "Enter the text to search :" under which I can write a word to search.
#     when clicking "enter", the programme looks for this specific word in my notes and print notes (with their special characters) in which it did find the word
#     then quit or replay

file = open("notes.txt", "a")

first_choice = input("What do you want to do ?\nPress 1 for adding a note\nPress 2 for searching your notes\nPress 3 to stop the programme\n")

#adding notes to the text : 
def adding_note() :
    note = input("Enter your note :\n")
    file = open("notes.txt", "a")
    file.write("----\n" + note + "\n")
    file.close()

#search through notes
def searching_note() :
    search = input("Enter the text to search :\n")
    file = open("notes.txt")
    content = file.read() 
    notes = content.split("----")#transform each note into elements of an array (seperated with ----)
    for notes in content :
        if notes.find(search) != -1:
            index = content.index(search)
            print(content[index])    

#in a loop ? :
if first_choice == "1" :
    print(adding_note())
elif first_choice == "2" :
    print(searching_note())
else :
    print("I can not opperate this commande")

# if first_choice == "1" :
#     note = input("Enter your note :\n")
#     file = open("notes.txt", "a")
#     file.write("----\n" + note + "\n")
#     file.close()
# elif first_choice == "2" : 
#     search = input("Enter the text to search :\n")
#     file = open("notes.txt")
#     content = file.read() 
#     notes = content.split("----")#transform each note into elements of an array (seperated with ----)
#     for line in content :
#         if line.find(search) != -1:
#             index = content.index(search)
#             print(content[index])
#     else :
#         print("you have no notes with the word " + str(search))
# else :
#     print("I can not opperate this commande")
    
    
    

file.close()