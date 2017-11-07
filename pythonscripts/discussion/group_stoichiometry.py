import random
import types
import inspect
import importlib
import math
import stuff.elements as se
import stuff.molecularFormulas as smf

def sf(n,s=3):
    return round(n, s-int(math.floor(math.log10(n)))-1)
    
class avg_weight_of_coins():
    '''Weigh several coins and find average weight'''
    area = ["stoichiometry"]
    skill = ["average"]
    
    def __init__(self):  
        self.question = ['''<div id="question"> 
    Find the average weight of the given type of object. 
    Explain your solution completely.
    </div>''']
    
        self.answer = [ur'''<div id="answer">
    The average weight of one object is the total weight of the objects 
    divided by the number of objects.
$$
wt_{avg} =
\frac{wt_{tot}} {n}  = 
\frac{\qquad g }{\qquad objects }  = 
\frac{\: %.2f \: g}{object}
$$
</div>'''] 

class unc_avg_weight_of_coins():
    '''Estimate the uncertainty of an average as half the range.'''
    area = ["stoichiometry"]
    skill = ["uncertainty"]
    
    def __init__(self): 
        self.question = ['''<div id="question"> 
    An average calculated for multiple measurements has some uncertainty. 
    If we made more measurements, the average might change a bit. 
    To estimate how much it might change, that is, to calculate the uncertainty, 
    we divide the range of measurements by 2. 
    The range is the maximum measurement minus the minimum measurement, 
    Find the uncertainty in the average weight of one object. 
    Explain your solution completely. 
    </div>''']
    
        self.answer = [ur'''<div id="answer">
    The uncertainty in the average weight of one object is the range, 
    the largest weight minus the smallest weight, divided by 2.
$$
unc =
\frac{wt_{max} - wt_{min}}  {2}  = 
\frac{\qquad g}{object}
$$
</div>''']
        
class perc_prec_avg_weight_of_coins():
    '''Estimate percent precision error by dividing uncertainty by average.'''
    area = ["stoichiometry"]
    skill = ["fraction","percent"]
    
    def __init__(self): 
        self.question = ['''<div id="question"> 
    The precision error of a repeated measurement is a comparison of the uncertainty 
    of the measurements to the average of the measurements.
    Any fraction multiplied by 100 turns the fraction into a percentage, also called parts per hundred.
    The percent precision error is the uncertainty divided by the average times 100.
    The lower the percent precision error, the better the repeatablity of the measurement.
    Find the percent precision error (%PE) for the average measurements.
    Explain your solution completely.
    </div>''']
    
        self.answer = [ur'''<div id="answer">
    The percent precision error is the uncertainty divided by the average times 100.
$$
\% PE =
\frac{unc}  {avg} \cdot 100 = 
\qquad \%
$$
</div>''' ]

class elements_with_rev_at_wt(): 
    '''Find pairs of elements on periodic table with reversed atomic weights.'''
    area = ["periodic table"]
    skill = ["atomic weight"]
    
    pairs=[]
    elements = se.get_elements()
    for e1 in elements:
        for e2 in elements:
            if elements[e1][1] < elements[e2][1] and elements[e1][2] > elements[e2][2]:
                pairs.append([e1,e2])

    question = '''<div id="question"> 
    Find all pairs of elements where the average atomic weight 
    of the element with the smaller atomic number is more than the
    average atomic weight of the element with the larger atomic number.
    </div>'''
    
    answer = '<div id="answer"> '
    for i in pairs:
        answer += str(i)
    answer += '</div> '
        
class per_table_poem():
    '''Write a poem using atomic symbols.'''
    area = ["periodic table"]
    skill = ["atomic symbols"]
    
    question = '''<div id="question"> 
    Using only atomic symbols, write a short poem. 
    Keep all leters upper and lower case as on the periodic table. 
    Examples: Ar + K = ArK, Ti + N + Y = TiNY
    </div>'''
    
    answer = '<div id="answer"> various</div>'  
      
class convert_g_to_kg():
    '''Convert using kilo prefix.'''
    area = ["metric system"]
    skill = ["scientific notation"]
    
    def __init__(self):
        self.man = [random.randint(100,800)/100. for i in range(5)]
        self.exp = [random.randint(-50,50) for i in range(5)]
    
        self.question = '''<div id="question"> 
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
    </div>'''.format(m=self.man,e=self.exp)
        self.exp1 = []
        for i in range(5):
            self.exp1.append(self.exp[i]-3)
        self.answer = '''<div id="answer">
    {m[0]}e{e[0]} g = {m[0]}e{e1[0]} kg<br>
    {m[1]}e{e[1]} g = {m[1]}e{e1[1]} kg<br>
    {m[2]}e{e[2]} g = {m[2]}e{e1[2]} kg<br>
    {m[3]}e{e[3]} g = {m[3]}e{e1[3]} kg<br>
    {m[4]}e{e[4]} g = {m[4]}e{e1[4]} kg<br>

</div>''' .format(m=self.man,e=self.exp,e1=self.exp1)        
        
class convert_kg_to_g():
    '''Convert using kilo prefix.'''
    area = ["metric system"]
    skill = ["scientific notation"]
    
    def __init__(self):
        self.man = [random.randint(100,800)/100. for i in range(5)]
        self.exp = [random.randint(-50,50) for i in range(5)]
    
        self.question = '''<div id="question"> 
    Convert the following to g:<br>
    {m[0]}e{e[0]} kg<br>
    {m[1]}e{e[1]} kg<br>
    {m[2]}e{e[2]} kg<br>
    {m[3]}e{e[3]} kg<br>
    {m[4]}e{e[4]} kg<br>
    </div>'''.format(m=self.man,e=self.exp)
        self.exp1 = []
        for i in range(5):
            self.exp1.append(self.exp[i]+3)
        self.answer = '''<div id="answer">
    {m[0]}e{e[0]} kg = {m[0]}e{e1[0]} g<br>
    {m[1]}e{e[1]} kg = {m[1]}e{e1[1]} g<br>
    {m[2]}e{e[2]} kg = {m[2]}e{e1[2]} g<br>
    {m[3]}e{e[3]} kg = {m[3]}e{e1[3]} g<br>
    {m[4]}e{e[4]} kg = {m[4]}e{e1[4]} g<br>

</div>''' .format(m=self.man,e=self.exp,e1=self.exp1)        

class convert_g_to_mg(): 
    '''Convert using milli prefix.'''
    area = ["metric system"]
    skill = ["scientific notation"]
    
    def __init__(self):
        self.man = [random.randint(100,800)/100. for i in range(5)]
        self.exp = [random.randint(-50,50) for i in range(5)]
    
        self.question = '''<div id="question"> 
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
    </div>'''.format(m=self.man,e=self.exp)
        self.exp1 = []
        for i in range(5):
            self.exp1.append(self.exp[i]+3)
        self.answer = '''<div id="answer">
    {m[0]}e{e[0]} g = {m[0]}e{e1[0]} mg<br>
    {m[1]}e{e[1]} g = {m[1]}e{e1[1]} mg<br>
    {m[2]}e{e[2]} g = {m[2]}e{e1[2]} mg<br>
    {m[3]}e{e[3]} g = {m[3]}e{e1[3]} mg<br>
    {m[4]}e{e[4]} g = {m[4]}e{e1[4]} mg<br>

</div>''' .format(m=self.man,e=self.exp,e1=self.exp1)

class convert_mg_to_g(): 
    '''Convert using milli prefix.'''
    area = ["metric system"]
    skill = ["scientific notation"]
    
    def __init__(self):
        self.man = [random.randint(100,800)/100. for i in range(5)]
        self.exp = [random.randint(-50,50) for i in range(5)]
        
        self.question = '''<div id="question"> 
        Convert the following to g:<br>
        {m[0]}e{e[0]} mg<br>
        {m[1]}e{e[1]} mg<br>
        {m[2]}e{e[2]} mg<br>
        {m[3]}e{e[3]} mg<br>
        {m[4]}e{e[4]} mg<br>
        </div>'''.format(m=self.man,e=self.exp)
        self.exp1 = []
        for i in range(5):
           self.exp1.append(self.exp[i]-3)
        self.answer = '''<div id="answer">
        {m[0]}e{e[0]} mg = {m[0]}e{e1[0]} g<br>
        {m[1]}e{e[1]} mg = {m[1]}e{e1[1]} g<br>
        {m[2]}e{e[2]} mg = {m[2]}e{e1[2]} g<br>
        {m[3]}e{e[3]} mg = {m[3]}e{e1[3]} g<br>
        {m[4]}e{e[4]} mg = {m[4]}e{e1[4]} g<br>
    
    </div>''' .format(m=self.man,e=self.exp,e1=self.exp1)

class convert_mg_to_kg(): 
    '''Convert using milli and kilo prefixes.'''
    area = ["metric system"]
    skill = ["scientific notation"]
    
    def __init__(self):
        self.man = [random.randint(100,800)/100. for i in range(5)]
        self.exp = [random.randint(-50,50) for i in range(5)]
        
        self.question = '''<div id="question"> 
        Convert the following to kg:<br>
        {m[0]}e{e[0]} mg<br>
        {m[1]}e{e[1]} mg<br>
        {m[2]}e{e[2]} mg<br>
        {m[3]}e{e[3]} mg<br>
        {m[4]}e{e[4]} mg<br>
        </div>'''.format(m=self.man,e=self.exp)
        self.exp1 = []
        for i in range(5):
           self.exp1.append(self.exp[i]-6)
        self.answer = '''<div id="answer">
        {m[0]}e{e[0]} mg = {m[0]}e{e1[0]} kg<br>
        {m[1]}e{e[1]} mg = {m[1]}e{e1[1]} kg<br>
        {m[2]}e{e[2]} mg = {m[2]}e{e1[2]} kg<br>
        {m[3]}e{e[3]} mg = {m[3]}e{e1[3]} kg<br>
        {m[4]}e{e[4]} mg = {m[4]}e{e1[4]} kg<br>
    
    </div>''' .format(m=self.man,e=self.exp,e1=self.exp1)

class convert_kg_to_mg(): 
    '''Convert using milli and kilo prefixes.'''
    area = ["metric system"]
    skill = ["scientific notation"]
    
    def __init__(self):
        self.man = [random.randint(100,800)/100. for i in range(5)]
        self.exp = [random.randint(-50,50) for i in range(5)]
        
        self.question = '''<div id="question"> 
        Convert the following to mg:<br>
        {m[0]}e{e[0]} kg<br>
        {m[1]}e{e[1]} kg<br>
        {m[2]}e{e[2]} kg<br>
        {m[3]}e{e[3]} kg<br>
        {m[4]}e{e[4]} kg<br>
        </div>'''.format(m=self.man,e=self.exp)
        self.exp1 = []
        for i in range(5):
           self.exp1.append(self.exp[i]+6)
        self.answer = '''<div id="answer">
        {m[0]}e{e[0]} kg = {m[0]}e{e1[0]} mg<br>
        {m[1]}e{e[1]} kg = {m[1]}e{e1[1]} mg<br>
        {m[2]}e{e[2]} kg = {m[2]}e{e1[2]} mg<br>
        {m[3]}e{e[3]} kg = {m[3]}e{e1[3]} mg<br>
        {m[4]}e{e[4]} kg = {m[4]}e{e1[4]} mg<br>
    
    </div>''' .format(m=self.man,e=self.exp,e1=self.exp1)

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
