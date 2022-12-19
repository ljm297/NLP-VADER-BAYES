import os
import csv
def smote():
    #drop columns we dont care about
    with open("./output/sentiment_out.csv","r") as source:
        rdr= csv.reader( source )
        with open("./output/sentiment_temp.csv","w", newline='', encoding='utf-8') as result:
            wtr= csv.writer( result )
            for r in rdr:
                wtr.writerow((r[1],r[5]))
    #remove neutral elements
    with open("./output/sentiment_temp.csv","r") as result:
        rdr = csv.reader(result)
        with open("output/noNeutral_train.csv", "w", newline='', encoding='utf-8') as writeresult:
            wtr = csv.writer(writeresult)
            for r in rdr:
                if r[1] != "Neutral":
                    wtr.writerow(r)
    #remove temp file
    os.remove("./output/sentiment_temp.csv")                      
smote()