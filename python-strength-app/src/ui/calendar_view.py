import tkinter as tk
from tkcalendar import *
from services.user_service import user_service
import datetime
from file_reader import squat_file_path, deadlift_file_path, bench_press_file_path, shoulder_press_file_path, pull_up_file_path
from repositories.exercise_repository import ExerciseRepository


class CalendarView:
    """Kalenterista vastaava näkymä."""

    def __init__(self, root, press_login):
        """Luokan konstruktori. Luo kalenterinäkymän.

        Args:
            root:
                TKinter-elementti, joka vastaa Tkinter-ikkunasta.
            press_login:
                Kutsuttava arvo, jolla siirrytään takaisin sovelluksen harjoituslistanäkymään.
        """
        self._root = root
        self._frame = None
        self._user = user_service.get_user()
        self._squat_file_path = squat_file_path
        self._deadlift_file_path = deadlift_file_path
        self._bench_press_file_path = bench_press_file_path
        self._shoulder_press_file_path = shoulder_press_file_path
        self._pull_up_file_path = pull_up_file_path
        self._user_data = ExerciseRepository()._user_data
        self._press_login = press_login
        self.squat_dates = []
        self.max_squat_weight = 0
        self.max_deadlift_weight = 0
        self.deadlift_dates = []
        self.max_bench_press_weight = 0
        self.bench_press_dates = []
        self.max_shoulder_press_weight = 0
        self.shoulder_press_dates = []
        self.max_pull_up_weight = 0
        self.pull_up_dates = []
        ExerciseRepository.read_squat(self)
        ExerciseRepository.read_deadlift(self)
        ExerciseRepository.read_bench_press(self)
        ExerciseRepository.read_shoulder_press(self)
        ExerciseRepository.read_pull_up(self)
        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=tk.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)

        back_button = tk.Button(
            master=self._frame, text="BACK TO EXERCISE LIST", command=self._press_login)
        back_button.pack(pady=10)

        colour_text = tk.Label(
            master=self._frame, text="The days you have been training are coloured in green.")
        colour_text.pack(side=tk.TOP, anchor=tk.NW)

        my_calendar = Calendar(master=self._frame)
        my_calendar.pack(pady=10)

        for date in self.squat_dates:
            my_calendar.calevent_create(datetime.datetime.strptime(
                date, '%d.%m.%Y'), "", tags="training day")
            my_calendar.tag_config("training day", background="green")

        for date in self.deadlift_dates:
            my_calendar.calevent_create(datetime.datetime.strptime(
                date, '%d.%m.%Y'), "", tags="training day")
            my_calendar.tag_config("training day", background="green")

        for date in self.bench_press_dates:
            my_calendar.calevent_create(datetime.datetime.strptime(
                date, '%d.%m.%Y'), "", tags="training day")
            my_calendar.tag_config("training day", background="green")

        for date in self.shoulder_press_dates:
            my_calendar.calevent_create(datetime.datetime.strptime(
                date, '%d.%m.%Y'), "", tags="training day")
            my_calendar.tag_config("training day", background="green")

        for date in self.pull_up_dates:
            my_calendar.calevent_create(datetime.datetime.strptime(
                date, '%d.%m.%Y'), "", tags="training day")
            my_calendar.tag_config("training day", background="green")
