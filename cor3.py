#marks but we didn't change the variables.
import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    iceCSales=[]
    coldDrink=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            iceCSales.append(float(row["marks"]))
            coldDrink.append(float(row["days"]))
    return {"x":iceCSales,"y":coldDrink}

def findcorr(data_source):
    correlation=np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between marks vs days: ", correlation[0,1])

def setup():
    data_path="./data/marks.csv"
    data_source=getdatasource(data_path)
    findcorr(data_source)

setup()