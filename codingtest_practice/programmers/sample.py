book_time=[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
lst=[]
room=[]
for i in book_time:
    sh,sm=(i[0].split(":"))
    eh,em=(i[1].split(":"))
    lst.append([(int(sh)*60+int(sm)),(int(eh)*60+int(em)+10)])
    lst.sort()
print(lst)