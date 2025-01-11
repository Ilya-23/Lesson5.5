import time


class UrTube:
    current_user = None

    def __init__(self):
        self.users = []
        self.videos = []

    def log_in(self, nickname, password):
        addit1 = False
        for i in self.users:
            if nickname == i.nickname:
                if i.password == hash(password):
                    self.current_user = i.nickname
                    addit1 = True
                    break
                else:
                    continue
            else:
                continue
        if addit1 is False:
            print('Пользователь не найден')
        else:
            print(self.current_user)


    def register(self, nickname, password, age):
        addit2 = False
        new_user = User(nickname, password, age)


        if len(self.users) == 0:
            self.users.append(new_user)
            self.current_user = new_user.nickname
        else:
            for i in self.users:
                if nickname == i.nickname:
                    print(f'Пользователь {nickname} уже существует')
                    addit2 = False
                    break
                else:
                    addit2 = True
        if addit2 is True:
            self.users.append(new_user)
            self.current_user = new_user.nickname


    def log_out(self):
        self.current_user = None

    def add(self, *args):

        for i in args:
           self.videos.append(i)


    def get_videos(self, search):
        list_search =[]
        search1 = str(search).lower()
        for i in self.videos:
            title_video = i.title.lower()
            if search1 in title_video:
                list_search.append(i.title)
            else:
                continue
        return list_search

    def watch_video(self, title):
        age1 = 0
        for i in self.videos:
            if title == i.title:
                if self.current_user != None:
                    for j in self.users:
                        if self.current_user == j.nickname:
                            age1 = j.age
                            break
                        else:
                            continue
                    if i.adult_mode is False or (i.adult_mode is True and age1 >= 18):
                        for k in range(i.duration):
                            time.sleep(1)
                            print(k+1)

                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                break
            else:
                continue






class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def lk(self):
        return [self.nickname, self.password, self.age]

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
