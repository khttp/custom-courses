import requests
from models import STUDENT

url = "https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json"
student_data = requests.get(url).json()

for student in student_data:
    model = STUDENT(**student)
    print(model.json())
