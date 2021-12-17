from tkinter import *
def clear():
    principle.delete(0,END)
    rate.delete(0,END)
    number.delete(0,END)
    time.delete(0,END)
    output.delete(0,END)
    principle.focus_set()

def calculate():
    p=int(principle.get())
    r=float(rate.get())
    n=int(number.get())
    t=int(time.get())
    ans= p*pow((1+(r/n)),(n*t))
    output.insert(10,ans)

if __name__=="__main__":
    root=Tk()
    root.geometry('400x400')
    root.title('Compound interest calculator')
    l1=Label(root,text='Principle amount:')
    l2=Label(root,text='Interest rate:')
    l3=Label(root,text='No. of times interest is compounded:')
    l4=Label(root,text='Years:')

    l1.grid(row=1,column=0, padx=10, pady=10)
    l2.grid(row=2,column=0, padx=10, pady=10)
    l3.grid(row=3,column=0, padx=10, pady=10)
    l4.grid(row=4,column=0, padx=10, pady=10)

    principle=Entry(root)
    rate=Entry(root)
    number=Entry(root)
    time=Entry(root)
    output=Entry(root)

    principle.grid(row=1,column=1, padx=10, pady=10)
    rate.grid(row=2,column=1, padx=10, pady=10)
    number.grid(row=3,column=1, padx=10, pady=10)
    time.grid(row=4,column=1, padx=10, pady=10)
    output.grid(row=5,column=1,padx=10,pady=10)

    button1 = Button(root, text='Calculate', padx=10, pady=10, command=calculate)
    button2 = Button(root, text='Clear', padx=10, pady=10, command=clear)
    button1.grid(row=5, column=0,pady=10)
    button2.grid(row=6,column=0,pady=10)

    root.mainloop()