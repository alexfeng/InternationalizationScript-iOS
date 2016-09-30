# -*- coding: utf-8 -*-
import sys
import xdrlib
import xlrd
import os
import shutil
##########################################################
reload(sys)
sys.setdefaultencoding('utf-8')

##########################################################
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

##########################################################
def main(argv):
    data = open_excel(sys.argv[1])
    table = data.sheets()[0]
    colnames = table.row_values(0) #第一行数据
    
    colKeys = table.col_values(0) #第一列key数据
    colValues_zh_CN = table.col_values(1) #简体中文数据
    colValues_English = table.col_values(2)#英文数据
    nrows = len(colKeys) #总行数
    ncols = len(colnames) #总列数
    
    languageList = []
    for indexCol in range(1,ncols):
        list = []
        colValues = table.col_values(indexCol)
        for indexRow in range(1,nrows):
            
            value = colValues[indexRow]
            value
            if (len(value)==0):
                value = colValues_English[indexRow]
            keyValue = '"' + colKeys[indexRow] + '"' + ' = ' + '"' + value + '"' + ';\n'
            list.append(keyValue)
        languageList.append(''.join(list))


    for index in range(len(languageList)):
        print languageList[index]
        fileName = str(index) + 'Localizable.strings'
        os.system(r'touch %s' % fileName)
        
        fp = open(fileName,'wb+')
        fp.write(languageList[index])
        fp.close()

if __name__=="__main__":
    main(sys.argv[1])