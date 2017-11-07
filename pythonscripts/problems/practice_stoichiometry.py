import random
import types
import inspect
import importlib
import math
import stuff.elements as se
import stuff.molecularFormulas as smf

def sf(n,s=3):
    return round(n, s-int(math.floor(math.log10(n)))-1)
    
class weight_of_coins():
    '''Given an average weight, find the weight of n coins.'''
    area = ["stoichiometry"]
    skill = ["number to mass conversion"]
    
    def __init__(self):
        self.n = random.randint(100,400)
        self.avg_wt = random.randint(250,567)/100.
        self.wt = self.n*self.avg_wt
    
        self.question = ['''
            <div id="question"> 
            The average weight of a coin is {0} g. 
            Find the total weight of {1} coins.
            </div>'''.format(self.avg_wt,self.n)]
    
        self.answer = [ur'''
            <div id="answer">
            $$
            \require{cancel}
            wt_{tot} =
            wt_{avg} \cdot n  = 
            \frac{ %.2f \: g }{ 1 \: \cancel{coin} } \cdot %d \: \cancel{coin} = 
            %.1f \: g =
            %d \: g
            $$
            </div>
        ''' %(self.avg_wt,self.n,self.wt,sf(self.wt))]

class weight_of_coins_kg():
    '''Given an average weight, find the weight of n coins in kg.'''
    area = ["stoichiometry"]
    skill = ["number to mass conversion", "metric conversion"]
    
    def __init__(self):
        self.n = random.randint(100000,400000)
        self.avg_wt = random.randint(250,567)/100.
        self.wt = self.n*self.avg_wt
    
        self.question = ['''
            <div id="question"> 
            The average weight of a coin is {0} g. 
            Find the total weight of {1} coins in kg.
            </div>'''.format(self.avg_wt,self.n)]
    
        self.answer = [ur'''
            <div id="answer">
            $$
            \require{cancel}
            wt_{tot} =
            wt_{avg} \cdot n  = 
            \frac{ %.2f \: g }{ 1 \: \cancel{coin} } \cdot %d \: \cancel{coin} = 
            %.1f \: g =
            %d \: \cancel{g} \cdot \frac{1 \: kg}{1000 \: \cancel{g}} = %d \: kg
            $$
            </div>
        ''' %(self.avg_wt,self.n,self.wt,sf(self.wt),sf(self.wt/1000.))]
        
class number_of_coins():
    '''Given an average weight and a total weight, find the number of coins.'''
    area = ["stoichiometry"]
    skill = ["mass to number conversion"]
    
    def __init__(self):
        self.n = random.randint(100,400)
        self.avg_wt = random.randint(300,500)/100.
        self.wt = round(self.n*self.avg_wt)
        self.n1 = self.wt/self.avg_wt
    
        self.question = ['''<div id="question"> 
        The average weight of a coin is %.2f grams. 
        Find the number of coins in %d grams.
       </div>''' % (self.avg_wt,self.wt)]
    
        self.answer = [ur'''<div id="answer">
        $$\require{cancel}
        n =
        wt_{tot} \cdot \frac{1}{wt_{avg}}  = 
        %d \: \cancel{g} \cdot \frac{ 1 \: {coin} }  {%.2f \cancel{g}} = 
        %.1f \: coins =
        %d \: coins
        $$</div>''' %(self.wt,self.avg_wt,self.n1,sf(self.n1))]

class number_of_coins_kg():
    '''Given an average weight in g and a total weight in kg, find the number of coins.'''
    area = ["stoichiometry"]
    skill = ["mass to number conversion","metric conversion"]
    
    def __init__(self):
        self.n = random.randint(100000,400000)
        self.avg_wt = random.randint(300,500)/100.
        self.wt = round(self.n*self.avg_wt)/1000.
        self.n1 = self.wt*1000./self.avg_wt
    
        self.question = ['''<div id="question"> 
        The average weight of a coin is %.2f grams. 
        Find the number of coins in %d kilograms.
       </div>''' % (self.avg_wt,self.wt)]
    
        self.answer = [ur'''<div id="answer">
        $$\require{cancel}
        n =
        wt_{tot} \cdot \frac{1}{wt_{avg}}  = 
        %d \: \cancel{kg} \cdot \frac{1000 \: \cancel{g}}{1 \: \cancel{kg}}\cdot \frac{ 1 \: {coin} }  {%.2f \cancel{g}} = 
        %.1f \: coins =
        %d \: coins
        $$</div>''' %(self.wt,self.avg_wt,self.n1,sf(self.n1))]

class grams_to_moles_atoms():
    '''Convert grams of an element to moles and number of atoms.'''
    area = ["stoichiometry"]
    skill = ["mass to moles conversion","mass to atoms conversion"]
    
    def __init__(self):
        self.elements = se.get_elements()
        self.m = random.randint(100,800)/100.
        self.s = random.choice(self.elements.keys())
        self.name = self.elements[self.s][0]
        self.mm = self.elements[self.s][2]
        self.mol = self.m/self.mm
        self.a = self.mol*6.02e23
        
        self.question = ['''<div id="question"> 
        Convert {0} grams of {1} to moles of {1} and atoms of {1}.
        Use the unit conversion method and show cancellation of units.
        </div>'''.format(self.m,self.name,)]
        
        self.answer = [ur'''<div id="answer">
        $$
        \require{cancel}
        %.2f \cancel{g \: %s} \cdot \frac{ 1 \: mol \: %s }{ %.2f \cancel{g \: %s} } = %.2e \: mol \: %s
        $$
        $$
        \require{cancel}
        %.2f \cancel{g \: %s} \cdot \frac{ 6.02e23 \: atoms \: %s }{ %.2f \cancel{g \: %s} } = %.2e \: atoms \: %s 
        $$
        </div>''' %(self.m,self.s,self.s,self.mm,self.s,sf(self.mol),
                self.s,self.m,self.s,self.s,self.mm,self.s,sf(self.a),self.s)]
                
class moles_to_grams_atoms():
    '''Convert grams of an element to moles and number of atoms.'''
    area = ["stoichiometry"]
    skill = ["mass to moles conversion","mass to atoms conversion"]
    
    def __init__(self):
        self.elements = se.get_elements()
        self.m = random.randint(100,800)/100.
        self.s = random.choice(self.elements.keys())
        self.name = self.elements[self.s][0]
        self.mm = self.elements[self.s][2]
        self.mol = self.m/self.mm
        self.a = self.mol*6.02e23
        
        self.question = ['''<div id="question"> 
        Convert %.2e moles of %s to grams of %s and atoms of %s.
        Use the unit conversion method and show cancellation of units.
        </div>''' % (self.mol,self.name,self.name,self.name)]
        
        self.answer = [ur'''<div id="answer">
        $$
        \require{cancel}
        %.2e \cancel{mol \: %s} \cdot \frac{ %.2f {g \: %s} }{ 1 \: \cancel{mol \: %s} } = %.2f \: g \: %s
        $$
        $$
        \require{cancel}
        %.2e \cancel{mol \: %s} \cdot \frac{ 6.02e23 \: atoms \: %s }{ 1\cancel{mol \: %s} } = %.2e \: atoms \: %s 
        $$
        </div>''' %(self.mol,self.s,self.mm,self.s,self.s,sf(self.m),
                self.s,self.mol,self.s,self.s,self.s,sf(self.a),self.s)]

class atoms_to_grams_moles():
    '''Convert atoms of an element to moles and grams.'''
    area = ["stoichiometry"]
    skill = ["atoms to moles conversion","atoms to mass conversion"]
    
    def __init__(self):
        self.elements = se.get_elements()
        self.m = random.randint(100,800)/100.
        self.s = random.choice(self.elements.keys())
        self.name = self.elements[self.s][0]
        self.mm = self.elements[self.s][2]
        self.mol = self.m/self.mm
        self.a = self.mol*6.02e23
        
        self.question = ['''<div id="question"> 
        Convert %.2e atoms of %s to grams of %s and moles of %s.
        Use the unit conversion method and show cancellation of units.
        </div>''' % (self.a,self.name,self.name,self.name)]
        
        self.answer = [ur'''<div id="answer">
        $$
        \require{cancel}
        %.2e \cancel{atoms \: %s} \cdot \frac{ %.2f {g \: %s} }{ 6.02e23 \: \cancel{atoms \: %s} } = %.2f \: g \: %s
        $$
        $$
        \require{cancel}
        %.2e \cancel{atoms \: %s} \cdot \frac{ 1 \: mol \: %s }{ 6.02e23 \cancel{atoms \: %s} } = %.2e \: mol \: %s 
        $$
        </div>''' %(self.a,self.s,self.mm,self.s,self.s,sf(self.m),
                    self.s,self.a,self.s,self.s,self.s,sf(self.mol),self.s)]

class coin_formula_to_percent_comp():
    '''Convert combination of coins to percent coins by weight.'''
    area = ["stoichiometry"]
    skill = ["number to gram conversion","fraction to percent"]
    
    def __init__(self):
        self.np = random.randint(1,5)
        self.nn = random.randint(1,5)
        self.nd = random.randint(1,5)
        self.nq = random.randint(1,5)
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
