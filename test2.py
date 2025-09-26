import time
import tkinter as tk

root = tk.Tk()
root.title("Linear search")
root.geometry("800x600")

def iterate_array(index = 0):
        if index < 5:
            canv.itemconfig(rect_arr[index], fill="yellow", font=("Arial", 34, "bold"))
            root.after(500, iterate_array, index+1)


def linear_search(val, index = 0):
    if index == 5:
        canv.create_text(400, 400, text="Entry not found", font=("Arial", 34 ))
    elif arr[index] == val:
        canv.create_text(400, 400, text="Entry found", font=("Arial", 34 ))
        canv.itemconfig(rect_arr[index], fill="green")
    else:
        canv.itemconfig(rect_arr[index], fill="yellow")
        root.after(500, linear_search, val, index+1)
         
         

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky= (tk.N, tk.W, tk.E, tk.S))

canv =  tk.Canvas(main_frame, width=800, height = 600, bg = "white")
canv.grid(row=0, column=0)

linear_search_window = tk.Toplevel(root)
arr = [1,4,5,9,3]

rect_arr = list()

for i,v in enumerate(arr):

    rect_arr.append(canv.create_rectangle((i)*100 + 20, 200, (i)*100 + 100,300, fill= "lightblue", outline = "black"))
    canv.create_text(((i)*100 + 60), 250 , text = v)
canv.pack()





print(rect_arr)
linear_search(11)
root.mainloop()





