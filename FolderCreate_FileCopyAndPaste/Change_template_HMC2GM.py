import os
import tkinter
import CAL_working.Cal__header_DirListUp

ErrMasterFileList=[]
PassMasterFileList=[]

ErrFileList = []
PassFileList = []
Dir = r'C:\Users\Mando\Desktop\FORD_CAL\IDB\WSLC\IDB_BRK'

SearchDir = CAL_working.Cal__header_DirListUp.DirList_Info()
DirList_BTC=SearchDir.search(Dir)


#print(DirList_BTC)



for Dirname in DirList_BTC:
    #print(Dirname)
    f = open(Dirname, 'r')

    lines = f.readlines()

    if '01' in Dirname:
       Firstlines = lines

       if "{" in Firstlines[23] :

           PassMasterFileList.append(Dirname)
       else:

           ErrMasterFileList.append(Dirname)






    #print(Firstlines)

    for k in range(0,9) :

        if "{" in lines[8]:

            PassFileList.append(Dirname)
        else:

            ErrFileList.append(Dirname)


        lines[k]=Firstlines[k]



    f.close()

    f = open(Dirname, 'w')
    #print(Dirname)
    dir, fname=os.path.split(Dirname)

    temp_name=fname.split('.h')


    temp_name =temp_name[0]

    i = 0
    for line in lines:

        i=i+1



        if '#ifndef' in line and i < 10:

            temp_line='#ifndef ' + temp_name.upper() + '_H_'+'\n'
            f.write(temp_line)
        elif '#define' in line and i < 10:

            temp_line = '#define ' + temp_name.upper() +'_H_'+ '\n'
            f.write(temp_line)
        else :
            f.write(line)







    f.close()

print(ErrFileList)
print(ErrMasterFileList)