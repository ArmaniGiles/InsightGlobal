import csv
import json

with open('Demographic_Statistics_By_Zip_Code.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
import random
recordOfId = []
wholeRecord = []
fields = {}
mainJson = {}
import copy
with open('./fixtures/myFixtures.json', 'w') as f:
    someStr = json.loads(json.dumps(rows))
    for it in someStr:
        for k in list(it.keys()):
            if k != 'JURISDICTION NAME' and k != 'COUNT FEMALE' and  k != 'COUNT MALE':
                del it[k] 
        while(1):
            subVar = random.randint(0,1000)
            if subVar not in recordOfId:
                    it['JURISDICTION_NAME'] = it.pop('JURISDICTION NAME')
                    it['COUNT_FEMALE'] = it.pop('COUNT FEMALE')
                    it['COUNT_MALE'] = it.pop('COUNT MALE')
                    mainJson['pk'] = subVar
                    mainJson['model'] = 'search.zipcode'
                    mainJson['fields'] = it
                    wholeRecord.append(copy.deepcopy(mainJson))
                    recordOfId.append(subVar)
                    break
    json.dump(wholeRecord, f)



