import random



toWrite = []

appse = 383
appre = 127

toolse = 245
toolre = 101


se = []
re = []

with open('13-apps.csv', 'r') as inputFile:
    dataset = inputFile.readlines()

for item in dataset:
    split = item.split(',')

    if split[-2] == 'STILL_EXISTS':
        se.append(item)

    else:
        re.append(item)

for i in range(appse):
    index = random.randint(0,len(se) - 1)

    temp = se[index]
    temp.strip('\n')
    se.pop(index)

    temp = temp.split(',')

    while 'site-package' in temp[2]:
        index = random.randint(0,len(se) - 1)

        temp = se[index]
        temp.strip('\n')
        se.pop(index)

        temp = temp.split(',')

    temp[3] = 'https://github.com/' + temp[1] + '/commit/' + temp[3]

    temp.insert(1, 'Application')

    temp = ','.join(temp)

    toWrite.append(temp)



for i in range(appre):
    index = random.randint(0,len(re) - 1)

    temp = re[index]
    temp.strip('\n')
    dataset.pop(index)

    temp = temp.split(',')

    while 'site-package' in temp[2]:
        index = random.randint(0,len(se) - 1)

        temp = se[index]
        temp.strip('\n')
        dataset.pop(index)

        temp = temp.split(',')

    temp[3] = 'https://github.com/' + temp[1] + '/commit/' + temp[3]
    temp[4] = 'https://github.com/' + temp[1] + '/commit/' + temp[4]

    temp.insert(1, 'Application')

    temp = ','.join(temp)

    toWrite.append(temp)


    #begin tools

se = []
re = []

with open('13-tools.csv', 'r') as inputFile:
    dataset = inputFile.readlines()

for item in dataset:
    split = item.split(',')

    if split[-2] == 'STILL_EXISTS':
        se.append(item)

    else:
        re.append(item)

for i in range(toolse):
    index = random.randint(0,len(se) - 1)

    temp = se[index]
    temp.strip('\n')
    dataset.pop(index)

    temp = temp.split(',')

    while 'site-package' in temp[2]:
        index = random.randint(0,len(se) - 1)

        temp = se[index]
        temp.strip('\n')
        dataset.pop(index)

        temp = temp.split(',')

    temp[3] = 'https://github.com/' + temp[1] + '/commit/' + temp[3]

    temp.insert(1, 'Tool')

    temp = ','.join(temp)

    toWrite.append(temp)


for i in range(toolre):
    index = random.randint(0,len(re) - 1)

    temp = re[index]
    temp.strip('\n')
    dataset.pop(index)

    temp = temp.split(',')

    while 'site-package' in temp[2]:
        index = random.randint(0,len(se) - 1)

        temp = se[index]
        temp.strip('\n')
        dataset.pop(index)

        temp = temp.split(',')

    temp[3] = 'https://github.com/' + temp[1] + '/commit/' + temp[3]
    temp[4] = 'https://github.com/' + temp[1] + '/commit/' + temp[4]

    temp.insert(1, 'Tool')

    temp = ','.join(temp)

    toWrite.append(temp)


with open('sample_label_dataset.csv', 'w') as outputFile:
    for item in toWrite:
        outputFile.write(item)