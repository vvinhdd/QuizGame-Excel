# QuizGame-Excel 🎯

Ứng dụng mini giúp ôn tập câu hỏi trắc nghiệm từ file Excel, có giao diện đơn giản với tkinter.

## 📁 Cấu trúc thư mục

```txt
QuizGame-Excel/
├─ quizgame/                # Chứa logic trò chơi và xử lý Excel
├─ data/                    # Chứa file câu hỏi .xlsx
├─ Main.py                  # Chạy ứng dụng chính
├─ requirements.txt         # Thư viện cần thiết
└─ README.md # Giới thiệu dự án
└─ .gitignore               # Bỏ qua file không cần push (cache, spec,...)
```

## 📦 Cài đặt

### 1. Clone project

```sh
git clone https://github.com/vvinhdd/QuizGame-Excel.git
cd QuizGame-Excel
```

### 2. Cài thư viện

```sh
pip install -r requirements.txt
```

## 🚀 Chạy ứng dụng

```sh
python Main.py
```

---

## 🧾 Yêu cầu

* Python 3.8+
* File `data/Source_2.xlsx` phải đúng định dạng (gồm các cột: `Question`, `Answer`, `W1`, `W2`, `W3`, `Group`).

## 🛠 Công nghệ sử dụng

* Python
* Pandas
* Tkinter (GUI)