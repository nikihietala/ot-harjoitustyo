import tkinter as tk
from csv import *
from tkinter import messagebox
import datetime
import re
from file_reader import shoulder_press_file_path
from services.user_service import user_service


class ShoulderPressView:
    """Uuden pystypunnerrus-tuloksen lisäämisestä vastaava näkymä."""

    def __init__(self, root, press_login, press_shoulder_press_data):
        """Luokan konstruktori. Luo pystypunnerrus-tuloksen lisäämisnäkymän.

        Args:
            root:
                TKinter-elementti, joka vastaa Tkinter-ikkunasta.
            press_login:
                Kutsuttava arvo, jolla siirrytään takaisin sovelluksen harjoituslistanäkymään.
            press_shoulder_press_data:
                Kutsuttava arvo, jolla siirrytään pystypunnerrus-tulosten katselunäkymään.
        """
        self._root = root
        self._frame = None
        self._user = user_service.get_user()
        self._press_login = press_login
        self._press_shoulder_press_data = press_shoulder_press_data
        self._shoulder_press_file_path = shoulder_press_file_path
        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=tk.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = tk.Frame(master=self._root)

        shoulder_press_text = tk.Label(master=self._frame,
                                       text="New Shoulder Press", font=("Arial", 14, "bold"))
        shoulder_press_text.pack(side=tk.TOP, pady=1)

        date_text = tk.Label(master=self._frame, text="Date (day.month.year)")
        date_text.pack(pady=2)

        self._date_entry = tk.Entry(master=self._frame)
        self._date_entry.pack(fill=tk.X)

        rep_text = tk.Label(master=self._frame, text="Best rep(amount)")
        rep_text.pack(pady=2)

        self._rep_entry = tk.Entry(master=self._frame)
        self._rep_entry.pack(fill=tk.X)

        weight_text = tk.Label(master=self._frame, text="Weight (kg)")
        weight_text.pack(pady=2)

        self._weight_entry = tk.Entry(master=self._frame)
        self._weight_entry.pack(fill=tk.X)

        write_button = tk.Button(
            master=self._frame, text="SAVE RESULT", command=self._write_to_file)
        write_button.pack(pady=10)

        shoulder_press_data_button = tk.Button(
            master=self._frame, text="PAST RESULTS", command=self._press_shoulder_press_data)
        shoulder_press_data_button.pack(pady=10)

        back_button = tk.Button(
            master=self._frame, text="BACK TO EXERCISE LIST", command=self._press_login)
        back_button.pack(pady=10)

    def _write_to_file(self):
        """Kirjoittaa käyttäjän kirjoittaman tuloksen ylös shoulder_press.csv tiedostoon."""
        confirmation = messagebox.askquestion("Confirm", "You are about to enter the following data\n" + "Date: " + self._date_entry.get(
        ) + "\n" + "Best Rep: " + self._rep_entry.get() + "\n" + "Weight: " + self._weight_entry.get())
        allowed = re.compile(r"[0-9]+")
        if confirmation == 'yes':
            try:
                datetime.datetime.strptime(self._date_entry.get(), '%d.%m.%Y')
            except ValueError:
                messagebox.showerror(
                    "Error", "Date has to be in format day.month.year (E.g. 5.4.2022)")
                return
            if not re.fullmatch(allowed, self._weight_entry.get()):
                messagebox.showerror(
                    "Error", "Weight has to be a positive number (E.g. 80), round to nearest whole number")
                return
            if not re.fullmatch(allowed, self._rep_entry.get()):
                messagebox.showerror(
                    "Error", "Best rep has to be a positive number (E.g. 5)")
                return
            with open(self._shoulder_press_file_path, "a", newline='') as file:
                Writer = writer(file)
                Writer.writerow([self._date_entry.get(), self._rep_entry.get(
                ) + " reps", self._weight_entry.get() + " kg", self._user.username])
            messagebox.showinfo("Success", "Result saved!")
        else:
            messagebox.showerror("Cancel", "Result not saved")
            return
