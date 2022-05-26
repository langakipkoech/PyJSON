#determine the most popular package

from audioop import reverse
import json


#function to sort the list

def install_sort(package):
    return package['analytics']['30d']



with open('package_infor.json','r') as f:
    data = json.load(f)

#to access data with the keyword video
data = [ item for item in data if 'video' in item['desc']]


data.sort(key=install_sort, reverse=True)
#shows the top 5
data_str = json.dumps(data[:5], indent=2)
print(data_str)

#function to sort the list
