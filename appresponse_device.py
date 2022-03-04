#from xmlrpc.client import boolean
import requests
import json
import appresponse_mgmt_api

class AppResponse:
    
    num_of_ars = int(0)
    
    def __init__(self,ip_addr,bearer_token):
        self.ip_addr=ip_addr
        self.bearer_token=bearer_token

        self.ntp_class = appresponse_mgmt_api.Ar_Ntp(self.ip_addr,self.bearer_token)
        self.ntp_data = self.ntp_class.get_data_with_api_call()
        print("=====================================================================================")
        self.snmp_class = appresponse_mgmt_api.Ar_Snmp(self.ip_addr,self.bearer_token)
        self.snmp_data = self.snmp_class.get_data_with_api_call()
        print("=====================================================================================")
        self.common_class = appresponse_mgmt_api.Appresponse_Mgmt(self.ip_addr,self.bearer_token)
        self.common_data = self.common_class.get_data_with_api_call()
        print("=====================================================================================")
        self.vifgs_class = appresponse_mgmt_api.Ar_Vifgs(self.ip_addr,self.bearer_token)
        self.vifgs_data = self.vifgs_class.get_data_with_api_call()
        print("=====================================================================================")
        self.cap_job_class = appresponse_mgmt_api.Ar_Capture_Jobs(self.ip_addr,self.bearer_token)
        self.cap_job_data = self.cap_job_class.get_data_with_api_call()
        print("=====================================================================================")
        self.dns_class = appresponse_mgmt_api.Ar_Dns(self.ip_addr,self.bearer_token)
        self.dns_data = self.dns_class.get_data_with_api_call()
        print("=====================================================================================")
        self.phy_int_class = appresponse_mgmt_api.Ar_Phy_Int(self.ip_addr,self.bearer_token)
        self.phy_int_data = self.phy_int_class.get_data_with_api_call()
        print("=====================================================================================")
        self.ar_apps_class = appresponse_mgmt_api.Ar_Applications(self.ip_addr,self.bearer_token)
        self.ar_apps_data = self.ar_apps_class.get_data_with_api_call()
        print("=====================================================================================")
        self.hostgroups_class = appresponse_mgmt_api.Ar_Hostgroups(self.ip_addr,self.bearer_token)
        self.hostgroups_data = self.hostgroups_class.get_data_with_api_call()
        print("=====================================================================================")
        self.urls_class = appresponse_mgmt_api.Ar_Urls(self.ip_addr,self.bearer_token)
        self.urls_data = self.urls_class.get_data_with_api_call()
    
        AppResponse.num_of_ars += 1
      
    def api_get_request(self,received_api_url):
        url = f"https://{self.ip_addr}{received_api_url}"
        payload = ""
        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json'
            }
        response = requests.request("GET", url, headers=headers, data=payload,verify=False)
        return response.json()
    
    def snmp_info(self):
        snmp_data_dictionary = self.api_get_request(self.snmp_url)
        print(json.dumps(snmp_data_dictionary, sort_keys=False, indent=4))
        return snmp_data_dictionary

    def timezone_info(self):
        timezone_string = self.api_get_request(self.timezone_url)
        print(f"data type of response is \t {type(timezone_string)}")
        print(timezone_string)
        return timezone_string

    def networking_info(self):
        networking_data_dictionary = self.api_get_request(self.networking_url)
        print(f"data type of response is \t {type(networking_data_dictionary)}")
        print(json.dumps(networking_data_dictionary, sort_keys=False, indent=4))
        return networking_data_dictionary

    def update_ar_with_new_config(self,received_new_config):
        self.new_config = received_new_config
        print(self.ntp_class.update_old_with_new_config(self.new_config))
        print (self.new_config)