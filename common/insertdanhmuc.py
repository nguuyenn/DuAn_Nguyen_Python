from ketnoidb.ketnoi_mysql import create_connection
from mysql.connector import Error

def insert_danhmuc(ten_danhmuc, mo_ta, trang_thai=1):
    """
    Thêm một bản ghi mới vào bảng danhmuc.
    - ten_danhmuc: tên danh mục (VARCHAR)
    - mo_ta: mô tả danh mục (TEXT)
    - trang_thai: 1 = hiển thị, 0 = ẩn
    """
    connection = create_connection()
    if connection is None:
        print("❌ Không thể kết nối database.")
        return

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta, trang_thai) VALUES (%s, %s, %s)"
        val = (ten_danhmuc, mo_ta, trang_thai)
        cursor.execute(sql, val)
        connection.commit()
        print(f"✅ Đã thêm danh mục: {ten_danhmuc}")
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        cursor.close()
        connection.close()
        print("🔒 Kết nối MySQL đã đóng.")
