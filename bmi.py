from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter.messagebox as mb

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("700x600")
window.resizable(0,0)
window.configure(bg='#ff9933')
Bg = window.cget("bg")
icon = PhotoImage(file='img.png')
window.iconphoto(False, icon)

head_bmi = Label(window, text="BMI (Body Mass Index) Calculator", font=("poppins,20,bold"), fg='#fff', bg=Bg)
head_bmi.pack(padx=5, pady=15)

def BMIcalculate():
    
    classification.config(text="")
    classification.config(bg=Bg)
    output.config(text="")
    healthy.config(text="") 
    healthy_weight_range.config(text="")
    suggest_weight_height.config(text="")
    
    
    age = age_entry.get()
    gender = gender_select.get()
    height = height_entry.get()
    weight = weight_entry.get()
    
    try:
        if(age):
            age = int(age)
            if age < 2 or age > 120:
                raise ValueError("Age must be between 2 and 120")

        height = float(height)
        weight = float(weight)
        
        height_option = height_options.get()
        weight_option = weight_options.get()

        if height_option == 'inch':
            height *= 2.54
        if weight_option == 'lbs':
            weight *= 0.45359237

        height /= 100
        BMI = weight / (height ** 2)

        weight_min = 18.5 * (height ** 2)
        weight_max = 24.9 * (height ** 2)

        output_text = f"BMI = {BMI:0,.2f} kg/m²"
        output.config(text=output_text)
        healthy.config(text="Healthy BMI Range = 18.5 kg/m² - 24.9 kg/m²")
        healthy_weight_range.config(text=f"Healthy Weight for the Height = {weight_min:0,.2f} kg - {weight_max:0,.2f} kg")

        if BMI <= 16:
            classification.config(text="Severe Thinness", fg='#7407f0',bg="#fff")
        elif BMI <= 17:
            classification.config(text="Moderate Thinness", fg="#2a07f0",bg="#fff")
        elif BMI <= 18.5:
            classification.config(text="Mild Thinness", fg="#0760f0",bg="#fff")
        elif BMI <= 25:
            classification.config(text="Normal", fg="#07f074",bg="#fff")
        elif BMI <= 30:
            classification.config(text="Overweight", fg="#6cf007",bg="#fff")
        elif BMI <= 35:
            classification.config(text="Obese Class I", fg="#ff0000",bg="#fff")
        elif BMI <= 40:
            classification.config(text="Obese Class II", fg="#ff0000",bg="#fff")
        else:
            classification.config(text="Obese Class III", fg="#ff0000",bg="#fff")
        
            
        if BMI < 18.5:
            suggest_weight=weight_min-weight
            suggest_weight_height.config(text=f"Gain {suggest_weight:0,.2f}kg to reach normal BMI")
        elif BMI > 25:
            suggest_weight=weight-weight_max
            suggest_weight_height.config(text=f"Loss {suggest_weight:0,.2f} kg to reach normal BMI")
            

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clr_fields():
    age_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    classification.config(text="")
    classification.config(bg=Bg)
    output.config(text="")
    healthy.config(text="") 
    healthy_weight_range.config(text="")
    suggest_weight_height.config(text="")

age_label = Label(window, text="Age", font=("poppins,15"), fg="#fff", bg=Bg).place(x=77, y=100)
age_entry = tk.Entry(window, font=("poppins,15"), fg="#0707f5", bg=Bg)
age_entry.place(x=150, y=100)
age_prefer = Label(window, text="(preferred Age Range: 2-120)", font=("poppins,15"), fg="#fff", bg=Bg).place(x=400, y=100)

gender_label = Label(window, text="Gender", font=("poppins,15"), fg="#fff", bg=Bg).place(x=77, y=150)
gender_select = tk.StringVar()
gender_select.set("male")
option1 = Radiobutton(window, text="Male", font=("poppins,15"), fg="#fff", bg=Bg, variable=gender_select, value="male")
option2 = Radiobutton(window, text="Female", font=("poppins,15"), fg="#fff", bg=Bg, variable=gender_select, value="female")
option1.place(x=150, y=150)
option2.place(x=230, y=150)

height_label = Label(window, text="Height", font=("poppins,15"), fg="#fff", bg=Bg).place(x=77, y=200)
height_entry = tk.Entry(window, font=("poppins,15"), fg="#0707f5", bg=Bg)
height_entry.place(x=150, y=200)
height_options = tk.StringVar()
type_options_height = ['cm', 'inch']
height_combo = Combobox(window, values=type_options_height, font=("poppins,15"), width=5, textvariable=height_options)
height_combo.place(x=350, y=200)
height_options.set("cm")

weight_label = Label(window, text="Weight", font=("poppins,15"), fg="#fff", bg=Bg).place(x=77, y=250)
weight_entry = tk.Entry(window, font=("poppins,15"), fg="#0707f5", bg=Bg)
weight_entry.place(x=150, y=250)
weight_options = tk.StringVar()
type_options_weight = ['kg', 'lbs']
weight_combo = Combobox(window, values=type_options_weight, font=("poppins,15"), width=5, textvariable=weight_options)
weight_combo.place(x=350, y=250)
weight_options.set("kg")

submit = Button(window, text="Calculate", font=("poppins,15"), fg="#0707f5", width=15, height=1, cursor="hand2", command=BMIcalculate)
submit.place(x=150, y=300)

clear = Button(window, text="Clear", font=("poppins,15"), fg="#0707f5", width=15, height=1, cursor="hand2", command=clr_fields)
clear.place(x=350, y=300)

classification = Label(window, text="", font=("poppins,15"),bg=Bg)
classification.place(x=77, y=350)
output = Label(window, text="", font=("poppins,15"), fg="#001f4d", bg=Bg)
output.place(x=77, y=380)
healthy = Label(window, text="", font=("poppins,15"), fg="#001f4d", bg=Bg)
healthy.place(x=77, y=410)
healthy_weight_range = Label(window, text="", font=("poppins,15"), fg="#001f4d", bg=Bg)
healthy_weight_range.place(x=77, y=440)
suggest_weight_height=Label(window, text="", font=("poppins,15"), fg="#001f4d", bg=Bg)
suggest_weight_height.place(x=77,y=470)

window.mainloop()
