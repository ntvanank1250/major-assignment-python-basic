'''(Mã môn học) Tên môn học. Thêm/sửa/xóa/tìm kiếm'''
from provider import *

#hàm thêm môn học
def themmonhoc():
    #input
    subjectCode = ghi_mamonhoc()
    subjectName = ghi_subjectname()
    # ghi vào file
    subjects = {
        "subjectCode": subjectCode,
        "subjectName": subjectName
    }
    writeSubject(subjects)
    print('Thêm môn học thành công!')

#hàm tìm kiếm môn học
def timkiemmonhoc():
    #trả ra các kết quả gần đúng
    subject = readSubjects()
    a=0 
    search=input("Nhập thông tin cần tìm kiếm:")
    for line in subject:
        daTimThay=False
        values=line.values()
        for info in values:
            if search not in info:
                continue
            else:
                daTimThay= True
        if daTimThay ==False:
            continue
        elif daTimThay==True:
            a+=1
            print(f"STT: {a}")
            print_to(line)
            continue
    if a==0:
        print(f"Không tìm thấy giá trị {search}")

#hàm sửa môn học
def suamonhoc():
    subjects = readSubjects()
    while True:
        search=input("Điền mã môn học muốn sửa \nNếu không biết điền '1' để tìm kiếm:")
        if search=='1':
            while True:
                timkiemmonhoc()
                x=input("'1' Để tìm lại\nEnter để bỏ qua:")
                if x=="1":
                    continue
                search=input("Điền mã môn học muốn sửa:")
                break              
        else:
            y=check_mamonhoc(search)
            if y  is False:
                continue
        break
    for line in subjects:
        if search == line["subjectCode"]:
            print_to(line)
            break
    listSua=[   "[1] Sửa mã môn học",
                "[2] Sửa tên môn học",
                "[0] Để thoát"]
    for i in listSua:
        print(i)
    
    while True:
        a=input("Nhập lựa chọn:")
        if a not in ("0","1","2"):
            print("Bạn đã nhập sai, mời nhập lại:")
            continue
        break
    if a=="0":
        print("Cảm ơn bạn đã sử dụng")
        return
    if a=="1":
        subjectNew=ghi_mamonhoc()
        line["subjectCode"]=subjectNew
    if a=="2":
        subjectNew=ghi_subjectname()
        line["subjectName"]=subjectNew
    writeSubjects(subjects)
    print("Đã thay đổi thành công")
    print_to(line)

#hàm xóa môn học
def xoamonhoc():
    subjects = readSubjects()
    while True:
        search=input("Điền mã môn học: \nNếu không biết điền '1' để tìm kiếm:")
        if search=='1':
            while True:
                timkiemmonhoc()
                x=input("'1' Để tìm lại\nEnter để bỏ qua:")
                if x=="1":
                    continue
                search=input("Điền mã môn học muốn xóa:")
                break              
        else:
            y=check_mamonhoc(search)
            if y  is False:
                continue
        break
    index=0
    for line in subjects:
        if search == line["subjectCode"]:
            print_to(line)
            break
        index+=1
    listXoa=[   "[1] Xóa môn học",
                "[0] Thoát chương trình"]
    for i in listXoa:
        print(i)
    while True:
        a=input("Nhập lựa chọn:")
        if a not in ("0","1"):
            print("Bạn đã nhập sai, mời nhập lại:")
            continue
        break
    if a=='0':
        print("Cảm ơn bạn đã sử dụng")
        return
    if a=='1':
        popped1 = subjects.pop(index)
    print(f"Đã xóa{popped1}")
    writeSubjects(subjects)
    print("Đã xóa thành công")
'''Hàm phụ trợ'''

#check mã môn học:
def check_mamonhoc(mamonhoc):
    #Subjects sẽ là 1 cái list bao gồm nhiều cái dict. đọc hàm để hiểu thêm
    Subjects = readSubjects()
    subjectCode = mamonhoc
    exists = False
    for st in Subjects:#chạy biến st(là 1 cái dict) trên list. check key[subjectCode] để xem giá trị trùng lặp
        if st['subjectCode'] == subjectCode:
            exists = True
            break
    if exists != True:
        print('Mã môn học không tồn tại !')
        return False
    if subjectCode == '':
        print('Không được để trống Mã môn học !')
        return False
    # Check định dạng mã môn học có 8 ký tự như thầy yêu cầu
    if len(subjectCode)!=8:
        print("Mã môn học không hợp lệ")
        return False
#check primary key mã môn học
def ghi_mamonhoc():
    #ghi, kiểm tra, trả về mã môn học
    #Subjects sẽ là 1 cái list bao gồm nhiều cái dict. đọc hàm để hiểu thêm
    Subjects = readSubjects()
    while True:
        subjectCode = input('Mã Môn Học: ')
        # Check giá trị rỗng
        if subjectCode == '':
            print('Không được để trống Mã môn học !')
            continue  # Next vòng lặp luôn

        # Check trùng lặp
        exists = False
        for st in Subjects:#chạy biến st(là 1 cái dict) trên list. check key[subjectCode] để xem giá trị trùng lặp
            if st['subjectCode'] == subjectCode:
                exists = True
                break
        if exists == True:
            print('Mã môn học đã tồn tại !')
            continue  # Next vòng lặp luôn

        # Check định dạng mã môn học có 8 ký tự như thầy yêu cầu
        if len(subjectCode)!=8:
            print("Mã môn học không hợp lệ")
            continue # Next vòng lặp luôn

        # Tat ca cac dieu kien hop le thi thoat vong lap
        break
    return subjectCode

#ghi subjectName:
def ghi_subjectname():
    subjectName=input('Tên môn học:')
    return subjectName

#in ra dưới dạng |       
def print_to(line:dict):
    for x in line.keys():
        print(f"{x}:{line[x]}")
    print("-"*20)   
