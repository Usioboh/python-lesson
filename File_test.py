# import json

# about = {
#     "name": "Ehidiamhen Usioboh",
#     "gender": "male",
#     "age": 17,
#     "skills": ["HTML, CSS, C#, Python"]
# }

# with open("about.json", "w", encoding="utf-8") as f:
#     json.dump(about, f, indent=4)

# with open("about.json", "r") as f:
#     about = json.load(f)

# print(about)

import csv

attendance = [["Name", "Age", "Gender"],
              ["Isaac", 17, "Male"],
              ["John", 22, "Male"],
              ["James", 20, "Male"],
              ["Grace", 19, "Female"]

              ]

with open("attendance.csv", "w", newline="", encoding="utf-8") as f:
    att = csv.writer(f)
    att.writerows(attendance)

with open("attendance.csv", "r") as f:
    att = csv.reader(attendance)
for att in attendance:
    print(att)
