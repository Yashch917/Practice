#student marks analyzer
#use numpy to store analyze and display statistic of student marks
#array creation create 2d array take 5 subjects of 5 students
#find average mean of student
#highest marks and lowest by a student
#find all marks greater than 90
#find index of student highest average

import numpy as np
marks=np.array([[85,67,45,88,24],
                [45,33,22,86,56],
                [95,97,98,99,100],
                [45,77,12,35,97],
                [78,87,47,56,78]])
print("Student Marks:\n",marks)
print("Average Marks of each Student:",np.mean(marks,axis=1))
print("Highest Marks of each Student:",np.max(marks,axis=0))
print("Lowest Marks of each Student:",np.min(marks,axis=0))
print("Marks greater than 90:",marks[marks>90])
print("Index of Student with Highest Average Marks:",np.argmax(np.mean(marks,axis=1)))