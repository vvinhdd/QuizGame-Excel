import random
import pandas as pd
from tkinter import *
from tkinter import ttk

# Đọc bộ nguồn từ file Excel
df = pd.read_excel("Source_2.xlsx", header=1)

list_group = df['Group'].unique()
random_choice = random.choice(list_group)

question_choice = df[ df['Group'] == random_choice]

print(question_choice)#
#print("Random number: ", random_choice)#

current_index = 0


def show_question():
    question_label.config(text=question_choice["Question"].iloc[current_index])
    #answer_text.delete(1.0, tk.END)  # Xóa câu trả lời cũ
    #answer_text.insert(tk.END, user_answers[current_index])  # Điền câu trả lời nếu có
    #progress_var.set((current_index + 1) / len(questions) * 100)  # Cập nhật tiến độ
    #result_label.config(text="")  # Xóa kết quả cũ khi chuyển sang câu mới
    check_Button()

def next_question():
    global current_index
    if current_index < len(question_choice)-1:
        current_index += 1
        show_question()

def previous_question():
    global current_index
    if current_index >= 0:
        current_index -= 1
        show_question()

def check_Button():
    global current_index
    # Disable next button in last question
    if current_index == 0:
        f_previous.config(state=DISABLED)
    else:
        f_previous.config(state=NORMAL)
    # Disable next button in last question
    if current_index == len(question_choice)-1:
        f_next.config(state=DISABLED)
    else:
        f_next.config(state=NORMAL)

def submit():
    return 0


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
nested_frame_1 = Frame(frame, width=500, height=430, bg="lightgray")
nested_frame_1.pack_propagate(False)
nested_frame_1.grid( row=1, column=0, padx=10, pady=(0,10), sticky="E")

nested_frame_2 = Frame(frame, width=230, height=430, bg="lightgray")
nested_frame_2.pack_propagate(False)
nested_frame_2.grid( row=1, column=1, padx=(0,10), pady=(0,10), sticky="E")

# Test consider layout 420 = 300+10 + (?+10) + (?+10)
topic = Frame( nested_frame_1, width=480, height=300, bg="lightgray")
topic.pack_propagate(False)
topic.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="E")
question_label = Label(topic, text="", bg="lightgray", font=("Arial", 12))
question_label.pack(expand=True)

# Test consider layout for answer
btn_x = 5
btn_h = 2
question_A = Button( nested_frame_1, width=btn_x, height=btn_h, text="A")
question_A.grid(row=1, column=0, padx=(10,5), pady=(0,13), sticky="NSEW")
question_B = Button( nested_frame_1, width=btn_x, height=btn_h, text="B")
question_B.grid(row=1, column=1, padx=(5,10), pady=(0,13), sticky="NSEW")
question_C = Button( nested_frame_1, width=btn_x, height=btn_h, text="C")
question_C.grid(row=2, column=0, padx=(10,5), pady=(0,13), sticky="NSEW")
question_D = Button( nested_frame_1, width=btn_x, height=btn_h, text="D")
question_D.grid(row=2, column=1, padx=(5,10), pady=(0,13), sticky="NSEW")

# Test consider layout for Function
btn_x_2 = 28
btn_h_2 = 8
f_previous = Button( nested_frame_2, width=btn_x_2, height=btn_h_2, text="<< Previous", command=previous_question)
f_previous.grid(row=0, column=0, padx=10, pady=(10,5), sticky="NSEW")
f_next = Button( nested_frame_2, width=btn_x_2, height=btn_h_2, text=">> Next", command=next_question)
f_next.grid(row=1, column=0, padx=10, pady=(5,5), sticky="NSEW")
f_submit = Button( nested_frame_2, width=btn_x_2, height=btn_h_2, text="SUBMIT")
f_submit.grid(row=2, column=0, padx=10, pady=(5,10), sticky="NSEW")

# ----------
show_question()

root.mainloop()