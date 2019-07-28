# coding: utf-8
import pprint
from pypodio2 import api


client_id = "tester-2a2ebd"
client_secret = "Jh1qGaLD4wjBHnqrEXC5lXXO2j1k6cF7s6z1NpDG2ATBT6qIKS2oI1nDScssQgZG"
username = "ryan393brown@gmail.com"
password = "Cascadia3"

podioUrl = "https://podio.com/hypertext-labs-co/"
wrkSpaceUrl = "https://podio.com/hypertext-labs-co/"
wrkSpace = "body-back-company" 


c = api.OAuthClient(
    client_id,
    client_secret,
    username,
    password,    
)

url_n = raw_input("workspace url_label:")

#org = raw_input("org:")
#wrkSpace()


apps = []
def wrkSpace(url_slug):

    url = 'https://podio.com/applegate-solutions/' + url_slug
    url2 = 'https://podio.com/hypertext-labs-co/' + url_slug

    print(url)

    space_id = c.Space.find_by_url(url)

    print space_id

wrkSpace(url_n)

sid = raw_input("space id:")
def getApps(space_id):

    resp = c.Application.list_in_space(space_id)
    apps = []
    ids = []

    for i in resp:
        app_id = i['app_id']
        ids.append(app_id)
    return ids

d = getApps(sid)
print type(d)
print d
def getFields(idx):

    #resp = c.Application.get_items(idx)
    #nx = json.loads(raw)
    print idx
    for a in idx:
        print a
                
        types = []
        flabels = []
        fids = []
        
        esp = c.Application.find(a)
        nx = esp['fields']
        print esp['url_label']
       # print nx

        for i in nx:
            fapps = []
            label = i['label']
            typ = i['type']
            fid = i['field_id']
            if typ == 'calculation':
                rtyp = i['config']['settings']['return_type']
                tpl = (fid, label.encode('utf-8'), rtyp.encode('utf-8'))
                fapps.append(tpl)
        
            else:
                tpl = (fid, label.encode('utf-8'), typ.encode('utf-8'))
                fapps.append(tpl)
            print fapps




getFields(d)


"""
 c.__dir__ 
 
 returns...

['Application',
 'Area',
 'Connection',
 'Contact',
 'Conversation',
 'Embed',
 'Files',
 'Hook',
 'Item',
 'Notification',
 'Org',
 'Search',
 'Space',
 'Status',
 'Stream',
 'Task',
 'User',
 'View',
 '__builtins__',
 '__doc__',
 '__file__',
 '__name__',
 '__package__',
 'json',
 'urlencode']

"""


"""
 Workspace

(1) get info (url, url_label, space_id)
(2) get list of apps (app_id_lst)

"""

"""
 Application(app_id_lst)

(1) iterate through each application 
(2) for e iter on app - get all_fields
(3) for e field get type and json struct

"""    

"""
for i in wrks_ndn:
    print i
    
"""


