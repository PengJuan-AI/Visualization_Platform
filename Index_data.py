import mysql.connector
import numpy as np

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:

import json


import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="719458145",
    database="bank_index",
    auth_plugin='mysql_native_password'
)


    # @property
def radar1(month):

    #------------------------雷达图1-----------------
    mycursor = mydb.cursor()
    #
    mycursor.execute("SELECT * FROM radar1 Where MONTH(date)="+month+" order BY name")
    #
    data1= mycursor.fetchall()
    mycursor.execute("SELECT * FROM radar1_industry Where MONTH(date)="+month+" order BY name")
    data2 = mycursor.fetchall()
    jsonData1 = []
    jsonData2 = []

    for row in data1:
        result = {}
        result['value'] = row[2]
        jsonData1.append(result)
    # print(jsonData1)
    for row in data2:
        result = {}
        result['value'] = row[2]
        jsonData2.append(result)
    # print(jsonData2)
    try:
        echart = {
            'title1':"本行",
            'xAxis1': [i.get("value") for i in jsonData1],
            'title2': "行业",
            'xAxis2': [i.get("value") for i in jsonData2]
        }
        return echart
    except:
        print("Error")


    mycursor.close()
    return echart

def radar2(month):
    # ------------------------1113尝试-----------------
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM radar2 Where MONTH(date)="+month+" order BY name")
    data1 = mycursor.fetchall()
    mycursor.execute("SELECT * FROM radar2_industry Where MONTH(date)=" + month +" Order by name")
    data2 = mycursor.fetchall()
    jsonData1 = []
    jsonData2 = []

    for row in data1:
        result = {}
        result['value'] = row[2]
        jsonData1.append(result)
    # print(jsonData1)
    for row in data2:
        result = {}
        result['value'] = row[2]
        jsonData2.append(result)
    # print(jsonData2)
    try:
        echart = {
            'title1': "本行",
            'xAxis1': [i.get("value") for i in jsonData1],
            'title2': "参照值",
            'xAxis2': [i.get("value") for i in jsonData2]
        }
        return echart
    except:
        print("Error")

    mycursor.close()
    return echart


def get_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="719458145",
        database="bank_index",
        auth_plugin='mysql_native_password'
    )
    # 同比和环比都可以用data
    mycursor1 = mydb.cursor()
    sql = "Select Date_FORMAT(Date,'%y年%m月'),Total_Asset,Total_Deposit from Balance_Sheet order by Date desc limit 6"
    mycursor1.execute(sql)
    data = mycursor1.fetchall()
    data.reverse()

    jsonData = []
    last1 = 0
    last2 = 0
    for row in data:
        result = {}
        # result['month'] = str(row[0])+'月',
        result['month'] = str(row[0])
        result['value1'] = round(row[1]/100000000) #单位为亿元
        result['value2'] = round(row[2]/100000000)  # 单位为亿元
        if last1 == 0:
            result['g_rate1'] = 0.0
            result['g_rate2'] = 0.0
        else:
            result['g_rate1'] = round((row[1]/last1 - 1)*100,1)
            result['g_rate2'] = round((row[2] / last2 - 1) * 100, 1)
        jsonData.append(result)
        last1 = row[1]
        last2 = row[2]

    try:
        echart = {
            'title':"概览模块",
            'Asset': [i.get("value1") for i in jsonData],
            'Deposit': [i.get("value2") for i in jsonData],
            'growth1': [i.get("g_rate1") for i in jsonData],
            'growth2': [i.get("g_rate2") for i in jsonData],
            'month': [i.get("month") for i in jsonData],
            'current_asset':str(jsonData[5].get("value1")),
            'current_deposit':str(jsonData[5].get("value2")),
        }
        print(echart)
        return echart
    except:
        print("Error")
    # print(data)

@property
def map_1(self):
    data = self.map_1_data
    echart = {
        'symbolSize': data.get('symbolSize'),
        'data': data.get('data'),
    }
    return echart
