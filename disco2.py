import requests,random,re,time,linecache
from random import choice
def get_count(url,k ,proy):
        #print(k)
        header={'imei':k,'platform':'android','systemVersion':'8.1.0',
                'channel':'GW','user-agent':'okhttp/3.14.1',
                'appVersion':'1.0.7','Accept':'application/json',
                'versioncode':'7'}
        r=requests.post(url,headers=header,data='h4DTanVobu8H5znghXQnjJLBMCgx+wNbIYtieex/Nfo=',proxies=proy,timeout=4).text
        #print(r)
        tk=re.findall(r'(?<="token":").+(?=","expiredIn")',r)
        return tk
def invite_active(url2,k,tk,invitecode,proy):  #X4FBDHNSRZXT
        tk1='Token '+tk[0]
        #print(tk1)
        header = {'authorization':tk1,'imei': k, 'platform': 'android', 'systemVersion': '8.1.0',
                  'channel': 'GW', 'user-agent': 'okhttp/3.14.1',
                  'appVersion': '1.0.7', 'Accept': 'application/json',
                  'versioncode': '7'}
        date={'inviteCode':invitecode}
        r = requests.post(url2, headers=header, data=date,proxies=proy,timeout=4).text
        return r
def get_proxy():
    try:
        count=random.randrange(1,3)
        if count==1:
            #print('all')
            url='http://34.92.50.181:8080/get_all'
        else:
            #print('random')
            url='http://34.92.242.128:5555/random'
        response = requests.get(url=url,timeout=4)
        if response.status_code == 200:
                l=re.findall(r'\d+.\d+.\d+.\d+:\d+', response.text)
                return l
    except ConnectionError:
        return None
def get_invitecode():
    s=open('invite.txt','r')
    k=s.readlines()
    i=len(k)
    #print(i)
    if i==0:
        return False
    elif i==1:
        a=0
    else:
        i=i+1
        a = random.randrange(1,i)  # 1-9中生成随机数
        a=a-1
        # 从文件poem.txt中对读取第a行的数据
    #print(a)
    invitecode = k[a]
    #print(invitecode)
    s.close()
    return invitecode
def frist_write(invitecode): #判断是否第一次写入
     f=open('111.txt','r')
     s1=f.read()
     f.close()
     if invitecode in s1:
         return  True
     else:
         f=open('111.txt','a')
         f.write(invitecode+'邀请成功:1次!\n')
         f.close()
def find_invite(invitecode):
    #找到需要替换的
    f=open('111.txt','r')
    s=f.readlines()
    for line in s:
        if invitecode in line:
        #print('find')
            d=re.findall(r'(?<=邀请成功:).*(?=次!\n)',line)
            d=int(d[0])+1
            break
    return line,d
    f.close()
def re_line(line,d,invitecode):
    f=open('111.txt','r')
    s1=f.read()
    newline=invitecode+'邀请成功:'+str(d)+'次!\n'
    line=s1.replace(line,newline)
    #print(line)
    f.close()
    f=open('111.txt','w')
    f.write(line)
    f.close()
def invite_log_write(invitecode):
    if frist_write(invitecode):
        #print('not frist')
        line,d=find_invite(invitecode)
        re_line(line,d,invitecode)
def main():
        url = 'https://discovpn.com/api/v2/trial/'
        url2 = 'https://discovpn.com/api/v2/invite/active/'
        m = 1
        n = 0
        b = 0
        while True:
                #
                try:
                   invitecode=get_invitecode().replace('\n','')
                   while invitecode:
                        invitecode=get_invitecode().replace('\n','')
                        #invite_log_write(invitecode)
                        #print(len(invitecode))
                        #print(invitecode)
                        ip = get_proxy()
                        ip1 = choice(ip)
                        print(ip1)
                        # porxies = "http://" + porx.strip("\n")
                        proy = {'http': ip1, 'https': ip1}
                        #print(proy)
                        webdata = requests.post(url='http://icanhazip.com/', proxies=proy, timeout=4).text  # 查看>此时代理IP
                        #print(webdata)
                        time.sleep(2)
                        k = str(random.randint(10000000, 99999999))
                        tk = get_count(url, k, proy)
                        te = invite_active(url2, k, tk, invitecode, proy)
                        #print(te)
                        if 'success' in te:
                                #print('抓取好IP成功第'+str(m)+'次！')
                                invite_log_write(invitecode)
                                #log=open('/home/ouyangshazhu/ok_ip_proxy_pool/history_log/'+invitecode+'.txt','a')
                                print(invitecode+'-' +'邀请成功1次！')
                                #print(te)
                                #log.write('-' * 20 + '邀请成功' + str(1) + '次！' + '-' * 20+'\n')
                                #log.close()
                                m=m+1
                        else:
                                log = open('/home/ouyangshazhu/ok_ip_proxy_pool/history_log/'+invitecode+'.txt','a'
)
                                b = 1
                                print(invitecode+'-' +'邀请失败1次！')
                                log.write('-' * 20 + '邀请失败' + str(n) + '次！' + '-' * 20 + '\n')
                                log.close()
                except:
                    None
        #print('邀请结束\n成功：' + str(n) + '次!\n失败：' + str(b) + "次！")
if __name__ == "__main__":
    main()

