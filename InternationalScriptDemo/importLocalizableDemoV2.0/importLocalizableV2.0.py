# -*- coding: utf-8 -*-
import sys
import xlrd
import os
from optparse import OptionParser
##########################################################
reload(sys)
sys.setdefaultencoding('utf-8')

##########################################################
def openExcel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)


##########################################################
def writeKeysValuesInToLocalizableFile(keys,values,targetFolder):
    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)

    fileName = targetFolder + 'Localizable.strings'
    os.system(r'touch %s' % fileName)
    fp = open(fileName,'wb+')

    keyValueList = []
    for indexRow in range(len(keys)):
        key = keys[indexRow]
        value = values[indexRow]
        keyValue = '"' + key + '"' + ' = ' + '"' + value + '"' + ';\n'
        keyValueList.append(keyValue)

    content = ''.join(keyValueList)
    fp.write(content)
    fp.close()

##########################################################
def importLocalizable(options):
    data = openExcel(options.filePath)
    table = data.sheets()[0]
    colnames = table.row_values(0) #第一行数据
    colKeys = table.col_values(0) #第一列key数据
    # print (colKeys)
    del colKeys[0]

    for indexCol in range(len(colnames)):
        if indexCol > 0:
            languageName = colnames[indexCol]
            values = table.col_values(indexCol)
            # print(values)
            del values[0]
            writeKeysValuesInToLocalizableFile(colKeys,values,os.getcwd()+"/iOSLocal/"+languageName+".proj/")



##########################################################
def main():
    parser = OptionParser()
    parser.add_option("-f", "--filePath",
                      help="original.xls File Path.",
                      metavar="filePath")
    (options, args) = parser.parse_args()
    importLocalizable(options)

##########################################################
main()