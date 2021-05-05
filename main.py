import csv
import plotly.figure_factory as ff

# Getting all the Data in an Object-format in a variable
File_Object = open("Bell_CurveData\Mobile_Data.csv")
Csv_File_Object = csv.reader(File_Object)

# Stoaring it in a list and removing the titles
Csv_List_Data = list(Csv_File_Object)
Csv_List_Data.pop(0)

# Creating a Total Variable to Store the Total
# And Appending it in All_RatingTotal
Total = 0
All_Rating_Total = []

for i in Csv_List_Data:
    AvgRating = float(i[2])
    Total += AvgRating

    All_Rating_Total.append(Total)

Graph = ff.create_distplot([All_Rating_Total], ["Rating"], show_hist=False)
Graph.show()