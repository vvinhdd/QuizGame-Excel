import pandas as pd
import sys
import os

def resource_path(relative_path):
    """Lấy đường dẫn tuyệt đối, hỗ trợ khi đóng gói .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_questions(excel_path="data/Source_2.xlsx"):
    df = pd.read_excel(resource_path(excel_path), header=1)
    return df