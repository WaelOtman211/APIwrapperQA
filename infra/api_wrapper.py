import requests
from infra.config_handler import ConfigHandler


class APIWrapper:

    def __init__(self):
        self.response = None
        config_file_path = 'C:\AutomationWithTsahi\APITesting\config.json'
        self.config_handler = ConfigHandler(config_file_path)
        self.base_url = self.config_handler.get_base_url()
        self.cards = self.config_handler.get_cards()



    def api_get_request(self, endpoint):
        url = self.base_url + endpoint
        self.response = requests.get(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_post_request(self, endpoint, data=None):
        url = self.base_url + endpoint
        self.response = requests.post(url, json=data)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code