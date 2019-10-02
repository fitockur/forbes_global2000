import csv
import requests


NAME_OF_LIST = 'global2000'
YEAR = '2019'
LIMIT = 2000
FILE_NAME = f"{NAME_OF_LIST}_{YEAR}.csv"
col_names = [
 'uri',
 'description',
 'rank',
 'organizationName',
 'industry',
 'country',
 'revenue',
 'profits',
 'assets',
 'marketValue',
 'employees',
 'ceoName',
 'ceoTitle',
 'city',
 'yearFounded',
 'webSite']


raw_ref = f'https://www.forbes.com/forbesapi/org/{NAME_OF_LIST}/{YEAR}/position/true.json?limit={LIMIT}'
res = requests.get(raw_ref).json()['organizationList']['organizationsLists']

with open(FILE_NAME, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=col_names, delimiter=';')
    writer.writeheader()
    for company in res:
        cur_list = []
        for name in col_names:
            cur_list.append(company.get(name))
        writer.writerow(dict(zip(col_names, cur_list)))
