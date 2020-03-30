# -*- coding: utf-8 -*-
import falcon, os, json

# adapt to your needs
os.chdir("/opt/app")


class getWkByPlz():
    def on_get(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')

        try:
            key = req.params['plz']
            data = {"status": "success", "data": {}}      
        except:
            resp.status = falcon.HTTP_404
            return


    
        try: 
            with open('data/wahlkreise_btw_plz.json') as json_file:
                data = json.load(json_file)

                if key in data['data'].keys():
                    resp.body = json.dumps({"status": "success", "data": data['data'][key]}) 
                    resp.status = falcon.HTTP_200
                else: 
                    resp.body = json.dumps({"status": "success", "data": None}) 
                    resp.status = falcon.HTTP_200
        except:
            resp.status = falcon.HTTP_404

class getWkByName():
    def on_get(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')

        try:
            key = req.params['name']
            data = {"status": "success", "data": {}}      
        except:
            resp.status = falcon.HTTP_404
            return


    
        try: 
            with open('data/wahlkreise_btw_gemeinde.json') as json_file:
                data = json.load(json_file)
                res = []
                for key_ in data['data'].keys():
                    if key in key_:
                        ap = data['data'][key_]
                        ap['gemeinde']  = key_
                        res.append(ap)
                if len(res)>0:
                    resp.body = json.dumps({"status": "success", "data": res}) 
                    resp.status = falcon.HTTP_200
                else: 
                    resp.body = json.dumps({"status": "success", "data": None}) 
                    resp.status = falcon.HTTP_200
        except:
            resp.status = falcon.HTTP_404

class getWkByWkname():
    def on_get(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')

        try:
            key = req.params['name']
            data = {"status": "success", "data": {}}      
        except:
            resp.status = falcon.HTTP_404
            return


    
        try: 
            with open('data/wahlkreise_btw_wahlkreis.json') as json_file:
                data = json.load(json_file)

                res = []
                for key_ in data['data'].keys():
                    if key in key_:
                        ap = data['data'][key_]
                        ap['wahlkreis_bezeichnung']  = key_
                        res.append(ap)
                if len(res)>0:
                    resp.body = json.dumps({"status": "success", "data": res}) 
                    resp.status = falcon.HTTP_200
                else: 
                    resp.body = json.dumps({"status": "success", "data": None}) 
                    resp.status = falcon.HTTP_200
        except:
            resp.status = falcon.HTTP_404

class getWkByWknum():
    def on_get(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')

        try:
            key = req.params['number']
            data = {"status": "success", "data": {}}      
        except:
            resp.status = falcon.HTTP_404
            return


    
        try: 
            with open('data/wahlkreise_btw_wahlkreisnummer.json') as json_file:
                data = json.load(json_file)

                if key in data['data'].keys():
                    resp.body = json.dumps({"status": "success", "data": data['data'][key]}) 
                    resp.status = falcon.HTTP_200
                else: 
                    resp.body = json.dumps({"status": "success", "data": None}) 
                    resp.status = falcon.HTTP_200
        except:
            resp.status = falcon.HTTP_404
        

        

api = falcon.API()
api.req_options.auto_parse_form_urlencoded=True
api.add_route('/getwkbyplz', getWkByPlz())
api.add_route('/getwkbyname', getWkByName())
api.add_route('/getwkbywkname', getWkByWkname())
api.add_route('/getwkbywknum', getWkByWknum())
