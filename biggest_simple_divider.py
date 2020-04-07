import tkinter as tk

class Window(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_button()
		self.create_field()
		self.create_result()
				
	def create_button(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Найти самый большой простой делитель"
		self.hi_there["command"] = self.calc
		self.hi_there.pack(side="top")

	def create_field(self):
		self.hi_there = tk.Entry(self)
		self.hi_there["text"] = "Для какого числа?"
		#self.hi_there["command"] = self.calc
		self.hi_there.pack(side="bottom")

	def create_result(self):
		self.hi_there = tk.Label(self)
		self.hi_there["text"] = "Результат"
		#self.hi_there["command"] = self.calc
		#self.hi_there.pack(side="bottom")

	def calc(self):
		num = int(input('Enter any number: '))
		z = 1
		divid = []
		while z <= num:
			x = num/z
			x = str(x)
			if x[-1::] == '0':
				divid.append(z)
				num = num/z
			z +=1
		print(f'Max simple divider is {max(divid)}')

root = tk.Tk()
app = Window(master=root)
app.mainloop()