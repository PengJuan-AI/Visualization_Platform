import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="719458145",
    database="bank_index",
    auth_plugin='mysql_native_password'
)

def loan_data():

    mycursor = mydb.cursor()
    sql = "Select * from Loan"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    jsonData = []
    mycursor.close()
    # 获取每月预期贷款和实际贷款数据
    for row in data:
        result = {}
        result['exp'] = row[3]/1000 #预计应当发放的贷款
        result['actual'] = row[4]/1000  #实际发放的贷款
        jsonData.append(result)
    # print(jsonData)
    try:
        echart = {
            'data1': [i.get("exp") for i in jsonData],
            'data2': [i.get("actual") for i in jsonData]
        }
        return echart
    except:
        print("Error")

    return jsonData

def adj_weight(tag):

    mycursor = mydb.cursor()
    sql = "Select weight from Loan WHERE actual_loan=0 "
    mycursor.execute(sql)
    data = mycursor.fetchall()
    jsonData = []

    # 初始化权重数组
    length = 12 - len(data)
    L = [0] * length
    weight = L
    for row in data:
        weight.append(row[0])

    # 计算实际和预期的差距
    sql = "select SUM(expected_loan)-SUM(actual_loan) from Loan"
    mycursor.execute(sql)
    diff = mycursor.fetchall()
    diff = diff[0][0]
    mycursor.close()
    # 计算调整后的权重
    s = sum(weight)
    adj_w = [w / s for w in weight]
    # 计算调整后的loan
    result = {}
    result['adj'] = [round((w * diff) / 1000) for w in adj_w]
    jsonData.append(result)

    # 用tag判断是否是按输入值调整，tag=1和tag=2都是传给表格的数据格式
    if tag == 1:
        return result['adj'], length
    elif tag==2:
        return  result['adj']
    else:
        try:
            echart = {
                'data': result['adj'],
            }
            return echart
        except:
            print("Error")

# 如果是手动调整时，调用这个函数
def manual_adj(m,n,tag):
    # m表示调整的月份，n表示调整的贷款
    m = int(m)
    n = int(n)

    mycursor = mydb.cursor()
    sql = "Select weight from Loan WHERE actual_loan=0 "
    mycursor.execute(sql)
    data = mycursor.fetchall()
    jsonData = []

    # 初始化权重数组
    length = 12 - len(data)
    L = [0] * length
    weight = L

    for row in data:
        weight.append(row[0])
    # 设置第n个月的weight为0，即不参与调整权重
    weight[m-1] = 0

    # 计算实际和预期的差距
    sql = "select SUM(expected_loan)-SUM(actual_loan) from Loan"
    mycursor.execute(sql)
    diff = mycursor.fetchall()
    # 这里的差值只剩下几个待调整的月份
    diff = diff[0][0]
    # print("这是传入的贷款",n)
    # print("这是差值：",diff)
    if n>diff:  # 如果调整的贷款大于差值，不接受调整
        return False
    else:
        diff = diff-n

    mycursor.close()

    s = sum(weight)
    adj_w = [w / s for w in weight]
    # 计算调整后的loan
    result = {}
    result['adj'] = [round((w * diff) / 1000) for w in adj_w]
    #第m个月的loan等于传进来的n
    result['adj'][m-1] = n

    jsonData.append(result)
    # 根据tag设置传输出去的值，tag=1是传递给表格的数据，tag=0是传递给柱状图的数据，数据格式不同
    if tag == 1:
        return result['adj']
    else:
        try:
            echart = {'data': result['adj']}
            return echart
        except:
            print("Error")


# 计算每月完成度
def completion():
    exp_actual = loan_data()
    adj,l = adj_weight(1)

    # print("实际", exp_actual['data2'])
    # print("调整后", adj)

    actual = exp_actual['data2']
    exp = exp_actual['data1'][0:l]

    # print("今年实际完成", actual)
    # print("今年预期完成", exp)
    # 计算调整后与预期的偏差
    deviation = [round((a/b-1)*100) for a,b in zip(actual, exp)]
    # print("今年目标完成情况为：", deviation)

    try:
        echart = {
            'data': deviation
        }
        return echart
    except:
        print("Error")

def Months():
    mycursor = mydb.cursor()
    sql = "Select MONTH(date) from Loan WHERE actual_loan=0 "
    mycursor.execute(sql)
    data = mycursor.fetchall()
    jsonData = []

    for row in data:
        result = {}
        result['month'] = row[0]
        jsonData.append(result)

    # print(jsonData)
    mycursor.close()

    return jsonData

def GOAL():
    mycursor = mydb.cursor()
    sql = "Select SUM(expected_loan),SUM(actual_loan) from Loan "
    mycursor.execute(sql)
    data = mycursor.fetchall()
    jsonData = []
    mycursor.close()

    for row in data:
        result = {}
        result['value'] = round(row[0]/1000)
        result['complet_r'] = round(row[1]/row[0]*100,1)
        jsonData.append(result)

    return jsonData

def func1(data,d):

    j=0
    diff = []
    l = len(data)
    for i in range(0,l):
        if data[i]!=0:
            diff.append(data[i]-d[j])
            j = j+1

    return diff

# 用来组合table的值
def table(adj):

    mycursor = mydb.cursor()
    sql = "Select weight,expected_loan from Loan WHERE actual_loan=0 "
    mycursor.execute(sql)
    data = mycursor.fetchall()
    jsonData = []

    # 初始化权重数组
    # length = 12 - len(data)
    # L = [0] * length
    # weight = L
    d = []  # 调整后和预期的差距
    for row in data:
        # weight.append(row[0])
        d.append(row[1] / 1000)

    # 计算实际和预期的差距
    # sql = "select SUM(expected_loan)-SUM(actual_loan) from Loan"
    # mycursor.execute(sql)
    # diff = mycursor.fetchall()
    # diff = diff[0][0]
    # mycursor.close()
    #
    # s = sum(weight)
    # adj_w = [w / s for w in weight]
    # # 计算调整后的loan
    # adj = [round((w * diff) / 1000) for w in adj_w]
    # print(adj)
    diff = func1(adj, d)

    month = Months()
    l = len(diff)
    jsondata = []

    for i in range(0,l):
        data = {}
        data['month'] = month[i]['month']
        data['diff'] = diff[i]
        jsondata.append(data)

    print('jsondata的值为，',jsondata)
    return jsondata

def likelihood():

    mycursor = mydb.cursor()
    sql = "select expected_loan,actual_loan from Loan"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    sql = "select SUM(expected_loan) from Loan"
    mycursor.execute(sql)
    total = mycursor.fetchall()
    total = total[0][0]
    mycursor.close()

    sum=0
    for row in data:
        if row[1]==0:
            sum=sum+row[0]
        else:
            sum=sum+row[1]

    return sum/total
