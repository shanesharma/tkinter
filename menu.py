import tkinter as tk

class App(tk.Tk):
    def __init__(self, i_title, **kwargs):
        super().__init__()
        self.title(i_title)
        self.geometry("800x600")

        lin_arr = kwargs.pop("lin_arr", [] )
        lin_window = linear_search_window(self, lin_arr)
        


    

class linear_search_window(tk.Toplevel):
    def __init__(self,parent, arr = []):
        self.arr =  arr
        super().__init__(parent)
        self.title("Linear Search")
        self.geometry("800x600")
        self.frame = tk.Frame(self)
        linear_canvas = array_canvas(self.frame,self.arr)
        linear_canvas.pack()
        self.frame.pack()




class array_canvas(tk.Canvas):
    def __init__(self, parent, arr = []):
        super().__init__(parent, width=800, height=600, bg= "white")
        self.rectangleArray = list()
        size_list = len(arr)
        win_height = 600
        win_width = 800
        box_height = 60
        gap = (win_width - size_list*80)/(size_list+1)


        for i,v in enumerate(arr):
            self.rectangleArray.append(self.create_rectangle(gap + i * (80 + gap), (win_height-box_height)/2, gap + i * (80 + gap) + 80,(win_height+box_height)/2, fill= "lightblue", outline = "black"))
            self.create_text((gap + i * (80 + gap) + 40), (win_height/2) , text = v)
            self.grid(row=0, column=0)
        self.pack()
    def get_canvas_array(self):
        return self.rectangleArray
        


if __name__ == "__main__":
    root = App("Sup", lin_arr = [1,2,3,4])

    root.mainloop()

