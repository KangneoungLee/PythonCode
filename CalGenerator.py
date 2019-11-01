# _*_ coding: utf-8 _*_

import os
os.chdir('./')
import xlrd
import os
import shutil
import subprocess
from mako.template import Template

class InputStruct():
    def __init__(self):
        self.CaldataIdx = ""
        self.SymbolName = ""
        self.DefineName = ""
        self.Datatype = ""
        self.Conversion = ""
        self.Group = ""
        self.Comment = ""
        self.CalData = ""
        self.SymbolNameLen = ""
        self.DefineNameLen = ""
        self.DatatypeLen = ""
        self.ConversionLen = ""
        self.GroupLen = ""
        self.CommentLen = ""
        self.CalDataLen = ""

class ConfigStruct():
    def __init__(self):
        self.ModuleName = ""
        self.CalType = ""
        self.NumOfCal = ""
        #self.GenType = ""

class LenMaxStruct():
    def __init__(self):
        self.SymbolName = ""
        self.DefineName = ""
        self.Datatype = ""
        self.Conversion = ""
        self.Group = ""
        self.Comment = ""
        self.CalData = ""

class CalInfoStruct():
    def __init__(self):
        self.sheetName = ""
        self.CalName = ""
        self.CalColNum = ""
        self.GenType = " "

#Dump = Template.render(input_st = input_st)
#f.write(dump)

def Parse_CalCofigInfo(file):

    book = xlrd.open_workbook(file)

    sheet = book.sheet_by_name(u'Component Definition')

    coldata = []
    Config_Engstlist = []
    Config_Brkstlist = []

    for row in range(1, sheet.nrows):
        for col in range(sheet.ncols):
            coldata.append(sheet.cell_value(row, col))

        InputCfg_St = ConfigStruct()
        InputCfg_St.ModuleName = coldata[1 + (row - 1) * sheet.ncols]
        InputCfg_St.NumOfCal   = int(coldata[2 + (row - 1) * sheet.ncols])
        if (InputCfg_St.NumOfCal == "") :
            InputCfg_St.NumOfCal   = 0
        InputCfg_St.CalType   = "Eng"

        Config_Engstlist.append(InputCfg_St)

    for row in range(1, sheet.nrows):
        for col in range(sheet.ncols):
            coldata.append(sheet.cell_value(row, col))

        InputCfg_St = ConfigStruct()
        InputCfg_St.ModuleName = coldata[1 + (row - 1) * sheet.ncols]
        InputCfg_St.NumOfCal   = int(coldata[3 + (row - 1) * sheet.ncols])
        if (InputCfg_St.NumOfCal == "") :
            InputCfg_St.NumOfCal   = 0
        InputCfg_St.CalType   = "Brk"

        Config_Brkstlist.append(InputCfg_St)

    return Config_Engstlist, Config_Brkstlist

def Parse_CalDataInfo(file, ConfigSt) :

    CalInfo_stlist = []

    sheetName = ConfigSt.ModuleName.upper() + "_" + ConfigSt.CalType.upper()
    print ("Selected sheetName: " + sheetName)
    book = xlrd.open_workbook(file)
    sheet = book.sheet_by_name(sheetName)

    for col in range(sheet.ncols):
        CalInfo_st = CalInfoStruct()
        coldata = str(sheet.cell_value(0, col))
        if (coldata.find("CAL_") != -1 ) :
            CalInfo_st.sheetName = sheetName
            CalInfo_st.CalName = coldata.split("CAL_")[1]
            CalInfo_st.CalColNum = col
            if (CalInfo_st.CalName.find("GM") != -1) :
                CalInfo_st.GenType = "GM"
            else :
                CalInfo_st.GenType = "NotGM"
            CalInfo_stlist.append(CalInfo_st)

    totalcolNum = sheet.ncols
    totalrowNum = sheet.nrows

    return totalcolNum, totalrowNum, CalInfo_stlist

def Parse_Excel(file, CalDataNum, sheetName):

    book = xlrd.open_workbook(file)

    sheet = book.sheet_by_name(sheetName)

    coldata = []
    Output_stlist = []
    LenMaxSt = LenMaxStruct();
    LenMaxSt.SymbolName = 0
    LenMaxSt.DefineName = 0
    LenMaxSt.Datatype = 0
    LenMaxSt.Conversion = 0
    LenMaxSt.Group = 0
    LenMaxSt.Comment = 0
    LenMaxSt.CalData = 0
    CaldataIdxColNum = 0
    SymbolNameColNum = 0
    DefineNameColNum = 0
    DatatypeColNum = 0
    ConversionColNum = 0
    GroupColNum = 0
    CommentColNum = 0

    for firstcol in range(sheet.ncols):
        firstcoldata = str(sheet.cell_value(0, firstcol))
        firstcolstlipdata = firstcoldata.strip()

        if (firstcolstlipdata == "No.") :
            CaldataIdxColNum = firstcol
        elif (firstcolstlipdata == "T/P") :
            SymbolNameColNum = firstcol
        elif (firstcolstlipdata == "DefineName") :
            DefineNameColNum = firstcol
        elif (firstcolstlipdata == "DataType") :
            DatatypeColNum = firstcol
        elif (firstcolstlipdata == "Conversion") :
            ConversionColNum = firstcol
        elif (firstcolstlipdata == "GROUP") :
            GroupColNum = firstcol
        elif (firstcolstlipdata == "Description") :
            CommentColNum = firstcol


    for row in range(1, sheet.nrows):
        for col in range(sheet.ncols):
            coldata.append(sheet.cell_value(row, col))

        # print("col number :" + str(col))
        # print("row number :" + str(row))

        input_st = InputStruct()
        input_st.CaldataIdx = coldata[CaldataIdxColNum + (row - 1) * sheet.ncols]
        input_st.SymbolName = str(coldata[SymbolNameColNum + (row - 1) * sheet.ncols])
        input_st.DefineName = str(coldata[DefineNameColNum + (row - 1) * sheet.ncols])
        input_st.Datatype   = str(coldata[DatatypeColNum + (row - 1) * sheet.ncols])
        input_st.Conversion = str(coldata[ConversionColNum + (row - 1) * sheet.ncols])
        input_st.Group      = str(coldata[GroupColNum + (row - 1) * sheet.ncols])
        input_st.Comment    = (coldata[CommentColNum + (row - 1) * sheet.ncols]).encode('utf-8')
        if (str(coldata[CalDataNum + (row - 1) * sheet.ncols]) == "") :
            print (sheetName + " sheet" + ", line" + str(row) + " has no values, please fill in the calibration value!! ")
        else :
            input_st.CalData    = str(int(coldata[CalDataNum + (row - 1) * sheet.ncols]))

        # for caldatacol in range(7, sheet.ncols):
        #     input_st.CalData.append(str(coldata[caldatacol+ (row -1) *sheet.ncols]))

        input_st.SymbolNameLen = len(input_st.SymbolName)
        input_st.DefineNameLen = len(input_st.DefineName)
        input_st.DatatypeLen   = len(input_st.Datatype)
        input_st.ConversionLen = len(input_st.Conversion)
        input_st.GroupLen      = len(input_st.Group)
        input_st.CommentLen    = len(input_st.Comment)
        input_st.CalDataLen    = len(input_st.CalData)

        if LenMaxSt.SymbolName <= input_st.SymbolNameLen :
            LenMaxSt.SymbolName = input_st.SymbolNameLen
        if LenMaxSt.DefineName <= input_st.DefineNameLen :
            LenMaxSt.DefineName = input_st.DefineNameLen
        if LenMaxSt.Datatype <= input_st.DatatypeLen :
            LenMaxSt.Datatype = input_st.DatatypeLen
        if LenMaxSt.Conversion <= input_st.ConversionLen :
            LenMaxSt.Conversion = input_st.ConversionLen
        if LenMaxSt.Group <= input_st.GroupLen :
            LenMaxSt.Group = input_st.GroupLen
        if LenMaxSt.Comment <= input_st.CommentLen :
            LenMaxSt.Comment = input_st.CommentLen
        if LenMaxSt.CalData <= input_st.CalDataLen :
            LenMaxSt.CalData = input_st.CalDataLen

        # for caldatacol in range(7, sheet.ncols):
        #     input_st.CalDataLen.append(len(str(coldata[caldatacol+ (row -1) *sheet.ncols])))

        Output_stlist.append(input_st)

    return Output_stlist, LenMaxSt

def CreateCommonFolders():
    if os.path.isdir('./CAL_GEN') == True:
        shutil.rmtree('./CAL_GEN')
    os.mkdir('./CAL_GEN')
    os.mkdir('./CAL_GEN/CAL_SEL')
    os.mkdir('./CAL_GEN/CAL_SEL/ESC')
    os.mkdir('./CAL_GEN/CAL_STRUCT')
    os.mkdir('./CAL_GEN/CAL_STRUCT/ESC')

def CreateFolders(CalName, ConfigSt):
    if (ConfigSt.NumOfCal != 0) :
        if os.path.isdir('./CAL_GEN/CAL_SEL/ESC/'+CalName) != True :
            os.mkdir('./CAL_GEN/CAL_SEL/ESC/'+CalName)
        if os.path.isdir('./CAL_GEN/CAL_SEL/ESC/'+CalName+'/'+ConfigSt.ModuleName.upper()) != True :
            os.mkdir('./CAL_GEN/CAL_SEL/ESC/'+CalName+'/'+ConfigSt.ModuleName.upper())
        if os.path.isdir('./CAL_GEN/CAL_SEL/ESC/'+CalName+'/'+ConfigSt.ModuleName.upper()+'/'+ConfigSt.CalType.upper()) != True :
            os.mkdir('./CAL_GEN/CAL_SEL/ESC/'+CalName+'/'+ConfigSt.ModuleName.upper()+'/'+ConfigSt.CalType.upper())

def MakeCalStructFile(ConfigSt, Output_stlist, LenMaxSt ):
    f = open('./CAL_GEN/CAL_STRUCT/ESC/'+ConfigSt.ModuleName+'_'+ConfigSt.CalType+'CalStruct.h', 'w')
    mytemplate = Template(filename='.\Template\CalStruct_h.tmpl', default_filters=['decode.utf8'])
    genDump = mytemplate.render(ConfigSt = ConfigSt, CalDatalist = Output_stlist, LenMaxSt = LenMaxSt ).replace('\r\n','\n')
    f.write(genDump.encode('utf-8'))
    f.close()

def MakeCalDataFile(CalName, ConfigSt, CalInfoSt, Output_stlist, LenMaxSt, CalNum):
    if (len(str(CalNum+1))<2):
        CalIndex = "0" + str(CalNum+1)
    else:
        CalIndex = str(CalNum+1)
    f = open('./CAL_GEN/CAL_SEL/ESC/'+CalName+'/'+ConfigSt.ModuleName.upper()+'/'+ConfigSt.CalType.upper()+'/'+ConfigSt.ModuleName+'_'+ConfigSt.CalType+'Cal_'+CalIndex+'.h', 'w')
    mytemplate = Template(filename='.\Template\CalData_h.tmpl', default_filters=['decode.utf8'])
    genDump = mytemplate.render(CalName=CalName, ConfigSt = ConfigSt, CalInfoSt = CalInfoSt, CalDatalist = Output_stlist, LenMaxSt = LenMaxSt, CalIndex= CalIndex).replace('\r\n','\n')
    f.write(genDump.encode('utf-8'))
    f.close()

if __name__ == '__main__':
    print "####################################################################"
    print("             Creating the generate forders")
    print "####################################################################"


    CreateCommonFolders()

    EngConfigStlist = []
    BrkConfigStlist = []
    CalInfoSt = []

    EngConfigStlist, BrkConfigStlist  = Parse_CalCofigInfo('./CalExcel.xlsx')

    for EngIdx in range (0, len(EngConfigStlist)) :
        EngCalMaxColNum, EngCalMaxRowNum, EngCalInfoSt = Parse_CalDataInfo('./CalExcel.xlsx', EngConfigStlist[EngIdx])

        print "####################################################################"
        print("             Configuration Infomation")
        print("Component Name                     : " + str(EngConfigStlist[EngIdx].ModuleName))
        print("Engnine or Brake Cal               : " + str(EngConfigStlist[EngIdx].CalType))
        print("Number of Cal Set                  : " + str(EngConfigStlist[EngIdx].NumOfCal))
        print("Number of Calibration Parameter    : " + str(EngCalMaxRowNum))
        print "####################################################################"

        CalIdx = 0
        for CalIdx in range (0, len(EngCalInfoSt)):
            EngOutCalStlist, EngLenMaxSt = Parse_Excel('./CalExcel.xlsx',EngCalInfoSt[CalIdx].CalColNum, EngCalInfoSt[CalIdx].sheetName)
            print("           Creating the " + EngCalInfoSt[CalIdx].CalName + " forders")
            CreateFolders(EngCalInfoSt[CalIdx].CalName, EngConfigStlist[EngIdx])
            for EngCalNum in range(int(EngConfigStlist[EngIdx].NumOfCal)) :
                MakeCalDataFile(EngCalInfoSt[CalIdx].CalName.upper(), EngConfigStlist[EngIdx], EngCalInfoSt[CalIdx], EngOutCalStlist, EngLenMaxSt, EngCalNum)
            print("     "+ EngConfigStlist[EngIdx].ModuleName + " cal data is generating now..")
            print "####################################################################"

        if (EngConfigStlist[EngIdx].NumOfCal != 0) :
            MakeCalStructFile(EngConfigStlist[EngIdx], EngOutCalStlist, EngLenMaxSt )
        print("     "+ str(EngConfigStlist[EngIdx].ModuleName) + "_" + str(EngConfigStlist[EngIdx].CalType)+ " Struct is generating now..")
        print "####################################################################"

    for BrkIdx in range (0, len(BrkConfigStlist)) :
        BrkCalMaxColNum, BrkCalMaxRowNum, BrkCalInfoSt = Parse_CalDataInfo('./CalExcel.xlsx', BrkConfigStlist[BrkIdx])
        print "####################################################################"
        print("             Configuration Infomation")
        print("Component Name                     : " + str(BrkConfigStlist[BrkIdx].ModuleName))
        print("Engnine or Brake Cal               : " + str(BrkConfigStlist[BrkIdx].CalType))
        print("Number of Cal Set                  : " + str(BrkConfigStlist[BrkIdx].NumOfCal))
        print("Number of Calibration Parameter    : " + str(BrkCalMaxRowNum))
        print "####################################################################"

        CalIdx = 0
        for CalIdx in range (0, len(BrkCalInfoSt)):
            BrkOutCalStlist, BrkLenMaxSt = Parse_Excel('./CalExcel.xlsx',BrkCalInfoSt[CalIdx].CalColNum, BrkCalInfoSt[CalIdx].sheetName)
            print("           Creating the " + BrkCalInfoSt[CalIdx].CalName + " forders")
            CreateFolders(BrkCalInfoSt[CalIdx].CalName, BrkConfigStlist[BrkIdx])
            for BrkCalNum in range(int(BrkConfigStlist[BrkIdx].NumOfCal)) :
                MakeCalDataFile(BrkCalInfoSt[CalIdx].CalName.upper(), BrkConfigStlist[BrkIdx], BrkCalInfoSt[CalIdx], BrkOutCalStlist, BrkLenMaxSt, BrkCalNum)
            print("     "+ BrkConfigStlist[BrkIdx].ModuleName + " cal data is generating now..")
            print "####################################################################"

        if (BrkConfigStlist[BrkIdx].NumOfCal != 0) :
            MakeCalStructFile(BrkConfigStlist[BrkIdx], BrkOutCalStlist, BrkLenMaxSt)
        print("     "+ str(BrkConfigStlist[BrkIdx].ModuleName) + "_" + str(BrkConfigStlist[BrkIdx].CalType)+ " Struct is generating now..")
        print "####################################################################"

    print "####################################################################"
    print("             CAL Generation is complete!!!!!!")
    print "####################################################################"

