# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @Site    : 
# @File    : get_excel.py
# @Software: PyCharm
import xlrd,xlwt
import unittest,sys
from xlutils.copy import copy
from Interface.feng import reques
def datacel():
	filepath='.\\Data\\Data.xlsx'
	file=xlrd.open_workbook(filepath)
	me=file.sheets()[0]
	nrows=me.nrows
	listkey=[]
	listconeent=[]
	listurl=[]
	listfangshi=[]
	listqiwang=[]
	for i in range(1,nrows):
		listkey.append(me.cell(i,2).value)
		listconeent.append(me.cell(i,3).value)
		listurl.append(me.cell(i,4).value)
		listfangshi.append((me.cell(i,5).value))
		listqiwang.append((me.cell(i,6).value))
	return listkey,listconeent,listurl,listfangshi,listqiwang