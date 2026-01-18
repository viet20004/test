import pandas as pd
from pathlib import Path

# 1. Xác định thư mục gốc của dự án (D:\test)
# .parent.parent có nghĩa là nhảy từ thư mục 'notebooks' lên thư mục 'test'
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Tạo đường dẫn đến file dữ liệu (Hãy đổi 'Superstore.csv' thành tên file của bạn)
data_path = BASE_DIR / 'data' / 'iris.csv'

# 3. Đọc dữ liệu với thông báo lỗi rõ ràng
try:
    df = pd.read_csv(data_path)
    print("Chúc mừng! Bạn đã đọc file thành công.")
    print(df.head())
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file tại: {data_path}")
    print("Mẹo: Hãy kiểm tra xem bạn đã đổi tên 'Superstore.csv' đúng với file trong thư mục data chưa nhé!")