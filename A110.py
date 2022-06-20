import csv
import statistics
import random
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
#mainstd = statistics.mean(data)
#print(mainstd)

#mean and std dev of 100 data points


def random_mean():
    dataset = []
    for i in range(0,100):
        rx = random.randint(0,6508)
        value = data[rx]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#function to plot the mean graph
def show_fig(mlist):
    df = mlist
    fig = ff.create_distplot([df],["average"],show_hist = False)
    fig.show()

#function to get mean 1000 times 
def setup():
    mlist = []
    for i in range(0,1000):
        mean_set = random_mean()
        mlist.append(mean_set)
    show_fig(mlist)
    mean = statistics.mean(mlist)
    print(mean)

setup()

