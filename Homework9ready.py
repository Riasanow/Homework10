import requests

#1

import requests

intellegence_values = []

response_hulk = requests.get('https://superheroapi.com/api.php/1430014010524830/search/hulk')
hulk = response_hulk.json()['results'][0]['powerstats']['intelligence']
intellegence_values.append(int(hulk))

response_captain_america = requests.get('https://superheroapi.com/api.php/1430014010524830/search/capt.. america')
captain_america = response_captain_america.json()['results'][0]['powerstats']['intelligence']
intellegence_values.append(int(captain_america))

response_thanos = requests.get('https://superheroapi.com/api.php/1430014010524830/search/thanos')
thanos = response_thanos.json()['results'][0]['powerstats']['intelligence']
intellegence_values.append(int(thanos))


biggest = max(intellegence_values)
print(biggest)
if biggest == int(hulk):
print(response_hulk.json()['results'][0]['name'],',', biggest)
if biggest == int(captain_america):
print(response_captain_america.json()['results'][0]['name'],',', biggest)
else:
print(response_thanos.json()['results'][0]['name'],',', biggest)


#2

import requests
import os


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        user_input = input('Введите токен: ')
        header = {'Authorization': None}
        header['Authorization'] = user_input

        with open(self.file_path, 'r+b') as f:
            test_file = f.read()  # читаем/записываем данные из файла

        _, fname = os.path.split(self.file_path)

        response = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path=/{fname}',
                                headers=header)  # в ссылку вставляем название переменной file_name

        href = response.json()['href']  # ссылку для загрузки добавляем в переменную

        r = requests.put(href,
                         data=test_file)  # загружаем файл на YD, в поле data передаем нашу переменную, где считывали данные из файла

        print('Загрузка успешно завершена!')


if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload()


