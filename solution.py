

import tkinter as tk
root = tk.Tk()
root.title("Lightweight Notes")
root.geometry("800x500")
root.configure(bg="#A9A9A9")

left_frame = tk.Frame(root, bg="#A9A9A9")
left_frame.pack(side="left", expand=True, fill="both", padx=40, pady=40)

# The Title box
title = tk.Entry(left_frame, font=("Arial", 18, "bold"), justify="center", bg="#EEEEEE")
title.insert(0, "TITLE")
title.pack(fill="x", pady=(0, 30))
for i in range(5):
    row = tk.Frame(left_frame, bg="#A9A9A9")
    row.pack(fill="x", pady=5)
   
    tk.Label(row, text="•", font=("Arial", 18), bg="#A9A9A9").pack(side="left")
   
    point = tk.Entry(row, font=("Arial", 12), bg="#A9A9A9", relief="flat")
    point.insert(0, "Points")
    point.pack(side="left", fill="x", expand=True, padx=5)
right_frame = tk.Frame(root, bg="white", highlightthickness=1, highlightbackground="black")
right_frame.pack(side="right", expand=True, fill="both", padx=40, pady=40)
summary = tk.Text(right_frame, font=("Arial", 12), bg="#EEEEEE", relief="flat", padx=10, pady=10)
summary.insert("1.0", "SUMMARY")
summary.pack(expand=True, fill="both", pady=(0, 20))

root.mainloop()