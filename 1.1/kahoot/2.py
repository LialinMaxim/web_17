cc = {}


def addone(country):
    if country in cc:
        cc[country] += 1
    else:
        cc[country] = 1


addone('1')
addone('2')
addone('3')

print(len(cc))
