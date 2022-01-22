import requests

base = 'http://127.0.0.1:5000/'

data = [{'likes': 12, 'name': 'pokemon theme song by smosh', 'views': 1000000000},
        {'likes': 197, 'name': 'majora\'s mask rap video', 'views': 9000000000},
        {'likes': 1232132, 'name': 'goku vs vageta', 'views': 347435},
        {'likes': 143654632132, 'name': 'crazyinesssa', 'views': 259347435},
        {'likes': 1132, 'name': 'gtesttest', 'views': 9347435},
        {'likes': 43242, 'name': 'placehold ya', 'views': 435},
        {'likes': 2132, 'name': 'Gangnam STyle', 'views': 5},
        {'likes': 600900, 'name': 'Taylor Swift Cover', 'views': 47435},
        {'likes': 4442, 'name': 'EnNopp112 World Record', 'views': 25934},
        {'likes': 12322, 'name': 'Water Bottle Drink', 'views': 259}]

for i in range(len(data)):
    response = requests.post(base + 'video/' + str(i), data=data[i])
    print(response.json())

input('\nPress enter to patch video 2...')
response = requests.patch(base + 'video/2', {'views':69, 'name': 'please work'})
print(response.json())

input('\nPress enter to delete video 90...')
response = requests.delete(base + 'video/90')
print(response.text)

input('\nPress enter to delete video 7...')
response = requests.delete(base + 'video/7')
print(response.text)