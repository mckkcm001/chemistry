import random
import types
import inspect
import importlib
import math
def sf(n,s=3):
    return round(n, s-int(math.floor(math.log10(n)))-1)
    
class Boyles_p2():
    '''Use Boyle's Law to find final pressure.'''
    area = ["Gas Laws"]
    skill = ["Boyle's Law", "conversions"]
    
    def __init__(self):
        self.v1 = random.randint(100,400)/100.
        self.p1 = random.randint(100,400)/100.
        self.v2 = random.randint(100,400)/100.
        self.p2 = self.p1*self.v1/self.v2
        
        self.question = ['''<div id="question">%.2f L of a gas at %.2f atm is changed to %.2f L </div>
        <div></div>''' % (self.v1,self.p1,self.v2)]
        
        self.answer = [ur'''<div id="answer">
        $$\text{formula:}\:
        \boxed {p_{2} = \frac {p_{1} \cdot v_{1}} {v_{2}}} 
        $$</div>''' ,
        ur'''<div id="answer">
        $$\require{cancel} 
        \text{substitution:}\:
        \boxed { p_{2} = \frac {%.2f \: atm \cdot %.2f \: \cancel{L}} {%.2f \: \cancel{L}}}
        $$</div>'''  %(self.p1,self.v1,self.v2),
        ur'''<div id="answer">
        $$ \text{calculation:} \:
        \boxed{ p_{2} = %s \: atm} 
        $$</div><div></div>''' %(sf(self.p2))
        ]
 
class Boyles_v2():
    '''Use Boyle's Law to find final volume.'''
    area = ["Gas Laws"]
    skill = ["Boyle's Law", "conversions"]
    
    def __init__(self):
        self.v1 = random.randint(100,400)/100.
        self.p1 = random.randint(100,400)/100.
        self.p2 = random.randint(100,400)/100.
        self.v2 = self.p1*self.v1/self.p2
        self.question = ['''<div id="question">%.2f L of a gas at %.2f atm is changed to %.2f atm </div>
        <div></div>''' % (self.v1,self.p1,self.p2)]
        
        self.answer = [ur'''<div id="answer">
        $$\text{formula: } \:
        \boxed {v_{2} = \frac {p_{1} \cdot v_{1}} {p_{2}}} $$</div>''' ,
        ur'''<div id="answer">
        $$\require{cancel} 
        \text{substitution: } \:
        \boxed { v_{2} = \frac {%.2f \: \cancel{atm} \cdot %.2f \:L} {%.2f \: \cancel{atm}}} 
        $$</div>'''  %(self.p1,self.v1,self.p2),
        ur'''<div id="answer">
        $$\text{calculation: } \:
        \boxed { v_{2} = %s \: L} 
        $$</div><div></div>''' %(sf(self.v2))
        ]
    
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
   
    