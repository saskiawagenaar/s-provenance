# 
import os
import time
from pprint import pprint
import yaml
from collections import OrderedDict


pathflaskraas = '../src/prov-services/flask_raas.py'

print "parse to swagger"
print pathflaskraas
start = time.time()

approute = '@app.route('


''' YAML FOR ORDERED DICT, online'''
class UnsortableList(list):
    def sort(self, *args, **kwargs):
        pass

class UnsortableOrderedDict(OrderedDict):
    def items(self, *args, **kwargs):
        return UnsortableList(OrderedDict.items(self, *args, **kwargs))

yaml.add_representer(UnsortableOrderedDict, yaml.representer.SafeRepresenter.represent_dict)

yaml_dict = UnsortableOrderedDict()



''' INITIALISE YAML SWAGGER '''

yaml_dict['swagger'] = '2.0' 
yaml_dict['info']    = {
                        'version': '1.0.0',
                        'title': 'Provenance Store',
                        'description': '| \
#### S-ProvFlow provenance api \
Provenance framework for storage and access of data-intensive streaming lineage. It offers a a web API and a range of dedicated visualisation tools and a provenance model (S-PROV) which utilises and extends PROV and ProvONE models. \
'} 

yaml_dict['schemes'] = ['http']
yaml_dict[ 'host' ] = 'prov.knmi.nl'
yaml_dict[ 'basePath' ] = '/'
yaml_dict[ 'paths' ] = {} 

with open(pathflaskraas,'r+') as file:
    pathis = None
    for line in file:
        if (line.find(approute) ) > -1:
            path = line.replace(approute,'').replace(')\n','')

            try:
                pathis0 , m = path.split(', methods=')\

                pathis = pathis0.replace('\"','')
                yaml_dict['paths'][pathis] = {}

                if 'GET' in m :
                  yaml_dict['paths'][pathis]['get'] = { 'responses': { 200 : {'description':'GET '+str(pathis) }}}
                if 'POST' in m :
                  yaml_dict['paths'][pathis]['post'] = { 'responses': { 200 : {'description':'POST '+str(pathis) }}}
                if 'DELET' in m :
                  yaml_dict['paths'][pathis]['delete'] = { 'responses': { 200 : {'description':'DELET '+str(pathis) }}}
            except:
                pathis = path.replace('\"','')   
                yaml_dict['paths'][pathis] = {}
                yaml_dict['paths'][pathis]['get'] = { 'responses': { 200 : {'description': 'GET '+str(pathis) }}}
        elif ('def' in line) and ( pathis != None ):
            try:
              yaml_dict['paths'][pathis]['get']['summary'] = line.replace("\n","")
            except:
              pass

pprint(yaml_dict.items())


with open('swagger.test','w') as swag:
  yaml.dump( yaml_dict , swag, default_flow_style=False)

swag.close()

print time.asctime(time.localtime(start))
print time.time() - start
print 'end'
file.close()