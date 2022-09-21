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
        
        if ("affiliation" in x): 
            if ("Air" in x['affiliation']):
                affiliation.append('Air')
            elif ("Fire" in x['affiliation']):
                affiliation.append('Fire')
            elif ("Water" in x['affiliation']):
                affiliation.append('Water')
            elif ("Earth" in x['affiliation']):
                affiliation.append('Earth')
            else:
                affiliation.append('None')
        else:
            affiliation.append("")
        

header = ['Employee Id', 'First Name', 'Last Name', 'Preferred First Name', 'Email', 'Secondary Email', 'Phone Number', 
'Username', 'Password', 'Hire Date', 'Birth Date', 'Role', 'Country Code', 'Supervisor Id', 'Group Name', 'Langauge', "#Affiliation"]
data = []

i = 0

for x in names:
    first_name = ""
    last_name = ""
    id = ""
    i +=1
    if (i >=10 and i<100):
        id = "0" + str(i)
    elif (i >=100):
        id = str(i)
    else:
        id = "00" + str(i)

    spaces = x.count(" ")
    if (spaces >= 1):
        holder = x.index(" ")
        first_name = x[0:holder]
        last_name = x[holder+1:len(x)]
    else:
        first_name = x
    data.append([id, first_name, last_name, '', '', '', '', '', '', '', '', '', '', '', '', '', affiliation[i]])



file_name= "fournations.csv"
with open(file_name, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    #write the header:
    writer.writerow(header)

    #write the rows:
    writer.writerows(data)


# print(data)

