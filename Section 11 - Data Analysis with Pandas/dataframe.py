import pandas as pd

data = {"Students":["Aj","Mark","Bob","Rachel","Steven"],"Maths":[98,50,23,72,87],"Science":[96,45,76,54,1],"Sports":["Basketball","Swimming","TT","Badminton","Tae Kwon Do"]}

students = pd.DataFrame(data,columns=["Students","Maths","Science","Sports"])
print(students)