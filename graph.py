#direct correlation
#import plotly.express as px
#import csv

#with open("./data/IceCream.csv") as csv_file:
    #df=csv.DictReader(csv_file) 
    #fig=px.scatter(df,x="Temperature", y ="Ice-cream Sales")
    #fig.show()

#inverse correlation
import plotly.express as px
import csv

with open("./data/coffee.csv") as csv_file:
    df=csv.DictReader(csv_file) 
    fig=px.scatter(df,x="Coffee", y ="Sleep")
    fig.show()