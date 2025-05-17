# import requests

# api_url = "https://jsonplaceholder.typicode.com/users/1"
# response = requests.get(api_url)
# if response.status_code == 200:
#     print("Запрос выполнен успешно!")
# else:
#     print("Ошибка запроса:", response.status_code)

# data = response.json()
# print(data)
# print(f"Имя: {data['name']}")

# import requests

# picsum_url = "https://picsum.photos/200/300"
# response = requests.get(picsum_url)

# if response.status_code == 200:
#     print("Изображение успешно получено. Код состояния:", response.status_code)
# else:
#     print("Ошибка при запросе к API:", response.status_code)

# import requests

# meow_facts_url = "https://meowfacts.herokuapp.com/"
# response = requests.get(meow_facts_url)

# if response.status_code == 200:
#     data = response.json()
#     print("Случайный факт о кошках:", data['data'][0])
# else:
#     print("Ошибка при запросе к API:", response.status_code)

# import requests

# waifu_pics_url = "https://waifu.pics/docs"
# response = requests.get(meow_facts_url)

# if response.status_code == 200:
#     data = response.json()
#     print("Случайный факт о кошках:", data['data'][0])
# else:
#     print("Ошибка при запросе к API:", response.status_code)
