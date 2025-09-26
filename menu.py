import tkinter as tk

class main_window(tk.Tk):
    def __init__(self, i_title):
        super().__init__()
        self.title(i_title)
        self.geometry("800x600")

class linear_search_window(tk.Tk):
    def __init__(self, arr = []):
        self.arr =  arr
        super().__init__()
        self.title("Linear Search")
        self.geometry("800x600")
        


if __name__ == "__main__":
    root = main_window("Sup")

    test = Label(root, "test").grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    root.mainloop()

