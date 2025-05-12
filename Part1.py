import tkinter as tk
from tkinter import ttk
import pandas as pd

# Đọc bộ nguồn từ file Excel
df = pd.read_excel("Source.xlsx", header=1)
df = df.drop(columns=["STT"])  # Loại bỏ cột STT nếu không cần thiết

# Hàm chuẩn hóa chuỗi
def normalize_string(s):
    items = [i.strip().lower() for i in s.split("/")]
    return " / ".join(items)

# Áp dụng chuẩn hóa cho câu hỏi
df['Question'] = df['Question'].apply(normalize_string)

# Lấy ngẫu nhiên 5 câu hỏi
df_sampled = df.sample(n=5, random_state=None)
questions = df_sampled.to_dict(orient='records')

current_index = 0
user_answers = [""] * len(questions)

# Hiển thị câu hỏi và cập nhật trả lời
def show_question():
    question_label.config(text=questions[current_index]["Question"])
    answer_text.delete(1.0, tk.END)  # Xóa câu trả lời cũ
    answer_text.insert(tk.END, user_answers[current_index])  # Điền câu trả lời nếu có
    progress_var.set((current_index + 1) / len(questions) * 100)  # Cập nhật tiến độ
    result_label.config(text="")  # Xóa kết quả cũ khi chuyển sang câu mới

# Kiểm tra câu trả lời và hiển thị kết quả
def check_answer():
    user_answer = answer_text.get(1.0, tk.END).strip()  # Đọc câu trả lời từ Text widget
    user_answers[current_index] = user_answer  # Lưu câu trả lời
    correct_answer = questions[current_index]["Answer"].strip().lower()

    # Hiển thị kết quả kiểm tra
    if user_answer.lower() == correct_answer:
        result_label.config(text=f"Correct! The correct answer is: \n{correct_answer}")
    else:
        result_label.config(text=f"Incorrect! The correct answer is: \n{correct_answer}")
    
    result_label.config(wraplength=600)  # Đảm bảo nội dung không bị cắt, có thể xuống dòng
    result_label.config(height=4)  # Tăng chiều cao để có đủ không gian hiển thị

    # Sau khi trả lời, cho phép người dùng chuyển sang câu tiếp theo
    next_button.config(state=tk.NORMAL)  # Kích hoạt nút "Next"

# Chuyển sang câu hỏi tiếp theo
def next_question():
    global current_index
    if current_index < len(questions) - 1:
        current_index += 1
        show_question()  # Hiển thị câu hỏi tiếp theo
        next_button.config(state=tk.DISABLED)  # Vô hiệu hóa nút "Next" cho đến khi câu trả lời được kiểm tra
    else:
        submit()  # Nếu là câu hỏi cuối cùng, nộp bài

# Nộp bài và kiểm tra đáp án tổng quát
def submit():
    correct = 0
    for i in range(len(questions)):
        if user_answers[i].strip().lower() == questions[i]["Answer"].strip().lower():
            correct += 1
    result_label.config(text=f"You got {correct} out of {len(questions)} correct!")

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Part-1 App")
root.geometry("800x400")

# Progress Bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill=tk.X, padx=40, pady=10)

# Câu hỏi
question_label = tk.Label(root, text="", font=("Arial", 18), wraplength=550)
question_label.pack()

# Trường nhập câu trả lời (Thay thế Entry bằng Text widget)
answer_text = tk.Text(root, font=("Arial", 14), width=50, height=4, wrap="word")
answer_text.pack()

# Nút điều hướng (Chỉ còn nút "Next")
button_frame = tk.Frame(root)
button_frame.pack()

# Nút kiểm tra câu trả lời (chỉ cho phép sau khi người dùng nhập câu trả lời)
check_button = tk.Button(button_frame, text="Check Answer", command=check_answer)
check_button.grid(row=0, column=0)

# Nút điều hướng chuyển câu (chỉ hiện sau khi đã kiểm tra câu hiện tại)
next_button = tk.Button(button_frame, text="Next", command=next_question, state=tk.DISABLED)
next_button.grid(row=0, column=1)

submit_button = tk.Button(button_frame, text="Submit", command=submit)
submit_button.grid(row=0, column=2)

# Hiển thị kết quả sau khi nộp bài
result_label = tk.Label(root, text="", font=("Arial", 14), justify=tk.LEFT)
result_label.pack()

# Hiển thị câu hỏi đầu tiên
show_question()

root.mainloop()