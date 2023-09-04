from provider import *

def ghepDiem():
    try:
        subjects=readSubjects()
        scrores=readScores()
        students=readStudents()
        ghepDiem=[]
        #bảng điếm có 2 khóa nên lấy làm gốc
        for line in scrores:
            studentCode=line["StudentCode"]
            subjectCode= line["subjectCode"]
            scoreSupport=line['scoreSupport']
            scoreMain=line["scoreMain"]
            for i in subjects:
                if i["subjectCode"]==subjectCode:
                    break
            subjectName = i['subjectName']        
                    
            for y in students:
                if y['StudentCode']==studentCode:
                    break
            fullName=y['FullName']
            birthday=y['Birthday']
            sex=y['Sex']
            address=y['Address']
            phone=y['Phone']
            email=y['Email']
            
            ghepDiem.append({"StudentCode": studentCode,
                            'subjectCode': subjectCode,
                            'subjectName':subjectName,
                            'FullName':fullName,
                            'Birthday':birthday,
                            'Sex':sex,
                            'Address':address,
                            'Phone':phone,
                            'Email':email,
                            'scoreSupport':scoreSupport,
                            'scoreMain':scoreMain
                            })
        writeBangDiems(ghepDiem)
        print("In bảng điểm thành công")
    except:
        print("Lỗi gì đó ở phần ghi điểm")