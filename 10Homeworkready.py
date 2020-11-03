from urllib.parse import urlencode
import requests


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f'https://vk.com/id''{}'.format(self.user_id)

    def __and__(self, other):
        response = requests.get(f'https://api.vk.com/method/friends.get?PARAMETERS&user_id={self.user_id}&access_token=10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c&v=5.21&order=name&')
        response_dict = response.json()
        all_items1 = response_dict['response']['items']  # доходим до друзей
        all_items1_set = set(all_items1)

        response1 = requests.get(f'https://api.vk.com/method/friends.get?PARAMETERS&user_id={other.user_id}&access_token=10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c&v=5.21&order=name&')
        answer1 = response1.text
        response_dict1 = eval(answer1)
        all_items2 = response_dict1['response']['items']
        all_items2_set = set(all_items2)
        list_of_common_friends = []
        if len(all_items1_set) & len(all_items2_set) == 0:
            print('общих друзей нет!')
        else:
          for loop in all_items1_set:
            if loop in all_items2_set:
                list_of_common_friends.append(loop)



        com_fr = []
        for friendd in list_of_common_friends:
            com_fr.append(User(friendd))
        return com_fr





user1 = User(52312949)
user2 = User(56256805)
print(user2)
common_friends = user1 & user2
for friend in common_friends:
    assert isinstance(friend, User)
    print(friend)






