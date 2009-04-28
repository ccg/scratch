import re
import urllib
#from xml.dom.ext.
from xml.dom.minidom import parseString

EMAIL="ccg_spam@yahoo.com"

# FILL IN YOUR PASSWORD HERE! DON'T CHECK IT INTO THE REPO!
PASSWORD=""

url_getLoginHash = ("http://voo2do.com/api/getLoginHash?email=" + EMAIL +
                    "&password=" + PASSWORD)
data = urllib.urlopen(url_getLoginHash).read()

m = re.search(r'loginHash="(\w*)" userId="(\w*)"', data)
(loginHash, userId,) = m.groups()
print 'loginHash',loginHash,'userId',userId

dom = parseString(data)
#print dom.toprettyxml()
#print '='*70
#print "root element type:", dom.documentElement.tagName
login = dom.getElementsByTagName('login')[0]
loginHash = login.getAttribute('loginHash')
userId = login.getAttribute('userId')
print "DOM loginHash:",loginHash,"userId:",userId
dom.unlink()

####

url_getViews = "http://voo2do.com/api/getViews?userId=" + userId + "&loginHash=" + loginHash
data = urllib.urlopen(url_getViews).read()
dom = parseString(data)
print dom.toprettyxml()
dom.unlink()

########

url_getProjects = "http://voo2do.com/api/getProjects?userId=" + userId + "&loginHash=" + loginHash + "&viewId=32139"
data = urllib.urlopen(url_getProjects).read()
dom = parseString(data)
print dom.toprettyxml()
projects = dom.getElementsByTagName("project")
#print 'projects.length:', projects.length
#for project in projects:
#    print 'project', project.getAttribute('projName'), 'with', project.getAttribute('taskcount'), 'tasks'
dom.unlink()
