import importlib
import datetime

def make_practice(teacher,roster,period,unit,lesson,probs): 
    f = open(teacher+'/'+unit+'/'+lesson+'/'+teacher.split('.')[1]+unit+lesson+'Period'+period+'.html','w')
    g = open(teacher+'/'+unit+'/'+lesson+'/'+teacher.split('.')[1]+unit+lesson+'Period'+period+'KEY.html','w')
    head = '''<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">

     <title>%s</title>
      
     <style>
     #question {font-size: 20px; font-weight: bold; display: inline-block; 
                 padding-left:5px; padding-bottom:15px; white-space: normal; 
                 vertical-align:top; padding-right:20px; margin-right:10px;}
     #answer {padding-left:40px; display: inline-block;margin-right:10px;}
     #nbr {font-size: 20px; font-weight: bold; display: inline-block; padding:5px; border: 1px solid black; white-space: normal; vertical-align:top;}
     #t {//white-space: nowrap; }
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

    <body>''' % (teacher+unit+lesson+period)
    
    page_break = ' <p style="page-break-after:always;"></p>'
    footer = '''</body></html>'''
    
    f.write(head)
    g.write(head)
    for student in roster:
        f.write('<h3>{} {} Period {} {} {}</h3>'.format(student,datetime.datetime.now().date(),period,unit,lesson ))
        g.write('<h3>{} {} Period {} {} {}</h3>'.format(student,datetime.datetime.now().date(),period,unit,lesson ))
        c = 1
        for prob in probs: 
            s = 'problems.'+prob[0]
            area = importlib.import_module(s)
            p = eval("area."+prob[1]+'()')
            f.write('<div id="t"><div id="nbr">{0}. </div>'.format(c))
            g.write('<div id="t"><div id="nbr">{0}. </div>'.format(c))
            c+=1
            for i in p.question:
                f.write(i)
                g.write(i)
            f.write('</div>')
            g.write('</div>')
            for i in p.answer:
                g.write(i)
        if student != roster[-1]:
            f.write(page_break)
            g.write(page_break)
    f.write(footer)
    g.write(footer)
    f.close()
    g.close()

if __name__ == '__main__':  
    make_practice('chris.mckinnon',['joe','jill'],'1','Unit1','Sum',[('gas_laws', 'Boyles_p2'), ('gas_laws', 'Boyles_v2'), ('stoichiometry', 'weight_of_coins'), ('stoichiometry', 'number_of_coins')])
    