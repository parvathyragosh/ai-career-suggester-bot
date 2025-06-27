import tkinter as tk
from tkinter import messagebox

# Function to suggest career
def suggest_career():
    interest = entry_interest.get().lower()
    skill = entry_skill.get().lower()
    
    # Example simple logic
    if "data" in interest and "python" in skill:
        result = "You might enjoy a career as a Data Scientist."
    elif "design" in interest:
        result = "Consider becoming a UI/UX Designer."
    else:
        result = "Explore more to find your perfect AI career path!"

    messagebox.showinfo("Career Suggestion", result)

# GUI window
window = tk.Tk()
window.title("AI Career Suggester Bot")
window.geometry("400x300")

# Widgets
tk.Label(window, text="Enter your interest:").pack(pady=5)
entry_interest = tk.Entry(window, width=30)
entry_interest.pack()

tk.Label(window, text="Enter your primary skill:").pack(pady=5)
entry_skill = tk.Entry(window, width=30)
entry_skill.pack()

tk.Button(window, text="Suggest Career", command=suggest_career).pack(pady=20)

window.mainloop()
