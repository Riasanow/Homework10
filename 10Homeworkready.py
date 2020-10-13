from urllib.parse import urlencode
import requests
class user:


    def get_friends(self):
        ident = input('Enter person id: ')
        response = requests.get(f'https://api.vk.com/method/friends.get?PARAMETERS&user_id={ident}&access_token=10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c&v=5.21&order=name&')
        return response


def common_friends():

  person1 = user()
  answer = person1.get_friends()
  response = answer.text
  response_dict = eval(response) #convert str to dict
  all_items1 = response_dict['response']['items']         #доходим до друзей

  person2 = user()
  answer1 = person2.get_friends()
  response1 = answer1.text
  response_dict1 = eval(response1)
  all_items2 = response_dict1['response']['items']
  list_of_common_friends = []
  for loop in all_items1:
      if loop in all_items2:
          list_of_common_friends.append(loop)
  print("Common id's of person1 and person2:",len(list_of_common_friends),':', list_of_common_friends)
  return list_of_common_friends

# common_friends()


def print_user(user_id):
    user = f'https://vk.com/id{user_id}'
    print(user)

print_user(62171087)





