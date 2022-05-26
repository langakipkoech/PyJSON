
from unittest import result
import requests
import json
import time
#capture the requuiests of  all the packgages

r = requests.get('https://formulae.brew.sh/api/formula.json')
#parse to json
packages_json = r.json()

#empty list to store the data captured from the requests

results = []

#gettting accurate timings in python

t1 = time.perf_counter()

#looping over all packages 
for package in packages_json:

#the package name
    package_name = package['name']
    package_desc = package['desc']
# Genrate url 

    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

#get analytics
    r=requests.get(package_url)

    package_json = r.json()

#use json modle to make it neater and the packages will be dumped as string
#dump data as a string
    #package_str = json.dumps(package_json, indent = 2)
    installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

#python dictionary will be used to generate the values for this file
    data = {
        'name':package_name,
        'desc':package_desc,
        'analytics':
        {
            '30d':installs_30,
            '90d':installs_90,
            '365d':installs_365
        }
    }

    results.append(data)

    time.sleep(r.elapsed.total_seconds())

    print(f'Got {package_name} in {r.elapsed.total_seconds()}')

   

#time after for loop
t2 = time.perf_counter()
print('Finished in {t2 - t1} seconds')
  
#open new file

with open('package_infor.json', 'w') as f:
    json.dump(results, f, indent=2)

#print(package_str)
print(results)