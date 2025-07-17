import tkinter as tk
from tkinter import messagebox
import pandas as pd
import datetime
import matplotlib.pyplot as plt

FILENAME = "mood_log.csv"
moods = ['Happy', 'Sad', 'Anxious', 'Excited', 'Tired', 'Neutral']

def save_mood():
    selected_mood = mood_var.get()
    if selected_mood == "":
        messagebox.showwarning("Warning", "Please select a mood!")
        return

    today = datetime.date.today()
    new_entry = pd.DataFrame([[today, selected_mood]], columns=["Date", "Mood"])

    try:
        df = pd.read_csv(FILENAME)
        df = pd.concat([df, new_entry], ignore_index=True)
    except:
        df = new_entry

    df.to_csv(FILENAME, index=False)
    messagebox.showinfo("Saved", f"Mood '{selected_mood}' saved successfully!")

def show_chart():
    try:
        df = pd.read_csv(FILENAME)
        mood_counts = df["Mood"].value_counts()
        mood_counts.plot(kind="bar", color="coral", title="Mood Frequency")
        plt.xlabel("Mood")
        plt.ylabel("Count")
        plt.show()
    except:
        messagebox.showerror("Error", "No mood data available!")

root = tk.Tk()
root.title("Daily Mood Tracker")
root.geometry("300x250")

tk.Label(root, text="How are you feeling today?", font=("Helvetica", 14)).pack(pady=10)

mood_var = tk.StringVar(value="")
mood_menu = tk.OptionMenu(root, mood_var, *moods)
mood_menu.pack(pady=10)

tk.Button(root, text="Submit", command=save_mood, width=15).pack(pady=5)
tk.Button(root, text="View Mood Chart", command=show_chart, width=15).pack(pady=5)

root.mainloop()
