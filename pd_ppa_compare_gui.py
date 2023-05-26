#!/raid/tools/Python/python-3.6.2/bin/python
print("""
####################################################################################################
## [Desc]    Compare PPA Data with JSON files : GUI Program
##   - Return: Image Chart / Graph / Histogram
## [Author] Jingu Lee (jingu.lee@lge.com)
## [Input] JSON files
## [History]
##      Author          Date         Description
##      Jingu.lee       2022.5.16.  Init. Release
####################################################################################################
""")

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import re, os
from glob import glob
import sys
import time
from   pathlib import Path

#########################################################
list = 'vt_group, power, timing, utilization, drc'
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import * # 파일 탐색창
import tkinter.ttk
import tkinter.font
import getpass # user name 가져오기

#----------------------------------------------------------------------

class MainWindow():

    #----------------
    
    def __init__(self, main):
        
        # canvas for image
        self.canvas = Canvas(main, width=60, height=60)
        self.canvas.grid(row=0, column=0)
        
        # images
        self.my_images = []
        self.my_images.append(PhotoImage(file="ball1.gif"))
        self.my_images.append(PhotoImage(file="ball2.gif"))
        self.my_images.append(PhotoImage(file="ball3.gif"))
        self.my_image_number = 0
        
        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.my_images[self.my_image_number])
        
        # button to change image
        self.button = Button(main, text="Change", command=self.onButton)
        self.button.grid(row=1, column=0)
        
    #----------------

    def onButton(self):
        
        # next image
        self.my_image_number += 1

        # return to first image
        if self.my_image_number == len(self.my_images):
            self.my_image_number = 0

        # change image
        self.canvas.itemconfig(self.image_on_canvas, image=self.my_images[self.my_image_number])

#----------------------------------------------------------------------

from tkinter import *
from tkinter import filedialog
def doAbout(window):
    filewin = Toplevel(window)
    filewin.config(background='lightgray')
    filewin.geometry("500x300+1200+100")
    # user_id = getpwuid(os.getuid()).pw_name
    user_id = getpass.getuser()

    about_explan = f"""
    LG Electronics. CTO SIC Center SDM TP
    버전 22M8(OS 빋드 19042.1110)
    ⓒ LG Electornics, Inc. All Right Reserved.

    Red Hat Enterprise Linux 운영 체제 및 해당 사용자 인터페이스는 미국, 대한민국 및 
    기타 여러 나라에서 상표권 및 출원 중이거나 등록된 지적 재산권에 의해 보호됩니다.

    이 제품은 LG Electornics 소프트웨어 사용 조건에 따라 다음 사용자가 사용할 수 
    있습니다.

    - {user_id}

    위 내용은 모두 Fake 입니다.
    
    """
    
    s = tkinter.ttk.Separator(filewin, orient=HORIZONTAL).pack(fill="both")
    
    message = Message(filewin,text=about_explan)
    message.config(width=500, anchor='nw',background='lightgray',foreground="black") # relief 테두리 모양 / foreground 문자열 색 / background 배경색상
    message.pack(side='top',anchor='nw',padx=0)
    
    s = tkinter.ttk.Separator(filewin, orient=HORIZONTAL).pack(fill="both")
    
    button = Button(filewin, text="   확인   ",command=lambda :filewin.destroy())
    button.config(background='lightgray',foreground="black")
    button.pack(side='top',anchor="ne",padx=10,pady=10)

#global dir_path
def Load():
    global dir_path
#    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
#                                          filetypes=(("PPTX files", "*.pptx"), ("all files", "*.*")))
    dir_path = filedialog.askdirectory(initialdir="./",title='Please select a directory')
    print(dir_path)
    return dir_path


def Save():
    filename = filedialog.asksaveasfilename(initialdir="./", title="Select file",
                                          filetypes=(("PPTX files", "*.pptx"), ("all files", "*.*")))
    print(filename)

def domenu():
#    global dir_path
    print("OK")
def CrMenu(root):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    editmenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=editmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)


    filemenu.add_command(label="New", command=domenu)
    filemenu.add_command(label="Open", command=Load)
    # filemenu.add_command(label="Save", command=Save)
    # filemenu.add_command(label="Save as...", command=Save)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    # editmenu.add_command(label="Copy", command=domenu)
    # editmenu.add_command(label="Paste", command=domenu)
    # editmenu.add_separator()
    # editmenu.add_command(label="Delete", command=domenu)

    helpmenu.add_command(label="About...", command=domenu)
    root.config(menu=menubar)

def CrTab(window):
    pass
# getpwuid(os.getuid()).pw_name 리눅스 에서만 먹히는 커맨드

### class generation session #############################
class PPACompareGUI:
    def __init__(self,Parent) -> None:
        # self.Frame = Frame(Parent)
        # self.Frame.pack()
        self.notebook = tkinter.ttk.Notebook(Parent)
        self.notebook.pack()



class Category:
    pass
class StageSelection:
    pass
class OpenDir:
    pass
class ChartVtGroup:
    pass

### Default Setup #########################################################
windowWidth  = 1000
windowHeight = 700

windowGeometry = f"{windowWidth}x{windowHeight}-1920+10"
windowTitle    = "SDM TP Physical Implementation PPA Compare GUI"

### window Generation ##############################################################
window = Tk()
window.geometry(windowGeometry) # Program SIZE Setup
window.title(windowTitle)
### notebook 을 이용하여 페이지를 나눌 수 있다. ########################################
font=tkinter.font.Font(family='courier new', size=9) # 리눅스에서 보기에 괜찮아보임 / Tk() 선언하고 생성하여야함
### Notebook SIZE
notebook=tkinter.ttk.Notebook(window, width=windowWidth - 20, height=windowHeight - 10)
notebook.pack()

#####################################################################################
CrMenu(window)

#####################################################################################

window.mainloop()






# root = Tk()
# MainWindow(root)
# root.mainloop()
