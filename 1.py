import plotly.express as pe
import csv
import numpy as np

def getdatasource(datapath):
    marks = []
    days = []

    with open("stud.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks.append(float(row["marks"]))
            days.append(float(row["days"]))
        return{"x":marks,"y":days}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def main():
    datapath = "stud.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

main()