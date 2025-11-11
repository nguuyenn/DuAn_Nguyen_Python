from common.update_danhmuc import update_danhmuc

while True:
    madm = input("Ma danh muc")
    ten=input("Nhap vao ten danh muc")
    mota=input("Nhap vao mo ta")

    update_danhmuc(madm,ten,mota)
    con=input("Tiep tuc Y, Thoat thi nhan ki tu bat ki")
    if con!="Y":
        break