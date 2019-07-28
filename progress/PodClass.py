# coding: utf-8
import pprint
from pypodio2 import api
import json
import os

client_id = "tester-2a2ebd"
client_secret = "Jh1qGaLD4wjBHnqrEXC5lXXO2j1k6cF7s6z1NpDG2ATBT6qIKS2oI1nDScssQgZG"
username = "ryan393brown@gmail.com"
password = "Cascadia3"

cwd = os.getcwd() 
path = './'
fileName = 'develop'

"""
 Make these ENV variables 

Additionally make it so it appends (not rewrites*) or creates schema.py and pod_models.py

Returns:
    Next: Add django command interfacing so it can be a django package + app possibly
"""



class Pod(object):

    url_n = raw_input("workspace url_label:")
    sid = raw_input("space id:")
    apps = []
    c = api.OAuthClient(
        client_id,
        client_secret,
        username,
        password
        )
    
    def wrkSpace(url_slug):

        url = 'https://podio.com/applegate-solutions/' + url_slug
        url2 = 'https://podio.com/hypertext-labs-co/' + url_slug

        space_id = c.Space.find_by_url(url2)

    def getApps(space_id):

        """
         getApps
        
        takes workspace id and gives a list of space ids 
        
        Returns:
            list: space_ids
        """


        resp = c.Application.list_in_space(space_id)
        apps = []
        ids = []

        for i in resp:
            app_id = i['app_id']
            ids.append(app_id)
    
        return ids

    def appData(idx):
        """
        appData 
        
        [description]
        
        Args:
            idx ([type]): [description]
        
        Returns:
            [type]: [description]
        """


        #resp = c.Application.get_items(idx)
        #nx = json.loads(raw)
        #print idx
        apps = []
        ags_apps = {}
        cats = []

        return apps 
    
    def appName(app):            
            esp = c.Application.find(app)
            nx = esp['fields']
            nfm = len(nx)
            
            d = esp['url_label']
            ags_apps['app'] = d

    def appFields(i):


        
        fapps = {}
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
            print rtyp
                #lst.append()
            lb = label.encode('utf-8')
            fapps['field_id'] = fid
            fapps['label'] = lb
            fapps['type'] = lb
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

    ags_apps['fields'] = cats
    apps.append(ags_apps)


    def author(object):
        
        with open('check.py', 'a') as f:
            
            fields = data['fields']
            app = data['app']
            
            django_model_class = "class {}(models.Model):\n".format(app.upper())
            f.write(django_model_class)
                
            for i in fields:
                n = i['label']

                django_model_field = "    {} = models.TextField(max_length=100)\n".format(n)
                f.write(django_model_field)          
                print(type(django_model_field))
            f.write('\n')
                       
        with open('schema.py', 'a') as s:
            k = data['app']

            schema_type_def = "class {0}Type(DjangoObjectType):\n    class Meta:\n        model = {0}\n".format(k)
            s.write(schema_type_def)
            s.write('\n')


    def podioAuthor(data):
        for i in data:
            author(data)
    
    pass


