import re


def isPossible(A: dict, B: dict):
    keys = set(B.keys())
    keys.remove('id')
    if not keys.issubset(A.keys()):
        return False
    for k in keys:
        if A[k] < B[k]:
            return False
    return True



def p1():
    with open("input.txt", 'r') as f:
        results = list()
        for line in f:
            name, record = line.split(':')
            name = int(name.split()[1])
            games = record.split(';')
            result = dict()
            result['id'] = name
            for game in games:
                groups = re.findall(r'\d+\s\w+',game)
                for group in groups:
                    num, color = group.split()
                    num = int(num)
                    if color in result:
                        result[color] = max(num, result[color])
                    else:
                        result[color] = num
            results.append(result.copy())
    compare_to = {'red': 12, 'green': 13, 'blue': 14}
    s = 0
    for game in results:
        if isPossible(compare_to, game):
            s += game['id']
    print(s)

def p2():
    with open("input.txt", 'r') as f:
        results = list()
        for line in f:
            name, record = line.split(':')
            name = int(name.split()[1])
            games = record.split(';')
            result = dict()
            result['id'] = name
            for game in games:
                groups = re.findall(r'\d+\s\w+',game)
                for group in groups:
                    num, color = group.split()
                    num = int(num)
                    if color in result:
                        result[color] = max(num, result[color])
                    else:
                        result[color] = num
            results.append(result.copy())
    compare_to = {'red': 12, 'green': 13, 'blue': 14}
    s = 0
    for game in results:
        m = 1
        for k, v in game.items():
            if k != 'id':
                m *= v
        s += m
    print(s)


p1()
p2()