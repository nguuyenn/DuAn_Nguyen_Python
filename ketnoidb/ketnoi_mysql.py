import mysql.connector
from mysql.connector import Error

def create_connection():
    """Kết nối đến MySQL và trả về đối tượng connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',       # Địa chỉ máy chủ (hoặc IP)
            user='root',            # Tên tài khoản MySQL
            password='',            # Mật khẩu MySQL (nếu có thì điền vào)
            database='qlthuocankhang'  # Tên database của bạn
        )
        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
