import json 

json_obj = """

{
  "app": "appointments",
  "fields": [
    {
    "type": "text", 
    "field_id": 168274028, 
    "label": "peeps"
   },
    {
    "type": "text", 
    "field_id": 268274028, 
    "label": "points"
   }
  ]
}

"""
d = json.loads(json_obj)
f = d['fields']
#print(f)
x = d['app']


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


author(d)

14 hr - 