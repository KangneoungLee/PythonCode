import os
import tkinter
import tkinter.messagebox
import CAL_working.CAL_workCP

global ESCcheckVariety, IDBcheckVariety
global Dir
global Dir_Emidas_header
global BRK_CAL_FOLDER_LIST, ENG_CAL_FOLDER_LIST

def StartbuttonClick(event):

    global Dir
    global BRK_CAL_FOLDER_LIST, ENG_CAL_FOLDER_LIST
    Dir = Dir_For_CalFolder_Creat.get()

    if ESCcheckVariety.get() ==1 and IDBcheckVariety.get() ==0:
        CAL_FOLDER_LIST = ['AUTOBRKCOORR', 'AWDCTRLR', 'BRKASSISCOORR', 'BRKTQCTRLR', 'COMMON', 'ELECVACPMP', 'ESTMR',
                           'LATDYNSCOORR', 'LOWPCOORR', 'RGNBRKCTRLR', 'SIGPROCR', 'SSM', 'STRSTABYCTRL', 'VEHLGTCOORR',
                           'WSLC', 'WSPC']
        BRK_CAL_FOLDER_LIST = ['AUTOBRKCOORR', 'BRKASSISCOORR', 'BRKTQCTRLR', 'COMMON', 'ELECVACPMP', 'ESTMR',
                               'LATDYNSCOORR', 'LOWPCOORR', 'RGNBRKCTRLR', 'SIGPROCR', 'SSM', 'STRSTABYCTRL',
                               'VEHLGTCOORR', 'WSLC']
        ENG_CAL_FOLDER_LIST = ['AUTOBRKCOORR', 'AWDCTRLR', 'BRKASSISCOORR', 'COMMON', 'SIGPROCR', 'SSM', 'VEHLGTCOORR',
                               'WSLC', 'WSPC']

    elif IDBcheckVariety.get() ==1 and ESCcheckVariety.get() ==0:
        CAL_FOLDER_LIST = ['AUTOBRKCOORR', 'AWDCTRLR', 'BRKASSISCOORR', 'COMMON', 'ESTMR',
                           'LATDYNSCOORR', 'LOWPCOORR', 'SIGPROCR', 'SSM', 'STRSTABYCTRL', 'VEHLGTCOORR',
                           'WSLC', 'WSPC']
        BRK_CAL_FOLDER_LIST = ['AUTOBRKCOORR', 'BRKASSISCOORR', 'COMMON', 'ESTMR',
                               'LATDYNSCOORR', 'LOWPCOORR', 'SIGPROCR', 'SSM', 'STRSTABYCTRL',
                               'VEHLGTCOORR', 'WSLC']
        ENG_CAL_FOLDER_LIST = ['AUTOBRKCOORR', 'AWDCTRLR', 'BRKASSISCOORR', 'COMMON', 'SIGPROCR', 'SSM', 'VEHLGTCOORR',
                               'WSLC', 'WSPC']
    elif IDBcheckVariety.get() ==1 and ESCcheckVariety.get() ==1:
        tkinter.messagebox.showwarning("Warning","Only one system should be selected")
        return
    else :
        tkinter.messagebox.showwarning("Warning", "System should be selected")
        return

    for i in CAL_FOLDER_LIST:

         Upper_Dir = Dir + "/" + i

         if not os.path.isdir(Upper_Dir):
             os.mkdir(Upper_Dir)



         if i in BRK_CAL_FOLDER_LIST:
            Brk_lower_Dir = Upper_Dir + "/" + "BRK"

            if not os.path.isdir(Brk_lower_Dir):
                os.mkdir(Brk_lower_Dir)


         if i in ENG_CAL_FOLDER_LIST:
             Eng_lower_Dir = Upper_Dir + "/" + "ENG"

         if not os.path.isdir(Eng_lower_Dir):
             os.mkdir(Eng_lower_Dir)




def CopyAndPasteStart(event):


   DIR_PASTE= Dir_For_CalFolder_Creat.get()
   ESC_OK=ESCcheckVariety.get()
   IDB_OK=IDBcheckVariety.get()
   DIR_COPY=Dir_Emidas_header.get()

   CopyP=CAL_working.CAL_workCP
   CopyP.Execute(ESC_OK,IDB_OK,DIR_COPY,DIR_PASTE,BRK_CAL_FOLDER_LIST,ENG_CAL_FOLDER_LIST)



window = tkinter.Tk()
window.title("KangNeoung")
window.geometry("600x400+100+100")
window.resizable(True,True)

lbl = tkinter.Label(window,text="CAL Folder 생성 경로")
lbl.place(x=100, y=20)

Dir_For_CalFolder_Creat=tkinter.Entry(window)
Dir_For_CalFolder_Creat.place(x=140, y=40, width =300)



lbl_2 = tkinter.Label(window,text="emidas 헤더파일 추출 경로")
lbl_2.place(x=100, y=60)

Dir_Emidas_header=tkinter.Entry(window)
Dir_Emidas_header.place(x=140, y=80, width =300)


Startbutton=tkinter.Button(window,text="폴더생성")
Startbutton.place(x=60, y=360)
Startbutton.bind("<Button-1>",StartbuttonClick)

ESCcheckVariety = tkinter.IntVar()
IDBcheckVariety = tkinter.IntVar()


ESCcheckbutton = tkinter.Checkbutton(window,text="ESC",variable=ESCcheckVariety,activebackground="blue")
ESCcheckbutton.place(x=50,y=50)
IDBcheckbutton = tkinter.Checkbutton(window,text="IDB",variable=IDBcheckVariety,activebackground="blue")
IDBcheckbutton.place(x=50,y=70)


CopyAndPastebutton=tkinter.Button(window,text="CAL헤더복사붙여넣기")
CopyAndPastebutton.place(x=60, y=330)
CopyAndPastebutton.bind("<Button-1>",CopyAndPasteStart)




window.mainloop()