import tkinter as tk

# bot made by Rahul Kumar, February 3rd

#original base strings to add one to
watercounter = ""
mealcounter = ""



#random letters for length counter
n = "n"
k = "k"

# trying arrays instead

waterlist = list()
meallist = list()

#Keeps water count
def add_to_watercounter(watercounter):
    waterlist.append(1)
    print("Glasses of water had today: ")
    x = len(waterlist)
    print(x)

#Keeps meal count 
def add_to_mealcounter(mealcounter):
    meallist.append(1)
    print("Meals had today: ")
    y = len(meallist)
    print(y)
    
    
#Root-title
root = tk.Tk()
root.title("Water Counter")
label = tk.Label(root, fg = "red")
label.pack()

#defining button 1
button1 = tk.Button(root, width = 50, text = "I just had a glass of water", bg="blue", command=lambda: add_to_watercounter(watercounter))
button1.pack()

#defining button 2
button2 = tk.Button(root, width = 50, text = "I just had a meal", bg="red", command=lambda: add_to_mealcounter(mealcounter))
button2.pack()


root.mainloop()
