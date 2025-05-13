import random
import pandas as pd
from tkinter import *
from tkinter import ttk

# Đọc bộ nguồn từ file Excel
df = pd.read_excel("Source_2.xlsx", header=1)

list_group = df['Group'].unique()
random_choice = random.choice(list_group)

question_choice = df[ df['Group'] == random_choice]

#print(question_choice)#
#print("Random number: ", random_choice)#

# -----------UI----------------
root = Tk()
root.title("Part-1 App")
root.minsize(width=800, height=600)

root.config(bg="skyblue")
# Create Frame widget
frame = Frame(root, width=800, height=600)
frame.pack(padx=20, pady=20)

# Frame for Progess bar
top_bar_frame = Frame(frame, width=740, height=100, bg="blue")
top_bar_frame.grid( row=0, column=0, padx=10, pady=10, columnspan=2, sticky="E")
# Progess bar
progress_var = DoubleVar()
progress = ttk.Progressbar(top_bar_frame, variable=progress_var, orient="horizontal", length=720, mode="determinate")
progress.grid(row=0, column=0, padx=10, pady=10)

# Frame for Main content
nested_frame_1 = Frame(frame, width=500, height=430, bg="red")
nested_frame_1.grid( row=1, column=0, padx=10, pady=(0,10), sticky="E")
nested_frame_2 = Frame(frame, width=230, height=430, bg="yellow")
nested_frame_2.grid( row=1, column=1, padx=(0,10), pady=(0,10), sticky="E")

# Test consider layout 420 = 300+10 + (?+10) + (?+10)
topic = Frame( nested_frame_1, width=480, height=300, bg="yellow")
topic.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="E")
# Test consider layout for answer
btn_x = 5
btn_h = 2
question_A = Button( nested_frame_1, width=btn_x, height=btn_h, bg="yellow")
question_A.grid(row=1, column=0, padx=(10,5), pady=(0,13), sticky="NSEW")
question_B = Button( nested_frame_1, width=btn_x, height=btn_h, bg="yellow")
question_B.grid(row=1, column=1, padx=(5,10), pady=(0,13), sticky="NSEW")
question_C = Button( nested_frame_1, width=btn_x, height=btn_h, bg="yellow")
question_C.grid(row=2, column=0, padx=(10,5), pady=(0,13), sticky="NSEW")
question_D = Button( nested_frame_1, width=btn_x, height=btn_h, bg="yellow")
question_D.grid(row=2, column=1, padx=(5,10), pady=(0,13), sticky="NSEW")

root.mainloop()