import time
import requests
from lxml import etree
import csv
import os
cookie='Cookie: user_trace_token=20220419211913-b7b2b0cb-75c5-4b2f-95d6-a608b5d5195e; _ga=GA1.2.1195128002.1650374355; LGUID=20220419211914-af1a0d60-be95-4f3b-bae1-de38adbb916c; RECOMMEND_TIP=true; _gid=GA1.2.241335308.1650374361; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; LG_HAS_LOGIN=1; hasDeliver=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=d73449a6c9b881435b2d3e004ba96a9f79ee97f8e0b5596a0d10b9d5072edc22; LG_LOGIN_USER_ID=745cf30d5a8ad6bfb4fa671b453ceaa63f488e1c52fadf5e6153f09e9f40a1e9; __lg_stoken__=76fc9d9a06cada08e94f14690c2d8ab1ef91d8769ef157d60eeefa00f5201f7a47290a5ff0e2de304f67ebdf47106c35fec3bf6d36a9895ce5733315512f0fa0a733ca0aafff; __SAFETY_CLOSE_TIME__24370519=1; JSESSIONID=ABAAAECABFAACEAA41BFFB241809124C9E950B57257A627; WEBTJ-ID=20220422171857-18050913de74bf-090ef6a51fd84-f791539-1327104-18050913de81029; _gat=1; _putrc=DC55DEE7E3E2F979123F89F2B170EADC; LGSID=20220422171857-1805b737-065c-410e-983f-2ef9626e7d5d; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5F%2Fp-city%5F0%3F%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2224370519%22%2C%22first_id%22%3A%2218041fa442b101-086afcef7c08ab-f791539-1327104-18041fa442c3a3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22pctop%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2297.0.4692.99%22%2C%22lagou_company_id%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218041fa442b101-086afcef7c08ab-f791539-1327104-18041fa442c3a3%22%7D; login=true; unick=%E7%94%A8%E6%88%B72179; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1650378405,1650516565,1650611382,1650619138; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1650619139; SEARCH_ID=c925e2fcef91401a855c0454fdb5ae47; LGRID=20220422171923-e35261aa-4b85-49ab-9490-4d87bfaa3bcb; X_HTTP_TOKEN=0a5d926f71c0a26c361916056100bc03d752993740'
print(('你是否想设置Cookie?(y/n)'))
judge=''
while True:
    judge=input("")
    if judge == 'y':
        cookie = input('请输入Cookie:')
        break
    elif judge == 'n':
        break
    else:
        print("请输入y/n")

headers={

# 数据跳转
'Referer':'https://www.lagou.com/zhaopin/Java/?filterOption=3&sid=ea664570b0b34a12a3b47bf2a57c80d4',
# 请求头
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',

'Cookie':cookie

}

# 嵌入式软件工程师
def Spider1(url):
    response=requests.get(url,headers=headers,timeout=5,verify=0)
    result=[]
    r=response.text
    html=etree.HTML(r)
    num=1
    while num<=15:

        xpath_gangwei='//*[@id="jobList"]/div[1]/div[%d]/div[1]/div[1]/div[1]/a/text()[1]'%num
        xpath_money='//*[@id="jobList"]/div[1]/div[%d]/div[1]/div[1]/div[2]/span/text()'%num
        xpath_gongsi='//*[@id="jobList"]/div[1]/div[%d]/div[1]/div[2]/div[1]/a/text()'%num
        xpath_didian='//*[@id="jobList"]/div[1]/div[%d]/div[1]/div[1]/div[1]/a/text()[2]'%num
        xpath_jingyan='//*[@id="jobList"]/div[1]/div[%d]/div[1]/div[1]/div[2]/text()'%num
        xpath_jineng='//*[@id="jobList"]/div[1]/div[%d]/div[2]/div[1]//text()'%num
        xpath_gongsiqianjing='//*[@id="jobList"]/div[1]/div[%d]/div[2]/div[2]/text()'%num
        xpath_gongsixingzhi='//*[@id="jobList"]/div[1]/div[%d]/div[1]/div[2]/div[2]/text()'%num

        result_gangwei=html.xpath(xpath_gangwei)
        result_jineng=html.xpath(xpath_jineng)
        result_money=html.xpath(xpath_money)
        result_jingyan=html.xpath(xpath_jingyan)
        result_didian=html.xpath(xpath_didian)
        result_gongsi=html.xpath(xpath_gongsi)
        result_gongsixingzhi=html.xpath(xpath_gongsixingzhi)
        result_gongsiqianjing=html.xpath(xpath_gongsiqianjing)
        result.append([result_gangwei,result_jineng,result_gongsi,result_jingyan,result_money,result_gongsixingzhi,result_didian,result_gongsiqianjing])
        num+=1
    return result




def deal(kd,start,end):

    with open(kd+'/'+kd+"合集.csv","w",encoding='utf8',newline="")as fpw:
        i=start
        while i<=end:
            path =kd+'/'+kd+'%d.csv' % i
            with open(path, 'r', encoding='utf8') as fpr:
                while True:
                    line = fpr.readline()
                    if line == '':
                        break
                    line=(line.replace('"','').replace(" ","").replace("\\n","").replace('[',"")).strip().strip(']')
                    # print(line)
                    line_list=line.split('],')
                    print(line_list)
                    try:
                        for index in range(8):
                            line_list[index]=line_list[index].replace("'","")
                            if index==2:
                                line_list[index] = line_list[index].replace(',','')
                            if index==6:
                                line_list[index]=line_list[index].replace('"',"").replace("”","")
                    except:
                        pass
                    print(line_list)
                    csvWriter = csv.writer(fpw)
                    csvWriter.writerow(line_list)
            i += 1
    pass

kd=input('请输入想爬取内容：')
start=int(input('请输入开始页（1~30）：'))
end=int(input('请输入截至页：'))
page=start
if not os.path.exists(kd):
    os.mkdir(kd)
count=0
while page<=end:
    url=f"https://www.lagou.com/wn/jobs?pn={page}&kd={kd}&city=%E5%85%A8%E5%9B%BD"
    print("\n正在爬取第%d页\n" % page)
    print("url:\t", url)
    path =kd+'/'+ kd + str(page)+'.csv'
    spider = Spider1(url)

    if spider[0]==[[], [], [], [], [], [], [], []] :
        print("\n请求失败\n")
        time.sleep(5)
        count+=1
        if count==5:
            print('触发反爬，请设置cookie或稍后再试（可考虑适当所要获取的减少数据量）或无查询内容')
            break
        continue
    print(spider)
    count=0
    with open(path, "w", encoding='utf8', newline='') as fp:
        csvWriter = csv.writer(fp)
        for i in spider:
            csvWriter.writerow(i)
            print(i)

    time.sleep(3)
    page+=1
deal(kd,start,end)
print(f"\n完成,请在当前路径查找{kd}文件夹!")
print('注意，此时直接打开csv文件可能会出现乱码，可在Excle中导入csv文件需手动去重')
input('双击回车退出')
input('双击回车退出')