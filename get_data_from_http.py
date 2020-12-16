import requests
import re
import time
import csv
def get_all_page():
    global all_page
    url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html"
    reponse = requests.get(url=url)
    reponse.encoding = 'utf-8'
    html = reponse.text
    all_page = int(re.findall(r"class=\"pg\".*?<strong>(.*?)</strong>", html)[0])
    return all_page

def get_num():
    result = []
    for page_num in range(1, all_page + 1):
        url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_" + str(page_num) + ".html"
        reponse = requests.get(url=url)
        time.sleep(2)
        reponse.encoding = 'utf-8'
        html = reponse.text
        # rule = r"<tr>.*?<td align=\"center\">(.*?)</td>.*?<td align=\"center\">(.*?)</td>.*?<td align=\"center\" style=\"padding-left:10px;\">.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em>(.*?)</em></td>"
        rule = r"<tr>.*?<td align=\"center\">(.*?)</td>.*?<td align=\"center\">(.*?)</td>.*?<td align=\"center\" style=\"padding-left:10px;\">.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em class=\"rr\">(.*?)</em>.*?<em>(.*?)</em></td>.*?<td><strong>(.*?)</strong></td>.*?<td align=\"left\" style=\"color:#999;\"><strong>(.*?)</strong>.*?</td>.*?<td align=\"center\"><strong class=\"rc\">(.*?)</strong></td>"

        num = re.findall(rule, html, re.S | re.M)

        for k in range(0, len(num)):
            cost_str = num[k][9]
            cost = 0
            for i in range(len(cost_str)-1, 0, -1):
                if cost_str[i] == ',':
                    continue
                cost = cost*10 + int(cost_str[i])
            result.append([str(num[k][0]), str(num[k][1]), int(num[k][2]), int(num[k][3]), int(num[k][4]), int(num[k][5]), int(num[k][6]), int(num[k][7]), int(num[k][8]),
                           int(cost), int(num[k][10]), int(num[k][11])])
            # print(kjrq, qs, red_ball, blue_ball)
        # return result
    return result

if __name__ == '__main__':
    get_all_page()
    res = get_num()


    csv_file = './data.csv'
    with open(csv_file, 'w', newline='') as f:
        header = ['date', 'issue', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'cost', 'one', 'two']
        writer = csv.writer(f)
        writer.writerow(header)
        for item in res:
            writer.writerow(item)