import json

with open("student.csv",encoding='utf-8')as f:
    student=f.read() 
with open("student.json",'wb')as f:
    f.write(json.dumps(student).encode('utf-8'))