'''Hiển thị danh sách các chức năng của chương trình'''
from monhoc import *
from hocvien import *
from diemthi import *
from inbangdiem import *
from provider import *

def menuMain():
    '''Chào Hiệu'''
    menu=[  '[1]    Quản lý thông tin Học viên',
            '[2]    Quản lý thông tin Môn học',
            '[3]    Quản lý thông tin Điểm thi',
            '[4]    Kết xuất bảng điểm ra tệp tin Excel',
            '[0]    Để thoát chương trình'
    ]


    #in ra menu
    for i in menu:
        print(i)

    #vòng lặp vào menu chính
    while True:
        a=input("Nhập lựa chọn:")
        if a not in ("0","1","2","3","4",'resethocvien'):
            print("Bạn đã nhập sai, mời nhập lại:")
            continue
        break
    if a=="1":
        menuhocvien()
    if a=='2':
        menumonhoc()
    if a=='3':
        menudiemthi()
    if a=='4':
        ghepDiem()
    if a=="0":
        print("Cảm ơn bạn đã sử dụng")          
    if a=="resethocvien":
        resethocvien()

def menuhocvien():
    menu=[  "[1] Thêm học viên",
            "[2] Sửa học viên",
            "[3] Xóa học viên",
            "[4] Tìm kiếm học viên",
            "[0] Thoát chương trình"
    ]
    for i in menu:
        print(i)
    while True:
        a=input("Nhập lựa chọn:")
        if a not in ("0","1","2","3","4"):
            print("Bạn đã nhập sai, mời nhập lại:")
            continue
        break
    
    if a=="1":
        themhocvien()
    if a=="2":
        suahocvien()
    if a=="3":
        xoahocvien()
    if a=="4":
        timkiemhocvien()
    
    if a=="0":
        print("Cảm ơn bạn đã sử dụng")

def menumonhoc():
    menu=[  "[1] Thêm môn học",
            "[2] Sửa môn học",
            "[3] Xóa môn học",
            "[4] Tìm kiếm môn học",
            "[0] Thoát chương trình"
    ]
    for i in menu:
        print(i)
    while True:
        a=input("Nhập lựa chọn:")
        if a not in ("0","1","2","3","4"):
            print("Bạn đã nhập sai, mời nhập lại:")
            continue
        break
    
    if a=="1":
        themmonhoc()
    if a=="2":
        suamonhoc()
    if a=="3":
        xoamonhoc()
    if a=="4":
        timkiemmonhoc()
    if a=="0":
        print("Cảm ơn bạn đã sử dụng")

def menudiemthi():
    menu=[  "[1] Nhập điểm",
            "[2] Sửa điểm",
            "[3] Tính điểm tổng kết",
            "[4] Tra cứu điểm",
            "[0] Thoát chương trình"
    ]
    for i in menu:
        print(i)
    while True:
        a=input("Nhập lựa chọn:")
        if a not in ("0","1","2","3","4"):
            print("Bạn đã nhập sai, mời nhập lại:")
            continue
        break
    
    if a=="1":
        themdiemthi()
    if a=="2":
        suadiemthi()
    if a=="3":
        tinhDiem()
    if a=="4":
        timkiemdiemthi()
    if a=="0":
        print("Cảm ơn bạn đã sử dụng")
if __name__=="__main__":
    menuMain()
