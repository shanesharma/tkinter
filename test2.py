import time
import tkinter as tk

root = tk.Tk()
root.title("Alg functions")
root.geometry("800x600")

win_width = 800
win_height = 600
box_height = 60
'''
TODO
    1. add more buttons
    2. divide buttons into files
    3. Dynamically size the boxes as only 12 boxes can fit on screen


'''


default_font = ("Arial", 34)
default_frame_grid = dict(row = 0, column= 0, sticky=(tk.N, tk.S, tk.E, tk.W))

def iterate_array(low, high, target):
        if low > high:
            canv.create_text(400, 400, text="Entry not found", font=default_font)
            return
        mid = (low + high)//2
        if bin_search_arr[mid] == target:
                canv.create_text(400, 400, text="Entry found", font=default_font)
                canv.itemconfig(rect_arr2[mid], fill="green")
        elif bin_search_arr[mid]> target:
                canv.itemconfig(rect_arr2[mid], fill="yellow")
                root.after(500, iterate_array, 0, mid-1, target )
        else:
                canv.itemconfig(rect_arr2[mid], fill="yellow")
                root.after(500, iterate_array, mid+1, high, target )
             



def linear_search(val, index = 0):
    if index == len(linear_arr):
        canv.create_text(400, 400, text="Entry not found", font=default_font)
    elif linear_arr[index] == val:
        canv.create_text(400, 400, text="Entry found", font=default_font)
        canv.itemconfig(rect_arr[index], fill="green")
    else:
        canv.itemconfig(rect_arr[index], fill="yellow")
        root.after(500, linear_search, val, index+1)
         
         
def create_lin_window():
     linear_search_window = tk.Toplevel(root)
     linear_search_frame  = tk.Frame(linear_search_window)
     linear_search_frame.grid( row = 0, column= 0, sticky=(tk.N, tk.S, tk.E, tk.W))
     global canv
     global linear_arr
     global rect_arr
     canv =  tk.Canvas(linear_search_frame, width=800, height = 600, bg = "white")
     canv.grid(row=0, column=0)
     
     linear_arr = [1,4,5,9,3,7,21,35]

     rect_arr = list()
     size_list = len(linear_arr)
     gap = (win_width - size_list*80)/(size_list+1)
     for i,v in enumerate(linear_arr):
          

        rect_arr.append(canv.create_rectangle(gap + i * (80 + gap), (win_height-box_height)/2, gap + i * (80 + gap) + 80,(win_height+box_height)/2, fill= "lightblue", outline = "black"))
        canv.create_text((gap + i * (80 + gap) + 40), (win_height/2) , text = v)
        canv.grid(row=0, column=0)
    
     linear_search(11)
        

if __name__ == "__main__":
    main_frame = tk.Frame(root)
    main_frame.grid(row=0, column=0, sticky= (tk.N, tk.W, tk.E, tk.S))

    binary_search_window = tk.Toplevel(root)
    binary_search_frame = tk.Frame(binary_search_window)
    binary_search_frame.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    canv =  tk.Canvas(binary_search_frame, width=800, height = 600, bg = "white")
    canv.grid(row=0, column=0)
    



    linear_search_button = tk.Button(main_frame, text = "Linear Search", command= create_lin_window)
    linear_search_button.grid(row=0, column=0)
    bin_search_arr = [1,2,3,4,5,6,7,8,9]
   
    size_list = len(bin_search_arr)
    rect_arr2 = list()
    gap = (win_width - size_list*80)/(size_list+1)
    for i,v in enumerate(bin_search_arr):
          

        rect_arr2.append(canv.create_rectangle(gap + i * (80 + gap), (win_height-box_height)/2, gap + i * (80 + gap) + 80,(win_height+box_height)/2, fill= "lightblue", outline = "black"))
        canv.create_text((gap + i * (80 + gap) + 40), (win_height/2) , text = v)
        canv.grid(row=0, column=0)

    binary_search_button = tk.Button(main_frame, text = "Binary Search")

    


    binary_search_button.grid(row=0, column=1)
    

    iterate_array(0, size_list-1, 0)
    root.mainloop()





