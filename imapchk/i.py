import getpass, imaplib, re

getFrom = re.compile(r"""From: .*?\r\n""")
getDate = re.compile(r"""Date: .*?\r\n""")
getSubj = re.compile(r"""Subject: .*?\r\n""")

class Login():
    def __init__(self, server='', user='', port=993, folder='INBOX', name=''):
        self.server = server
        self.user = user
        self.port = port
        self.folder = folder
        self.name = name

emailuser = Login(server = 'mail.messagingengine.com',
                  user   = 'chadmail@emailuser.net',
                  folder = 'INBOX.testf',
                  name   = 'emailuser')

gmail = Login(server = 'imap.gmail.com',
              user   = 'chad@glendenin.com',
              folder = 'fm-sent-2003',
              name   = 'gmail')

fastmail = Login(server = 'mail.messagingengine.com',
                 user   = 'chadg@fastmail.fm',
                 folder = 'INBOX.sent-mail-old.2003',
                 name   = 'fastmail')

login = gmail

print login.name, login.user, 'login...'
m = imaplib.IMAP4_SSL(login.server, login.port)
m.login(login.user, getpass.getpass())
print m.state

#print 'list...'
#print m.list()
#print m.state

print 'select...'
print m.select(mailbox=login.folder, readonly=True)
print m.state

print 'search (all)...'
typ, idList = m.search(None, 'ALL')
print typ, idList, m.state

print 'messages...'
def getField(regex, FieldName, str):
    x = regex.search(str)
    if x is None:
        return FieldName + ": <EMPTY>"
    else:
        return x.group(0).rstrip()

f = open(login.name + '.txt', 'w')
#print >>f, login.folder

for id in idList[0].split(' '):
    typ,data = m.fetch(id, '(RFC822.HEADER)')
    #s = re.sub('\d+ ','', data[0])
    print typ, id
    str = data[0][1]
    #From = getFrom.search(str).group(0).rstrip()
    #Date = getDate.search(str).group(0).rstrip()
    #Subj = getSubj.search(str).group(0).rstrip()
    From = getField(getFrom, "From", str)
    Date = getField(getDate, "Date", str)
    Subj = getField(getSubj, "Subject", str)
    #print >>f, str
    print >>f, Date, From, Subj
print m.state

# Now, after this code run, I can do this stuff...
#   sort < fastmail.txt > f.txt
#   sort < gmail.txt > g.txt
#   vimdiff f.txt g.txt
# ...to figure out why my mailbox message tallies don't match.

print 'close...'
m.close()
print m.state

print 'logout...'
print m.logout()
print m.state

print 'shutdown...'
m.shutdown()
print m.state
