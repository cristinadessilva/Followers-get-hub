import requests
import json

class listFollowers():
    def __init__(self, user):
        self.user = user

    def request_api(self):
        response = requests.get(
            f'https://api.github.com/users/{self.user}/followers')
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def show_followers(self):
        data_api = self.request_api()
        if type(data_api) is not int:
            for i in range(len(data_api)):
                print(data_api[i]['login'])
        else:
            print(data_api)


followers = listFollowers('cristinadessilva')
followers.show_followers()