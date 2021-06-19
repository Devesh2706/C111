from os import stat
import pandas as pd
import plotly.express as px
import plotly.figurefactory as ff
import csv
import statistics
import random

df = pd.read_csv("studentMarks.csv")
data = df["Maths_score"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index= random.randint(0,len(data) -1)
        value=data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean 

mean_list = []
for i in range (0, 1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

std_deviation = statistics.stdev(mean_list)    
mean = statistics.mean