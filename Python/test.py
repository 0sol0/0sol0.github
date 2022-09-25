from dis import disco
import tkinter as tk
from turtle import color

disvalue = 0
operator = {'+':1, '-':2, '/':3, '*':4, 'C':5, "=":6}
stovalue = 0
oppre = 0


def number_click(value):
    # print('숫자', value)
    global disvalue
    disvalue = (disvalue*10) + value
    str_value.set(disvalue)

def clear():
    global disvalue, operator, stovalue, oppre
    disvalue = 0
    stovalue = 0
    oppre = 0
    str_value.set(disvalue)

def oprator_click(value):
    # print('명령', value)
    global disvalue, operator, stovalue, oppre
    op = operator[value]
    if op == 5: #C
        clear()
    elif disvalue == 0:
        oppre = 0
    elif oppre == 0:
        oppre = op
        stovalue = disvalue
        disvalue = 0
        str_value.set(disvalue)
    elif op == 6: # =
        if oppre == 1: #+
            disvalue = stovalue + disvalue
        if oppre == 2: #-
            disvalue = stovalue - disvalue
        if oppre == 3: #/
            disvalue = stovalue / disvalue
        if oppre == 4: #*
            disvalue = stovalue * disvalue
        
        str_value.set(str(disvalue))
        disvalue = 0
        stovalue = 0
        oppre = 0
    else:
        clear()

def button_click(value):
    # print(value)
    try:
        value = int(value)
        number_click(value)
    except:
        oprator_click(value)

win = tk.Tk()
win.title('계산기')


str_value = tk.StringVar()
str_value.set(str(disvalue))
dis = tk.Entry(win, textvariable=str_value, justify='right')
dis.grid(column=0, row=0, columnspan=4, ipadx=80, ipady=20)

callItem = [['1', '2', '3', 'C'],
            ['4','5', '6', '/'],
            ['7', '8', '9', '*'],
            ['0', '+', '-', '=']]

for i, items in enumerate(callItem):
    for k, item in enumerate(items):
        try:
            color = int(item)
            color = 'black'
        except:
            color = 'green'

        bt = tk.Button(win, 
            text=item, 
            width = 10, 
            height=5,
            bg = color,
            fg = 'white',
            command = lambda cmd = item: 
            button_click(cmd))
            
        bt.grid(column=k, row=(i+1))

# btn = tk.Button(win, text="1", width=10, height=5).grid(column=0, row=1)
# btn = tk.Button(win, text="2", width=10, height=5).grid(column=1, row=1)
# btn = tk.Button(win, text="3", width=10, height=5).grid(column=2, row=1)
# btn = tk.Button(win, text="C", width=10, height=5).grid(column=3, row=1)

# btn = tk.Button(win, text="4", width=10, height=5).grid(column=0, row=2)
# btn = tk.Button(win, text="5", width=10, height=5).grid(column=1, row=2)
# btn = tk.Button(win, text="6", width=10, height=5).grid(column=2, row=2)
# btn = tk.Button(win, text="/", width=10, height=5).grid(column=3, row=2)

# btn = tk.Button(win, text="7", width=10, height=5).grid(column=0, row=3)
# btn = tk.Button(win, text="8", width=10, height=5).grid(column=1, row=3)
# btn = tk.Button(win, text="9", width=10, height=5).grid(column=2, row=3)
# btn = tk.Button(win, text="*", width=10, height=5).grid(column=3, row=3)

# btn = tk.Button(win, text="+", width=10, height=5).grid(column=0, row=4)
# btn = tk.Button(win, text="0", width=10, height=5).grid(column=1, row=4)
# btn = tk.Button(win, text="-", width=10, height=5).grid(column=2, row=4)
# btn = tk.Button(win, text="=", width=10, height=5).grid(column=3, row=4)


win.mainloop()

