import importlib
import datetime

def make_practice(teacher,student,period,unit,lesson,probs): 
    f = open(teacher+'/'+unit+'/'+lesson+'/'+teacher.split('.')[1]+unit+lesson+'Period'+period+'.html','a')
    g = open(teacher+'/'+unit+'/'+lesson+'/'+teacher.split('.')[1]+unit+lesson+'Period'+period+'KEY.html','a')
    head = '''<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">

     <title></title>
      
     <style>
     #question {font-size: 20px; font-weight: bold; display: inline-block; padding-left:5px; vertical-align:top; padding-bottom:15px;}
     #answer {padding-left:40px;}
     #nbr {font-size: 20px; font-weight: bold; display: inline-block; padding:5px; border: 1px solid black;}
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

    <body>'''
    
    foot = ''' <p style="page-break-after:always;"></p>
    </body>
    </html>'''
    
    f.write(head)
    g.write(head)
    f.write('<h3>{} {} Period {} {} {}</h3>'.format(student,datetime.datetime.now().date(),period,unit,lesson ))
    g.write('<h3>{} {} Period {} {} {}</h3>'.format(student,datetime.datetime.now().date(),period,unit,lesson ))
    c = 1
    for prob in probs: 
        s = 'problems.'+prob[0]
        area = importlib.import_module(s)
        p = eval("area."+prob[1]+'()')
        f.write('<div id="nbr">{0}. </div>'.format(c))
        g.write('<div id="nbr">{0}. </div>'.format(c))
        c+=1
        for i in p.question:
            f.write(i)
            g.write(i)
        for i in p.answer:
            g.write(i)
    f.write(foot)
    g.write(foot)
    f.close()
    g.close()

if __name__ == '__main__':  
    make_practice('chris.mckinnon','joe','1','Unit1','Form1',[('gas_laws', 'Boyles_p2'), ('gas_laws', 'Boyles_v2'), ('stoichiometry', 'weight_of_coins'), ('stoichiometry', 'number_of_coins')])
    