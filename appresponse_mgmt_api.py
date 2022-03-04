import requests
import json


class Appresponse_Mgmt:
    api_url = "/api/common/1.0/info"

    def __init__(self,received_ar_ip_addr,received_ar_bearer_token):
        self.ar_ip_addr=received_ar_ip_addr
        self.ar_bearer_token=received_ar_bearer_token

    def api_call(self,received_api_method,received_api_url,received_payload):
        url = f"https://{self.ar_ip_addr}{received_api_url}"

        payload = received_payload
        headers = {
            'Authorization': f'Bearer {self.ar_bearer_token}',
            'Content-Type': 'application/json'
            }
        response = requests.request(received_api_method, url, headers=headers, data=payload,verify=False)
        return response

    def get_data_with_api_call(self): 
        repsonse = (self.api_call("GET",self.api_url,""))
        self.orginal_config = repsonse.json()
        print(json.dumps(self.orginal_config, sort_keys=False, indent=4))
        return self.orginal_config

    def post_new_config(self):
        print("posting new config")
        for config in self.new_config:
            print(self.api_call("POST",self.api_url,(json.dumps(config))))
            print(config)

    def put_new_config(self):
        print("put new config")
        for config in self.new_config:
            print(self.api_call("PUT",self.api_url,(json.dumps(config))))
            print(config)

class Ar_Vifgs(Appresponse_Mgmt):
    api_url = "/api/npm.packet_capture/3.0/vifgs"

class Ar_Capture_Jobs(Appresponse_Mgmt):
    api_url = "/api/npm.packet_capture/3.0/jobs"
    
class Ar_Snmp(Appresponse_Mgmt):
    api_url = '/api/npm.snmp/1.0/snmp/config'

class Ar_Ntp(Appresponse_Mgmt):

    api_url = '/api/mgmt.time/1.0/ntp/servers'
    ntp_items_url = '/api/mgmt.time/1.0/ntp/servers/items'


    def remove_old_config(self):
        for config in reversed(self.orginal_config['items']):
            print(config['server_id'])
            url= f"{self.ntp_items_url}/{(config['server_id'])}"
            print(f"\n\t the URL is ----->> {url}\n")
            print(self.api_call("DELETE",url,""))

    def update_old_with_new_config(self,received_new_config):
        self.new_config=received_new_config

        if self.is_new_config_correct():
            self.remove_old_config()
            self.post_new_config()
            return True
        else:
            print("\n########## error in config data ##############\n")
            return False

    def is_new_config_correct(self):
        print("##############")
        print("testing config")
        print("##############")
        for ntp_config in self.new_config:
            print (ntp_config)

            if (type(ntp_config['server_id']) != int or 
                type(ntp_config['address']) != str or 
                type(ntp_config['prefer']) != bool or 
                type(ntp_config['encryption']) != str or 
                type(ntp_config['version']) != int
                ):
                print("\tBad base config")
                return False
            #check if there is a encryption
            if ntp_config['encryption'] != 'none':
                if (ntp_config['encryption'] == 'md5' or
                    ntp_config['encryption'] == 'sha1'):
                    print("\t\t\t\twe have encrytion")
                    if (type(ntp_config['key_id'])!= int or
                        type(ntp_config['secret'])!= str):
                        
                        print("\t\t\t\tencrytion is bad")
                        print("False 3")
                        return False
                else:
                    print("False 2")
                    return False

        return True

class Ar_Dns(Appresponse_Mgmt):
    api_url = '/api/mgmt.networking/1.1/settings/host'


class Ar_Phy_Int(Appresponse_Mgmt):
    api_url = "/api/npm.packet_capture/3.0/interfaces"

class Ar_Applications(Appresponse_Mgmt):
    api_url = "/api/npm.classification/3.2/applications"

class Ar_Hostgroups(Appresponse_Mgmt):
    api_url = "/api/npm.classification/3.2/hostgroups"

class Ar_Urls(Appresponse_Mgmt):
    api_url = "/api/npm.classification/3.2/urls"

