from ketnoidb.ketnoi_mysql import create_connection
from mysql.connector import Error

def get_all_danhmuc():
    """
    Lấy danh sách tất cả các danh mục trong bảng 'danhmuc'.
    Trả về danh sách tuple hoặc in ra console.
    """
    connection = create_connection()
    if connection is None:
        print("❌ Không thể kết nối database.")
        return

    try:
        cursor = connection.cursor(dictionary=True)  # Trả về kiểu dict thay vì tuple
        cursor.execute("SELECT id, ten_danhmuc, mo_ta, trang_thai FROM danhmuc")

        danhmuc_list = cursor.fetchall()

        if len(danhmuc_list) == 0:
            print("⚠️ Chưa có danh mục nào trong cơ sở dữ liệu.")
        else:
            print("📋 Danh sách danh mục:")
            for dm in danhmuc_list:
                print(f"🆔 {dm['id']} | {dm['ten_danhmuc']} | {dm['mo_ta']} | Trạng thái: {'Hiển thị' if dm['trang_thai'] else 'Ẩn'}")

        return danhmuc_list

    except Error as e:
        print("❌ Lỗi khi truy vấn dữ liệu:", e)
    finally:
        cursor.close()
        connection.close()
        print("🔒 Kết nối MySQL đã đóng.")
