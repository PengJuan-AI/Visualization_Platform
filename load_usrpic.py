import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="719458145",
    database="bank_index",
    auth_plugin='mysql_native_password'
)

def usr_info(prod):

    mycursor = mydb.cursor()
    sql = "select avg(Invest_amount),avg(Overdue_rate),avg(Age),avg(Degree) from Usr_info as t1, Prod_data as t2 where t1.Usr_ID=t2.Usr_ID and Prod=" + "'" + prod + "'"
    mycursor.execute(sql)
    data = mycursor.fetchall()

    # print(data)
    jsonData = []
    for row in data:
        result = {}
        result['trd'] = round(row[0],2)
        result['overdue'] = round(row[1], 2)  # 平均违约率
        result['age'] = round(row[2])  # 平均投资额
        dgr = round(row[3])
        if dgr==0:
            result['degree'] = '高中及以下'
        elif dgr==1:
            result['degree'] = '大专'
        elif dgr == 2:
            result['degree'] = '本科'
        elif dgr == 3:
            result['degree'] = '硕士'
        else:
            result['degree'] = '博士及以上'


        jsonData.append(result)
    print(jsonData)

    return jsonData

# usr_info('A')