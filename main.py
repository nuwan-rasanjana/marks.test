

from flask import Flask,render_template,request
import csv
import pandas as pd
from sklearn.cluster import KMeans

app=Flask(__name__)

@app.route("/home" )
def home():
      return render_template("home.html")

@app.route("/analyse" )
def analyse():
      return render_template("check.html")

@app.route("/back" )
def back():
      return render_template("add.html")

@app.route("/view" )
def view():

    csvfile = csv.reader(open('marks.csv', 'r'))
    itercsvfile = iter(csvfile)
    next(itercsvfile)

    return render_template("view.html",itercsvfile=itercsvfile)


@app.route("/checkvalidate", methods=['post'] )
def checkvalidate():
    noofgroups=request.form['noofgroups']
    intnoofgroups=int(noofgroups)

    df = pd.read_csv("marks.csv")
    dfata = df.iloc[:,1:10]
    dftarget = df.iloc[:,-1]

    kmeans = KMeans(intnoofgroups)
    kmodel = kmeans.fit(dfata)

    s=[]
    csvfile = csv.reader(open('marks.csv', 'r'))
    for row in csvfile:
        s = s+[row[0]]
    l=len(s)

    return render_template('result.html',s=s,data=kmeans.labels_,l=l,intnoofgroups=intnoofgroups)



if __name__ == "__main__":
    app.run()



