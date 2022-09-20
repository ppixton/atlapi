import csv
import requests

names = []
affiliation = []
count = 0
for i in range(26):

    count +=1
    url = "https://last-airbender-api.herokuapp.com/api/v1/characters?perPage=20&page=" + str(count)
    response = requests.get(url)

    for x in response.json():

        if ("(" not in x['name']):
            names.append(x['name'])

header = ['first name', 'last name']
data = []

for x in names:
    first_name = ""
    last_name = ""
    spaces = x.count(" ")
    if (spaces >= 1):
        holder = x.index(" ")
        first_name = x[0:holder]
        last_name = x[holder+1:len(x)]
    else:
        first_name = x
    data.append([first_name, last_name])



print(data)

