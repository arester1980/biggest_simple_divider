import tkinter as tk

root = tk.Tk()


# def calc(num):
#     z = 1
#     divide = []
#     while z <= num:
#         x = num / z
#         x = str(x)
#         if x[-1::] == '0':
#             divid.append(z)
#             num = num / z
#         z += 1
#     return max(divide)

def calc(num):
    return print(num)


num_field = tk.Entry()
calc_butt = tk.Button(
    text='Посчитать',
    font=('Helvetica', '12', 'bold'),
    command=calc(num_field.get())
)
lab_entry = tk.Label(text='Введите число', font=('Helvetica', '12'))
lab_res = tk.Label(text='Результат', font=('Helvetica', '12'))
res = tk.Label(text=calc, font=('Helvetica', '14', 'bold'))
calc_butt.grid(row=1, column=3, columnspan=2)
num_field.grid(row=1, column=2)
lab_entry.grid(row=1, column=1, sticky='w')
lab_res.grid(row=2, column=1, sticky='w')
res.grid(row=2, column=2, sticky='w')

root.mainloop()
