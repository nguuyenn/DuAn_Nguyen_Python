# ---------------------------
# GIAO DIỆN TKINTER
# ---------------------------
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

from common.insertdanhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
from common.delete_danhmuc import delete_danhmuc
from ketnoidb.ketnoi_mysql import create_connection

# ---------------------------
# HÀM LẤY DANH SÁCH DANH MỤC
# ---------------------------
def load_data():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM danhmuc")
    for row in cursor.fetchall():
        tree.insert("","end",values=row)
    conn.close()
# ---------------------------
# HÀM THÊM DANH MỤC
# ---------------------------
def insert_danhmuc():
    ten = entry_ten.get()
    mota = entry_mota.get()
    if ten == "":
        messagebox.showwarning("Cảnh báo", "Tên danh mục không được để trống!")
        return
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO danhmuc (ten_danhmuc, mo_ta, trang_thai) VALUES (%s, %s, 1)", (ten, mota))
    conn.commit()
    conn.close()
    load_data()
    clear_fields()
    messagebox.showinfo("Thành công", "Đã thêm danh mục!")

# ---------------------------
# HÀM XÓA DANH MỤC
# ---------------------------
def delete_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn danh mục cần xóa!")
        return
    id = tree.item(selected[0])['values'][0]
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM danhmuc WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    load_data()
    clear_fields()
    messagebox.showinfo("Thành công", "Đã xóa danh mục!")

# ---------------------------
# HÀM CẬP NHẬT DANH MỤC
# ---------------------------
def update_danhmuc():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn danh mục để sửa!")
        return
    id = tree.item(selected[0])['values'][0]
    ten = entry_ten.get()
    mota = entry_mota.get()
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE danhmuc SET ten_danhmuc=%s, mo_ta=%s WHERE id=%s", (ten, mota, id))
    conn.commit()
    conn.close()
    load_data()
    clear_fields()
    messagebox.showinfo("Thành công", "Đã cập nhật danh mục!")

# ---------------------------
# HÀM XÓA Ô NHẬP
# ---------------------------
def clear_fields():
    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)
# ---------------------------
# HÀM CHỌN DÒNG TRONG TREEVIEW
# ---------------------------
def select_item(event):
    selected = tree.selection()
    if selected:
        values = tree.item(selected[0])['values']
        entry_ten.delete(0, tk.END)
        entry_ten.insert(0, values[1])
        entry_mota.delete(0, tk.END)
        entry_mota.insert(0, values[2])

root = tk.Tk()
root.title("Quản lý Danh Mục")
root.geometry("700x500")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, padx=5, pady=5)
entry_ten = tk.Entry(frame_input, width=40)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5)
entry_mota = tk.Entry(frame_input, width=40)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

btn_add = tk.Button(frame_btn, text="Thêm", width=10, command=insert_danhmuc)
btn_add.grid(row=0, column=0, padx=5)

btn_update = tk.Button(frame_btn, text="Sửa", width=10, command=update_danhmuc)
btn_update.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_btn, text="Xóa", width=10, command=delete_danhmuc)
btn_delete.grid(row=0, column=2, padx=5)

btn_clear = tk.Button(frame_btn, text="Làm mới", width=10, command=clear_fields)
btn_clear.grid(row=0, column=3, padx=5)

# TreeView hiển thị danh sách
columns = ("id", "ten", "mota")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.heading("id", text="ID")
tree.heading("ten", text="Tên danh mục")
tree.heading("mota", text="Mô tả")
tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<<TreeviewSelect>>", select_item)

load_data()

root.mainloop()