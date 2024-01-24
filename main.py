import math
from tkinter import * 

windowHeight = 600
windowWidth = 600

def create_calculator():
    #Variable to control operations made
    global operation,afterOperation
    operation = ""
    afterOperation = 0

    #Window creation and settings(size of th window, title, resizable or not)
    window = Tk()
    window.title("Tk Claculator")
    window.geometry(f"{windowWidth}x{windowHeight}")
    window.resizable(False, False)#(True, True)->enable resizable

    #Create main frame where all the widgets will be
    mainFrame = Frame(window, width=600, height=600)
    mainFrame.pack(pady=0)

    #creation of calculator´s screen
    screen = Entry(mainFrame, width=60)
    screen.grid(row=0, column=0,pady=27, columnspan=4)

    #creation of the buttons
    #first row
    percentageBtn = Button(mainFrame, text="%",width=20,height=5,border=3)
    ceBtn = Button(mainFrame, text="CE", width=20,height=5,border=3,command=lambda: ceBtn())
    cBtn = Button(mainFrame, text="C",width=20,height=5,border=3,command=lambda: cBtn())
    eraseBtn = Button(mainFrame, text="<X",width=20,height=5,border=3, command=lambda: eraseLastNumber())
    percentageBtn.grid(row=1, column=0)
    cBtn.grid(row=1, column=1)
    ceBtn.grid(row=1, column=2)
    eraseBtn.grid(row=1, column=3)

    #second row
    multiInvBtn = Button(mainFrame, text="1/x",width=20,height=5,border=3, command=lambda: invMulti())
    scndPowBtn = Button(mainFrame, text="x^2", width=20,height=5,border=3, command=lambda: scndPow())
    sqrRootBtn = Button(mainFrame, text="V2",width=20,height=5,border=3,command=lambda: sqrRoot())
    divideBtn = Button(mainFrame, text="/",width=20,height=5,border=3,command=lambda: divide())
    multiInvBtn.grid(row=2, column=0)
    scndPowBtn.grid(row=2, column=1)
    sqrRootBtn.grid(row=2, column=2)
    divideBtn.grid(row=2, column=3)

    #third row
    num7Btn = Button(mainFrame, text="7",width=20,height=5,border=3, command=lambda: insertNumber("7"))
    num8Btn = Button(mainFrame, text="8", width=20,height=5,border=3, command=lambda: insertNumber("8"))
    num9Btn = Button(mainFrame, text="9",width=20,height=5,border=3, command=lambda: insertNumber("9"))
    multiplyBtn = Button(mainFrame, text="X",width=20,height=5,border=3, command=lambda: multiply())
    num7Btn.grid(row=3, column=0)
    num8Btn.grid(row=3, column=1)
    num9Btn.grid(row=3, column=2)
    multiplyBtn.grid(row=3, column=3)

    #fourth row
    num4Btn = Button(mainFrame, text="4",width=20,height=5,border=3, command=lambda: insertNumber("4"))
    num5Btn = Button(mainFrame, text="5", width=20,height=5,border=3, command=lambda: insertNumber("5"))
    num6Btn = Button(mainFrame, text="6",width=20,height=5,border=3, command=lambda: insertNumber("6"))
    minusBtn = Button(mainFrame, text="-",width=20,height=5,border=3,command=lambda: minus())
    num4Btn.grid(row=4, column=0)
    num5Btn.grid(row=4, column=1)
    num6Btn.grid(row=4, column=2)
    minusBtn.grid(row=4, column=3)

    #fifth row
    num1Btn = Button(mainFrame, text="1",width=20,height=5,border=3, command=lambda: insertNumber("1"))
    num2Btn = Button(mainFrame, text="2", width=20,height=5,border=3,command=lambda: insertNumber("2"))
    num3Btn = Button(mainFrame, text="3",width=20,height=5,border=3,command=lambda: insertNumber("3"))
    plusBtn = Button(mainFrame, text="+",width=20,height=5,border=3,command=lambda: plus())
    num1Btn.grid(row=5, column=0)
    num2Btn.grid(row=5, column=1)
    num3Btn.grid(row=5, column=2)
    plusBtn.grid(row=5, column=3)

    #sixth row
    invBtn = Button(mainFrame, text="+/-",width=20,height=5,border=3, command=lambda: inverseNumber())
    num0Btn = Button(mainFrame, text="0", width=20,height=5,border=3, command=lambda: insertNumber("0"))
    commaBtn = Button(mainFrame, text=",",width=20,height=5,border=3, command=lambda: insertComma())
    equalBtn = Button(mainFrame, text="=",width=20,height=5,border=3,command=lambda: equal())
    invBtn.grid(row=6, column=0)
    num0Btn.grid(row=6, column=1)
    commaBtn.grid(row=6, column=2)
    equalBtn.grid(row=6, column=3)

    #Function that inserts numbers on the screen
    def insertNumber(number):
        global afterOperation
        if afterOperation==1:#Control done to delete last used numbers in operations made
            screen.delete(0,END)
            currentNumber = screen.get()#Obtain the current number
            screen.insert(0, currentNumber+number)#insert it again adding the number to it´s end ex:("Hello" + "world")
            afterOperation=0
           
        else:
            currentNumber = screen.get()#Obtain the current number
            screen.delete(0,END)#delete it
            screen.insert(0, currentNumber+number)#insert it again adding the number to it´s end ex:("Hello" + "world")


    #Function that deletes last inserted value
    def eraseLastNumber():
        currentNumber = screen.get()#Obtain the current number
        screen.delete(0,END)#delete it
        screen.insert(0,currentNumber[0:-1])#insert it again on screen, but this time without the last value inserted

    #Function that turn number positive into negative and vice versa
    def inverseNumber():
        currentNumber = screen.get()#Obtain number
        screen.delete(0, END)#Delete screen content
        if float(currentNumber)>0:
            screen.insert(0, '-' + currentNumber)#If positive adds '-' to it´s beginning
        elif float(currentNumber)<0:
            screen.insert(0,currentNumber[1:])#If negative deletes '-' from it´s beginning
    
    #Function to turn integer numbers into decimals
    def insertComma():
        currentNumber = screen.get()
        if(currentNumber.count('.')==0):#Prevents from having an infinite number of '.'
            screen.delete(0, END)
            screen.insert(0, currentNumber+'.')

    #Function that divides 1 by the number inserted
    def invMulti():
        currentNumber = screen.get()
        screen.delete(0, END)
        result = 1/float(currentNumber)
        screen.insert(0, str(result))

    #Function that multiplies the number by itself 'x**2'
    def scndPow():
        currentNumber = screen.get()
        screen.delete(0, END)
        result = float(currentNumber)**2
        screen.insert(0, result)
    #Square Root of the number    
    def sqrRoot():
        currentNumber = screen.get()
        screen.delete(0, END)
        result = math.sqrt(float(currentNumber))
        screen.insert(0, str(result))
    #Adding numbers
    def plus():
        global operation,firstNumber
        operation = "plus"
        firstNumber = screen.get()
        screen.delete(0, END)
    #Subtracting numbers
    def minus():
        global operation, firstNumber
        operation = "minus"
        firstNumber = screen.get()
        screen.delete(0, END)
    #Multiplying Numbers
    def multiply():
        global operation, firstNumber
        operation = "multiply"
        firstNumber = screen.get()
        screen.delete(0, END)
    #Divide numbers
    def divide():
        global operation, firstNumber
        operation = "divide"
        firstNumber = screen.get()
        screen.delete(0, END)

    #Function that deletes the currentNumber inserted but mantain saved the firstNumber
    def ceBtn():
        screen.delete(0,END)

    #Function that deletes currentnNumber and the first number inserted
    def cBtn():
        global firstNumber,secondNumber
        screen.delete(0,END)
        firstNumber=""
        secondNumber=""

    #Function that analyzes the operation performed and inserts the result on screen
    def equal():
        global firstNumber,afterOperation,secondNumber
        secondNumber = screen.get()

        if operation=="plus":
            if firstNumber!="":
                screen.delete(0, END)
                result = float(firstNumber) + float(secondNumber)
                screen.insert(0,str(result))
                afterOperation=1
            else:
                screen.delete(0, END)
                screen.insert(0,secondNumber)

        elif operation=="minus":
            if firstNumber!="":   
                screen.delete(0, END)
                result = float(firstNumber) - float(secondNumber)
                screen.insert(0,str(result))
                afterOperation=1
            else:
                screen.delete(0, END)
                screen.insert(0,"-"+secondNumber)

        elif operation == "multiply":
            if firstNumber!="":
                screen.delete(0, END)
                result = float(firstNumber) * float(secondNumber)
                screen.insert(0,str(result))
                afterOperation=1
            else:
                screen.delete(0, END)
                screen.insert(0,"0")

        elif operation == "divide":
            if firstNumber!="":
                screen.delete(0, END)
                result = float(firstNumber) / float(secondNumber)
                screen.insert(0,str(result))
                afterOperation=1
            else:
                screen.delete(0, END)
                screen.insert(0,"0")

    window.mainloop()



if __name__ == '__main__':
    app = create_calculator()
