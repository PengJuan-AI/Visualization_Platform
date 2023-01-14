
/***
$(function (){
    var myChart2 = echarts.init(document.getElementById('asset_2'));
    option = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            top: '5%',
            left: 'center',
            textStyle: { color: "#ffffff" },
        },
        series: [
            {
                name: '资产',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                label:{            //饼图图形上的文本标签
                    normal:{
                        show:true,
                        position:'inner', //标签的位置
                        textStyle : {
                            fontWeight : 300 ,
                            fontSize : 16    //文字的字体大小
                        },
                        formatter:'{d}%'
                    }
                },
                emphasis: {
                    label: {
                        show: false,
                        fontSize: '40',
                        fontWeight: 'bold',
                        color: "#ffac11"
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    { value: 57, name: "发放贷款及垫款" },
                    { value: 22, name: "存放同业款项" },
                    { value: 10, name: "现金" },
                    { value: 6, name: "金融投资" },
                    { value: 5, name: "其他" }
                ],
                itemStyle: {
                    normal: {
                        color: function(params) {
                            //自定义颜色
                            var colorList = ['#F68944', '#FBC10D','#DCE02A','#96E043','#42D43F','#10B680'];
                            return colorList[params.dataIndex]
                        },
                        label: {
                            show: true,		//开启显示
                            position: 'top',	//在上方显示
                            textStyle: {	    //数值样式
                                color: 'white',
                                fontSize: 16
                            }
                        }
                    }
                }
            }
        ]
    };
    myChart2.setOption(option);
    tools.loopShowTooltip(myChart2, option, {
        loopSeries: true
    });
});
***/
// ----------------------
/***
$(function (){
    var myChart4 = echarts.init(document.getElementById('asset_4'));
    option = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            top: '5%',
            left: 'center',
            textStyle: { color: "#ffffff" },
        },
        series: [
            {
                name: '营收来源(%)',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                label:{            //饼图图形上的文本标签
                    normal:{
                        show:true,
                        position:'inner', //标签的位置
                        textStyle : {
                            fontWeight : 300 ,
                            fontSize : 16    //文字的字体大小
                        },
                        formatter:'{d}%'
                    }
                },
                emphasis: {
                    label: {
                        show: false,
                        fontSize: '40',
                        fontWeight: 'bold',
                        color: "#ffac11"
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    { value: 57, name: '华南区' },
                    { value: 22, name: '华中区' },
                    { value: 21, name: '华北区' }
                ],
                itemStyle: {
                    normal: {
                        color: function(params) {
                            //自定义颜色
                            var colorList = ['#F68944', '#FBC10D','#DCE02A','#96E043','#42D43F','#10B680'];
                            return colorList[params.dataIndex]
                        },
                        label: {
                            show: true,		//开启显示
                            position: 'top',	//在上方显示
                            textStyle: {	    //数值样式
                                color: 'white',
                                fontSize: 16
                            }
                        }
                    }
                }
            }
        ]
    };
    myChart4.setOption(option);
    tools.loopShowTooltip(myChart4, option, {
        loopSeries: true
    });
});
***/
// ----------------------



$(function (){
    var myChart6 = echarts.init(document.getElementById('asset_6'));
    option = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            top: '5%',
            left: 'center',
            textStyle: { color: "#ffffff" },
        },
        series: [
            {
                name: '利润来源',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                label:{            //饼图图形上的文本标签
                    normal:{
                        show:true,
                        position:'inner', //标签的位置
                        textStyle : {
                            fontWeight : 300 ,
                            fontSize : 16    //文字的字体大小
                        },
                        formatter:'{d}%'
                    }
                },
                emphasis: {
                    label: {
                        show: false,
                        fontSize: '40',
                        fontWeight: 'bold',
                        color: "#ffac11"
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    { value: 52, name: '贷款利息' },
                    { value: 34, name: '存放央行' },
                    { value: 10, name: '同业资产' },
                    { value: 4, name: '证券投资' }
                ],
                itemStyle: {
                    normal: {
                        color: function(params) {
                            //自定义颜色
                            var colorList = ['#F68944', '#FBC10D','#DCE02A','#96E043','#42D43F','#10B680'];
                            return colorList[params.dataIndex]
                        },
                        label: {
                            show: true,		//开启显示
                            position: 'top',	//在上方显示
                            textStyle: {	    //数值样式
                                color: 'white',
                                fontSize: 16
                            }
                        }
                    }
                }
            }
        ]
    };
    myChart6.setOption(option);
    tools.loopShowTooltip(myChart6, option, {
        loopSeries: true
    });
});

// //非利息收入
// $(function (){
//     var myChart6 = echarts.init(document.getElementById('asset_8'));
//     option = {
//         tooltip: {
//             trigger: 'item'
//         },
//         legend: {
//             top: '5%',
//             left: 'center',
//             textStyle: { color: "#ffffff" },
//         },
//         series: [
//             {
//                 name: '利润来源',
//                 type: 'pie',
//                 radius: ['40%', '70%'],
//                 avoidLabelOverlap: false,
//                 label:{            //饼图图形上的文本标签
//                     normal:{
//                         show:true,
//                         position:'inner', //标签的位置
//                         textStyle : {
//                             fontWeight : 300 ,
//                             fontSize : 16    //文字的字体大小
//                         },
//                         formatter:'{d}%'
//                     }
//                 },
//                 emphasis: {
//                     label: {
//                         show: false,
//                         fontSize: '40',
//                         fontWeight: 'bold',
//                         color: "#ffac11"
//                     }
//                 },
//                 labelLine: {
//                     show: false
//                 },
//                 data: [
//                     { value: 20, name: '银行卡' },
//                     { value: 30, name: '结算手续费' },
//                     { value: 15, name: '咨询顾问' },
//                     { value: 5, name: '代理委托' },
//                     { value: 5, name: '资产托管' },
//                     { value: 25, name: '财富管理' }
//                 ],
//                 itemStyle: {
//                     normal: {
//                         color: function(params) {
//                             //自定义颜色
//                             var colorList = ['#F68944', '#FBC10D','#DCE02A','#96E043','#42D43F','#10B680'];
//                             return colorList[params.dataIndex]
//                         },
//                         label: {
//                             show: true,		//开启显示
//                             position: 'top',	//在上方显示
//                             textStyle: {	    //数值样式
//                                 color: 'white',
//                                 fontSize: 16
//                             }
//                         }
//                     }
//                 }
//             }
//         ]
//     };
//     myChart6.setOption(option);
//     tools.loopShowTooltip(myChart6, option, {
//         loopSeries: true
//     });
// });
// ----------------------
//不良率
$(function (){
    var myChart8 = echarts.init(document.getElementById('asset_10'));
    var markLineData = [];
    var source =  [
        ['贷款等级情况', '2015', '2016'],
        ['正常', 98.12],
        ['关注', 0.81],
        ['次级', 0.29],
        ['可疑', 0.44],
        ['损失', 0.34]
    ];

    // 添加“其他”
    addOtherData(source,4);

    option = {
        legend: {
            textStyle: { color: "#ffffff" },
        },
        tooltip: {},
        dataset: {
            source: source
        },
        series: [{
            type: 'pie',
            radius: "50%",
            center: ['25%', '50%'],
            label:{            //饼图图形上的文本标签
                normal:{
                    show:true,
                    position:'inner', //标签的位置
                    textStyle : {
                        fontWeight : 300 ,
                        fontSize : 16    //文字的字体大小
                    },
                    formatter:'{d}%'
                }
            },
            startAngle: 45, // 起始角度 45
            clockwise: false, // 逆时针
            markLine:{
                lineStyle: {
                    type: 'solid',
                    color:"#ffffff"
                },
                symbol: 'none',
                data:markLineData
            },

        },
            {
                type: 'pie',
                radius: "30%",
                center: ['75%', '50%'],
                encode: {
                    itemName: '贷款等级情况',
                    value: '2016',
                },
                label: {
                    show: true,
                    position: "inside"
                },
                itemStyle: {
                    normal: {
                        color: function (params) {
                            //自定义颜色
                            var colorList = ['#F68944', '#FBC10D', '#DCE02A', '#96E043', '#42D43F', '#10B680'];
                            return colorList[params.dataIndex]
                        },
                    }
                }
            }
        ]
    };

// 获取表标线 对应点坐标
    function getMarkLineData(percent) {
        // 1.获取画布 width,height
        let height = myChart8.getHeight();
        let width = myChart8.getWidth() ;

        // 2.  根据 series[0].center 获取圆心坐标
        let x0 = width*0.25 ;// 圆心x轴坐标

        //3.圆边上点坐标
        // let x1   =   x0   +   r   *   cos(ao   *   3.14   /180   )
        // let y1   =   y0   +   r   *   sin(ao   *   3.14   /180   )

        // “其他” 终点坐标series[0].startAngle 45
        let x1 = x0 + (height/4) * Math.cos(45 * 3.14 / 180);
        let y1 = (height*0.5)   -   (height/4)   *   Math.sin(45   *   3.14   /180   );

        let ao = 360 * (percent/100) ;// 扇形角度

        let ao1 = 0 ;// 用来计算的坐标角度
        ao1=(ao<=45)?(45-ao):(360-(ao-45));
        if(ao1<270 && ao1>45)ao1=270 ;// 角度当270用，要不样式不好看

        let x2=0,y2=0;
        x2=x0 + (height/4) * Math.cos(ao1 * 3.14 / 180);
        y2 = (height*0.5)  -   (height/4)   *   Math.sin(ao1   *   3.14   /180   );

        return [[{x:x1,y:y1},{x: "75%", y: "35%"}],[{x:x2,y:y2},{x: "75%", y: "65%"}]]
    }
// 添加其他
    function addOtherData(datasetSource,len){
        let percent = 0;
        let sum=0 ;// 总计
        datasetSource.forEach((data,rowIndex)=>{
            if(rowIndex>0){ // 第一行数据不算
                let count=0;
                for(let key of data){
                    let value = isNaN(key)?0:Number(key);
                    if(count===1)sum+=value;
                    count++
                }
            }
        });
        let endData = datasetSource.slice(datasetSource.length-len);
        let other = ["异常"];
        for(let i=0;i<endData.length;i++){
            let j=0;
            for(let key of endData[i]){
                let value = isNaN(key)?0:key;
                if(j)other[j]?(other[j]+=value):other.push(value);
                j++
            }
            endData[i].splice(1,0,"")
        }
        datasetSource.push(other);
        // "其他"占比
        percent = sum?((other[1]/sum)*100).toFixed(2):100;
        markLineData = getMarkLineData(percent)
    }
    myChart8.setOption(option);
    tools.loopShowTooltip(myChart8, option, {
        loopSeries: true
    });

});

