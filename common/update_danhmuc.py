from ketnoidb.ketnoi_mysql import create_connection
from mysql.connector import Error

def update_danhmuc(id_danhmuc, ten_moi=None, mo_ta_moi=None, trang_thai_moi=None):
    """
    Cập nhật thông tin danh mục theo ID.
    - id_danhmuc: ID của danh mục cần cập nhật
    - ten_moi: tên danh mục mới (tùy chọn)
    - mo_ta_moi: mô tả mới (tùy chọn)
    - trang_thai_moi: trạng thái mới (1 = hoạt động, 0 = ẩn)
    """
    connection = create_connection()
    if connection is None:
        print("❌ Không thể kết nối database.")
        return

    try:
        cursor = connection.cursor()

        # Tạo câu lệnh UPDATE linh hoạt tùy theo tham số được truyền vào
        fields = []
        values = []

        if ten_moi is not None:
            fields.append("ten_danhmuc = %s")
            values.append(ten_moi)
        if mo_ta_moi is not None:
            fields.append("mo_ta = %s")
            values.append(mo_ta_moi)
        if trang_thai_moi is not None:
            fields.append("trang_thai = %s")
            values.append(trang_thai_moi)

        if not fields:
            print("⚠️ Không có dữ liệu nào để cập nhật.")
            return

        sql = f"UPDATE danhmuc SET {', '.join(fields)} WHERE id = %s"
        values.append(id_danhmuc)

        cursor.execute(sql, tuple(values))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục có ID = {id_danhmuc}")
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID = {id_danhmuc}")

    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
    finally:
        cursor.close()
        connection.close()
        print("🔒 Kết nối MySQL đã đóng.")
