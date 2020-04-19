# -*- coding: utf-8 -*-
import falcon, os, json, requests

# adapt to your needs
os.chdir("/mnt/d/github_repos/Wahldaten-API")


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

class getKv():
    def on_get(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')

        try:
            key = req.params['kreis']
            data = {"status": "success", "data": {}}      
        except:
            resp.status = falcon.HTTP_404
            return
        res = []


        urls= [
            "https://raw.githubusercontent.com/CubicrootXYZ/Wahldaten/master/Piratenpartei/Gliederungen/gliederungen_bw_kv.json",
            "https://raw.githubusercontent.com/CubicrootXYZ/Wahldaten/master/Piratenpartei/Gliederungen/gliederungen_hb_kv.json"
        ]

        for url in urls:
            try: 
                json_file = requests.get(url)
                data = json_file.json()

                for key_ in data['data'].keys():
                    if key in key_:
                        ap = data['data'][key_]
                        ap['kreis']  = key_
                        res.append(ap)
            except Exception as e:
                print (e)


        try:
            if len(res)>0:
                resp.body = json.dumps({"status": "success", "data": res}) 
                resp.status = falcon.HTTP_200
            else: 
                resp.body = json.dumps({"status": "success", "data": None}) 
                resp.status = falcon.HTTP_200
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_404

class getBzv():
    def on_get(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')

        try:
            key = req.params['bezirk']
            data = {"status": "success", "data": {}}      
        except:
            resp.status = falcon.HTTP_404
            return
        res = []


        urls= [
            "https://raw.githubusercontent.com/CubicrootXYZ/Wahldaten/master/Piratenpartei/Gliederungen/gliederungen_bw_bzv.json"
        ]

        for url in urls:
            try: 
                json_file = requests.get(url)
                data = json_file.json()

                for key_ in data['data'].keys():
                    if key in key_:
                        ap = data['data'][key_]
                        ap['bezirk']  = key_
                        res.append(ap)
            except Exception as e:
                print (e)


        try:
            if len(res)>0:
                resp.body = json.dumps({"status": "success", "data": res}) 
                resp.status = falcon.HTTP_200
            else: 
                resp.body = json.dumps({"status": "success", "data": None}) 
                resp.status = falcon.HTTP_200
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_404

class getLv():
    def on_get(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')

        try:
            key = req.params['bundesland']
            data = {"status": "success", "data": {}}      
        except:
            resp.status = falcon.HTTP_404
            return
        res = []


        urls= [
            "https://raw.githubusercontent.com/CubicrootXYZ/Wahldaten/master/Piratenpartei/Gliederungen/gliederungen_lv.json"
        ]

        for url in urls:
            try: 
                json_file = requests.get(url)
                data = json_file.json()

                for key_ in data['data'].keys():
                    if key in key_:
                        ap = data['data'][key_]
                        ap['bundesland']  = key_
                        res.append(ap)
            except Exception as e:
                print (e)


        try:
            if len(res)>0:
                resp.body = json.dumps({"status": "success", "data": res}) 
                resp.status = falcon.HTTP_200
            else: 
                resp.body = json.dumps({"status": "success", "data": None}) 
                resp.status = falcon.HTTP_200
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_404
        

        

api = falcon.API()
api.req_options.auto_parse_form_urlencoded=True
api.add_route('/getwkbyplz', getWkByPlz())
api.add_route('/getwkbyname', getWkByName())
api.add_route('/getwkbywkname', getWkByWkname())
api.add_route('/getwkbywknum', getWkByWknum())
api.add_route('/getkv', getKv())
api.add_route('/getbzv', getBzv())
api.add_route('/getlv', getLv())
