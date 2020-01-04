import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

acerAspirePos = 0
acerAspireNeg = 0
macbookAirPos = 0
macbookAirNeg = 0
macbookProPos = 0
macbookProNeg = 0
asusChromePos = 0
asusChromeNeg = 0
delXpsPos = 0
delXpsNeg = 0
lenovoIdeaPadPos = 0
lenovoIdeaPadNeg = 0
microsoftPos = 0
microsoftNeg = 0

acerAspire = pd.read_csv('acerAspirePrediction.csv', encoding='utf-8').loc[:,'sentiment'].values
macbookAir = pd.read_csv('appleMacbookAirPrediction.csv', encoding='utf-8').loc[:,'sentiment'].values
macbookPro = pd.read_csv('appleMacbookProPrediction.csv', encoding='utf-8').loc[:,'sentiment'].values
asusChrome = pd.read_csv('asusChromePrediction.csv', encoding='utf-8').loc[:,'sentiment'].values
delXps = pd.read_csv('dellXpsPrediction.csv', encoding='utf-8').loc[:,'sentiment'].values
lenovoIdeaPad = pd.read_csv('lenovoIdeapadPrediction.csv', encoding='utf-8').loc[:,'sentiment'].values
microsoft = pd.read_csv('microsoftSurfacePrediction.csv', encoding='utf-8').loc[:,'sentiment'].values

for iterate in acerAspire:
    if iterate == "pos":
        acerAspirePos = acerAspirePos + 1
    else:
        acerAspireNeg = acerAspireNeg + 1
for iterate in macbookAir:
    if iterate == 'pos':
        macbookAirPos += 1
    else:
        macbookAirNeg += 1
for iterate in macbookPro:
    if iterate == 'pos':
        macbookProPos += 1
    else:
        macbookProNeg += 1
for iterate in asusChrome:
    if iterate == 'pos':
        asusChromePos += 1
    else:
        asusChromeNeg += 1
for iterate in delXps:
    if iterate == 'pos':
        delXpsPos += 1
    else:
        delXpsNeg += 1
for iterate in lenovoIdeaPad:
    if iterate == 'pos':
        lenovoIdeaPadPos += 1
    else:
        lenovoIdeaPadNeg += 1
for iterate in microsoft:
    if iterate == 'pos':
        microsoftPos += 1
    else:
        microsoftNeg += 1

x_axis = []
x_axis.append("Acer")
x_axis.append("Macbook Air")
x_axis.append("Macbook Pro")
x_axis.append("Asus")
x_axis.append("Dell")
x_axis.append("Lenovo")
x_axis.append("Microsoft")

listnew = []
listnew.append(int(acerAspirePos/len(acerAspire) * 100))
listnew.append(int(macbookAirPos/len(macbookAir) * 100))
listnew.append(int(macbookProPos/len(macbookPro) * 100))
listnew.append(int(asusChromePos/len(asusChrome) * 100))
listnew.append(int(delXpsPos/len(delXps) * 100))
listnew.append(int(lenovoIdeaPadPos/len(lenovoIdeaPad) * 100))
listnew.append(int(microsoftPos/len(microsoft) * 100))

plt.bar(x_axis,listnew)
plt.xlabel("Product Name")
plt.ylabel("Percentage of Positive Comments")
plt.show()
