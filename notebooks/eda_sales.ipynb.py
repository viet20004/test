import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Cấu hình đường dẫn hệ thống
# Nhảy từ thư mục 'notebooks' lên thư mục gốc 'test'
BASE_DIR = Path(__file__).resolve().parent.parent
data_path = BASE_DIR / 'data' / 'iris.csv'

# 2. Đọc dữ liệu
try:
    df = pd.read_csv(data_path)
    print("--- 1. Đọc dữ liệu thành công ---")

    # 3. Kiểm tra dữ liệu cơ bản
    print("\n5 dòng đầu tiên của dữ liệu:")
    print(df.head())

    print("\nThông tin cấu trúc dữ liệu (kiểm tra giá trị trống):")
    print(df.info())

    print("\nThống kê mô tả (Trung bình, Min, Max...):")
    print(df.describe())

    # 4. Trực quan hóa dữ liệu (Data Visualization)
    print("\n--- 2. Đang khởi tạo biểu đồ... ---")

    # Thiết lập giao diện biểu đồ
    sns.set_theme(style="whitegrid")

    # Biểu đồ 1: Pairplot - Xem mối quan hệ giữa tất cả các cặp thuộc tính
    # Đây là biểu đồ quan trọng nhất để phân loại các loài hoa
    pair_plot = sns.pairplot(df, hue='variety', palette='husl', markers=["o", "s", "D"])
    pair_plot.fig.suptitle("Ma trận phân tích đặc tính các loài hoa Iris", y=1.02)

    # Biểu đồ 2: Boxplot - Xem phân phối chiều dài cánh hoa (Petal Length) theo từng loài
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='variety', y='petal.length', data=df, palette='Set2')
    plt.title('Phân phối chiều dài cánh hoa theo từng loài')
    plt.xlabel('Loài hoa')
    plt.ylabel('Chiều dài cánh hoa (cm)')

    # Hiển thị tất cả biểu đồ
    plt.show()

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file tại: {data_path}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")