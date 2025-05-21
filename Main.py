import tkinter as tk
from tkinter import ttk, messagebox
from quizgame import QuizGame, load_questions

def main():
    df = load_questions()
    quiz = QuizGame(df)

    root = tk.Tk()
    root.title("Quiz Game - Excel")
    root.minsize(800, 600)
    root.config(bg="skyblue")

    frame = tk.Frame(root, width=800, height=600)
    frame.pack(padx=20, pady=20)

    # Progress bar frame
    top_bar_frame = tk.Frame(frame, width=740, height=100, bg="blue")
    top_bar_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="E")
    progress_var = tk.DoubleVar()
    progress = ttk.Progressbar(top_bar_frame, variable=progress_var, orient="horizontal", length=720, mode="determinate")
    progress.grid(row=0, column=0, padx=10, pady=10)

    # Main content frames
    nested_frame_1 = tk.Frame(frame, width=500, height=430, bg="lightgray")
    nested_frame_1.pack_propagate(False)
    nested_frame_1.grid(row=1, column=0, padx=10, pady=(0,10), sticky="E")

    nested_frame_2 = tk.Frame(frame, width=230, height=430, bg="lightgray")
    nested_frame_2.pack_propagate(False)
    nested_frame_2.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky="E")

    # Question label
    topic = tk.Frame(nested_frame_1, width=480, height=300, bg="lightgray")
    topic.pack_propagate(False)
    topic.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="E")
    question_label = tk.Label(topic, text="", bg="lightgray", font=("Arial", 12))
    question_label.pack(expand=True)

    # Answer buttons
    btn_width = 5
    btn_height = 2

    question_buttons = []
    for i in range(4):
        btn = tk.Button(nested_frame_1, width=btn_width, height=btn_height, text="")
        question_buttons.append(btn)

    question_buttons[0].grid(row=1, column=0, padx=(10,5), pady=(0,13), sticky="NSEW")
    question_buttons[1].grid(row=1, column=1, padx=(5,10), pady=(0,13), sticky="NSEW")
    question_buttons[2].grid(row=2, column=0, padx=(10,5), pady=(0,13), sticky="NSEW")
    question_buttons[3].grid(row=2, column=1, padx=(5,10), pady=(0,13), sticky="NSEW")

    # Navigation buttons on nested_frame_2
    btn_nav_width = 28
    btn_nav_height = 8

    def previous_question():
        if quiz.current_index > 0:
            quiz.current_index -= 1
            show_question()

    def next_question():
        if quiz.current_index < quiz.total_questions() - 1:
            quiz.current_index += 1
            show_question()

    def submit():
        score = quiz.get_score()
        total = quiz.total_questions()
        result_text = ""
        for i in range(total):
            result_text += f"Question - {i+1}: "
            if quiz.check_answer(i):
                result_text += "Correct\n"
            else:
                result_text += "Incorrect\n"
        result_text += f"\nSCORE: {score} / {total}"
        messagebox.showinfo("RESULT", result_text)

    f_previous = tk.Button(nested_frame_2, width=btn_nav_width, height=btn_nav_height, text="<< Previous", command=previous_question)
    f_previous.grid(row=0, column=0, padx=10, pady=(10,5), sticky="NSEW")

    f_next = tk.Button(nested_frame_2, width=btn_nav_width, height=btn_nav_height, text=">> Next", command=next_question)
    f_next.grid(row=1, column=0, padx=10, pady=(5,5), sticky="NSEW")

    f_submit = tk.Button(nested_frame_2, width=btn_nav_width, height=btn_nav_height, text="SUBMIT", command=submit)
    f_submit.grid(row=2, column=0, padx=10, pady=(5,10), sticky="NSEW")

    # Handle answer button clicks
    def on_answer_click(btn_index):
        def handler():
            selected_text = question_buttons[btn_index]['text']
            quiz.save_answer(quiz.current_index, selected_text)
            update_buttons_color()
        return handler

    for i, btn in enumerate(question_buttons):
        btn.config(command=on_answer_click(i))

    def update_buttons_color():
        idx = quiz.current_index
        if idx in quiz.user_answers:
            selected = quiz.user_answers[idx]
            for btn in question_buttons:
                if btn['text'] == selected:
                    btn.config(bg='lightblue')
                else:
                    btn.config(bg='SystemButtonFace')
        else:
            for btn in question_buttons:
                btn.config(bg='SystemButtonFace')

    def check_buttons_state():
        if quiz.current_index == 0:
            f_previous.config(state=tk.DISABLED)
        else:
            f_previous.config(state=tk.NORMAL)

        if quiz.current_index == quiz.total_questions() - 1:
            f_next.config(state=tk.DISABLED)
        else:
            f_next.config(state=tk.NORMAL)

    def show_question():
        idx = quiz.current_index
        question_label.config(text=quiz.get_question(idx))
        choices = quiz.get_choices(idx)
        for i in range(4):
            question_buttons[i].config(text=choices[i])
        update_buttons_color()
        check_buttons_state()
        progress_var.set((idx) / (quiz.total_questions() - 1) * 100)

    show_question()
    root.mainloop()

if __name__ == "__main__":
    main()
