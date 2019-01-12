# coding: utf-8
import pprint
from pypodio2 import api
import json
import os

cwd = os.getcwd() 

podio_string = '''
{
    "app_name":null,
    "app_id":null,
    "fields":[
        "id": null,
        "name": null,
        "type": null,
        "app": null,
        "choices": [],
        ],
    
}
'''
4
client_id = "tester-2a2ebd"
client_secret = "Jh1qGaLD4wjBHnqrEXC5lXXO2j1k6cF7s6z1NpDG2ATBT6qIKS2oI1nDScssQgZG"
username = "ryan393brown@gmail.com"
password = "Cascadia3"

c = api.OAuthClient(
    client_id,
    client_secret,
    username,
    password,    
)

url_n = raw_input("workspace url_label:")

apps = []

def wrkSpace(url_slug):

    url = 'https://podio.com/applegate-solutions/' + url_slug
    url2 = 'https://podio.com/hypertext-labs-co/' + url_slug

    print(url)

    space_id = c.Space.find_by_url(url)

    print(space_id)

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

path = './'
fileName = 'develop'




def json_handler(fname, data):
    t = []
    if not os.path.isfile(fname):
        t.append(data)
        with open(fname, mode='w') as f:
            f.write(json.dumps(data, indent=2))
    else:
        with open(fname) as feedsjson:
            feeds = json.load(feedsjson)

        feeds.append(data)
        with open(fname, mode='w') as f:
            f.write(json.dumps(feeds, indent=2))




def getFields(idx):

    #resp = c.Application.get_items(idx)
    #nx = json.loads(raw)
    print idx
    apps = []
    for a in idx:
        print a
                
        types = []
        flabels = []
        fids = []
        fapps = {}


        
        ags_apps = {}
        
        esp = c.Application.find(a)
        nx = esp['fields']
        nfm = len(nx)
        
        d = esp['url_label']
        ags_apps['app'] = d
        print d
        print nfm
        

        for i in nx:
            
            cats = []
            label = i['label']
            typ = i['type']
            fid = i['field_id']
            

            if typ == 'calculation':
                rtyp = i['config']['settings']['return_type']
                lb = label.encode('utf-8')
                tp = rtyp.encode('utf-8')
                fapps['field_id'] = fid
                fapps['label'] = lb
                fapps['type'] = tp
                ags_apps['fields'] = fapps

                pass
            
            elif typ == 'category':
                rtyp = i['config']['settings']['options']
                lst = []
                for i in rtyp:
                    h = i['text'].encode('utf-8')
                    lst.append(h)
                
                lb = label.encode('utf-8')
                fapps['field_id'] = fid
                fapps['label'] = lb
                fapps['type'] = { 'category': lst}
                ags_apps['fields'] = fapps

                pass


            elif typ == 'app':
                rtyp = i['config']['settings']['apps']
                lst = []
                for i in rtyp:
                    x = i['name'].encode('utf-8')
                    
                    app_str = typ.encode('utf-8')+": "+x
                    #lst.append()
                lb = label.encode('utf-8')
                fapps['field_id'] = fid
                fapps['label'] = lb
                fapps['type'] = app_str
                ags_apps['fields'] = fapps

                pass

            
            else:
                lb = label.encode('utf-8')
                tp = typ.encode('utf-8')
                fapps['field_id'] = fid
                fapps['label'] = lb
                fapps['type'] = tp
                ags_apps['fields'] = fapps
                pass
            
            cats.append(fapps)
    apps.append(cats)
    
    print json.dumps(apps, indent=4, sort_keys=True)
    
        
getFields(d)

