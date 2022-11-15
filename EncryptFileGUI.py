from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

def printf(name):
    print(name)

def encrypt(raw,key,name):
    for index, value in enumerate(raw):
        raw[index] = value ^ int(key)
        
    file = open(name, "wb")
    file.write(raw)
    file.close()
    
def decrypt(data,key,name):
    for index, value in enumerate(data):
        data[index] = value ^ int(key)
    
    file = open(name, "wb")
    file.write(data)
    file.close()



def upload_file():
    raw_file = filedialog.askopenfilename()
    file_name.set(raw_file)
    file=open(raw_file,'rb')
    global file_data
    file_data = bytearray(file.read())

win = Tk()
win.geometry("230x270") 
win.title('XOR!')

Label(win,text='Encryption System' ,width=16, font=('georgia', 15, 'bold'), fg="blue").grid(row=1,column=1)

Button(win, text='Open File', width=10,fg='grey' ,font=('georgia', 8), command = lambda:upload_file()).grid(row=2,column=1)

file_name = StringVar()
Label(win,textvariable=file_name,fg='grey' , font=('georgia', 7)).grid(row=3,column=1) 
file_name.set("")

Label(text="Encyption key :",font=('georgia', 8)).grid(row=4,column=1) 

secret_key = StringVar()
Entry(textvariable=secret_key,width=15,show="*").grid(row=5,column=1) 

Label(text=" ",fg="gray").grid(row=6,column=1) 
Button(text="Encrypt", height=2, width=10, bg="red", fg="white", font=('georgia', 10, 'bold'), command = lambda:encrypt(file_data,secret_key.get(),file_name.get())).grid(row=7,column=1)
Label(text=" ",fg="gray").grid(row=8,column=1) 
Button(text="Dencrypt", height=2, width=10, bg="green", fg="white", font=('georgia', 10, 'bold'), command = lambda:decrypt(file_data,secret_key.get(),file_name.get())).grid(row=9,column=1)
 
win.mainloop()

