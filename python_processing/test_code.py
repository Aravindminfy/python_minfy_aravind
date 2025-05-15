from python_processing import sorting 
from python_processing import savejson
from python_processing import  readingcsv
from python_processing import summary
from python_processing import filteringdata


# read_csv
print(readingcsv.read_csv(r'C:\Users\Minfy.DESKTOP-3E50D5N\Documents\py\python_processing\car.csv'))

#----------------------------------------------------------------------------------------------------
# save_as_json
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

path = r"C:\Users\Minfy.DESKTOP-3E50D5N\Documents\py\python_processing\check_json.json"
print("saving the json data in the file is successfull : ",savejson.save_as_json(data,path))
#-------------------------------------------------------------------------------------------------------

# genereate_summary

data = [
    {"name": "Alice", "department": "HR"},
    {"name": "Bob", "department": "IT"},
    {"name": "Charlie", "department": "HR"},
    {"name": "Diana", "department": "Finance"},
    {"name": "Eve", "department": "IT"},
]

print("summary module word successfully : ",summary.generate_summary(data,'department'))
#-----------------------------------------------------------------------------------------------------
# 
data = [
    {"name": "Alice", "department": "HR", "age": 30},
    {"name": "Bob", "department": "IT", "age": 25},
    {"name": "Charlie", "department": "HR", "age": 35},
    {"name": "Diana", "department": "Finance", "age": 30},
    {"name": "Eve", "department": "IT", "age": 25},
]
criteria = {"department": "IT", "age": 25}
print("filter module is working successfully : ",filteringdata.filter_data(data,criteria))