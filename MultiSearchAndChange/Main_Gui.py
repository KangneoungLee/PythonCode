import tkinter

import Main_Gui_class
import File_Listup
import ContentFind_Change

Entry_OldName=[]
Entry_NewName=[]
OldName_List=[]
NewName_List=[]
NumofClick = 0

def AddbuttonClick(event):

    global NumofClick


    Entry_Old_name_temp=tkinter.Entry(window)
    Entry_New_name_temp = tkinter.Entry(window)
    NumofClick =  NumofClick+1
    Entry_OldName.append(Entry_Old_name_temp)
    Entry_OldName[NumofClick-1].place(x=150, y=60 + 30 * NumofClick)

    Entry_NewName.append(Entry_New_name_temp)
    Entry_NewName[NumofClick - 1].place(x=350, y=60 + 30 * NumofClick)





def StartbuttonClick(event):

    global OldName_List
    global NewName_List

    for i in range(1,len(Entry_OldName)+1):
        OldName_List.append(Entry_OldName[i - 1].get())
        NewName_List.append(Entry_NewName[i - 1].get())

    Dir = Direntry.get()

    SearchDir = File_Listup.DirList_Info()
    b = SearchDir.search(Dir)
    ContentFind_Change.ContentChnage(b,OldName_List,NewName_List)

    print(Dir)
    print(type(Dir))





window = tkinter.Tk()
window.title("KangNeoung")
window.geometry("600x400+100+100")
window.resizable(True,True)

lbl = tkinter.Label(window,text="경로")
lbl.place(x=100, y=20)

Direntry=tkinter.Entry(window)
Direntry.place(x=140, y=20, width =300)




OldNamelbl=tkinter.Label(window,text="OldName")
OldNamelbl.place(x=200, y=60)
NewNamelbl=tkinter.Label(window,text="NewName")
NewNamelbl.place(x=400, y=60)

Addbutton=tkinter.Button(window,text="항목추가")
Addbutton.place(x=60, y=60)

Addbutton.bind("<Button-1>",AddbuttonClick)


Startbutton=tkinter.Button(window,text="시작")
Startbutton.place(x=60, y=360)
Startbutton.bind("<Button-1>",StartbuttonClick)


window.mainloop()