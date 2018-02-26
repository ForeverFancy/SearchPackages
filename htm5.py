import json,requests
def searchPackage():
    #输入运单号码，注意，只有正在途中的快递才可以查到！
    packageNum = input('请输入运单号码：')
    url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum
    #用url1查询运单号对应的快递公司，如中通，返回：zhongtong。

    company=json.loads(requests.get(url1).text)['auto'][0]['comCode']

    url2 = 'http://www.kuaidi100.com/query?type=' + company + '&postid=' + packageNum
    mess=requests.get(url2).text
    dateAndLocation=json.loads(mess)
    if dateAndLocation['message']=='ok':
        for item in dateAndLocation['data']:
            print(item['time'],item['context'])
    else:
        print("出错啦")

if __name__ =='__main__':
    searchPackage()