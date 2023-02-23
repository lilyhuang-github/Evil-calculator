from tkinter import *
import random
from tkinter import simpledialog
from PIL import ImageTk, Image


def new_img():
  # Pick a new number
  number = random.randint(1, 6)
  # Add '.jpg' to number
  myimg = str(number) + '.jpg'
  # Return the image name
  return "1.jpg"
  #return myimg


def btnClick(numbers):
  global operator
  operator = operator + str(numbers)
  text_input.set(operator)


def btnClearDisplay():  # Function for "C" button
  global operator
  operator = ''  # Reset operator
  text_input.set('')  # Reset TextBox


def btnEqualsInput():  # Function for "=" button
  global operator
  global answer
  the_sum = str(eval(operator))
  #text_input.set(the_sum)
  #eq = Tk()
  #eq.title("Answer?")
  #ans = Entry(eq, font=font,textvariable=input, bd=30, insertwidth=4,justify='right').grid(columnspan=4)
  USER_INP = simpledialog.askstring(title="Answer?",
                                    prompt="Whats the answer?")
  answer = USER_INP
  root = Tk()
  #print(answer)
  if (USER_INP == the_sum):
    print("Correct")
    root.title("RIGHT RIGHT RIGHT RIGHT")
  else:
    print("Wrong")
    root.title("WRONG WRONG WRONG WRONG WRONG")
    #canvas = Canvas(root, width = 300, height = 300)
    # canvas.pack()
    #img = ImageTk.PhotoImage(Image.open("bad photos/" + new_img()))
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()

    #img = ImageTk.PhotoImage(Image.open("bad photos/1.png"))
    img = PhotoImage(file="1.png")
    canvas.create_image(20, 20, anchor=NW, image=img)
    root.mainloop()


#    canvas.create_image(image=img)
#   root.mainloop()

  operator = ''

cal = Tk()
cal.title("Evil Calculator")
operator = ''
input = StringVar()
text_input = StringVar()

font = ('airal', 20, 'bold')
screen = Entry(cal,
               font=font,
               textvariable=text_input,
               bd=30,
               insertwidth=4,
               justify='right').grid(columnspan=4)

#======================================================================= 7 8 9 +
btn7 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='7',
              command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='8',
              command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='9',
              command=lambda: btnClick(9)).grid(row=1, column=2)
Addition = Button(cal,
                  padx=16,
                  bd=8,
                  fg="black",
                  font=('arial', 20, 'bold'),
                  text='+',
                  command=lambda: btnClick('+')).grid(row=1, column=3)
#======================================================================= 4 5 6 -
btn4 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='4',
              command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='5',
              command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='6',
              command=lambda: btnClick(6)).grid(row=2, column=2)
Subtraction = Button(cal,
                     padx=16,
                     bd=8,
                     fg="black",
                     font=('arial', 20, 'bold'),
                     text='-',
                     command=lambda: btnClick('-')).grid(row=2, column=3)
#======================================================================= 1 2 3 *
btn1 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='1',
              command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='2',
              command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='3',
              command=lambda: btnClick(3)).grid(row=3, column=2)
Multiply = Button(cal,
                  padx=16,
                  bd=8,
                  fg="black",
                  font=('arial', 20, 'bold'),
                  text='*',
                  command=lambda: btnClick('*')).grid(row=3, column=3)
#======================================================================= 0 clear = /
btn0 = Button(cal,
              padx=16,
              bd=8,
              fg="black",
              font=('arial', 20, 'bold'),
              text='0',
              command=lambda: btnClick(0)).grid(row=4, column=0)
btnClear = Button(cal,
                  padx=16,
                  bd=8,
                  fg="black",
                  font=('arial', 20, 'bold'),
                  text='C',
                  command=lambda: btnClearDisplay()).grid(row=4, column=1)
btnEquals = Button(cal,
                   padx=16,
                   bd=8,
                   fg="black",
                   font=('arial', 20, 'bold'),
                   text='=',
                   command=btnEqualsInput).grid(row=4, column=2)
Division = Button(cal,
                  padx=16,
                  bd=8,
                  fg="black",
                  font=('arial', 20, 'bold'),
                  text='/',
                  command=lambda: btnClick('/')).grid(row=4, column=3)

cal.mainloop
