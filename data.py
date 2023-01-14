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
def echart1(month):

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

def echart2(month):
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



@property
def map_1(self):
    data = self.map_1_data
    echart = {
        'symbolSize': data.get('symbolSize'),
        'data': data.get('data'),
    }
    return echart


