from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Unit Converter')
root.config(bg='grey94')

l1 = Label(root, text='   1. Enter the number to be converted:   ', font=('Helvetica','12','bold'))
l1.grid(row=0, columnspan=2)

displayStr = StringVar()
displayStr.set('0')
display = Entry(root, bd=4, width=10, font=('Helvetica','18'), textvariable=displayStr, justify=CENTER)
display.grid(row=1, columnspan=2)

l2 = Label(root, text='   2. Select the type of conversion:   ', font=('Helvetica','12','bold'))
l2.grid(row=2, columnspan=2)

def KgToLbs():
    global displayStr, result
    a = displayStr.get()
    result = float(a) * 2.20462262
    messagebox.showinfo('Result ', result)

def LbsToKg():
    global displayStr, result
    b = displayStr.get()
    result = float(b) * 0.45359237
    messagebox.showinfo('Result', result)

def CmToInches():
    global displayStr, result
    c = displayStr.get()
    result = float(c) * 0.393700787
    messagebox.showinfo('Result ', result)

def InchesToCm():
    global displayStr, result
    d = displayStr.get()
    result = float(d) * 2.54
    messagebox.showinfo('Result ', result)

def FtToM():
    global displayStr, result
    e = displayStr.get()
    result = float(e) * 0.3048
    messagebox.showinfo('Result ', result)

def MToFt():
    global displayStr, result
    f = displayStr.get()
    result = float(f) * 3.2808399
    messagebox.showinfo('Result ', result)

def KmToMiles():
    global displayStr, result
    g = displayStr.get()
    result = float(g) * 0.621371192
    messagebox.showinfo('Result ', result)

def MilesToKm():
    global displayStr, result
    h = displayStr.get()
    result = float(h) * 1.609344
    messagebox.showinfo('Result ', result)
            
switch = IntVar()
switch.set(1)

KgToLbsButton = Radiobutton(root, text='kg to lbs', variable = switch, value = 1)
KgToLbsButton.grid(row=3, column=0)

LbsToKgButton = Radiobutton(root, text='lbs to kg', variable = switch, value = 2)
LbsToKgButton.grid(row=3, column=1)

CmToInchesButton = Radiobutton(root, text='cm to inches', variable = switch, value = 3)
CmToInchesButton.grid(row=4, column=0)

InchesToCmButton = Radiobutton(root, text='inches to cm', variable = switch, value = 4)
InchesToCmButton.grid(row=4, column=1)

FtToMButton = Radiobutton(root, text='ft to m', variable = switch, value = 5)
FtToMButton.grid(row=5, column=0)

MToFtButton = Radiobutton(root, text='m to ft', variable = switch, value = 6)
MToFtButton.grid(row=5, column=1)

KmToMilesButton = Radiobutton(root, text='km to miles', variable = switch, value = 7)
KmToMilesButton.grid(row=6, column=0)

MilesToKmButton = Radiobutton(root, text='miles to km', variable = switch, value = 8)
MilesToKmButton.grid(row=6, column=1)

l3 = Label(root, text='   3. Press the button below:   ', font=('Helvetica','12','bold'))
l3.grid(row=7, columnspan=2)

def Convert():
    try:
        z = float(displayStr.get())
    except:
        messagebox.showerror('Error','You have entered text instead of a number!')
        return
    if z <= 0:
        messagebox.showwarning('Warning','It can not be neither a negative number nor zero!')
    else:
        y = switch.get()
        if y == 1:
            KgToLbs()
        elif y == 2:
            LbsToKg()
        elif y == 3:
            CmToInches()
        elif y == 4:
            InchesToCm()
        elif y == 5:
            FtToM()
        elif y == 6:
            MToFt()
        elif y == 7:
            KmToMiles()
        else:
            MilesToKm()
        
ConvertButton = Button(root, bd=1, text='CONVERT', font=('Helvetica','12'), bg='lavender', command=Convert)
ConvertButton.grid(row=8, columnspan=2)
    
root.mainloop()
