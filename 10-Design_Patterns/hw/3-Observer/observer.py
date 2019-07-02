"""
С помощью паттерна "Наблюдатель" реализуйте простую систему подписок и уведомлений видеохостинга MyTube.

Для реализации можно использовать следующие определения классов:

MyTubeChannel - канал, у которого есть владелец.
    Параметры:
        name: str - Название канала
        owner: MyTubeUser - Владелец канала
        playlists: Dict[str, List[str]] - Плейлисты на канале ({'Название плейлиста': ['видео 1', 'видео 2', 'видео 3']})

    Методы:
        __init__(channel_name: str, chanel_owner: MyTubeUser) - При создании канала указывается название канала и его владелец
        subscribe(user: MyTubeUser) - Подписка пользователя user на канал
        publish_video(video: str) - Публикация нового видео и рассылка новости о публикации всем подписчика
        publish_playlist(name: str, playlist: List[str]) - Публикация нового плейлиста и рассылка новости о публикации всем подписчикам

MyTubeUser - Пользователь видеохостинга MyTube
    Параметры:
        _name: str - Имя пользователя MyTube
    Методы:
        __init__(user_name: str) - У нового пользователя есть имя
        update(message: str): - Метод для приёма уведомлений о публикации

Примерн кода, который должен работать:

matt = MyTubeUser('Matt')
john = MyTubeUser('John')
erica = MyTubeUser('Erica')

dogs_life = YoutubeChannel('All about dogs', matt)
dogs_life.subscribe(john)
dogs_life.subscribe(erica)

dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos]

for video in dogs_nutrition_videos:
    dogs_life.publish_video(video)

dogs_life.publish_playlist(dogs_nutrition_playlist)

Output:
Dear John, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear Erica, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear John, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear Erica, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear John, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'
Dear Erica, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'

"""


class MyTubeUser:
    def __init__(self, name):
        self._name = name

    def update_video(self, message, channel_name=None):
        print(f'Dear {self._name}, there is new video on \'{channel_name}\' channel: \'{message}\'')

    def update_playlist(self, message, channel_name=None):
        if isinstance(message, dict):
            message = list(message.keys())[0]
        print(f'Dear {self._name}, there is new playlist on : \'{channel_name}\' channel: \'{message}\'')


class YoutubeChannel:
    def __init__(self, channel_name, chanel_owner):
        self.subscribers = dict()
        self._channel_name = channel_name
        self._chanel_owner = chanel_owner

    def subscribe(self, who, callback=None):
        if callback is None:
                callback_video = getattr(who, 'update_video')
                callback_playlist = getattr(who, 'update_playlist')

        self.subscribers[who] = [callback_video, callback_playlist]

    def publish_video(self, video):
        for subscriber, callback in self.subscribers.items():
            callback[0](video, channel_name=self._channel_name)

    def publish_playlist(self, playlist):
        for subscriber, callback in self.subscribers.items():
            callback[1](playlist, channel_name=self._channel_name)




matt = MyTubeUser('Matt')
john = MyTubeUser('John')
erica = MyTubeUser('Erica')

dogs_life = YoutubeChannel('All about dogs', matt)
dogs_life.subscribe(john)
dogs_life.subscribe(erica)

dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}

for video in dogs_nutrition_videos:
    dogs_life.publish_video(video)

dogs_life.publish_playlist(dogs_nutrition_playlist)
