import parse
import math

def get_aEQb(a_ij, b_i): #equal
    if (a_ij < b_i): return None
    if (a_ij == b_i): return [b_i, 1]
    if (a_ij > b_i): return [b_i,b_i]

def get_aLTb(a_ij, b_i): #less then
    if (a_ij <= b_i): return [0, 1]
    if (a_ij > b_i): return [0, b_i]

def choose_one(List, b, results):
    for main_i, main in enumerate(List):
        lists = []
        print(f'{main_i+1}.')
        for el_i, el in enumerate(List):
            if (main_i != el_i):
                lists.append(get_aLTb(el[1],b[1]))
                print(f'min({el[1]},{el[0]}) <= {b[1]}, {el[0]} in {get_aLTb(el[1],b[1])}')
            else:
                lists.append(get_aEQb(el[1],b[1]))
                print(f'min({el[1]},{el[0]}) = {b[1]}, {el[0]} in {get_aEQb(el[1],b[1])}')
        results.append(lists)
    return results
        
def printL(beginning,List):
    print(beginning)
    for line_i, line in enumerate(List):
        output = ''
        x = line_i + 1
        if x % len(line) == 1:
            output = '\n----\n'
        for el_i, el in enumerate(line):
            output += f'x{el_i+1} in {el}\t'
        print(output)

def intersection(interval1, interval2):
    if interval1 == None or interval2 == None: return None
    if interval1[0] >= interval2[0]: x1 = interval1[0]
    else: x1 = interval2[0]
    if interval1[1] >= interval2[1]: x2 = interval2[1]
    else: x2 = interval1[1]
    if x1 <= x2: return [x1, x2]
    else: return None

def intersection_cond(cond1, cond2):
    if None in cond1 or None in cond2: return []  
    answ = []
    for el_i, el in enumerate(cond1):
        answ.append(intersection(cond1[el_i], cond2[el_i]))
    if None in answ:
        return []
    else: return answ

def intersection_line(line1, line2):
    line = []
    for cond1 in line1:
        for cond2 in line2:
            newCond = intersection_cond(cond1, cond2)
            if newCond != []:
                line.append(newCond)
    return line

def cycle(results):
    while(len(results) > 1):
        temp = intersection_line(results[-2], results[-1])
        if (temp != None):
            results[-2] = intersection_line(results[-2], results[-1])
            results.pop()
        else: return None
    return results
    
def group(results):
    power = len(results[0])
    newRez = []
    while len(results)>0:
        newRez.append([results[i] for i in range(power)])
        for i in range(power):
            results.pop(0)
    return(newRez)

def return_max(list1, list2):
    timesG = 0
    timesL = 0
    for i, el in enumerate(list1): 
        if list1[i][0] >= list2[i][0] and list1[i][1] <= list2[i][1]:
            timesG += 1
        if list1[i][0] <= list2[i][0] and list1[i][1] >= list2[i][1]:
            timesL += 1
    if timesG == len(list1):
        return list2
    if timesG == len(list1):
        return list1
        
def cutter(results):
    for i in range(len(results)):
        for j in range(len(results)):
            if results[j] != None and  results[i] != None and i != j:
                rez = return_max(results[i], results[j])
                if rez == results[i]: results[j] = None
                if rez == results[j]: results[i] = None
    return results
        
def print_answer(line):
    if line != []:
        rezult = '\nAnswer: \t('
        for answ_i, answer in enumerate(line):
            for i in range(len(answer)):
                if i != len(answer)-1:
                    rezult += str(answer[i]) + ' x '
                else:
                    rezult += str(answer[i])
            if answ_i != len(line)-1:
                rezult += ') U ('  
            else: rezult +=')'
        print(rezult)
        return
    print('\nAnswer: \t{}')

def print_b(Bij):
    line = ''
    for el in Bij:
        line += f' <{el[0]},{el[1]}>'
    return line

def print_a(Aij):
    line=''
    for el in Aij:
        line += print_b(el)
    return line

def get_log(Aij, Bi):
    print('\n\nStarting...')
    print('Rule:\t',print_a(Aij))
    print('Inference:\t',print_b(Bi))
    results = []
    for list_i, List in enumerate(Aij):
        results = choose_one(List, Bi[list_i], results)
    printL('',results)   
    results = group(results)
    results = cycle(results)  
    c = cutter(*results)
    c = list(filter(lambda a: a != None, c))
    print_answer(c)
   
def column(line):
    new = []
    diff = len(line) // len(set(name[0] for name in line))
    i = 0
    while i < diff:
        li = []
        k = 0
        while i+diff*k < len(line):
            li.append(line[i+diff*k])
            k+=1
        new.append(li)
        i += 1
    return new
