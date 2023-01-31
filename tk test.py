import tkinter as tk
from tkinter import messagebox
w = tk.Tk()
w.title('BMI Calculator')
w.geometry('720x480')
w.config(bg='#40E0D0')
def reset_entry():
    agebx.delete(0, 'end')
    heightbx.delete(0, 'end')
    wheightbx.delete(0, 'end')



def calculate_bmi():
    kg = int(wheightbx.get())
    m = int(heightbx.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)


def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('Your BMI Results', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('Your BMI Results', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('Your BMI Results', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('Your BMI Results', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('Your BMI Results', 'something went wrong!')

frame = tk.Frame(w, padx = 10, pady = 10)
frame.pack()
age = tk.Label(frame, text="age enna da:" )
age.grid(row= 1, column=1)
agebx = tk.Entry(frame, )
agebx.grid(row=1, column=2)
height = tk.Label(frame, text="Height in CMS:")
height.grid(row=2, column=1)
heightbx = tk.Entry(frame, )
heightbx.grid(row=2, column=2)
wheight = tk.Label(frame, text="Weight in kgs:")
wheight.grid(row=3, column=1)
wheightbx = tk.Entry(frame, )
wheightbx.grid(row=3, column=2)

frame3 = tk.Frame(
    frame
)
frame3.grid(row=4, columnspan=3, pady=10)

cal_btn = tk.Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack()

reset_btn = tk.Button(
    frame3,
    text='Reset',
    command=reset_entry
)

reset_btn.pack()

exit_btn = tk.Button(
    frame3,
    text='Exit',
    command=lambda: w.destroy()
)
exit_btn.pack()


w.mainloop()