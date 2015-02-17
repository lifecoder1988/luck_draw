var smart = (function(s) {
  s.init_highcharts = function(charts) {
      charts.setOptions({
            chart: {
                style: {
                    fontSize: '150%'
                }
            },
            title: {
                style: {
                    fontSize: '100%'
                }
            },
            legend: {
                itemStyle: {
                    fontSize: '50%',
                    fontWeight: 'normal'
                }
            },
            xAxis: {
                labels: {
                    style: {
                        fontSize: '60%' //刻度字体大小
                    },
                    rotation: 0 //竖直放
                }
            },
            yAxis: {
                labels: {
                    style: {
                        fontSize: '60%' //刻度字体大小
                    },
                },
                title: {
                    style: {
                        fontSize: '60%'
                    },
                    rotation: -90 //竖直放
                }
            },
            credits: {
                enabled: false
            },
            plotOptions: {
                line: {
                    dataLabels: {
                        style: {
                            fontSize: '50%'
                        },
                        enabled: true
                    }
                },
                pie: {
                    dataLabels: {
                        style: {
                            fontSize: '50%'
                        }
                    }
                },
                column: {
                    dataLabels: {
                        style: {
                            fontSize: '30%'
                        }
                    }
                },
            }
        });
        return "success"
	};
	return s;

})(smart || {});