import tkinter as tk
from tkinter.font import BOLD
import tkinter.messagebox as tkmessage


def cambio():
    if bottoneGA3['text'] =='GA3 OCCUPATA': 
        bottoneGA3['text'] = 'GA3 LIBERA'
        bottoneGA3['background'] = 'green'
        tkmessage.showwarning('*AVVERTIRE TORRE*','Si è appena liberata GA3, AVVERTIRE LA TORRE!')
    elif bottoneGA3['text'] =='GA3 LIBERA': 
        bottoneGA3['text'] = 'GA3 OCCUPATA'
        bottoneGA3['background'] = 'red'
        tkmessage.showwarning('*AVVERTIRE TORRE*','GA3 occupata, AVVERTIRE LA TORRE!')

window = tk.Tk()
w = 150  
h = 38 
window.maxsize(w,h)
screen_width = window.winfo_screenwidth() 
x = (screen_width) - w - 5
y = (0)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.iconbitmap('tower.ico')
window.wm_attributes('-topmost', 'True',)
window.wm_attributes('-toolwindow','True')
window.wm_overrideredirect(True)

frame=tk.Frame(master=window,
            width=90,
            height=40,
            bg="black")

frame.pack(fill=tk.BOTH, 
            expand=True)

bottoneGA3 = tk.Button(master=frame,
                text="GA3 LIBERA",
                background="black",
                foreground="white",
                command=cambio,
                font=('Calibri',13,BOLD)
                )

bottonechiusura = tk.Button(master=frame,
                       text ='X',
                       background="black",
                       foreground="white",
                       command=window.destroy,
                       font=('Calibri',13,BOLD)
                )

bottoneGA3.place(x=0,y=1)
bottonechiusura.place(x=130,y=1)
frame.mainloop()

