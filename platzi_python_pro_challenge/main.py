from datetime import datetime
import time


class Pomodoro():
    def __init__(self):
        self.time_start: None
        self.time_finish: None

    def start(self):
        self.time_start = datetime.now()

    def end(self):
        self.time_finish = datetime.now()
        total_time = self.time_finish - self.time_start
        print(f'La tarea tomo {total_time}')


def main():
    pomodoro = Pomodoro()
    pomodoro.start()
    time.sleep(5)
    pomodoro.end()


if __name__ == "__main__":
    main()
