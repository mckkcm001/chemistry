import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import re
#import html2text

def get_roster(user, pw, per):
    # Browser
    br = mechanize.Browser()
    
    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    
    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    
    br.addheaders = [('User-agent', 'Chrome')]
    
    # The site we will navigate into, handling it's session
    html = br.open('https://teacher.twinriversusd.org/Login.aspx')
    
    # View available forms
    #for f in br.forms():
    #    print f
    
    # Select the second (index one) form (the first form is a search query box)
    br.select_form(nr=0)
    
    # User credentials
    br.form['Username_Aeries'] = user
    br.form['Password_Aeries'] = pw
    br.form['Year_Aeries'] = '2015-2016'
    
    # Login
    br.submit()
    
    html = br.open('https://teacher.twinriversusd.org/TeacherAttendance.aspx')
    
    br.select_form(nr=0)
    br["ctl00$MainContent$PeriodList"]=[per]
    
    #br.form["ctl00$MainContent$PeriodList"]=["2"]
    
    #br.select_form(nr=0)
    html = br.submit()
    br.select_form(nr=0)
    #print br["ctl00$MainContent$PeriodList"]
    
    soup = BeautifulSoup(html)
    
    names = []
    for i in range(1,10):
        try:
            name = soup.find('span', attrs = {'id':'ctl00_MainContent_ClassRptr_ctl0'+str(i)+'_lblStuName'})
            names.append(str(name.contents[0]))
        except AttributeError:
            break
       
    for i in range(10,40):
        try:
            name = soup.find('span', attrs = {'id':'ctl00_MainContent_ClassRptr_ctl'+str(i)+'_lblStuName'})
            names.append(str(name.contents[0]))
        except AttributeError:
            break     
    
    roster = []
    for i in names:
        n = re.split(', | \.',i)
        roster.append('{0},{1}'.format(n[0].split()[0],n[-1].split()[0]))
    return roster
    
if __name__ == "__main__" :
    print get_roster('chris.mckinnon','pass42015f','4')
