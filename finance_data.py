from flask import Flask, render_template,request,redirect, url_for
import mysql.connector
import numpy as np
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="719458145",
#     database="bank_index",
#     auth_plugin='mysql_native_password'
# )

def asset1():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="719458145",
        database="bank_index",
        auth_plugin='mysql_native_password'
    )

    # 同比和环比都可以用data
    mycursor1 = mydb.cursor()
    sql = "Select Date_FORMAT(Date,'%y年%m月'),Total_Asset from Balance_Sheet order by Date desc limit 6"
    mycursor1.execute(sql)
    data = mycursor1.fetchall()
    data.reverse()
    jsonData = []

    # 平均5年增速,取月份等于12的数据
    sql = "Select Total_Asset from Balance_Sheet where MONTH(Date)=12 order by Year(Date) desc limit 6"
    mycursor1.execute(sql)
    data2 = mycursor1.fetchall()
    data2.reverse()

    # 资产组合
    sql = "Select Cash,Interbank_deposit,trd_financial_asset,Outstanding_loan from Balance_Sheet where Date=(Select Date from Balance_Sheet order by Date desc limit 1)"
    mycursor1.execute(sql)
    data3 = mycursor1.fetchall()
    acocunts = ['现金','存放同业款项','交易性金融资产','发放贷款及垫款']

    mycursor1.close()
    last = 0

    for row in data:
        result = {}
        # result['month'] = str(row[0])+'月',
        result['month'] = str(row[0])
        result['value'] = round(row[1]/10000000) #单位为百万元
        if last == 0:
            result['g_rate'] = 0.0
        else:
            result['g_rate'] = round((row[1]/last - 1)*100,1)
        jsonData.append(result)
        last = row[1]

    # 计算5年平均
    growth_5y = []
    i = 0
    last = 0
    for row in data2:
        if last == 0:
            last = row[0]
        else:
            growth_5y.append(row[0] / last - 1)
            last = row[0]
            i = i+1

    for row in data3:
        temp = list(row)
        sub_asset = [str(x) for x in temp]

    try:
        echart = {
            'title':"资产规模",
            'xAxis1': [i.get("value") for i in jsonData],
            'xAxis2': [i.get("g_rate") for i in jsonData],
            'month': [i.get("month") for i in jsonData],
            'current':str(jsonData[5].get("value")),
            'Avg_5y': str(round(np.mean(growth_5y)*100,2))+'%',
            'YoY':str(round((jsonData[5].get("value")/jsonData[0].get("value")-1)*100,2))+'%',
            'QoQ':str(round((jsonData[5].get("value")/jsonData[4].get("value")-1)*100,2))+'%',
            'Pie_name':acocunts,
            'Pie_num':sub_asset
        }

        return echart
    except:
        print("Error")


def asset2():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="719458145",
        database="bank_index",
        auth_plugin='mysql_native_password'
    )

    mycursor2 = mydb.cursor()
    sql = "Select Date_FORMAT(Date,'%y年%m月'),Revenue, Operating_expense from Income_Sheet order by Date desc limit 5"
    mycursor2.execute(sql)
    data = mycursor2.fetchall()
    data.reverse()
    jsonData = []

    # 平均5年增速,取月份等于12的数据
    sql = "Select Revenue from Income_Sheet where MONTH(Date)=12 order by Year(Date) desc limit 6"
    mycursor2.execute(sql)
    data2 = mycursor2.fetchall()
    data2.reverse()

    # 饼图数据
    sql = "Select Area,sum(Sub_Revenue_by_area),sum(On_line),sum(Off_line) from Income_info where Year(Date)=(Select Year(date) from Income_info order by Date desc limit 1) group by Area"
    mycursor2.execute(sql)
    data3 = mycursor2.fetchall()
    # print(data3)

    mycursor2.close()
    last = 0

    for row in data:
        result = {}
        result['month'] = str(row[0])
        result['value'] = round(row[1]/1000000) #单位为百万元
        result['expense'] = round(row[2] / 1000000)  # 单位为百万元
        if last == 0:
            result['g_rate'] = 0.0
        else:
            result['g_rate'] = round((row[1]/last - 1)*100,1)
        jsonData.append(result)
        last = row[1]

    # 计算5年平均
    growth_5y = []
    i = 0
    last = 0
    for row in data2:
        if last == 0:
            last = row[0]
        else:
            growth_5y.append(row[0] / last - 1)
            last = row[0]
            i = i + 1
    # 饼图数据
    Pie = []
    for row in data3:
        result = {}
        result['name'] = str(row[0])
        result['value1'] = round(row[1]/1000000) # 单位为百万元
        result['value2'] = [round(row[2]/1000000),round(row[3]/1000000) ] # 单位为百万元
        # result['value3'] =  # 单位为百万元
        Pie.append(result)
    # print(Pie)

    try:
        echart = {
            'title':"营业收入",
            'xAxis1': [i.get("value") for i in jsonData],
            'xAxis2': [i.get("expense") for i in jsonData],
            'xAxis3': [i.get("g_rate") for i in jsonData],
            'YoY': str(round((jsonData[4].get("value") / jsonData[0].get("value") - 1) * 100, 2)) + '%',
            'QoQ': str(round((jsonData[4].get("value") / jsonData[3].get("value") - 1) * 100, 2)) + '%',
            'current': str(jsonData[4].get("value")),
            'Avg_5y': str(round(np.mean(growth_5y) * 100, 2)) + '%',
            'month': [i.get("month") for i in jsonData],
            'Pie_name':[i.get("name") for i in Pie],
            'Father':[i.get("value1") for i in Pie],
            'Children':[i.get("value2") for i in Pie],
            'Enddate':str(jsonData[4].get('month'))
        }
        # print(echart)
        return echart
    except:
        print("Error")

def asset3():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="719458145",
        database="bank_index",
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    sql = "Select Date_FORMAT(Date,'%y年%m月'),Interest_income,Interest_expense from Income_Sheet order by Date desc limit 5"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    data.reverse()

    # 平均5年增速,取月份等于12的数据
    sql = "Select Interest_income from Income_Sheet where MONTH(Date)=12 order by Year(Date) desc limit 6"
    mycursor.execute(sql)
    data2 = mycursor.fetchall()
    data2.reverse()

    # 饼图数据
    # sql = "Select Credit_Card,Settlement,Consultant,Agent_entrust,Asset_custody,Asset_managed from Income_Sheet where Year(Date)=(Select Year(date) from Income_Sheet order by Date desc limit 1)"
    mycursor.execute(sql)
    data3 = mycursor.fetchall()
    acocunts = ['现金', '存放同业款项', '交易性金融资产', '发放贷款及垫款']

    mycursor.close()

    last = 0
    jsonData = []
    for row in data:
        result = {}
        result['month'] = str(row[0])+'月'
        result['value'] = round(row[1]/1000000) #单位为百万元
        result['expense'] = round(row[2]/1000000) #单位为百万元
        # if last == 0:
        #     result['g_rate'] = 0.0
        # else:
        #     result['g_rate'] = round((row[1]/last - 1)*100,1)
        jsonData.append(result)


    # 计算5年平均
    growth_5y = []
    i = 0
    last = 0
    for row in data2:
        if last == 0:
            last = row[0]
        else:
            growth_5y.append(row[0] / last - 1)
            last = row[0]
            i = i + 1

    # 饼图


    try:
        echart = {
            'title':"利息收入",
            'xAxis1': [i.get("value") for i in jsonData],
            'xAxis2': [i.get("expense") for i in jsonData],
            'month': [i.get("month") for i in jsonData],
            'YoY': str(round((jsonData[4].get("value") / jsonData[0].get("value") - 1) * 100, 2)) + '%',
            'QoQ': str(round((jsonData[4].get("value") / jsonData[3].get("value") - 1) * 100, 2)) + '%',
            'current': str(jsonData[4].get("value")),
            'Avg_5y': str(round(np.mean(growth_5y) * 100, 2)) + '%'
        }
        # print(echart)
        # mycursor.close()
        return echart
    except:
        print("Error")


    mycursor.close()
    return echart

def asset5():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="719458145",
        database="bank_index",
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    sql = "Select Date_FORMAT(Date,'%y年%m月'),NPL from Loan_analysis where MONTH(Date)=12 order by Date desc limit 6 "
    mycursor.execute(sql)
    data = mycursor.fetchall()
    data.reverse()

    sql = "Select Outstanding_loan,Total_Deposit from Balance_Sheet where MONTH(Date)=12 order by Date desc limit 6"
    mycursor.execute(sql)
    data2 = mycursor.fetchall()
    data2.reverse()

    #
    sql = "Select Norl,Smentl,Subl,Doubtl,Lossl from Loan_analysis order by Date limit 1"
    mycursor.execute(sql)
    data3 = mycursor.fetchall()

    jsonData = []
    mycursor.close()

    for row in data:
        result = {}
        result['month'] = str(row[0])
        #result['value1'] = round(row[1]/row[2],2) #存贷比
        result['NPL'] = row[1] #不良率
        jsonData.append(result)

    # 存贷比
    jsonData2 = []
    for row in data2:
        result={}
        result['value'] = round(row[1]/row[0],2)
        jsonData2.append(result)

    temp = list(data3[0])
    pie_num = [float(x) for x in temp]
    quality =[]
    pie_name = ['正常','关注','次级','可疑','损失']

    try:
        echart = {
            'title':"存贷比例与不良率",
            'xAxis1': [i.get("value") for i in jsonData2],
            'xAxis2': [i.get("NPL") for i in jsonData],
            'month': [i.get("month") for i in jsonData],
            'pie_num': pie_num,
            'pie_name':pie_name
        }
        # print(echart)
        # mycursor.close()
        return echart
    except:
        print("Error")


    mycursor.close()
    return echart


def asset4():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="719458145",
        database="bank_index",
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    sql = "Select Date_FORMAT(Date,'%y年%m月'),Non_interest_income from Income_Sheet order by Date desc limit 5"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    data.reverse()

    # 平均5年增速,取月份等于12的数据
    sql = "Select Non_interest_income from Income_Sheet where MONTH(Date)=12 order by Year(Date) desc limit 6"
    mycursor.execute(sql)
    data2 = mycursor.fetchall()
    data2.reverse()

    # 饼图数据
    sql = "Select Credit_Card,Settlement,Consultant,Agent_entrust,Asset_custody,Asset_managed,Other from Income_Sheet order by Date desc limit 1"
    mycursor.execute(sql)
    data3 = mycursor.fetchall()
    acocunts = ['银行卡手续费', '结算', '咨询顾问', '代理委托','资产托管','资产管理','其他']

    mycursor.close()

    last = 0
    jsonData = []
    for row in data:
        result = {}
        result['month'] = str(row[0])
        result['value'] = round(row[1]/1000000) #单位为百万元
        if last == 0:
            result['g_rate'] = 0.0
        else:
            result['g_rate'] = round((row[1]/last - 1)*100,1)
        jsonData.append(result)
        last = row[1]

    # 计算5年平均
    growth_5y = []
    i = 0
    last = 0
    for row in data2:
        if last == 0:
            last = row[0]
        else:
            growth_5y.append(row[0] / last - 1)
            last = row[0]
            i = i + 1

    # 饼图数据
    Pie = []
    for row in data3:
        temp = list(row)
        Pie = [x/100000 for x in temp]

    try:
        echart = {
            'title':"非利息收入",
            'xAxis1': [i.get("value") for i in jsonData],
            'xAxis2': [i.get("g_rate") for i in jsonData],
            'month': [i.get("month") for i in jsonData],
            'YoY': str(round((jsonData[4].get("value") / jsonData[0].get("value") - 1) * 100, 2)) + '%',
            'QoQ': str(round((jsonData[4].get("value") / jsonData[3].get("value") - 1) * 100, 2)) + '%',
            'current': str(jsonData[4].get("value")),
            'Avg_5y': str(round(np.mean(growth_5y) * 100, 2)) + '%',
            'Pie_name':acocunts,
            'Pie_num':Pie
        }
        # print(echart)
        # mycursor.close()
        return echart
    except:
        print("Error")


    mycursor.close()
    return echart

asset5()