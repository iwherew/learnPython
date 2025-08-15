import json

from data_define import Record
from pyecharts.charts import Bar
from pyecharts import options as opts

file1 = open("2011年1月销售数据.txt","r",encoding="utf-8")

record_list: Record = []

for line in file1:
    item = line.strip().split(',')
    record_list.append(Record(item[0], item[1], item[2], item[3]))

file1.close()

file2 = open("2011年2月销售数据JSON.txt",'r',encoding="utf-8")

for line in file2:
    item = json.loads(line)
    record_list.append(Record(item['date'], item['order_id'], item['money'], item['province']))

file2.close()

sum_list = {}
for record in record_list:
    if(record.date in sum_list):
        sum_list[record.date] += int(record.money)
    else:
        sum_list[record.date] = int(record.money)

(Bar().add_xaxis(list(sum_list.keys()))
 .add_yaxis('销售额', list(sum_list.values()))
 .set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),
)
 .render())