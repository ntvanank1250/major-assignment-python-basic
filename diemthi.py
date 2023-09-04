from types import new_class
from provider import *

'''Hàm chính'''
#hàm thêm điểm thi
def themdiemthi():
    print("thêm điểm thi")
    #input
    StudentCode,subjectCode = ghi_diemthi()
    scoreSupport = ghi_scoreSupport()
    scoreMain=ghi_scoreMain()
    # ghi vào file
    scores = {
        "StudentCode": StudentCode,
        "subjectCode": subjectCode,
        "scoreSupport": scoreSupport,
        "scoreMain": scoreMain,
    }
    writeScore(scores)
    print('Thêm điểm thi thành công!')

#hàm tìm kiếm điểm thi
def timkiemdiemthi():
    #trả ra các kết quả theo mã sinh viên và mã môn học
    scores = readScores()
    a=0 
    search=input("Nhập thông tin cần tìm kiếm:")
    for line in scores:
        daTimThay=False
        values=(line["StudentCode"],line["subjectCode"])
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

#hàm sửa điểm thi
def suadiemthi():
    scores = readScores()
    while True:
        e=input("Điền mã học viên và mã môn học muốn sửa \nNếu không biết điền '1' để tìm kiếm\nEnter để tiếp tục:")
        if e=='1':
            while True:
                timkiemdiemthi()
                x=input("'1' Để tìm lại\nEnter để bỏ qua:")
                if x=="1":
                    continue
                c=input("Điền mã học viên:")
                d=input("Điền mã môn học:")
                break              
        else:
            c=input("Điền mã học viên:")
            d=input("Điền mã môn học:")
            y=check_diemthi(c,d)
            if y  is False:
                continue
        break
    for line in scores:
        if c == line["StudentCode"] and d==line["subjectCode"]:
            print_to(line)
            break
    listSua=[   "[1] Sửa mã sinh viên & Sửa mã môn học",
                "[2] Sửa điểm thành phần",
                "[3] Sửa cuối kỳ",
                "[0] Để thoát"]
    for i in listSua:
        print(i)
    
    while True:
        a=input("Nhập lựa chọn:")
        if a not in ("0","1","2","3"):
            print("Bạn đã nhập sai, mời nhập lại:")
            continue
        break
    if a=="0":
        print("Cảm ơn bạn đã sử dụng")
        return
    if a=="1":
        studentNew,studentNews=ghi_diemthi()
        line["StudentCode"]=studentNew
        line["subjectCode"]=studentNews
    if a=="2":
        studentNew=ghi_scoreSupport()
        line["scoreSupport"]=studentNew
    if a=="3":
        studentNew=ghi_scoreMain()
        line["scoreMain"]=studentNew
    writeScores(scores)
    print("Đã thay đổi thành công")
    print_to(line)

def tinhDiem():
    scores=readScores()
    for line in scores:
        tongKet=(int(line["scoreSupport"])+int(line["scoreMain"])*2)/3
        if tongKet>=90:
            xepLoai='A'
        elif tongKet>=70:
            xepLoai='B'
        elif tongKet>=50:
            xepLoai='C'
        else:
            xepLoai='D'
        line["summary"]=tongKet
        line["rank"]=xepLoai
    
    writeNewScores(scores)
    print("Đã tính thành công")
'''Hàm phụ trợ'''
#check mã sinh viên và mã môn học: trả về true or false
def check_diemthi(StudentCode:str,subjectCode:str):
    scores = readScores()
    exists = False

    if StudentCode == '' or subjectCode== '':
        print('Không được để trống!')
        return exists
    if len(StudentCode)!=8 or len(subjectCode)!=8:
        print("Điểm thi không hợp lệ")
        return exists
    for st in scores:
        if st['StudentCode'] == StudentCode and st['subjectCode']==subjectCode:
            exists = True
            return exists
    
    print("Điểm thi không tồn tại")
    return exists

#ghi primary key mã điểm thi
def ghi_diemthi():
    scores = readStudents()
    while True:
        StudentCode=input("Nhập mã học viên:")
        subjectCode=input("Nhập mã môn học :")
        # Check giá trị rỗng
        if StudentCode == '' or subjectCode== '':
            print('Không được để trống!')
            continue

        # Check trùng lặp
        exists = False
        for st in scores:
            if st['StudentCode'] == StudentCode and st['subjectCode']==subjectCode:
                exists = True
                break
        if exists == True:
            print('Điểm thi đã tồn tại !')
            continue  # Next vòng lặp luôn

        # Check định dạng mã sinh viên có 8 ký tự như thầy yêu cầu
        if len(StudentCode)!=8 or len(subjectCode)!=8:
            print("Điểm thi không hợp lệ")
            continue # Next vòng lặp luôn

        # Tat ca cac dieu kien hop le thi thoat vong lap
        break
    return StudentCode,subjectCode

#ghi điểm thành phần
def ghi_scoreSupport():
    while True:
        scoreSupport = input('Điểm thành phần: ')
        scoreSupport = int(scoreSupport)
        if scoreSupport  not in range(0,100):
            print("Điểm thi từ 0 đến 100\nĐiểm thành phần:")
            continue
        break
    return scoreSupport

#ghi điểm cuối kỳ
def ghi_scoreMain():
    while True:
        scoreMain = input('Điểm cuối kỳ:')
        scoreMain = int(scoreMain)
        if scoreMain not in range(0,100):
            print("Điểm thi từ 0 đến 100\nĐiểm cuối kỳ:")
            continue
        break
    return scoreMain

#in ra dưới dạng |       
def print_to(line:dict):
    for x in line.keys():
        print(f"{x}:{line[x]}")
    print("-"*20)   
