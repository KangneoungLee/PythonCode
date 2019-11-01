import re

def ContentChnage(Dirnames,OldName_List_local,NewName_List_local):


    print(OldName_List_local)
    print(NewName_List_local)

    for Dirname in Dirnames :

        f=open(Dirname,'r')

        lines = f.readlines()
        f.close()


        f = open(Dirname, 'w')
        for line in lines :

           Compare_Result_List=[]
           temp_line = line



           if len(OldName_List_local) == 1:
              Compare_Result_List.append(1)
              Compare_Ok = 1
           else:
                 i= 0
                 Compare_Ok = 0
                 for i in range(1,len(OldName_List_local)+1):


                    if temp_line.find(OldName_List_local[i-1]) != -1 :
                      Compare_Result_List.append(i)
                      Compare_Ok = 1


           if Compare_Ok == 1:

              index_temp=Compare_Result_List[0]

              print(Compare_Result_List[0])

              f.write(temp_line.replace(OldName_List_local[index_temp - 1], NewName_List_local[index_temp - 1]))

           else:

               f.write(line)



        f.close()

