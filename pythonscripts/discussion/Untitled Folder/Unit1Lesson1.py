import random
import math

def sf(n,s=3):
    return round(n, s-int(math.floor(math.log10(n)))-1)
    
def group_problem1(): 
    question = '''<div id="question"> 
    Find the average weight of a quarter. <br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The average weight of one quarter is the total weight of quarters divided by the number of quarters.
$$
wt_{avg} =
\frac{wt_{tot}} {n_{qtr}}  = 
\frac{\qquad g }{\qquad qtr }  = 
\frac{\qquad 5.67 g}{qtr}
$$
</div>''' 

    return question,answer

def group_problem2():
    question = '''<div id="question"> 
    Find the average weight of a dime. <br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The average weight of one dime is the total weight of dimes divided by the number of dimes.
$$
wt_{avg} =
\frac{wt_{tot}} {n_{dim}}  = 
\frac{\qquad g }{\qquad dim }  = 
\frac{\qquad 2.27 g}{dim}
$$
</div>''' 

    return question,answer
    
def group_problem3():
    question = '''<div id="question"> 
    Find the average weight of a nickel. <br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The average weight of one nickel is the total weight of nickels divided by the number of nickels.
$$
wt_{avg} =
\frac{wt_{tot}} {n_{nic}}  = 
\frac{\qquad g }{\qquad nic }  = 
\frac{\qquad 5.00 g}{nic}
$$
</div>''' 

    return question,answer
    
def group_problem4():
    question = '''<div id="question"> 
    Find the average weight of a penny. <br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The average weight of one penny is the total weight of pennies divided by the number of pennies.
$$
wt_{avg} =
\frac{wt_{tot}} {n_{pen}}  = 
\frac{\qquad g }{\qquad pen }  = 
\frac{\qquad 2.50 g}{pen}
$$
</div>''' 

    return question,answer
    
def group_problem5(): 
    question = '''<div id="question"> 
    The averages calculated for the four types of coins have some uncertainty. <br>
    If we weighted more coins, the average might change a bit.<br>
    To estimate how much it might change, that is, to calculate the uncertainty,<br>
    we divide the range of measurements by 2.<br>
    Find the uncertainty in the average weight of one quarter. <br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The uncertainty in the average weight of one quarter is the range, <br>
    the largest weight minus the smallest weight, divided by 2.
$$
unc =
\frac{wt_{max} - wt_{min}}  {2}  = 
\frac{\frac{\qquad g}{qtr} - \frac{\qquad g}{qtr}}{2}  = 
\frac{\qquad g}{qtr}
$$
</div>''' 

    return question,answer
    
def group_problem6(): 
    question = '''<div id="question"> 
    Find the uncertainty in the average weight of one dime. <br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The uncertainty in the average weight of one dime is the range, <br>
    the largest weight minus the smallest weight, divided by 2.
$$
unc =
\frac{wt_{max} - wt_{min}}  {2}  = 
\frac{\frac{\qquad g}{dim} - \frac{\qquad g}{dim}}{2}  = 
\frac{\qquad g}{dim}
$$
</div>''' 

    return question,answer
    
def group_problem7(): 
    question = '''<div id="question"> 
    Find the uncertainty in the average weight of one nickel. <br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The uncertainty in the average weight of one nickel is the range, <br>
    the largest weight minus the smallest weight, divided by 2.
$$
unc =
\frac{wt_{max} - wt_{min}}  {2}  = 
\frac{\frac{\qquad g}{nic} - \frac{\qquad g}{nic}}{2}  = 
\frac{\qquad g}{nic}
$$
</div>''' 

    return question,answer

def group_problem8(): 
    question = '''<div id="question"> 
    Find the uncertainty in the average weight of one penny. <br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The uncertainty in the average weight of one penny is the range, <br>
    the largest weight minus the smallest weight, divided by 2.
$$
unc =
\frac{wt_{max} - wt_{min}}  {2}  = 
\frac{\frac{\qquad g}{pen} - \frac{\qquad g}{pen}}{2}  = 
\frac{\qquad g}{pen}
$$
</div>''' 

    return question,answer
    
def group_problem9(): 
    question = '''<div id="question"> 
    The precision error of a repeated measurement is a comparison of the uncertainty <br>
    of the measurements to the average of the measurements.<br>
    Any fraction multiplied by 100 turns the fraction into a percentage, also called parts per hundred.<br>
    The percent precision error is the uncertainty divided by the average times 100.<br>
    The lower the percent precision error, the better the repeatablity of the measurement.<br>
    Find the percent precision error (%PE) for the quarter measurements.<br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The percent precision error is the uncertainty divided by the average times 100.<br>
$$
\% PE =
\frac{unc}  {avg} \cdot 100 = 
\frac{ \frac{ \qquad g}{qtr}} {\frac{ \qquad g}{qtr}} \cdot 100  = 
\qquad \%
$$
</div>''' 

    return question,answer
    
def group_problem10(): 
    question = '''<div id="question"> 
    Find the percent precision error (%PE) for the dime measurements.<br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The percent precision error is the uncertainty divided by the average times 100.<br>
$$
\% PE =
\frac{unc}  {avg} \cdot 100 = 
\frac{ \frac{ \qquad g}{dim}} {\frac{ \qquad g}{dim}} \cdot 100  = 
\qquad \%
$$
</div>''' 

    return question,answer
    
def group_problem11(): 
    question = '''<div id="question"> 
    Find the percent precision error (%PE) for the nickel measurements.<br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The percent precision error is the uncertainty divided by the average times 100.<br>
$$
\% PE =
\frac{unc}  {avg} \cdot 100 = 
\frac{ \frac{ \qquad g}{nic}} {\frac{ \qquad g}{nic}} \cdot 100  = 
\qquad \%
$$
</div>''' 

    return question,answer
    
def group_problem12(): 
    question = '''<div id="question"> 
    Find the percent precision error (%PE) for the penny measurements.<br>
    Explain your solution completely.
    </div>'''
    
    answer = ur'''<div id="answer">
    The percent precision error is the uncertainty divided by the average times 100.<br>
$$
\% PE =
\frac{unc}  {avg} \cdot 100 = 
\frac{ \frac{ \qquad g}{pen}} {\frac{ \qquad g}{pen}} \cdot 100  = 
\qquad \%
$$
</div>''' 

    return question,answer