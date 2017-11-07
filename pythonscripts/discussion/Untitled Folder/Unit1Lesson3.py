import random
import math

def sigfig(n,s=3):
    return round(n, s-int(math.floor(math.log10(n)))-1)
    
def group_problem1(): 
    np = random.randint(1,5)
    nn = random.randint(1,5)
    nd = random.randint(1,5)
    nq = random.randint(1,5)
    wp = 2.50*np
    wd = 2.27*nd
    wn = 5.00*nn
    wq = 5.67*nq
    tot = wp + wn + wd + wq
    pp = 2.50*np/tot*100
    pn = 5.00*nn/tot*100
    pd = 2.27*nd/tot*100
    pq = 5.67*nq/tot*100
    tp = pp + pn + pd + pq
    
    question = '''<div id="question"> 
    Find the percent composition of Pe<sub>{}</sub>Ni<sub>{}</sub>Di<sub>{}</sub>Qu<sub>{}</sub><br>
    Explain your solution completely.
    </div>'''.format(np,nn,nd,nq)
    
    answer = ur'''<div id="answer">
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
</div>''' %(np,wp,nn,wn,nd,wd,nq,wq,tot,wp,tot,pp,wn,tot,pn,wd,tot,pd,wq,tot,pq,tp)

    return question,answer

def group_problem2():
    np = random.randint(1,5)
    nn = random.randint(1,5)
    nd = random.randint(1,5)
    nq = random.randint(1,5)
    wp = 2.50*np
    wd = 2.27*nd
    wn = 5.00*nn
    wq = 5.67*nq
    tot = wp + wn + wd + wq
    pp = 2.50*np/tot*100
    pn = 5.00*nn/tot*100
    pd = 2.27*nd/tot*100
    pq = 5.67*nq/tot*100
    tp = pp + pn + pd + pq
    
    question = '''<div id="question"> 
    Find the percent composition of Pe<sub>{}</sub>Ni<sub>{}</sub>Di<sub>{}</sub>Qu<sub>{}</sub><br>
    Explain your solution completely.
    </div>'''.format(np,nn,nd,nq)
    
    answer = ur'''<div id="answer">
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
</div>''' %(np,wp,nn,wn,nd,wd,nq,wq,tot,wp,tot,pp,wn,tot,pn,wd,tot,pd,wq,tot,pq,tp)

    return question,answer
    
def group_problem3():
    np = random.randint(1,5)
    nn = random.randint(1,5)
    nd = random.randint(1,5)
    nq = random.randint(0,5)
    wp = 2.50*np
    wd = 2.27*nd
    wn = 5.00*nn
    wq = 5.67*nq
    tot = wp + wn + wd + wq
    pp = 2.50*np/tot*100
    pn = 5.00*nn/tot*100
    pd = 2.27*nd/tot*100
    pq = 5.67*nq/tot*100
    tp = pp + pn + pd + pq
    
    question = '''<div id="question"> 
    Find the formula for {0:.1f}% Pe, {1:.1f}% Ni, and {2:.1f}% Di.<br> 
    The total weight is {3:.2f}.<br>
    Explain your solution completely.
    </div>'''.format(pp,pn,pd,tot)
    
    answer = ur'''<div id="answer">
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
Formula = Pe_{%d}Ni_{%d}Di_{%d}''' %(pp/100,tot,wp,pn/100,tot,wn,pd/100,tot,wd,pq/100,tot,wq,tp,wp,np,wn,nn,wd,nd,wq,nq,tot,np,nn,nd)
    if nq > 0:
        answer += ur'''
Qu_{%d}
$$
</div>''' %(nq)
    else:
        answer += ur'''
$$
</div>''' 
    return question,answer
    
def group_problem4():
    np = random.randint(1,5)
    nn = random.randint(1,5)
    nd = random.randint(1,5)
    nq = random.randint(0,5)
    wp = 2.50*np
    wd = 2.27*nd
    wn = 5.00*nn
    wq = 5.67*nq
    tot = wp + wn + wd + wq
    pp = 2.50*np/tot*100
    pn = 5.00*nn/tot*100
    pd = 2.27*nd/tot*100
    pq = 5.67*nq/tot*100
    tp = pp + pn + pd + pq
    
    question = '''<div id="question"> 
    Find the formula for {0:.1f}% Pe, {1:.1f}% Ni, and {2:.1f}% Di.<br> 
    The total weight is {3:.2f}.<br>
    Explain your solution completely.
    </div>'''.format(pp,pn,pd,tot)
    
    answer = ur'''<div id="answer">
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
Formula = Pe_{%d}Ni_{%d}Di_{%d}''' %(pp/100,tot,wp,pn/100,tot,wn,pd/100,tot,wd,pq/100,tot,wq,tp,wp,np,wn,nn,wd,nd,wq,nq,tot,np,nn,nd)
    if nq > 0:
        answer += ur'''
Qu_{%d}
$$
</div>''' %(nq)
    else:
        answer += ur'''
$$
</div>''' 
    return question,answer
    
