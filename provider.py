'''Cung cấp các functions để giao tiếp và tập trung các function với database (các file .txt)'''
import os
# Địa chỉ các file .txt
databaseDir = 'database'
studentPath = os.path.join(databaseDir, 'hocvien.txt')
subjectPath = os.path.join(databaseDir, 'monhoc.txt')
scorePath = os.path.join(databaseDir, 'diemthi.txt')
newScorePath = os.path.join(databaseDir, 'ketquathi.txt')

# Tạo thư mục database trong trường hợp không tồn tại
if not os.path.exists(databaseDir):
    os.makedirs(databaseDir)
#----------------------------------------------------------------

# đọc file học viên
def readStudents():
    try:
        #hàm này trả về 1 list, mỗi phần tử là dict của 1 sinh viên
        students = []
        with open(studentPath, 'r', encoding="utf-8") as f:
            lines = f.readline()
            while lines != '':
                line=lines.strip()
                #cắt phần tử thông qua'|' tạo thành 1 list nhỏ
                values = line.split('|')
                #gán giá trị của list nhỏ tương ứng vs key để tạo thành 1 dict
                students.append({
                    "StudentCode": values[0],
                    "FullName": values[1],
                    "Birthday": values[2],
                    "Sex": values[3],
                    "Address": values[4],
                    "Phone": values[5],
                    "Email": values[6]
                })
                lines = f.readline()  # đọc dòng tiếp theo
        return students
    except:
        print("Lỗi gì đó ở phần đọc file học viên")

#ghi lại từ đầu hocvien.txt
def writeStudents(students: list):
    try:
        #truyền vào 1 list, mỗi list mỗi phần tử là 1 dict có định dạng key cố định. xóa nội dung trước đó
        with open(studentPath, 'w', encoding="utf-8") as f:
            for st in students:
                # Convert dict sang dinh dang phu hop trong .txt
                line = f"{st['StudentCode']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"
                f.write(line)
    except:
        print("Lỗi gì đó ở phần viết lại file học viên")

#ghi thêm vào hocvien.txt
def writeStudent(st: dict):
    try:
        #truyền vào 1 list, mỗi list mỗi phần tử là 1 dict có định dạng key cố định. giữ nội dung trước đó
        with open(studentPath, 'at',encoding="utf-8") as f:
            # Convert dict sang dinh dang phu hop trong .txt
            line = f"{st['StudentCode']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"
            f.write(line)
    except:
        print("Lỗi gì đó ở viết thêm vào file học viên")
#------------------------------------------------

#đọc file môn học
def readSubjects():
    try:
        #hàm này trả về 1 list, mỗi phần tử là dict của 1 sinh viên
        Subjects = []
        with open(subjectPath, 'r', encoding="utf-8") as f:
            lines = f.readline()
            while lines != '':
                line=lines.strip()
                #cắt phần tử thông qua'|' tạo thành 1 list nhỏ
                values = line.split('|')
                #gán giá trị của list nhỏ tương ứng vs key để tạo thành 1 dict
                Subjects.append({
                    "subjectCode": values[0],
                    "subjectName": values[1]
                })
                lines = f.readline()  # đọc dòng tiếp theo
        return Subjects
    except:
        print("Lỗi gì đó ở phần đọc file môn học")

#viết lại file môn học
def writeSubjects(Subjects:list):
    try:
        #truyền vào 1 list, mỗi list mỗi phần tử là 1 dict có định dạng key cố định. xóa nội dung trước đó
        with open(subjectPath, 'w', encoding="utf-8") as f:
            for st in Subjects:
                # Convert dict sang dinh dang phu hop trong .txt
                line = f"{st['subjectCode']}|{st['subjectName']}\n"
                f.write(line)
    except:
        print("Lỗi phần viết lại môn học")

#viết thêm vào file môn học
def writeSubject(st:dict):
    #truyền vào 1 list, mỗi list mỗi phần tử là 1 dict có định dạng key cố định. giữ nội dung trước đó
    with open(subjectPath, 'at',encoding="utf-8") as f:
        # Convert dict sang dinh dang phu hop trong .txt
        line = f"{st['subjectCode']}|{st['subjectName']}\n"
        f.write(line)
#--------------------------------------------------

#Đọc file điểm
def readScores():
     #hàm này trả về 1 list, mỗi phần tử là dict của 1 sinh viên
    scores = []
    with open(scorePath, 'r', encoding="utf-8") as f:
        lines = f.readline()
        while lines != '':
            line=lines.strip()
            #cắt phần tử thông qua'|' tạo thành 1 list nhỏ
            values = line.split('|')
            #gán giá trị của list nhỏ tương ứng vs key để tạo thành 1 dict
            scores.append({
                'StudentCode': values[0],
                'subjectCode': values[1],
                "scoreSupport": values[2],
                "scoreMain": values[3]
            })
            lines = f.readline()  # đọc dòng tiếp theo
    return scores

#viết lại file điểm
def writeScores(scores:list):
    try:
        #truyền vào 1 list, mỗi list mỗi phần tử là 1 dict có định dạng key cố định. xóa nội dung trước đó
        with open(scorePath, 'w', encoding="utf-8") as f:
            for st in scores:
                # Convert dict sang dinh dang phu hop trong .txt
                line = f"{st['StudentCode']}|{st['subjectCode']}|{st['scoreSupport']}|{st['scoreMain']}\n"
                f.write(line)
    except:
        print("Lỗi phần viết lại điểm")

#Viết lại file điểm sau khi tính
def writeNewScores(scores:list):
    try:
        #truyền vào 1 list, mỗi list mỗi phần tử là 1 dict có định dạng key cố định. xóa nội dung trước đó
        with open(newScorePath, 'w', encoding="utf-8") as f:
            for st in scores:
                # Convert dict sang dinh dang phu hop trong .txt
                line = f"{st['StudentCode']}|{st['subjectCode']}|{st['scoreSupport']}|{st['scoreMain']}|{st['summary']}|{st['rank']}\n"
                f.write(line)
    except:
        print("Lỗi phần tính điểm")

#ghi thêm file điểm
def writeScore(st:dict):
    #truyền vào 1 list, mỗi list mỗi phần tử là 1 dict có định dạng key cố định. giữ nội dung trước đó
    with open(scorePath, 'at',encoding="utf-8") as f:
        # Convert dict sang dinh dang phu hop trong .txt
        line = f"{st['StudentCode']}|{st['subjectCode']}|{st['scoreSupport']}|{st['scoreMain']}\n"
        f.write(line)

#reser dữ liệu học viên
def resethocvien():
    with open("database/info.csv", mode="r",encoding="utf-8") as f:
        a=f.readlines()
        info=''
        for i in a:
            b=i.split(';')
            info+=(f"{b[0]}|{b[2]}|{b[3]}|1|{b[4]}|0{b[5]}|{b[6]}")
    with open("database/hocvien.txt", mode='w',encoding='utf-8') as g:
        g.write(info)
    print (info)

#In bảng điểm
def writeBangDiems(bangdiem:list):
    with open("database/diemthi.csv",mode='w', encoding='utf-8-sig') as f:
        header="MHV; Họ tên; Ngày sinh; Giới tính; Địa chỉ; SĐT; Email; Môn học; Điểm QT; Điểm KT\n"
        f.write(header)
        for kq in bangdiem:
            line= f"{kq['StudentCode']};{kq['FullName']};{kq['Birthday']};{kq['Sex']};{kq['Address']};{kq['Phone']};{kq['Email']};{kq['subjectName']};{kq['scoreSupport']};{kq['scoreMain']}\n"
            f.write(line)
            