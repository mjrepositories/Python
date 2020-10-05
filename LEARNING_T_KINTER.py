import tkinter as tk
#
# wysok= 700
# szer = 700
# # i am adding here dialog window
# root = tk.Tk()
#
# def testing(entry):
#     print("This is entry: ", entry)
# #here i am specifing the values for canvas
# canvas = tk.Canvas(root,height = wysok,width = szer)
# # so pack() adds the functionality to the window
# canvas.pack()
# background_image =tk.PhotoImage(file = r'C:\Users\310295192\Desktop\Others\kendrick.png')
# background_label =tk.Label(root, image = background_image)
# background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
# #we can add also the color for frame
# frame =tk.Frame(root,bg = '#80c1ff', bd = 5)
# #places the color in frame and indicates how much of the file it covers
# frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor ='n')
#
# #we can also add field for inputing some information
# entry = tk.Entry(frame, font = 40)
# entry.place(relwidth = 0.65, relheight = 1)
# # i am adding here the button specification
# button = tk.Button(frame, text = "test button", font = 40, command =lambda: testing(entry.get()))
# # here i am adding button to dialog window
# button.place(relx = 0.7, relheight = 1, relwidth = 0.3)
#
# lower_frame = tk.Frame(root,bg = '#80c1ff', bd = 10)
# lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')
#
# label = tk.Label(lower_frame, bg = 'white')
# label.place(relwidth = 1, relheight = 1)
#
# #this lane of code stops python for further execution of code
# root.mainloop()



# root = tk.Tk()
#
#
# # i am creating a label widget
# mylabel = tk.Label(root,text='Hello World')
#
# # and here i am packing it on the screen
# mylabel.pack()
#
#
# root.mainloop()


# root = tk.Tk()
#
#
# # i am creatin  g a label widget
# mylabel = tk.Label(root,text='Hello World')
#
#
# mylabel2 = tk.Label(root,text='Maciej')
#
#
# # and here i am packing it on the screen
# mylabel.grid(row=0,column=0)
#
#
# # and here i am packing it on the screen
# mylabel2.grid(row=1,column=1)
#
#
# root.mainloop()


root = tk.Tk()

# e = tk.Entry(root, borderwidth=5)
# # e.pack()
# # e.insert(10,"Podaj")
# #
# #
# # def myclick():
# #     mylabel = tk.Label(root,text=e.get())
# #     mylabel.pack()
# #
# # # i am creatin  g a label widget
# # mybutton = tk.Button(root,text="Enter your name: ",command=myclick,fg='Blue',bg='Red')
# #
# #
# # # and here i am packing it on the screen
# # mybutton.pack()
# #
# #
# #
# #
# # root.mainloop()

root.title("Simple calculator")
e = tk.Entry(root, width=35,borderwidth=5)

e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_add():
    return


but_1 = tk.Button(root,text="1", padx=40,pady=20,command=button_add)
but_2 = tk.Button(root,text="2", padx=40,pady=20,command=button_add)
but_3 = tk.Button(root,text="3", padx=40,pady=20,command=button_add)
but_4 = tk.Button(root,text="4", padx=40,pady=20,command=button_add)
but_5 = tk.Button(root,text="5", padx=40,pady=20,command=button_add)
but_6 = tk.Button(root,text="6", padx=40,pady=20,command=button_add)
but_7 = tk.Button(root,text="7", padx=40,pady=20,command=button_add)
but_8 = tk.Button(root,text="8", padx=40,pady=20,command=button_add)
but_9 = tk.Button(root,text="9", padx=40,pady=20,command=button_add)
but_0 = tk.Button(root,text="0", padx=40,pady=20,command=button_add)
but_add =tk.Button(root,text="+", padx=40,pady=20,command=button_add)
but_equal  = tk.Button(root,text="=", padx=80,pady=20,command=button_add)
but_clear = tk.Button(root,text="CR ", padx=80,pady=20,command=button_add)


but_1.grid(column=2,row=3)
but_2.grid(column=1,row=3)
but_3.grid(column=0,row=3)
but_4.grid(column=2,row=2)
but_5.grid(column=1,row=2)
but_6.grid(column=0,row=2)
but_7.grid(column=2,row=1)
but_8.grid(column=1,row=1)
but_9.grid(column=0,row=1)
but_0.grid(column=0,row=4)

but_clear.grid(column=1,row=4,columnspan=2)
but_add.grid(column=0,row=5)
but_equal.grid(column=1,row=5,columnspan=2)


root.mainloop()