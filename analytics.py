import csv
import pandas as pd
import numpy as np



def write_to_csv_departments(time,teachingscore,teaching,courseContentscore,courseContent,
                 labWorkscore,labWork,libraryFacilitiesscore,
                 libraryFacilities):

    with open('dataset/database.csv', 'r') as f:
        reader = csv.reader(f)
        for header in reader:
            break
    with open('dataset/database.csv', "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        dict = {'Timestamp': time, 'teachingscore': teachingscore, 'teaching': teaching,
                'coursecontentscore': courseContentscore, 'coursecontent': courseContent,
                'labworkscore': labWorkscore, 'labwork': labWork,'libraryfacilitiesscore': libraryFacilitiesscore,
                'libraryfacilities': libraryFacilities, 'Email Address': ''}
        writer.writerow(dict)

def c2write_to_csv_departments(time,c2teachingscore,c2teaching,c2courseContentscore,c2courseContent,
                 c2labWorkscore,c2labWork,c2libraryFacilitiesscore,
                 c2libraryFacilities):

    with open('dataset/c2database.csv', 'r') as c2f:
        reader = csv.reader(c2f)
        for header in reader:
            break
    with open('dataset/c2database.csv', "a", newline='') as c2f:
        writer = csv.DictWriter(c2f, fieldnames=header)
        c2dict = {'Timestamp': time, 'teachingscore': c2teachingscore, 'teaching': c2teaching,
                'coursecontentscore': c2courseContentscore, 'coursecontent': c2courseContent,
                'labworkscore': c2labWorkscore, 'labwork': c2labWork,'libraryfacilitiesscore': c2libraryFacilitiesscore,
                'libraryfacilities': c2libraryFacilities, 'Email Address': ''}
        writer.writerow(c2dict)

def get_counts():
    path = 'dataset/database.csv'
    df = pd.read_csv(path)
    index = df.index
    no_of_students = len(index)
    total_feedbacks = len(index)*6

    df1 = df.groupby('teachingscore').count()[['teaching']]
    teaching_negative_count = df1['teaching'][-1]
    teaching_neutral_count = df1['teaching'][0]
    teaching_positive_count = df1['teaching'][1]

    df1 = df.groupby('coursecontentscore').count()[['coursecontent']]
    coursecontent_negative_count = df1['coursecontent'][-1]
    coursecontent_neutral_count = df1['coursecontent'][0]
    coursecontent_positive_count = df1['coursecontent'][1]


    df1 = df.groupby('labworkscore').count()[['labwork']]
    labwork_negative_count = df1['labwork'][-1]
    labwork_neutral_count = df1['labwork'][0]
    labwork_positive_count = df1['labwork'][1]

    df1 = df.groupby('libraryfacilitiesscore').count()[['libraryfacilities']]
    libraryfacilities_negative_count = df1['libraryfacilities'][-1]
    libraryfacilities_neutral_count = df1['libraryfacilities'][0]
    libraryfacilities_positive_count = df1['libraryfacilities'][1]


    total_positive_feedbacks = teaching_positive_count + coursecontent_positive_count  + labwork_positive_count + libraryfacilities_positive_count
    total_neutral_feedbacks = teaching_neutral_count + coursecontent_neutral_count  + labwork_neutral_count + libraryfacilities_neutral_count
    total_negative_feedbacks = teaching_negative_count + coursecontent_negative_count  +labwork_negative_count + libraryfacilities_negative_count 

    li = [teaching_positive_count,teaching_negative_count,teaching_neutral_count,
          coursecontent_positive_count,coursecontent_negative_count,coursecontent_neutral_count,
          labwork_positive_count,labwork_negative_count,labwork_neutral_count,
          libraryfacilities_positive_count,libraryfacilities_negative_count,libraryfacilities_neutral_count]

    return no_of_students,\
           int(round(total_positive_feedbacks / total_feedbacks * 100)),\
           int(round(total_negative_feedbacks / total_feedbacks * 100)),\
           int(round(total_neutral_feedbacks / total_feedbacks * 100)),\
            li

def c2get_counts():
    path = 'dataset/c2database.csv'
    df = pd.read_csv(path)
    index = df.index
    no_of_students = len(index)
    total_feedbacks = len(index)*6

    df1 = df.groupby('teachingscore').count()[['teaching']]
    teaching_negative_count = df1['teaching'][-1]
    teaching_neutral_count = df1['teaching'][0]
    teaching_positive_count = df1['teaching'][1]

    df1 = df.groupby('coursecontentscore').count()[['coursecontent']]
    coursecontent_negative_count = df1['coursecontent'][-1]
    coursecontent_neutral_count = df1['coursecontent'][0]
    coursecontent_positive_count = df1['coursecontent'][1]


    df1 = df.groupby('labworkscore').count()[['labwork']]
    labwork_negative_count = df1['labwork'][-1]
    labwork_neutral_count = df1['labwork'][0]
    labwork_positive_count = df1['labwork'][1]

    df1 = df.groupby('libraryfacilitiesscore').count()[['libraryfacilities']]
    libraryfacilities_negative_count = df1['libraryfacilities'][-1]
    libraryfacilities_neutral_count = df1['libraryfacilities'][0]
    libraryfacilities_positive_count = df1['libraryfacilities'][1]


    total_positive_feedbacks = teaching_positive_count + coursecontent_positive_count  + labwork_positive_count + libraryfacilities_positive_count
    total_neutral_feedbacks = teaching_neutral_count + coursecontent_neutral_count  + labwork_neutral_count + libraryfacilities_neutral_count
    total_negative_feedbacks = teaching_negative_count + coursecontent_negative_count  +labwork_negative_count + libraryfacilities_negative_count

    li = [teaching_positive_count,teaching_negative_count,teaching_neutral_count,
          coursecontent_positive_count,coursecontent_negative_count,coursecontent_neutral_count,
          labwork_positive_count,labwork_negative_count,labwork_neutral_count,
          libraryfacilities_positive_count,libraryfacilities_negative_count,libraryfacilities_neutral_count]

    return no_of_students,\
           int(round(total_positive_feedbacks / total_feedbacks * 100)),\
           int(round(total_negative_feedbacks / total_feedbacks * 100)),\
           int(round(total_neutral_feedbacks / total_feedbacks * 100)),\
            li

def get_tables():
    df= pd.read_csv('dataset/database.csv')
    df = df.tail(5)
    return [df.to_html(classes='data')]

def get_titles():
    df = pd.read_csv('dataset/database.csv')
    return df.columns.values

def c2get_tables():
    df= pd.read_csv('dataset/c2database.csv')
    df = df.tail(5)
    return [df.to_html(classes='data')]

def c2get_titles():
    df = pd.read_csv('dataset/c2database.csv')
    return df.columns.values
