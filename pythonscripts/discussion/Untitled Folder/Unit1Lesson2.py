import random
import math
import Stuff.elements

def sigfig(n,s=3):
    return round(n, s-int(math.floor(math.log10(n)))-1)
   
def group_problem1(): 
    pairs=[]
    elements = Stuff.elements.get_elements()
    for e1 in elements:
        for e2 in elements:
            if elements[e1][1] < elements[e2][1] and elements[e1][2] > elements[e2][2]:
                pairs.append([e1,e2])

    question = '''<div id="question"> 
    Find all pairs of elements where the average atomic weight <br>
    of the element with the smaller atomic number is more than the<br>
    average atomic weight of the element with the larger atomic number.<br>
    </div>'''
    
    answer = '<div id="answer"> '
    for i in pairs:
        answer += str(i)
    answer += '</div> '
    return question,answer

def group_problem2():
    question = '''<div id="question"> 
    Using only atomic symbols, write a short poem.<br>
    Keep all leters upper and lower case as on the periodic table<br>
    Examples: Ar + K = ArK, Ti + N + Y = TiNY
    </div>'''
    
    answer = '<div id="answer"> various</div>'

    return question,answer
    
def group_problem3():
    man = [random.randint(100,800)/100. for i in range(5)]
    exp = [random.randint(-50,50) for i in range(5)]
    
    question = '''<div id="question"> 
    The metric system uses prefixes to make new units.<br>
    For example, kilo added to gram makes kilogram.<br>
    The same is true using abbreviations: k with g makes kg.<br>
    The relation between grams and kilograms is 1000 g = 1 kg.<br>
    So kilo means 1000 or 10<sup>3</sup>.<br>
    Converting from grams to kilograms, decrease the power of ten by 3.<br>
    Converting from kilograms to grams, increase the power of ten by 3.<br>
    Examples: 1e6 g = 1e3 kg, 1e6 kg = 1e9 g<br>
    Convert the following to kg:<br>
    {m[0]}e{e[0]} g<br>
    {m[1]}e{e[1]} g<br>
    {m[2]}e{e[2]} g<br>
    {m[3]}e{e[3]} g<br>
    {m[4]}e{e[4]} g<br>
    </div>'''.format(m=man,e=exp)
    exp1 = []
    for i in range(5):
       exp1.append(exp[i]-3)
    answer = '''<div id="answer">
    {m[0]}e{e[0]} g = {m[0]}e{e1[0]} kg<br>
    {m[1]}e{e[1]} g = {m[1]}e{e1[1]} kg<br>
    {m[2]}e{e[2]} g = {m[2]}e{e1[2]} kg<br>
    {m[3]}e{e[3]} g = {m[3]}e{e1[3]} kg<br>
    {m[4]}e{e[4]} g = {m[4]}e{e1[4]} kg<br>

</div>''' .format(m=man,e=exp,e1=exp1)

    return question,answer
    
def group_problem4():
    man = [random.randint(100,800)/100. for i in range(5)]
    exp = [random.randint(-50,50) for i in range(5)]
    
    question = '''<div id="question"> 
    Convert the following to g:<br>
    {m[0]}e{e[0]} kg<br>
    {m[1]}e{e[1]} kg<br>
    {m[2]}e{e[2]} kg<br>
    {m[3]}e{e[3]} kg<br>
    {m[4]}e{e[4]} kg<br>
    </div>'''.format(m=man,e=exp)
    exp1 = []
    for i in range(5):
       exp1.append(exp[i]+3)
    answer = '''<div id="answer">
    {m[0]}e{e[0]} kg = {m[0]}e{e1[0]} g<br>
    {m[1]}e{e[1]} kg = {m[1]}e{e1[1]} g<br>
    {m[2]}e{e[2]} kg = {m[2]}e{e1[2]} g<br>
    {m[3]}e{e[3]} kg = {m[3]}e{e1[3]} g<br>
    {m[4]}e{e[4]} kg = {m[4]}e{e1[4]} g<br>

</div>''' .format(m=man,e=exp,e1=exp1)

    return question,answer
    
def group_problem5(): 
    man = [random.randint(100,800)/100. for i in range(5)]
    exp = [random.randint(-50,50) for i in range(5)]
    
    question = '''<div id="question"> 
    Another metrix prefix unit is milli.<br>
    For example, milli added to gram makes milligram.<br>
    The same is true using abbreviations: m with g makes mg.<br>
    The relation between grams and milligrams is 1000 mg = 1 g.<br>
    So milli means 0.001 or 10<sup>-3</sup>.<br>
    Converting from grams to milligrams, increase the power of ten by 3.<br>
    Converting from milligrams to grams, decrease the power of ten by 3.<br>
    Examples: 1e6 g = 1e9 mg, 1e6 mg = 1e3 g<br>
    Convert the following to mg:<br>
    {m[0]}e{e[0]} g<br>
    {m[1]}e{e[1]} g<br>
    {m[2]}e{e[2]} g<br>
    {m[3]}e{e[3]} g<br>
    {m[4]}e{e[4]} g<br>
    </div>'''.format(m=man,e=exp)
    exp1 = []
    for i in range(5):
       exp1.append(exp[i]+3)
    answer = '''<div id="answer">
    {m[0]}e{e[0]} g = {m[0]}e{e1[0]} mg<br>
    {m[1]}e{e[1]} g = {m[1]}e{e1[1]} mg<br>
    {m[2]}e{e[2]} g = {m[2]}e{e1[2]} mg<br>
    {m[3]}e{e[3]} g = {m[3]}e{e1[3]} mg<br>
    {m[4]}e{e[4]} g = {m[4]}e{e1[4]} mg<br>

</div>''' .format(m=man,e=exp,e1=exp1)

    return question,answer
    
def group_problem6(): 
    man = [random.randint(100,800)/100. for i in range(5)]
    exp = [random.randint(-50,50) for i in range(5)]
    
    question = '''<div id="question"> 
    Convert the following to g:<br>
    {m[0]}e{e[0]} mg<br>
    {m[1]}e{e[1]} mg<br>
    {m[2]}e{e[2]} mg<br>
    {m[3]}e{e[3]} mg<br>
    {m[4]}e{e[4]} mg<br>
    </div>'''.format(m=man,e=exp)
    exp1 = []
    for i in range(5):
       exp1.append(exp[i]-3)
    answer = '''<div id="answer">
    {m[0]}e{e[0]} mg = {m[0]}e{e1[0]} g<br>
    {m[1]}e{e[1]} mg = {m[1]}e{e1[1]} g<br>
    {m[2]}e{e[2]} mg = {m[2]}e{e1[2]} g<br>
    {m[3]}e{e[3]} mg = {m[3]}e{e1[3]} g<br>
    {m[4]}e{e[4]} mg = {m[4]}e{e1[4]} g<br>

</div>''' .format(m=man,e=exp,e1=exp1)

    return question,answer
    
def group_problem7(): 
    man = [random.randint(100,800)/100. for i in range(5)]
    exp = [random.randint(-50,50) for i in range(5)]
    
    question = '''<div id="question"> 
    Convert the following to kg:<br>
    {m[0]}e{e[0]} mg<br>
    {m[1]}e{e[1]} mg<br>
    {m[2]}e{e[2]} mg<br>
    {m[3]}e{e[3]} mg<br>
    {m[4]}e{e[4]} mg<br>
    </div>'''.format(m=man,e=exp)
    exp1 = []
    for i in range(5):
       exp1.append(exp[i]-6)
    answer = '''<div id="answer">
    {m[0]}e{e[0]} mg = {m[0]}e{e1[0]} kg<br>
    {m[1]}e{e[1]} mg = {m[1]}e{e1[1]} kg<br>
    {m[2]}e{e[2]} mg = {m[2]}e{e1[2]} kg<br>
    {m[3]}e{e[3]} mg = {m[3]}e{e1[3]} kg<br>
    {m[4]}e{e[4]} mg = {m[4]}e{e1[4]} kg<br>

</div>''' .format(m=man,e=exp,e1=exp1)

    return question,answer

def group_problem8(): 
    man = [random.randint(100,800)/100. for i in range(5)]
    exp = [random.randint(-50,50) for i in range(5)]
    
    question = '''<div id="question"> 
    Convert the following to mg:<br>
    {m[0]}e{e[0]} kg<br>
    {m[1]}e{e[1]} kg<br>
    {m[2]}e{e[2]} kg<br>
    {m[3]}e{e[3]} kg<br>
    {m[4]}e{e[4]} kg<br>
    </div>'''.format(m=man,e=exp)
    exp1 = []
    for i in range(5):
       exp1.append(exp[i]+6)
    answer = '''<div id="answer">
    {m[0]}e{e[0]} kg = {m[0]}e{e1[0]} mg<br>
    {m[1]}e{e[1]} kg = {m[1]}e{e1[1]} mg<br>
    {m[2]}e{e[2]} kg = {m[2]}e{e1[2]} mg<br>
    {m[3]}e{e[3]} kg = {m[3]}e{e1[3]} mg<br>
    {m[4]}e{e[4]} kg = {m[4]}e{e1[4]} mg<br>

</div>''' .format(m=man,e=exp,e1=exp1)

    return question,answer