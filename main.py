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
                print (data_api[i]['login'])
                

        else:
            print(data_api)



import PySimpleGUI as sg

layout = [[sg.Text("What's your user from Github?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

window = sg.Window('Followers GitHub', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    window['-OUTPUT-'].update('Followers from: ' + values['-INPUT-'],)
    user = listFollowers(values['-INPUT-'])
    user.show_followers()

window.close()

