import tkinter as tk
from tkinter import font
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%A, %B %d, %Y')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)  

root = tk.Tk()
root.title("Enhanced Digital Clock")
root.geometry("400x200")  
root.configure(bg='black')  
root.overrideredirect(True) 

time_font = font.Font(family='Helvetica', size=48, weight='bold')
date_font = font.Font(family='Arial', size=18)

time_label = tk.Label(root, font=time_font, bg='black', fg='white')
time_label.pack(pady=10)

date_label = tk.Label(root, font=date_font, bg='black', fg='gray')
date_label.pack(pady=5)

update_time()

root.mainloop()
#This is my py

