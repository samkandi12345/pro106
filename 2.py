import plotly.express as pe
import numpy as np
import csv

def getdatasource(datapath):
    coffee = []
    sleep = []

    with open("coffee.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            coffee.append(float(row["coffee"]))
            sleep.append(float(row["sleep"]))
        return{"x":coffee,"y":sleep}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def main():
    datapath = "coffe.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

main()