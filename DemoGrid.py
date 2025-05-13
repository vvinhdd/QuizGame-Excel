from tkinter import *
import pandas as pd
import random

root = Tk()

# Data mẫu
data = {
    'Question': ['What is 2+2?', 'Capital of France?'],
    'Answer': ['4', 'Paris'],
    'W1': ['3', 'London'],
    'W2': ['5', 'Rome'],
    'W3': ['6', 'Berlin'],
}
df = pd.DataFrame(data)

current_index = 0
btns = []
user_answers = {}
shuffled_choices = {}

question_label = Label(root, text='', font=("Arial", 16))
question_label.pack(pady=10)

# Tạo 4 nút trắc nghiệm
for _ in range(4):
    b = Button(root, text='', width=20, height=2)
    b.pack(pady=2)
    btns.append(b)

def handle_answer(selected_text):
    global user_answers, current_index

    # Lưu lại câu trả lời của người dùng
    user_answers[current_index] = selected_text

    # Tô màu lại nút đã chọn
    for btn in btns:
        if btn['text'] == selected_text:
            btn.config(bg='lightblue')
        else:
            btn.config(bg='SystemButtonFace')

def update_question():
    global current_index, shuffled_choices

    if current_index >= len(df):
        question_label.config(text="Hết câu hỏi!")
        for b in btns:
            b.config(text="", command=None, bg="SystemButtonFace")
        return

    row = df.iloc[current_index]
    question_label.config(text=row['Question'])

    # Trộn hoặc lấy lại đáp án đã trộn
    if current_index not in shuffled_choices:
        answers = [row['Answer'], row['W1'], row['W2'], row['W3']]
        random.shuffle(answers)
        shuffled_choices[current_index] = answers
    else:
        answers = shuffled_choices[current_index]

    # Cập nhật nút và màu
    for i in range(4):
        btns[i].config(text=answers[i],
                       command=lambda a=answers[i]: handle_answer(a))

        # Tô màu nếu đã chọn câu đó rồi
        if current_index in user_answers and answers[i] == user_answers[current_index]:
            btns[i].config(bg='lightblue')
        else:
            btns[i].config(bg='SystemButtonFace')

def move_next():
    global current_index
    if current_index < len(df) - 1:
        current_index += 1
        update_question()

def move_previous():
    global current_index
    if current_index > 0:
        current_index -= 1
        update_question()

Button(root, text="Câu trước", command=move_previous).pack(pady=5)
Button(root, text="Câu tiếp", command=move_next).pack(pady=5)

update_question()
root.mainloop()