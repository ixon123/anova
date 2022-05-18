import pandas
import numpy
import matplotlib.pyplot as pyplot

male = 1
female = 0

data = [ 
    {
        "name" : "diego",
        "age" : 12,
        "sex" : male,
        "icfes" : 299
    },
    {
        "name" : "dana",
        "age" : 12,
        "sex" : female,
        "icfes" : 299
    },
    {
        "name" : "ivon",
        "age" : 12,
        "sex" :  male,
        "icfes" : 299
    },
    {
        "name" : "dixon",
        "age" : 12,
        "sex" :  female,
        "icfes" : 299
    }
]

score_to_win = 251

data_frame = pandas.read_csv(f"e:\Anova\MOCK_DATA.csv")
data_frame["afect_prom"] = numpy.where(data_frame.icfes >= score_to_win, False, True)
print(data_frame.where(data_frame.icfes >= score_to_win).count())

print(data_frame.head())

sum = 0
sum_win = 0
sum_lost = 0
amount = len(data)

for a in data:
    score = a["icfes"]
    sum = score + sum
    if score >= score_to_win:
        sum_win = sum_win + 1
    else:
        sum_lost = sum_lost + 1

prom =  sum / amount