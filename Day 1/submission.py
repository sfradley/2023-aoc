import re


# part 1
def p1():
    s = 0
    with open('input.txt', 'r') as f:
        for line in f:
            t = ''.join(re.findall(r'[0-9]+', line))
            s += int(t[0] + t[-1])
    print(s)


def p2():
    s = 0
    nums = {'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
            }

    with open('input.txt', 'r') as f:

        for line in f:
            for left in range(len(line)):
                for k, v in nums.items():
                    if line[left:].startswith(k):
                        line_l = line[:left]
                        line_r = line[left + len(k):]
                        line = line_l + v + line_r
            t = ''.join(re.findall(r'[0-9]+', line))
            s += int(t[0] + t[-1])
    print(s)

p1()
p2()
