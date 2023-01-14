from flask import Flask, render_template,request,redirect, url_for
from data import *
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():  # put application's code here
    from Index_data import get_data

    data = get_data()
    return render_template('right_Index.html',form=data)


@app.route('/radar',methods=['GET','POST'])
def get_radar():
    from Index_data import radar1,radar2

    if request.method == 'POST':
        Month = request.get_data()
        Month = Month.decode('ascii')

        chart_data1 = radar1(Month)
        chart_data2 = radar2(Month)
    if request.method == 'GET':
         chart_data1 = radar1('1')
         chart_data2 = radar2('1')

    return render_template('/Index/radar_chart.html', form1=chart_data1, form2=chart_data2)

@app.route('/table1', methods=['GET','POST'])
def get_table1():
    from load_table import table1
    # 获取表格里的数据
    d = table1()
    if request.method == 'GET':
        return  render_template('/Index/Table1.html', form=d)

@app.route('/business')
def business():
    from business_data import get_data
    data = get_data()

    return render_template('/Business/Business.html',form=data)

@app.route('/usrpic', methods=['GET','POST'])
def load_usrpic():
    from load_usrpic import usr_info
    # 获取用户信息
    if request.method == 'POST':
        prod = request.get_data()
        prod = prod.decode('ascii')
        d = usr_info(prod)

    if request.method == 'GET':
        d = usr_info("A")

    return render_template('/Business/User_pic.html', form=d)

@app.route('/finance',methods=['GET','POST'])
def finance():

    return render_template('/Finance/Finance.html')

@app.route('/asset1',methods=['GET','POST'])
def asset1():
    from finance_data import asset1
    data = asset1()

    return render_template('/Finance/Asset1.html', form=data)

@app.route('/asset2',methods=['GET','POST'])
def asset2():
    from finance_data import asset2

    data = asset2()
    print(data)
    return render_template('/Finance/Asset2.html',form=data)

@app.route('/asset3',methods=['GET','POST'])
def asset3():
    from finance_data import asset3
    data = asset3()
    print(data)
    return render_template('/Finance/Asset3.html',form=data)

@app.route('/asset4',methods=['GET','POST'])
def asset4():
    from finance_data import asset4
    data = asset4()
    print(data)

    return render_template('/Finance/Asset4.html',form=data)

@app.route('/asset5',methods=['GET','POST'])
def asset5():
    from finance_data import asset5
    data = asset5()
    # print(data)
    return render_template('/Finance/Asset5.html',form=data)

@app.route('/Predict/predict', methods=['GET','POST'])
def predict():
    from predict import GOAL,completion,Months,table,likelihood

    devi = completion() #实际与目标的偏差
    m = Months()    #实际完成的月份
    g = GOAL()  # 目标值
    p = likelihood()    #完成目标可能性

    return render_template('Predict/predict.html', goal=g, form3=devi, form4=m,prob=p)

# 预测模块贷款预测分析URL映射的视图函数
@app.route('/Predict/predict1', methods=['GET','POST'])
def predict1():
    from predict import loan_data, adj_weight, manual_adj
    # 获取前端传递的数据，包括月份和调整的贷款
    month = request.form.get('month')
    loan = request.form.get('loan')

    d = loan_data()
    if request.method=='GET':
        adj = adj_weight(0) # 初始化贷款预测分析柱状图
    if request.method == 'POST':
        adj = manual_adj(month,loan,0)  # 重新调整权重

    return render_template('Predict/bar_chart.html', form=d, form2=adj)

# 预测模块贷款差值表格URL映射的视图函数
@app.route('/pre_table', methods=['GET','POST'])
def get_table2():
    from predict import adj_weight, manual_adj,table

    month = request.form.get('month')
    loan = request.form.get('loan')

    if request.method=='GET':
        adj = adj_weight(2)
        data = table(adj)
    if request.method == 'POST':
        adj = manual_adj(month,loan,1)
        data = table(adj)

    return render_template('Predict/pred_table.html', form=data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)