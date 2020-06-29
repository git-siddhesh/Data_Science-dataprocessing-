from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/Saprotrophic_nutrition'
response=requests.get(url)
response.text
#parsing library- html parser and lxml 
soup=BeautifulSoup(response.text, "lxml")
soup
'''
for i in soup.find_all('a'):
    print(i.get('href'))    

    # we cannot use nested loop here since href is not a tag 
    # instead it is the attribute of a tag

for ptag in soup.find_all('p'):
    #print(ptag)
    for btag in ptag.find_all('b'):
        print(btag)

# but here we would use nested loop since b tag is inside the p tag

#how to create a dataframe usng lists
import pandas as pd 
list=['sidd',18,'18k']
list1=['hinal',15,'22k']
list3=['sejal',22,'11k']
pd.DataFrame([list,list1,list3],columns=['name','age','sal'])


# Web-scapping using APIs (Application programming interfaces)

'''