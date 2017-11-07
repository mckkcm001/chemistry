import random
import types
import inspect
import importlib
import math
import stuff.elements as se
import stuff.molecularFormulas as smf
import fractions as fr

def sf(n,s=3):
    return round(n, s-int(math.floor(math.log10(n)))-1)
def lcm(a,b):
    return (a*b)/fr.gcd(a,b)    
    
class balance_coin_reaction():
    '''balance coin reaction and show mass balances.
       PeNi + Di -> PeDi + NiDi'''
    area = ["stoichiometry"]
    skill = ["number to gram conversion","mass conservation"]
    
    def __init__(self):
        self.sp1 = random.randint(1,3)
        self.sn1 = random.randint(1,3)
        self.sd1 = random.randint(1,3)

        self.sp2 = random.randint(1,3)
        self.sn2 = random.randint(1,3)
        self.sd2 = random.randint(1,3)

        self.c1 = lcm(self.sp1,self.sp2)
        
        self.wp = 2.50*self.np
        self.wd = 2.27*self.nd
        self.wn = 5.00*self.nn
        self.wq = 5.67*self.nq
        self.tot = self.wp + self.wn + self.wd + self.wq
        self.pp = 2.50*self.np/self.tot*100
        self.pn = 5.00*self.nn/self.tot*100
        self.pd = 2.27*self.nd/self.tot*100
        self.pq = 5.67*self.nq/self.tot*100
        self.tp = self.pp + self.pn + self.pd + self.pq
        
        self.question = ['''<div id="question"> 
        Find the percent composition of Pe<sub>{}</sub>Ni<sub>{}</sub>Di<sub>{}</sub>Qu<sub>{}</sub><br>
        Explain your solution completely.
        </div>'''.format(self.np,self.nn,self.nd,self.nq)]
        
        self.answer = [ur'''<div id="answer">
    $$
    wt_{Pe} = %d Pe \cdot \frac{2.50 \: g} {1 \: Pe} = %.2f \: g
    $$
    $$
    wt_{Ni} = %d Ni \cdot \frac{5.00 \: g} {1 \: Ni} = %.2f \: g
    $$
    $$
    wt_{Di} = %d Di \cdot \frac{2.27 \: g} {1 \: Di} = %.2f \: g
    $$
    $$
    wt_{Qu} = %d Qu \cdot \frac{5.67 \: g} {1 \: Qu} = %.2f \: g
    $$
    $$
    wt_{tot} = %.2f \: g 
    $$
    $$
    \%% \: Pe = \frac{wt_{Pe}} {wt_{tot}} \cdot 100 = \frac{%.2f \: g} {%.2f \: g} \cdot 100 = %.1f \: \%% \: Pe
    $$
    $$
    \%% \: Ni = \frac{wt_{Ni}} {wt_{tot}} \cdot 100 = \frac{%.2f \: g} {%.2f \: g} \cdot 100 = %.1f \: \%% \: Ni
    $$
    $$
    \%% \:Di = \frac{wt_{Di}} {wt_{tot}} \cdot 100 = \frac{%.2f \: g} {%.2f \: g} \cdot 100 = %.1f \: \%% \: Di
    $$
    $$
    \%% \:Qu = \frac{wt_{Qu}} {wt_{tot}} \cdot 100 = \frac{%.2f \: g} {%.2f \: g} \cdot 100 = %.1f \: \%% \: Qu
    $$
    $$
    \%%_{tot} = %.2f \: \%% 
    $$
    </div>''' %(self.np,self.wp,self.nn,self.wn,self.nd,self.wd,self.nq,self.wq,self.tot,
                self.wp,self.tot,self.pp,self.wn,self.tot,self.pn,self.wd,self.tot,self.pd,self.wq,self.tot,self.pq,self.tp)]

class coin_percent_comp_to_formula():
    '''Convert percent coins by weight to a combination of coins.'''
    area = ["stoichiometry"]
    skill = ["gram to number conversion"]
    
    def __init__(self):
        self.np = random.randint(1,5)
        self.nn = random.randint(1,5)
        self.nd = random.randint(1,5)
        self.nq = random.randint(0,5)
        self.wp = 2.50*self.np
        self.wd = 2.27*self.nd
        self.wn = 5.00*self.nn
        self.wq = 5.67*self.nq
        self.tot = self.wp + self.wn + self.wd + self.wq
        self.pp = 2.50*self.np/self.tot*100
        self.pn = 5.00*self.nn/self.tot*100
        self.pd = 2.27*self.nd/self.tot*100
        self.pq = 5.67*self.nq/self.tot*100
        self.tp = self.pp + self.pn + self.pd + self.pq
        
        self.question = ['''<div id="question"> 
        Find the formula for {0:.1f}% Pe, {1:.1f}% Ni, and {2:.1f}% Di.<br> 
        The total weight is {3:.2f} g.<br>
        Explain your solution completely.
        </div>'''.format(self.pp,self.pn,self.pd,self.tot)]
        
        self.answer = [ur'''<div id="answer">
    $$
    wt_{Pe} = %.3f \cdot %.2f = %.2f \: g
    $$
    $$
    wt_{Ni} = %.3f \cdot %.2f = %.2f \: g
    $$
    $$
    wt_{Di} = %.3f \cdot %.2f = %.2f \: g
    $$
    $$
    wt_{Qu} = %.3f \cdot %.2f = %.2f \: g
    $$
    $$
    \%%_{tot} = %.1f \: \%% 
    $$
    $$
    n_{Pe} = wt_{Pe} \cdot \frac{1 \: Pe}{2.50 \: g} = %.2f \: g \cdot \frac{1 \: Pe}{2.50 \: g}  = %d  \: Pe
    $$
    $$
    n_{Ni} = wt_{Ni} \cdot \frac{1 \: Ni}{2.50 \: g} = %.2f \: g \cdot \frac{1 \: Ni}{2.50 \: g}  = %d  \: Ni
    $$
    $$
    n_{Di} = wt_{Di} \cdot \frac{1 \: Di}{2.50 \: g} = %.2f \: g \cdot \frac{1 \: Di}{2.50 \: g}  = %d  \: Di
    $$
    $$
    n_{Qu} = wt_{Qu} \cdot \frac{1 \: Qu}{2.50 \: g} = %.2f \: g \cdot \frac{1 \: Qu}{2.50 \: g}  = %d  \: Qu
    $$
    $$
    wt_{tot} = %.2f \: g
    $$
    $$
    Formula = Pe_{%d}Ni_{%d}Di_{%d}''' %(self.pp/100,self.tot,self.wp,self.pn/100,self.tot,self.wn,self.pd/100,
                                         self.tot,self.wd,self.pq/100,self.tot,self.wq,self.tp,self.wp,self.np,
                                         self.wn,self.nn,self.wd,self.nd,self.wq,self.nq,self.tot,self.np,self.nn,self.nd)]
        if self.nq > 0:
            self.answer[0] += ur'''
    Qu_{%d}
    $$
    </div>''' %(self.nq)
        else:
            self.answer[0] += ur'''
    $$
    </div>''' 
        
class formula_to_percent_comp(): 
    '''Convert chemical formula to a percent by weight.'''
    area = ["stoichiometry"]
    skill = ["gram to number conversion"]
    
    def __init__(self):
        self.formulas = smf.get_formulas()
        self.formula = random.choice(self.formulas)
        self.elements = se.get_elements()
        self.e1 = self.formula[0]
        self.s1 = self.formula[1]
        self.e2 = self.formula[2]
        self.s2 = self.formula[3]
        self.aw1 = self.elements[self.e1][2]
        self.aw2 = self.elements[self.e2][2]
        self.w1 = self.s1*self.aw1
        self.w2 = self.s2*self.aw2
        self.wt = self.w1 + self.w2
        self.p1 = self.w1/self.wt*100
        self.p2 = self.w2/self.wt*100
        self.pt = self.p1 + self.p2
        
        self.question = ['''<div id="question"> 
        Find the percent composition of {0}'''.format(self.e1)]
        if self.s1 > 1:
            self.question[0] += '<sub>{0}</sub>'.format(self.s1)
        self.question[0] += '{0}'.format(self.e2)
        if self.s2 > 1:
            self.question[0] += '<sub>{0}</sub>'.format(self.s2)
        self.question[0] += '''<br>Explain your solution completely.
        </div>'''
        
        self.answer = [ur'''<div id="answer">
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
    </div>''' %(self.e1,self.s1,self.e1,self.aw1,self.e1,self.w1,self.e1,self.e2,self.s2,self.e2,
                self.aw2,self.e2,self.w2,self.e2,self.wt,self.e1,self.e1,self.w1,self.wt,self.p1,
                self.e1,self.e2,self.e2,self.w2,self.wt,self.p2,self.e2,self.pt) ]       

class percent_comp_to_formula():
    '''Convert percent by weight to a chemical formula.'''
    area = ["stoichiometry"]
    skill = ["gnumber to gram conversion"]
    
    def __init__(self):
        self.formulas = smf.get_formulas()
        self.formula = random.choice(self.formulas)
        self.elements = se.get_elements()
        self.e1 = self.formula[0]
        self.s1 = self.formula[1]
        self.e2 = self.formula[2]
        self.s2 = self.formula[3]
        self.aw1 = self.elements[self.e1][2]
        self.aw2 = self.elements[self.e2][2]
        self.w1 = self.s1*self.aw1
        self.w2 = self.s2*self.aw2
        self.wt = self.w1 + self.w2
        self.p1 = self.w1/self.wt*100
        self.p2 = self.w2/self.wt*100
        self.pt = self.p1 + self.p2
        self.n1 = self.p1/self.aw1
        self.n2 = self.p2/self.aw2
        self.a1 = self.n1/min(self.n1,self.n2)
        self.a2 = self.n2/min(self.n1,self.n2)
        self.f = self.s1/self.a1
        self.c1 = round(self.a1*self.f)
        self.c2 = round(self.a2*self.f)
        
        self.question = ['''<div id="question"> 
        Given the percent composition of <br>
        {0:.2f} % {1} <br>
        {2:.2f} % {3} <br>
        and a total weight of {4:.3f} amu, <br>
        find the molecular formula.
        Explain your solution completely.
        </div>'''.format(self.p1,self.e1,self.p2,self.e2,self.wt)]
        
        self.answer = [ur'''<div id="answer">
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
    formula \: weight = %.3f \: amu 
    $$
    </div>''' %(self.e1,self.p1,self.e1,self.e1,self.aw1,self.n1,self.e1, 
                self.e2,self.p2,self.e2,self.e2,self.aw2,self.n2,self.e2, 
                min(self.n1,self.n2),self.f,self.e1,self.c1,self.e2,self.c2,self.wt)] 



if __name__=='__main__':
    f = open('test.html','w')
    me = importlib.import_module( inspect.getmodulename(__file__))
    print me
    probs = [me.__dict__[k] for k in me.__dict__  if type(me.__dict__[k]) == types.ClassType]
    examples = [prob() for prob in probs]
    head = '''<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">

    <title>%s</title>

    <style>
    #question {font-size: 20px; font-weight: bold;}
    #answer {padding-left:20px;}
    </style>
      
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
    jax: ["input/TeX","output/HTML-CSS"],
    displayAlign: "left"
    });
    </script>

    <script type="text/javascript"
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
    </script>

    </head>
    <body>''' % (me)
    
    foot = '''</body>
    </html>'''
    
    f.write(head)
    
    for prob in examples:
        f.write('<div>{}</div>'.format(prob.__doc__))
        f.write('<div>Area: {}</div>'.format(prob.area))
        f.write('<div>Skill: {}</div>'.format(prob.skill))
        for i in prob.question:
            f.write(i)
        for i in prob.answer:
            f.write(i)
    f.write(foot)
    f.close()    
