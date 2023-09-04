'''Thêm/Sửa/Xoá/Tìm kiếm học viên'''
from os import truncate
from provider import *
import datetime
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

'''Hàm chính'''
#hàm thêm học viên
def themhocvien():
    print("thêm học viên")
    #input
    studentCode = ghi_mahocvien()
    fullName = ghi_fullname()
    birthday = ghi_birthday()
    sex=ghi_sex()
    address = ghi_address()
    phone=ghi_phone()
    email=ghi_email()
    # ghi vào file
    student = {
        "StudentCode": studentCode,
        "FullName": fullName,
        "Birthday": birthday,
        "Sex": sex,
        "Address": address,
        "Phone": phone,
        "Email": email
    }
    writeStudent(student)
    print('Thêm học viên thành công!')

#hàm tìm kiếm học viên
def timkiemhocvien():
    #trả ra các kết quả gần đúng
    students = readStudents()
    a=0 
    search=input("Nhập thông tin cần tìm kiếm:")
    for line in students:
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

#hàm sửa học viên
def suahocvien():
    students = readStudents()
    while True:
        search=input("Điền mã sinh viên muốn sửa \nNếu không biết điền '1' để tìm kiếm:")
        if search=='1':
            while True:
                timkiemhocvien()
                x=input("'1' Để tìm lại\nEnter để bỏ qua:")
                if x=="1":
                    continue
                search=input("Điền mã sinh viên muốn sửa:")
                break              
        else:
            y=check_mahocvien(search)
            if y  is False:
                continue
        break
    for line in students:
        if search == line["StudentCode"]:
            print_to(line)
            break
    listSua=[   "[1] Sửa mã sinh viên",
                "[2] Sửa Full name",
                "[3] Sửa birthday",
                "[4] Sửa giới tính",
                "[5] Sửa đại chỉ",
                "[6] Sửa SĐT",
                "[7] Sửa email",
                "[0] Để thoát"]
    for i in listSua:
        print(i)
    
    while True:
        a=input("Nhập lựa chọn:")
        if a not in ("0","1","2","3","4","5","6","7"):
            print("Bạn đã nhập sai, mời nhập lại:")
            continue
        break
    if a=="0":
        print("Cảm ơn bạn đã sử dụng")
        return
    if a=="1":
        studentNew=ghi_mahocvien()
        line["StudentCode"]=studentNew
    if a=="2":
        studentNew=ghi_fullname()
        line["FullName"]=studentNew
    if a=="3":
        studentNew=ghi_birthday()
        line["Birthday"]=studentNew
    if a=="4":
        studentNew=ghi_sex()
        line["Sex"]=studentNew
    if a=="5":
        studentNew=ghi_address()
        line["Address"]=studentNew
    if a=="6":
        studentNew=ghi_phone()
        line["Phone"]=studentNew
    if a=="7":
        studentNew=ghi_email()
        line["Email"]=studentNew
    writeStudents(students)
    print("Đã thay đổi thành công")
    print_to(line)
    
                # "StudentCode": values[0],
                # "FullName": values[1],
                # "Birthday": values[2],
                # "Sex": values[3],
                # "Address": values[4],
                # "Phone": values[5],
                # "Email": values[6]

    #todo

#hàm xóa học viên
def xoahocvien():
    students = readStudents()
    while True:
        search=input("Điền mã sinh viên muốn xóa \nNếu không biết điền '1' để tìm kiếm:")
        if search=='1':
            while True:
                timkiemhocvien()
                x=input("'1' Để tìm lại\nEnter để bỏ qua:")
                if x=="1":
                    continue
                search=input("Điền mã sinh viên muốn xóa:")
                break              
        else:
            y=check_mahocvien(search)
            if y  is False:
                continue
        break
    index=0
    for line in students:
        if search == line["StudentCode"]:
            print_to(line)
            break
        index+=1
    listXoa=[   "[1] Xóa sinh viên",
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
        popped1 = students.pop(index)
    print(f"Đã xóa{popped1}")
    writeStudents(students)
    print("Đã xóa thành công")
'''Hàm phụ trợ'''
#ghi email
def ghi_email():
    #ghi kiểm tra, trả về email
    students = readStudents()
    while True:
        email = input('Email: ')
        emailExists = False
        #check trùng lặp
        for st in students:#chạy biến st(là 1 cái dict) trên list. check key[Email] để xem giá trị trùng lặp
            if st['Email'] == email:
                emailExists = True
                break
        if emailExists == True:
            print(f'Email {email} đã tồn tại !')
            continue 
        #check định dạng
        if(re.fullmatch(regex, email)):
            return email
        else:
            print("Nhập sai Gmail, yêu cầu nhập lại")
            continue

#ghi sdt
def ghi_phone():
    #nhập, kiểm tra và trả về số điện thoại
    students = readStudents()
    while True:
        phone = input('Phone: ')
        phoneExists = False
        #check trùng lặp
        for st in students:#chạy biến st(là 1 cái dict) trên list. check key[Phone] để xem giá trị trùng lặp
            if st['Phone'] == phone:
                phoneExists = True
                break
        if phoneExists == True:
            print(f'Số điện thoại {phone} đã tồn tại !')
            continue 
        #check định dạng
        a=("1","2","3","4","5","6","7","8","9","0")
        type_phone=True
        for i in range(1,len(phone)):
            if phone[i] not in a:
                type_phone=False
        if 9>=len(phone) or len(phone)>=13 or type_phone==False:
            print("Số điện thoại không đúng, yêu cầu nhập lại1")
            continue
        if phone[0]!='0' and phone[0]!='+':
            print("Số điện thoại không đúng, yêu cầu nhập lại2")
            continue
        return phone
    
#truyển vào ngày/tháng/năm trả ra true or false
def ghi_birthday():
    # nhập, kiểm tra và ghi ngày sinh
    while True:
        birthday = input('Ngay sinh (DD/MM/YYYY): ')
        try:
            datetime.datetime.strptime(birthday, '%d/%m/%Y')
            return birthday
        except ValueError:
            #raise ValueError("Incorrect data format, should be DD/MM/YYYY")
            print("Nhập sai ngày tháng, mời bạn nhập lại!")
            continue

#check mã sinh viên:
def check_mahocvien(mahocvien):
    #students sẽ là 1 cái list bao gồm nhiều cái dict. đọc hàm để hiểu thêm
    students = readStudents()
    studentCode = mahocvien
    exists = False
    for st in students:#chạy biến st(là 1 cái dict) trên list. check key[StudentCode] để xem giá trị trùng lặp
        if st['StudentCode'] == studentCode:
            exists = True
            break
    if exists != True:
        print('Mã sinh viên không tồn tại !')
        return False
    if studentCode == '':
        print('Không được để trống Mã HV !')
        return False
    # Check định dạng mã sinh viên có 8 ký tự như thầy yêu cầu
    if len(studentCode)!=8:
        print("Mã sinh viên không hợp lệ")
        return False
#check primary key mã học viên
def ghi_mahocvien():
    #ghi, kiểm tra, trả về mã học viên
    #students sẽ là 1 cái list bao gồm nhiều cái dict. đọc hàm để hiểu thêm
    students = readStudents()
    while True:
        studentCode = input('Mã HV: ')
        # Check giá trị rỗng
        if studentCode == '':
            print('Không được để trống Mã HV !')
            continue  # Next vòng lặp luôn

        # Check trùng lặp
        exists = False
        for st in students:#chạy biến st(là 1 cái dict) trên list. check key[StudentCode] để xem giá trị trùng lặp
            if st['StudentCode'] == studentCode:
                exists = True
                break
        if exists == True:
            print('Mã sinh viên đã tồn tại !')
            continue  # Next vòng lặp luôn

        # Check định dạng mã sinh viên có 8 ký tự như thầy yêu cầu
        if len(studentCode)!=8:
            print("Mã sinh viên không hợp lệ")
            continue # Next vòng lặp luôn

        # Tat ca cac dieu kien hop le thi thoat vong lap
        break
    return studentCode

#ghi sex
def ghi_sex():
    while True:
        sex = input('Gioi tinh (0-Nu ; 1-Nam): ')
        if sex!='0' and sex!='1':
            print("Bạn nhập sai giới tính mời bạn nhập lại:")
            continue
        else:
            return sex

#ghi fullname:
def ghi_fullname():
    fullname=input('Ho ten: ')
    return fullname

#ghi địa chỉ:
def ghi_address():
    address = input('Dia chi: ')
    return address

#in ra dưới dạng |       
def print_to(line:dict):
    for x in line.keys():
        print(f"{x}:{line[x]}")
    print("-"*20)   
 
# suahocvien()
