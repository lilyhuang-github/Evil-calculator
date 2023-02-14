from tkinter import *

gui = Tk()
gui.title("Evil calculator")
e = Entry(gui, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add(num):
  # print(num)
  return
  #e.delete(0, END)


#  e.insert(0, num)

#button def
button_1 = Button(gui,
                  text="1",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(1))
button_2 = Button(gui,
                  text="2",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(2))
button_3 = Button(gui,
                  text="3",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(3))
button_4 = Button(gui,
                  text="4",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(4))
button_5 = Button(gui,
                  text="5",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(5))
button_6 = Button(gui,
                  text="6",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(6))
button_7 = Button(gui,
                  text="7",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(7))
button_8 = Button(gui,
                  text="8",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(8))
button_9 = Button(gui,
                  text="9",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(9))
button_0 = Button(gui,
                  text="0",
                  padx=40,
                  pady=20,
                  command=lambda: button_add(0))

button_add = Button(gui, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(gui, text="=", padx=39, pady=20, command=button_add)
#button add

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1)

gui.mainloop()
