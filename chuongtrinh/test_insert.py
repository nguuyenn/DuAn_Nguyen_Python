from common.insertdanhmuc import insert_danhmuc

while True:
    ten=input("Nhap vao ten danh muc")
    mota=input("Nhap vao mo ta")

    insert_danhmuc(ten,mota)
    con=input("Tiep tuc Y, Thoat thi nhan ki tu bat ki")
    if con!="Y":
        break