import tkinter as tk

file = "config.txt"


root = tk.Tk()
root.title("pounds to kg")

def calculate(*args):
    try:
        value = float(pounds.get())
        kilograms.set(round(value / 2.205,3))
    except ValueError:
        pass

frame = tk.Frame(root, padx=100, pady=100)
frame.configure(width=1200, height = 1200)
frame.grid(sticky=(tk.N, tk.W, tk.E, tk.S))


pounds = tk.StringVar()
pounds_box = tk.Entry(frame, textvariable=pounds)
pounds_box.grid(row=0, column=1, sticky=(tk.N, tk.W, tk.E, tk.S))


kilograms = tk.StringVar()
kilograms_box = tk.Entry(frame, textvariable=kilograms)
kilograms_box.grid(row = 1, column=1, sticky=(tk.N, tk.W, tk.E, tk.S))



tk.Label(frame, text="is equivalent to").grid(row = 1, column=0)
tk.Label(frame, text = "Pounds").grid(row=0, column=2)
tk.Label(frame, text="Kilograms").grid(row=1, column=2)

tk.Button(frame, text="Calculate", command=calculate).grid(row=2, column=2)

with open(file, "w") as f:
    f.write(str(frame.configure()))


pounds_box.focus()
root.bind("<Return>", calculate)
root.mainloop()
