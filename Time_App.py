# beepy sounds1 : 'coin', 2 : 'robot_error', 3 : 'error', 4 : 'ping', 5 : 'ready', 6 : 'success', 7 : 'wilhelm'

import tkinter as tk
from datetime import datetime, timedelta
from sys import argv
from time import sleep
from typing import List
from os import wait, fork

import beepy


class TimerObject:
    def __init__(self, start_time: str, label: tk.Label):
        self.start_time = datetime.strptime(start_time, '%H:%M:%S')
        self.timer_time = self.start_time
        self.zero = datetime.strptime('00:00:00', '%H:%M:%S')
        self.state = 1
        self.label = label

    def start_timer(self) -> datetime:
        if self.timer_time != self.zero and self.state == 1:
            self.timer_time -= timedelta(seconds=1)
            tvar = tk.StringVar()
            self.label.config(textvariable=tvar)
            tvar.set(self.timer_time.__format__('%H:%M:%S'))
            self.label.update()
            sleep(1)
            self.start_timer()
        elif self.timer_time == self.zero:
            beepy.beep(sound='success')
            return self.zero
        elif self.state == -1:
            return self.timer_time

    def skip_timer(self) -> None:
        self.state = -1


class CountdownTimers:
    def __init__(self, times: List[str]):
        self.times = times
        if len(times) > 15:
            self.error("tmt")
        self.timers: List[(TimerObject, tk.Label)] = []
        self.root = tk.Tk()
        self.root.geometry("300x75")
        self.create_timers()
        self.start()
        self.skipped = []
        self.root.mainloop()

    def start(self) -> None:
        timer = self.timers[0]
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(side=tk.RIGHT)
        skip = tk.Button(btn_frame, text="Skip", command=timer.skip_timer)
        skip.pack(side=tk.TOP)

        timer_return = timer.start_timer()
        if timer.state == -1:
            self.skipped.append(timer_return)
        timer.label.destroy()
        skip.destroy()
        del self.timers[0]
        self.root.update()
        if len(self.timers) > 0:
            self.root.after(0, self.start)
        else:
            ll = tk.Label(self.root, text="Timers finished!", font=("Arial", 20))
            ll.pack(padx=22, pady=22)
            sleep(3)
            self.root.destroy()
            exit(1)

    def create_timers(self) -> None:
        for time in self.times:
            time_var = tk.StringVar()
            label = tk.Label(self.root, textvariable=time_var, font=("Arial", 20))
            time_var.set(time)
            label.pack(padx=22, pady=22)
            self.timers.append(TimerObject(time, label))

    @staticmethod
    def error(error) -> None:
        if error == "tmt":
            raise ValueError("Too many timers")


class AlarmClock:
    def __init__(self, alarmtime: str):
        self.AlarmTime = alarmtime
        self.create_alarm()

    def create_alarm(self) -> None:
        while True:
            formatted = datetime.strptime(self.AlarmTime, '%H:%M')
            alarm_time = formatted.__format__('%H:%M')
            if alarm_time == datetime.now().strftime('%H:%M'):
                beepy.beep('success')
                break


if __name__ == '__main__':
    timers: List[str] = []
    sound: str = ''
    if argv[1] == "Configurations":
        with open("Configurations", 'r') as f:
            for line in f.readlines():
                if argv[2] in line:
                    timers += line.split(" ")[1:-1]
                    try:
                        sound = line.split(" ")[-1].split("=")[1]
                    except IndexError:
                        pass
        CountdownTimers(timers)
    else:
        CountdownTimers(argv[1:])
