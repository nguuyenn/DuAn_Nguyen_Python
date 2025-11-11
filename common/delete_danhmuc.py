from ketnoidb.ketnoi_mysql import create_connection
from mysql.connector import Error

def delete_danhmuc(id_danhmuc):
    """
    Xóa một danh mục khỏi bảng 'danhmuc' theo id.
    - id_danhmuc: ID của danh mục cần xóa
    """
    connection = create_connection()
    if connection is None:
        print("❌ Không thể kết nối database.")
        return

    try:
        cursor = connection.cursor()
        sql = "DELETE FROM danhmuc WHERE id = %s"
        cursor.execute(sql, (id_danhmuc,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có ID = {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID = {id_danhmuc}")

    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        cursor.close()
        connection.close()
        print("🔒 Kết nối MySQL đã đóng.")
