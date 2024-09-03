import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    users = []
    videos = []
    current_user: User | None = None

    def log_in(self, nickname: str, password: str):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f'вы зашли {user.nickname}')
                return
            print('Неверный логин и/или пароль')

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        return f"Пользователь {nickname} зарегистрирован и вошел в систему."

    def lof_out(self):
        print(f'Вы вышли {self.current_user.nickname}')
        self.current_user = None

    def add(self, *args):
        for movie in args:
            if movie.title not in [video.title for video in self.videos]:
                self.videos.append(movie)

    def get_videos(self, searching_str: str):
        searching_lst = []
        for video in self.videos:
            video.title = video.title.lower()
            if searching_str.lower() in video.title:
                searching_lst.append(video.title)
        return searching_lst

    def watch_video(self, title_video: str):
        if self.current_user is not None:
            for video in self.videos:
                if title_video.lower() == video.title.lower():
                    if self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        video.adult_mode = False
                        for i in range(video.time_now, video.duration):
                            print(i, end=' ')
                            time.sleep(1)
                        print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


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
