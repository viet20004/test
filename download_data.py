import pandas as pd
import os

# 1. Tạo thư mục data nếu chưa có
if not os.path.exists('data'):
    os.makedirs('data')
    print("Đã tạo thư mục data.")

# 2. Link file Iris (từ hình ảnh bạn đang xem)
url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

# 3. Tải và lưu vào thư mục data
try:
    df = pd.read_csv(url)
    df.to_csv('data/iris.csv', index=False)
    print("Tải thành công! File đã nằm tại: D:/test/data/iris.csv")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")