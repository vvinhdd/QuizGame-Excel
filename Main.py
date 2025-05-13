import random
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys, os

def resource_path(relative_path):
    """Lấy đường dẫn tuyệt đối khi chạy file .exe hoặc .py"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

df = pd.read_excel(resource_path("Source_2.xlsx"), header=1)

list_group = df['Group'].unique()
random_choice = random.choice(list_group)

question_choice = df[ df['Group'] == random_choice]
answers_choice = question_choice['Answer'].tolist()

# print(question_choice)#
# print("Random number: ", random_choice)#
# print("Answers: ", answers_choice)#

user_answers = {}
current_index = 0
selected_columns = ['Answer', 'W1', 'W2', 'W3']
def shuffer_choice():
    re_choice = []
    for i in range(0,5): # because i make an app work with A-B-C-D
        row_values = question_choice.iloc[i][selected_columns] # the choices get
        list_choices = row_values.tolist()
        random.shuffle(list_choices)
        re_choice.append(list_choices)
    return re_choice
list_choice_done = shuffer_choice()

def show_question():
    question_label.config(text=question_choice["Question"].iloc[current_index])
    gen_choices(current_index)
    color_button_change(current_index)
    #answer_text.delete(1.0, tk.END)  # Xóa câu trả lời cũ
    #answer_text.insert(tk.END, user_answers[current_index])  # Điền câu trả lời nếu có
    progress_var.set((current_index) / (len(question_choice)-1) * 100)  # Cập nhật tiến độ
    #result_label.config(text="")  # Xóa kết quả cũ khi chuyển sang câu mới
    check_Button()

def gen_choices(index):

    list_choices_show = list_choice_done[index]
    question_A.config(text=list_choices_show[0])
    question_B.config(text=list_choices_show[1])
    question_C.config(text=list_choices_show[2])
    question_D.config(text=list_choices_show[3])

def handle_click(btn):
    global user_answers, current_index
    selected_text = btn.cget("text")
    # Lưu lại câu trả lời của người dùng
    user_answers[current_index] = selected_text
    # Đổi màu ngay khi nhấn
    color_button_change(current_index)

def next_question():
    global current_index
    if current_index < len(question_choice)-1:
        current_index += 1
        show_question()

def previous_question():
    global current_index
    if current_index > 0:
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

def color_button_change(index):
    global user_answers
    list_buttons = [question_A, question_B, question_C, question_D]
    # Change color for each choice store
    if index in user_answers:
        for button in list_buttons:
            if button['text'] == user_answers[index]:
                button.config(bg='lightblue')
            else:
                button.config(bg='SystemButtonFace')
    else:
        for button in list_buttons:
            button.config(bg='SystemButtonFace')


def submit():
    global user_answers,answers_choice
    result_list_check = [ 'empty','empty', 'empty', 'empty', 'empty']
    result_text = ""
    score = 0
    for index in user_answers:
        if user_answers[index] == answers_choice[index]:
            result_list_check[index] = 'Correct'
            score += 1
        else:
            result_list_check[index] = 'Incorrect'

    for j in range(0,5):
        #print("Question-", j+1," ", result_list_check[j])
        result_text += f"Question - {j+1}:  {result_list_check[j]}\n"

    result_text += f"SCORE: {score} / 5"
    messagebox.showinfo("RESULT", result_text)


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
question_A = Button( nested_frame_1, width=btn_x, height=btn_h, text="", command=lambda: handle_click(question_A))
question_A.grid(row=1, column=0, padx=(10,5), pady=(0,13), sticky="NSEW")
question_B = Button( nested_frame_1, width=btn_x, height=btn_h, text="", command=lambda: handle_click(question_B))
question_B.grid(row=1, column=1, padx=(5,10), pady=(0,13), sticky="NSEW")
question_C = Button( nested_frame_1, width=btn_x, height=btn_h, text="", command=lambda: handle_click(question_C))
question_C.grid(row=2, column=0, padx=(10,5), pady=(0,13), sticky="NSEW")
question_D = Button( nested_frame_1, width=btn_x, height=btn_h, text="", command=lambda: handle_click(question_D))
question_D.grid(row=2, column=1, padx=(5,10), pady=(0,13), sticky="NSEW")

# Test consider layout for Function
btn_x_2 = 28
btn_h_2 = 8
f_previous = Button( nested_frame_2, width=btn_x_2, height=btn_h_2, text="<< Previous", command=previous_question)
f_previous.grid(row=0, column=0, padx=10, pady=(10,5), sticky="NSEW")
f_next = Button( nested_frame_2, width=btn_x_2, height=btn_h_2, text=">> Next", command=next_question)
f_next.grid(row=1, column=0, padx=10, pady=(5,5), sticky="NSEW")
f_submit = Button( nested_frame_2, width=btn_x_2, height=btn_h_2, text="SUBMIT", command=submit)
f_submit.grid(row=2, column=0, padx=10, pady=(5,10), sticky="NSEW")

# ----------
show_question()

root.mainloop()