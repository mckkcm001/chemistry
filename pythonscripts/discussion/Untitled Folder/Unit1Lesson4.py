import random
import math
import Stuff.elements
import Stuff.molecularFormulas

def sigfig(n,s=3):
    return round(n, s-int(math.floor(math.log10(n)))-1)
    
def group_problem1(): 
    formulas = Stuff.molecularFormulas.get_formulas()
    formula = random.choice(formulas)
    elements = Stuff.elements.get_elements()
    e1 = formula[0]
    s1 = formula[1]
    e2 = formula[2]
    s2 = formula[3]
    aw1 = elements[e1][2]
    aw2 = elements[e2][2]
    w1 = s1*aw1
    w2 = s2*aw2
    wt = w1 + w2
    p1 = w1/wt*100
    p2 = w2/wt*100
    pt = p1 + p2
    
    question = '''<div id="question"> 
    Find the percent composition of {0}'''.format(e1)
    if s1 > 1:
        question += '<sub>{0}</sub>'.format(s1)
    question += '{0}'.format(e2)
    if s2 > 1:
        question += '<sub>{0}</sub>'.format(s2)
    question += '''<br>Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
$$
wt_{%s} = %d \:atom\: %s \cdot \frac{%.3f \: amu} {1 \:atom\: %s} = %.3f \: amu \: %s
$$
$$
wt_{%s} = %d \:atom\: %s \cdot \frac{%.3f \: amu} {1 \:atom\: %s} = %.3f \: amu \: %s
$$
$$
wt_{tot} = %.3f \: amu 
$$
$$
\%% \: %s = \frac{wt_{%s}} {wt_{tot}} \cdot 100 = \frac{%.3f \: amu} {%.3f \: amu} \cdot 100 = %.2f \: \%% \: %s
$$
$$
\%% \: %s = \frac{wt_{%s}} {wt_{tot}} \cdot 100 = \frac{%.3f \: amu} {%.3f \: amu} \cdot 100 = %.2f \: \%% \: %s
$$
$$
\%%_{tot} = %.2f \: \%% 
$$
</div>''' %(e1,s1,e1,aw1,e1,w1,e1,e2,s2,e2,aw2,e2,w2,e2,wt,e1,e1,w1,wt,p1,e1,e2,e2,w2,wt,p2,e2,pt)

    return question,answer

def group_problem2():
    formulas = Stuff.molecularFormulas.get_formulas()
    formula = random.choice(formulas)
    elements = Stuff.elements.get_elements()
    e1 = formula[0]
    s1 = formula[1]
    e2 = formula[2]
    s2 = formula[3]
    aw1 = elements[e1][2]
    aw2 = elements[e2][2]
    w1 = s1*aw1
    w2 = s2*aw2
    wt = w1 + w2
    p1 = w1/wt*100
    p2 = w2/wt*100
    pt = p1 + p2
    
    question = '''<div id="question"> 
    Find the percent composition of {0}'''.format(e1)
    if s1 > 1:
        question += '<sub>{0}</sub>'.format(s1)
    question += '{0}'.format(e2)
    if s2 > 1:
        question += '<sub>{0}</sub>'.format(s2)
    question += '''<br>Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
$$
wt_{%s} = %d \:atom\: %s \cdot \frac{%.3f \: amu} {1 \:atom\: %s} = %.3f \: amu \: %s
$$
$$
wt_{%s} = %d \:atom\: %s \cdot \frac{%.3f \: amu} {1 \:atom\: %s} = %.3f \: amu \: %s
$$
$$
wt_{tot} = %.3f \: amu 
$$
$$
\%% \: %s = \frac{wt_{%s}} {wt_{tot}} \cdot 100 = \frac{%.3f \: amu} {%.3f \: amu} \cdot 100 = %.2f \: \%% \: %s
$$
$$
\%% \: %s = \frac{wt_{%s}} {wt_{tot}} \cdot 100 = \frac{%.3f \: amu} {%.3f \: amu} \cdot 100 = %.2f \: \%% \: %s
$$
$$
\%%_{tot} = %.2f \: \%% 
$$
</div>''' %(e1,s1,e1,aw1,e1,w1,e1,e2,s2,e2,aw2,e2,w2,e2,wt,e1,e1,w1,wt,p1,e1,e2,e2,w2,wt,p2,e2,pt)

    return question,answer
    
def group_problem3():
    formulas = Stuff.molecularFormulas.get_formulas()
    formula = random.choice(formulas)
    elements = Stuff.elements.get_elements()
    e1 = formula[0]
    s1 = formula[1]
    e2 = formula[2]
    s2 = formula[3]
    aw1 = elements[e1][2]
    aw2 = elements[e2][2]
    w1 = s1*aw1
    w2 = s2*aw2
    wt = w1 + w2
    p1 = w1/wt*100
    p2 = w2/wt*100
    pt = p1 + p2
    n1 = p1/aw1
    n2 = p2/aw2
    a1 = n1/min(n1,n2)
    a2 = n2/min(n1,n2)
    f = s1/a1
    c1 = round(a1*f)
    c2 = round(a2*f)
    
    question = '''<div id="question"> 
    Given the percent composition of <br>
    {0:.2f} % {1} <br>
    {2:.2f} % {3} <br>
    and a total weight of {4:.3f} amu, <br>
    find the molecular formula.
    Explain your solution completely.</div>'''.format(p1,e1,p2,e2,wt)
    
    answer = ur'''<div id="answer">
$$
atoms \: %s = %.2f \:amu\: %s \cdot \frac{1 \:atom\: %s} {%.3f \: amu} = %.3f \: atoms \: %s
$$
$$
atoms \: %s = %.2f \:amu\: %s \cdot \frac{1 \:atom\: %s} {%.3f \: amu} = %.3f \: atoms \: %s
$$
$$
smallest = %.3f 
$$
$$
factor = %d
$$
$$
formula = %s_{%d}%s_{%d}
$$
$$
formula weight = %.3f \: amu 
$$
</div>''' %(e1,p1,e1,e1,aw1,n1,e1, e2,p2,e2,e2,aw2,n2,e2, min(n1,n2),f,e1,c1,e2,c2,wt)

    return question,answer
    
def group_problem4():
    formulas = Stuff.molecularFormulas.get_formulas()
    formula = random.choice(formulas)
    elements = Stuff.elements.get_elements()
    e1 = formula[0]
    s1 = formula[1]
    e2 = formula[2]
    s2 = formula[3]
    aw1 = elements[e1][2]
    aw2 = elements[e2][2]
    w1 = s1*aw1
    w2 = s2*aw2
    wt = w1 + w2
    p1 = w1/wt*100
    p2 = w2/wt*100
    pt = p1 + p2
    n1 = p1/aw1
    n2 = p2/aw2
    a1 = n1/min(n1,n2)
    a2 = n2/min(n1,n2)
    f = s1/a1
    c1 = round(a1*f)
    c2 = round(a2*f)
    
    question = '''<div id="question"> 
    Given the percent composition of <br>
    {0:.2f} % {1} <br>
    {2:.2f} % {3} <br>
    and a total weight of {4:.3f} amu, <br>
    find the molecular formula.
    Explain your solution completely.</div>'''.format(p1,e1,p2,e2,wt)
    
    answer = ur'''<div id="answer">
$$
atoms \: %s = %.2f \:amu\: %s \cdot \frac{1 \:atom\: %s} {%.3f \: amu} = %.3f \: atoms \: %s
$$
$$
atoms \: %s = %.2f \:amu\: %s \cdot \frac{1 \:atom\: %s} {%.3f \: amu} = %.3f \: atoms \: %s
$$
$$
smallest = %.3f 
$$
$$
factor = %d
$$
$$
formula = %s_{%d}%s_{%d}
$$
$$
formula weight = %.3f \: amu 
$$
</div>''' %(e1,p1,e1,e1,aw1,n1,e1, e2,p2,e2,e2,aw2,n2,e2, min(n1,n2),f,e1,c1,e2,c2,wt)

    return question,answer