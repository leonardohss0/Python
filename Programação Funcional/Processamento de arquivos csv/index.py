import csv


#função de teste
def show(title, fileName, f):
    print('--- ' + title + ' ---')
    with open("arquivo.csv", 'r') as csv_file:
        data = csv.DictReader(csv_file)
        newData = f(data)

        try:
            iterator = iter(newData)
        except TypeError:
            print(newData)
        else:
            for row in newData:
                print(row)

getTeam = lambda team: lambda data: \
    filter(lambda e: e['Clube 1'] == team or e['Clube 2'] == team, data)

show('getTeam', 'arquivo.csv', getTeam('Bahia'))