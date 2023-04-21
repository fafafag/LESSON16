from time import time, localtime


class Clock:

    @staticmethod
    def Say_time():
        time = localtime()
        print(f'Текущее время: {time.tm_hour}:{time.tm_min}:{time.tm_sec}')


Clock.Say_time()
