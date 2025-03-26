from tkinter import *
import settings
import utils
from cell import Cell


root=Tk()
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.configure(bg="black")
root.title('Minesweeper Game X Bimal')
root.resizable(False,False)

Top_frame=Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_per(25)
)
Top_frame.place(x=0,y=0)
Left_frame=Frame(
    root,
    bg='black',
    width=utils.width_per(25),
    height=utils.height_per(75)

)
Left_frame.place(x=0,y=utils.height_per(25))
Center_frame=Frame(
    root,
    bg='black',
    width=utils.width_per(75),
    height=utils.height_per(75)
)
Center_frame.place(
    x=utils.width_per(25),
    y=utils.height_per(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c=Cell(x , y)
        btn=c.create_btn_object(Center_frame)
        c.cell_btn_object.grid(
            row=x,
            column=y,
        )
       


Cell.randomize_mines()
Cell.create_cell_count_label(Left_frame)
Cell.cell_count_label_object.place(
    x=0,
    y=0
)
game_title=Label(
    Top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('',33)
)
game_title.place(
    x=utils.width_per(25),
    y=50
)


root.mainloop()