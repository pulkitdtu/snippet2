
import json
import csv
import os
import pathlib

path4 = 'data/form004/' # read all json files here
path5 = 'data/form005/' # data/form004# data/form005 all files . 
outputPath = 'output/' # folder to keep output file.
outputFullPath = outputPath + 'output.csv'
row_list = [['S.No.', "Number","Name of Institute","Faculty Load Matrix","Courses","Syllabus "]]

def first_function():       
    serial_number = 1
    set4 = getFileNamesAsSet(path4)
    set5 = getFileNamesAsSet(path5)
    union = set4.union(set5)
    for fileName in union:
        form4 = None
        form5 = None
        if(fileName in set4 and os.path.isfile(path4 + fileName)):
            with open(path4+fileName) as f:
                form4 = json.load(f)
        if(fileName in set5 and os.path.isfile(path5 + fileName)):
            with open(path5 +fileName) as f:
                form5 = json.load(f)
        
        array = createArrayFromJson(serial_number, form4, form5)
        row_list.append(array)
        serial_number += 1

    print(row_list)
    pathlib.Path(outputPath).mkdir(parents=True, exist_ok=True) 
    with open(outputFullPath, 'w', newline='') as file2:
        output = csv.writer(file2)
        output.writerows(row_list)
        
    print('Done!')




def createArrayFromJson(serial_number, form4, form5):
    array1 = []
    number = ' '
    name = ' '
    destinationFile = ' '
    checkedCourses = ' '
    courseSyllabusDetail = ' '
    if form4 and isinstance(form4, dict):
        section1 = form4.get('section1', None)
        if section1:
            number = section1.get('mtiNumber', ' ')
            name = section1.get('mtiName', ' ')
            destinationFile = section1.get('dstFileName', ' ')
        
        section2 = form4.get('section2', None)
        if section2:
            for x in section2:
                id = str(x.get("courseId", " "))
                courseName = str(x.get("courseName", " "))
                check =  str(x.get("check", " "))
                checkedCourses +=  "  "+id + "-" + courseName + ":" + check + ";"

    if form5 and isinstance(form5, dict):
        section1_2 = form5.get('section1', None)
        if section1_2 and (number == ' ' or number == '') and (name == ' ' or name == ''):
            number = section1_2.get('mtiNumber', ' ')
            name = section1_2.get('mtiName', ' ')
        
        


section2_2 = form5.get('section2', None)
        if section2_2:
            for x in section2_2:
                id = str(x.get("courseId"))
                courseName = str(x.get("courseName", " "))
                uploaded =  str(x.get("uploaded", " "))
                status =  str(x.get("courseStatus", " "))
                courseFile = str(x.get("dstFileName", " "))
                courseSyllabusDetail += " " + id + "-" + courseName + ":" + uploaded + ":" + status + ":" + courseFile + ";"

    array1.append(serial_number)
    array1.append(number)
    array1.append(name)
    array1.append(destinationFile)
    array1.append(checkedCourses)
    array1.append(courseSyllabusDetail)
    return array1

def getFileNamesAsSet(path):
    set4 = set()
    if os.path.isdir(path):
        list = os.listdir(path)
        set4.update(list)
    return set4

first_function() # call the starting point of the execution


