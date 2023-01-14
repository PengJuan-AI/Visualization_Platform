import mysql.connector
import numpy as np

def get_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="719458145",
        database="bank_index",
        auth_plugin='mysql_native_password'
    )


    mycursor = mydb.cursor()
    sql = "Select Date_FORMAT(Date,'%y.%m'),COUNT(Usr_ID) from Usr_info group by Date_FORMAT(Date,'%y.%m') order by Date_FORMAT(Date,'%y.%m') desc limit 6"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    data.reverse()

    sql = "Select COUNT(Usr_ID) from Usr_info where Deposit_Amount>1000000 group by Date_FORMAT(Date,'%y.%m') order by Date_FORMAT(Date,'%y.%m') desc limit 6"
    mycursor.execute(sql)
    data2 = mycursor.fetchall()
    data2.reverse()

    finaldata1=[]
    for row in data:
        result = {}
        # result['month'] = str(row[0])+'月',
        result['month'] = str(row[0])   # 月份
        result['value'] = round(row[1]) # 零售客户量
        finaldata1.append(result)

    finaldata2 = []
    for row in data2:
        result = {}
        result['value'] = row[0]  # 高级客户（存款大于100w）
        finaldata2.append(result)

    # 私人银行数据
    sql = "Select Date_FORMAT(Date,'%y.%m'),SUM(Fund_agency),SUM(Insurance_agency),Sum(Investment_agency),SUM(Other) from Private_bank group by Date_FORMAT(Date,'%y.%m') order by Date_FORMAT(Date,'%y.%m') desc limit 6"
    mycursor.execute(sql)
    data3 = mycursor.fetchall()
    data3.reverse()

    finaldata3 = []
    last = 0
    accounts = ['代理基金','代理保险','代理理财','其他']
    for row in data3:
        result={}
        temp = list(row)
        SUM = sum(temp[1:4])
        result['investment'] = round(SUM/100000)
        if last == 0:
            result['g_rate'] = 0.0
        else:
            result['g_rate'] = round((SUM/last - 1)*100,1)
        finaldata3.append(result)
        last = SUM

    pie_num = temp[1:5]


    #线上线下获客量
    sql = "Select Date_FORMAT(Date,'%y.%m'),COUNT(Usr_ID),Method from Usr_info group by Date_FORMAT(Date,'%y.%m'),Method order by Date_FORMAT(Date,'%y.%m') desc limit 12"
    mycursor.execute(sql)
    data4 = mycursor.fetchall()
    data4.reverse()

    finaldata4 = []
    last = 0
    for row in data4:
        result = {}
        # temp = list(row)
        if row[2]==1:   #线上
            result['value1'] = round(row[1])
        else:
            result['value2'] = round(row[1])
        finaldata4.append(result)

    #app理财
    sql = "Select Date_FORMAT(Date,'%y.%m'),SUM(Transfer),SUM(Payment),SUM(Wealth_management),SUM(Living_payment),SUM(Foreign_currency),SUM(Other) from APP_data group by Date_FORMAT(Date,'%y.%m') order by Date_FORMAT(Date,'%y.%m') desc "
    mycursor.execute(sql)
    data5 = mycursor.fetchall()
    data5.reverse()

    finaldata5=[]
    accounts2=['转账','支付','理财','生活缴费','外汇','其他']
    for row in data5:
        result = {}
        # result['month'] = str(row[0])+'月',
        result['month'] = str(row[0])   # 月份
        result['value'] = round(row[3]/1000000) # 理财金额
        if last == 0:
            result['g_rate'] = 0.0
        else:
            result['g_rate'] = round((row[3]/last - 1)*100,1)
        finaldata5.append(result)
        last = row[3]

    temp = list(row)
    pie_num2=temp[1:7]

    # a = finaldata4[2].get("value1")
    # b = finaldata1[5].get("value")
    #
    # digitalization = str(round(a / b)*100,2)+'%'

    print(finaldata5)
    try:
        echart = {
            'title':"业务模块",
            'xAxis1': [i.get("value") for i in finaldata1],
            'xAxis2': [i.get("value") for i in finaldata2],
            'growth': [i.get("g_rate") for i in finaldata3],
            'online': [i.get("value1") for i in finaldata4],
            'offline': [i.get("value2") for i in finaldata4],
            'month': [i.get("month") for i in finaldata1],
            'ivstment':[i.get("investment") for i in finaldata3],
            'month2':[i.get("month") for i in finaldata5],
            'app_invest':[i.get("value") for i in finaldata5],
            'app_invest_growth':[i.get("g_rate") for i in finaldata5],
            'monthly_new': str(finaldata1[5].get("value")-finaldata1[4].get("value")),
            'YoY':str(round((finaldata1[5].get("value")/finaldata1[0].get("value")-1)*100,2))+'%',
            'QoQ':str(round((finaldata1[5].get("value")/finaldata1[4].get("value")-1)*100,2))+'%',
            'digitalize':str(round((finaldata4[2].get("value1")/finaldata1[5].get("value"))*100,2))+'%',
            'Pie1_name':accounts,
            'Pie1_num':pie_num,
            'Pie2_name': accounts2,
            'Pie2_num': pie_num2
        }
        # print(echart)
        return echart
    except:
        print("Error")

get_data()