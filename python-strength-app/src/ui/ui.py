import tkinter as tk
from csv import *
from ui.login_view import LoginView
from ui.create_new_user_view import CreateNewUserView
from ui.exercise_list_view import ExerciseListView
from ui.calendar_view import CalendarView
from ui.squat_view import SquatView
from ui.squat_data import SquatData
from ui.deadlift_view import DeadliftView
from ui.deadlift_data import DeadliftData
from ui.bench_press_view import BenchPressView
from ui.bench_press_data import BenchPressData
from ui.shoulder_press_view import ShoulderPressView
from ui.shoulder_press_data import ShoulderPressData
from ui.pull_up_view import PullUpView
from ui.pull_up_data import PullUpData


class UserInterface:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori, joka luo uuden käyttöliittymästä vastaavan luokan.
        Args:
            root:
                TKinter-elementti, joka vastaa Tkinter-ikkunasta.            
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._show_login_view()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän."""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _press_create_new_user(self):
        self._show_create_new_user_view()

    def _press_login(self):
        self._show_exercise_list_view()

    def _press_calendar(self):
        self._show_calendar_view()

    def _press_squat(self):
        self._show_squat_view()

    def _press_deadlift(self):
        self._show_deadlift_view()

    def _press_bench_press(self):
        self._show_bench_press_view()

    def _press_shoulder_press(self):
        self._show_shoulder_press_view()

    def _press_pull_up(self):
        self._show_pull_up_view()

    def _press_back_to_login(self):
        self._show_login_view()

    def _press_squat_data(self):
        self._show_squat_data()

    def _press_deadlift_data(self):
        self._show_deadlift_data()

    def _press_bench_press_data(self):
        self._show_bench_press_data()

    def _press_pull_up_data(self):
        self._show_pull_up_data()

    def _press_shoulder_press_data(self):
        self._show_shoulder_press_data()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._press_create_new_user,
            self._press_login,
        )

        self._current_view.pack()

    def _show_create_new_user_view(self):
        self._hide_current_view()

        self._current_view = CreateNewUserView(
            self._root,
            self._press_back_to_login
        )

        self._current_view.pack()

    def _show_exercise_list_view(self):
        self._hide_current_view()

        self._current_view = ExerciseListView(
            self._root,
            self._press_back_to_login,
            self._press_squat,
            self._press_deadlift,
            self._press_bench_press,
            self._press_shoulder_press,
            self._press_pull_up,
            self._press_calendar,
        )

        self._current_view.pack()

    def _show_calendar_view(self):
        self._hide_current_view()

        self._current_view = CalendarView(
            self._root,
            self._press_login
        )

        self._current_view.pack()

    def _show_squat_view(self):
        self._hide_current_view()

        self._current_view = SquatView(
            self._root,
            self._press_login,
            self._press_squat_data
        )

        self._current_view.pack()

    def _show_deadlift_view(self):
        self._hide_current_view()

        self._current_view = DeadliftView(
            self._root,
            self._press_login,
            self._press_deadlift_data
        )

        self._current_view.pack()

    def _show_bench_press_view(self):
        self._hide_current_view()

        self._current_view = BenchPressView(
            self._root,
            self._press_login,
            self._press_bench_press_data
        )

        self._current_view.pack()

    def _show_shoulder_press_view(self):
        self._hide_current_view()

        self._current_view = ShoulderPressView(
            self._root,
            self._press_login,
            self._press_shoulder_press_data
        )

        self._current_view.pack()

    def _show_pull_up_view(self):
        self._hide_current_view()

        self._current_view = PullUpView(
            self._root,
            self._press_login,
            self._press_pull_up_data
        )

        self._current_view.pack()

    def _show_squat_data(self):
        self._hide_current_view()

        self._current_view = SquatData(
            self._root,
            self._press_login,
        )

        self._current_view.pack()

    def _show_deadlift_data(self):
        self._hide_current_view()

        self._current_view = DeadliftData(
            self._root,
            self._press_login,
        )

        self._current_view.pack()

    def _show_bench_press_data(self):
        self._hide_current_view()

        self._current_view = BenchPressData(
            self._root,
            self._press_login,
        )

        self._current_view.pack()

    def _show_pull_up_data(self):
        self._hide_current_view()

        self._current_view = PullUpData(
            self._root,
            self._press_login,
        )

        self._current_view.pack()

    def _show_shoulder_press_data(self):
        self._hide_current_view()

        self._current_view = ShoulderPressData(
            self._root,
            self._press_login,
        )

        self._current_view.pack()
