from tkinter import *

root = Tk()
root.geometry("400x400")
root.title(" Шифровщик ")


	
l = Label(text = "Сообщение для шифрования ")
inputtxt = Text(root, height = 9,
				width = 40,
				bg = "light yellow")

Output = Text(root, height = 9,
			width = 40,
			bg = "light cyan")


Display = Button(root, height = 2,
				width = 10,
				text ="Зашифровать",)
Display = Button(root, height = 2,
				width = 10,
				text ="Зашифровать",)

bl = Label(root, text="Привет", font=("Arial Bold", 50))  
lbl.grid(column=4, row=0)  
btn = Button(root, text="Не нажимать!")  
btn.grid(column=5, row=0)  

				


l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
