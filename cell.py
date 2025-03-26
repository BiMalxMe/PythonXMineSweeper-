from tkinter import Button,Label
import random
import settings
import ctypes
import sys


class Cell:
    all=[]
    cell_count=settings.CELL_SIZE
    cell_count_label_object=None
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.is_opened=False
        self.cell_btn_object=None
        self.x=x
        self.y=y
        self.is_mine_candidate=False
        
        Cell.all.append(self)
    
    def create_btn_object(self,Location):
            btn=Button(
                 Location,
                 width=12,
                 height=4
               
     )
            btn.bind('<Button-1>',self.left_click)
            btn.bind('<Button-3>',self.right_click)
            self.cell_btn_object=btn
    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(
            location,
            bg='black',
            fg='white',
            text=f"Cell Count:{settings.CELL_SIZE}",
            width=12,
            height=4,
            font=("",25)
        )
        Cell.cell_count_label_object=lbl
        
        
    def left_click(self,event):
          if self.is_mine:
               self.show_mine()
          else:
               if self.surrounded_cells_mines_length==0:
                  for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()                     
               self.show_cell()
               #if mines count is equal to lefc cell count player wins
               if self.cell_count==settings.MINES_COUNT:
                         ctypes.windll.user32.MessageBoxW(0,'Congratulations!','You won',0)
                         sys.exit()
          self.cell_btn_object.unbind('<Button-1>')
          self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self,x,y):
         for cell in Cell.all:
              if cell.x==x and cell.y==y:
                   return cell
    @property          
    def surrounded_cells(self):
        cells=[
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1)

            ]
            # #filtering out none
      # cells = list(filter(None, cells)) # # can write this also
        cells =[cell for cell in cells if cell is not None]
        return cells
         

    def show_cell(self):
          if not self.is_opened:
               Cell.cell_count-=1
               self.cell_btn_object.config(text=self.surrounded_cells_mines_length)
               if Cell.cell_count_label_object:
                    Cell.cell_count_label_object.config(
                         text=f"Cell Count:{Cell.cell_count}"                        
                         )
          #Mark this cell as opened already
               self.cell_btn_object.configure(
                    bg='systembuttonface'
               )
          self.is_opened=True
          
    @property
    def surrounded_cells_mines_length(self):
        counter=0 
        for cell in self.surrounded_cells:
             if cell.is_mine:
                  counter+=1
        return counter
        print(counter)

         
  


    def show_mine(self):
         #A logic to put the background into red if its a mine
         self.cell_btn_object.configure(bg='red')
         ctypes.windll.user32.MessageBoxW(0,'You clicked on Mine','Game over',0)
         sys.exit()


    def right_click(self,event):
          if not self.is_mine_candidate:
               self.cell_btn_object.configure(
                   bg='Orange'
              )
               self.is_mine_candidate=True
          else:
               self.cell_btn_object.configure(
                    bg='systembuttonface'
               )
               self.is_mine_candidate=False

    @staticmethod
    def randomize_mines():#randomly picking cells from the list
        picked_cells=random.sample(
             Cell.all,
             settings.MINES_COUNT             
             )
        for picked_cell in picked_cells:
            picked_cell.is_mine=True
    def __repr__(self):
         return f'Cell({self.x},{self.y})'
        