import shutil
import os


class CalHdirList_Info:
    def __init__(self):
        self.CalHdirList = []

    def search(self, dirname):
        self.CalHdirList = os.listdir(dirname)



        return self.CalHdirList


def Execute(ESC_OK,IDB_OK,DIR_COPY,DIR_PASTE,BRK_CAL_FOLDER_LIST,ENG_CAL_FOLDER_LIST):

    if ESC_OK == 1 and IDB_OK == 0:
       BRK_HEADER_NAME_LIST = ['AutoBrkCoorr_BrkCal', 'BrkAssisCoorr_BrkCal', 'BrkTqCtrlr_BrkCal', 'Common_BrkCal',
                                'ElecVacPmp_BrkCal', 'Estmr_BrkCal', 'LatDynsCoorr_BrkCal', 'LowPCoorr_BrkCal',
                                'RgnBrkCtrlr_BrkCal', 'SigProcr_BrkCal', 'Ssm_BrkCal', 'StrStabyCtrl_BrkCal',
                                'VehLgtCoorr_BrkCal', 'Wslc_BrkCal']
       ENG_HEADER_NAME_LIST = ['AutoBrkCoorr_EngCal','AwdCtrlr_EngCal','BrkAssisCoorr_EngCal','Common_EngCal','SigProcr_EngCal','Ssm_EngCal','VehLgtCoorr_EngCal','Wslc_EngCal','Wspc_EngCal']

    if ESC_OK == 0 and IDB_OK == 1:
        BRK_HEADER_NAME_LIST = ['AutoBrkCoorr_BrkCal', 'BrkAssisCoorr_BrkCal', 'Common_BrkCal',
                                 'Estmr_BrkCal', 'LatDynsCoorr_BrkCal', 'LowPCoorr_BrkCal',
                                 'SigProcr_BrkCal', 'Ssm_BrkCal', 'StrStabyCtrl_BrkCal',
                                'VehLgtCoorr_BrkCal', 'Wslc_BrkCal']
        ENG_HEADER_NAME_LIST = ['AutoBrkCoorr_EngCal', 'AwdCtrlr_EngCal', 'BrkAssisCoorr_EngCal', 'Common_EngCal',
                                'SigProcr_EngCal', 'Ssm_EngCal', 'VehLgtCoorr_EngCal', 'Wslc_EngCal', 'Wspc_EngCal']



    SearchDir=CalHdirList_Info()
    Listedfile=SearchDir.search(DIR_COPY)
    for file_identifier in BRK_HEADER_NAME_LIST :

       List_index=BRK_HEADER_NAME_LIST.index(file_identifier)
       print(file_identifier)

       for file_name in Listedfile :

           if file_identifier in file_name :

               Copy_file_full_directory = DIR_COPY + "/" + file_name
               Paste_file_full_directory = DIR_PASTE + "/"+ BRK_CAL_FOLDER_LIST[List_index] +"/"+"BRK"

               print(Copy_file_full_directory)
               print(Paste_file_full_directory)

               shutil.copy(Copy_file_full_directory,Paste_file_full_directory)



    for file_identifier in ENG_HEADER_NAME_LIST:

        List_index = ENG_HEADER_NAME_LIST.index(file_identifier)
        print(file_identifier)

        for file_name in Listedfile:

            if file_identifier in file_name:
                Copy_file_full_directory = DIR_COPY + "/" + file_name
                Paste_file_full_directory = DIR_PASTE + "/" + ENG_CAL_FOLDER_LIST[List_index] + "/" + "ENG"

                print(Copy_file_full_directory)
                print(Paste_file_full_directory)

                shutil.copy(Copy_file_full_directory, Paste_file_full_directory)






