import requests
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def removeInvalidProxies(testUrl):
    global proxies
    global executor
    rqs = []
    for i in range(len(proxies) - 1, -1, -1):
        #
        curRq = {'proxy': proxies[i],
                   'req': executor.submit(requests.get, url=testUrl, proxies=setProxyPort(proxies[i]), timeout=10),
                   }
        rqs.append(curRq)

    goodRqs = []
    for curRq in rqs:
        print('curProxy : ' + str(curRq['proxy']))
        try:
            rq = curRq['req']
            content = rq.result()
            print('Response Content: ' + content.content)
            curRq['content'] = content.content
            goodRqs.append(curRq)
        except Exception as e:
            print(str(e))
            print("removing Port " + str(curRq['proxy']))
            proxies.remove(curRq['proxy'])
    goodRqs.sort(key=lambda x: proxies.index(x['proxy']))
    return goodRqs

def setProxyPort(proxy):
    if proxy is None:
        return None
    proxyDict = {
        'http': proxy,
        'https': proxy
    }
    return proxyDict

def getDefaultParams():
    return {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://friboi.com.br',
        'Referer': 'https://friboi.com.br/cadeia-produtiva/cadeia-fornecimento',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

def filterHighAnonymity():
    global proxies

    goodProxies = removeInvalidProxies('http://httpbin.org/ip')
    alreadyFoundIps = []
    for curTest in goodProxies:
        if (curTest['content'] in alreadyFoundIps) == True:
            proxies.remove(curTest['proxy'])


#Configuration Parameters
urlToTest = 'https://friboi.com.br/cadeia-produtiva/cadeia-fornecimento'
executor = ThreadPoolExecutor(max_workers=20)
iProxy = 0
qntOfTests = 3
onlyHighAnonymity = True #Filter only High Anonymity Proxies
proxies = [None, "187.73.68.14:53281",
"189.127.106.16:53897",
"186.225.106.114:46312",
"187.63.82.55:51769",
"186.219.210.86:52338",
"177.70.35.101:80",
"186.248.170.82:53281",
"177.53.59.96:55427",
"189.51.98.182:56906",
"186.224.229.105:53943",
"189.51.101.126:39108",
"186.193.37.21:52750",
"200.174.158.26:34112",
"187.44.177.178:41178",
"177.92.17.186:23500",
"177.53.8.125:47970",
"187.62.191.3:61456",
"200.205.21.66:8081",
"186.226.179.2:56089",
"177.101.253.43:8080",
"177.99.162.210:44456",
"201.59.201.92:40417",
"187.111.192.198:59114",
"201.86.99.130:39900",
"187.87.204.210:45597",
"177.23.104.114:38107",
"200.153.145.174:54748",
"187.111.192.202:52412",
"200.137.138.2:80",
"186.235.158.53:45403",



"200.217.168.98:4145",
"138.36.2.47:4145",
"45.70.205.105:4145",
"177.87.15.105:4145",
"168.194.164.96:1080",
"200.7.118.10:61441",
"191.243.79.252:4145",
"187.19.114.1:4145",
"138.99.93.224:4145",
"186.208.109.234:4145",
"189.126.67.230:33499",
"45.231.121.207:4145",
"170.79.169.78:4145",
"170.79.121.56:4145",
"170.244.0.178:4145",
"177.104.193.144:41443",
"191.253.80.114:4145",
"179.125.25.218:58273",
"200.53.216.153:57720",
"186.219.3.136:4145",
"177.87.14.73:4145",
"170.79.121.37:4145",
"186.219.96.193:57791",
"200.146.229.129:8291",
"200.220.202.1:4145",
"177.152.127.224:4145",
"177.86.44.100:31337",
"191.7.198.246:4145",
"177.86.158.181:33420",
"177.223.0.1:4145",
"170.84.48.105:55731",
"191.243.200.245:4145",
"170.238.160.4:4145",
"187.95.123.75:43573",
"177.223.1.89:4145",

"186.233.104.25:8080",
"177.91.127.56:43014",
"168.195.231.136:8080",
"189.89.243.142:42443",
"200.153.145.174:54748",
"189.125.170.36:80",
"187.111.192.198:59114",
"177.222.229.243:23500",
"138.204.23.89:53281",
"186.225.56.210:39018",
"160.19.245.59:48234",
"189.89.246.242:50832",
"191.5.0.79:53281",
"177.44.88.168:33922",
"177.86.158.102:38709",
"186.226.183.170:42315",
"200.170.144.185:8080",
"187.73.68.14:53281",
"191.240.156.154:36127",
"187.19.146.41:80",
"177.53.8.83:53514",
"179.124.240.210:56869",
"187.94.31.237:33296",
"177.92.20.182:55361",
"186.250.55.149:43844",
"138.0.77.30:80",
"201.16.156.220:80",
"45.4.237.72:42664",
"177.103.186.7:56030",
"191.36.244.230:51377",
"200.150.86.138:44677",
"187.62.191.3:61456",
"186.249.213.65:52018",
"187.111.192.50:33620",
"138.97.12.150:51431",

"201.86.99.130:39900",
"200.233.220.166:59694",
"177.72.72.217:54468",
"200.206.50.66:42515",
"187.60.161.75:8081",
"187.44.177.178:41178",
"200.0.46.50:37232",
"177.94.206.67:60666",
"186.225.106.114:46312",
"201.67.41.214:39849",
"177.99.162.210:44456",
"177.103.186.7:56030",
"200.199.114.226:33932",
"177.101.253.43:8080",
"186.216.81.21:31773",
"187.16.43.242:38278",
"187.111.160.29:40098",
"177.53.57.154:57984",
"187.111.160.8:42579",
"200.170.144.185:8080",
"200.233.134.85:43172",
"189.51.98.182:56906",
"177.75.143.211:35955",
"187.111.192.198:59114",
"187.62.191.3:61456",


"169.57.157.148:80",
"170.231.112.35:53281",
"45.70.218.102:45697",
"186.219.211.6:47982",
"200.137.138.2:80",
"200.187.18.225:80",
"177.37.161.4:59579",
"177.136.32.190:8080",
"138.204.179.162:44088",
"187.111.192.202:52412",
"128.201.97.154:53281",
"201.71.186.6:8081",
"200.174.158.26:34112",
"177.75.4.34:80",
"201.131.224.21:56200",
"200.187.18.247:80",
"177.54.200.65:54684",
"191.240.157.186:53556",
"45.70.60.98:43046",
"200.142.120.90:42827",
"191.241.166.248:41288",
"200.195.55.186:8080",
"45.6.136.245:53281",
"179.189.225.58:41881",
"186.249.213.101:53482",
"200.153.145.174:54748",
"200.225.140.130:56178",
"179.183.124.228:44456",
"128.201.97.155:53281",
"187.62.191.3:61456",
"191.7.193.50:61998",
"177.105.192.126:55715",
"138.36.106.251:42651",
"201.86.99.130:39900",
"191.7.201.45:53230",
"169.57.157.148:80",

"177.136.32.190:8080",
"177.101.253.43:8080",
"45.235.87.65:53781",
"200.195.55.186:8080",
"200.170.144.185:8080",
"168.195.231.136:8080",
"186.227.53.50:8080",
"186.229.25.18:8080",
"45.227.156.105:50013",
"201.71.186.6:8081",
"200.24.84.4:39136",
"200.225.140.130:56178",
"200.137.138.2:80",
"191.240.157.186:53556",
"186.227.112.78:6699",
"186.226.179.2:56089",
"186.225.56.210:39018",
"186.224.229.105:53943",
"177.67.8.223:48314",
"177.47.193.17:21231",
"177.38.232.40:30618",
"177.12.80.50:50556",
"170.78.60.134:49965",
"168.195.228.114:43109",
"138.204.179.162:44088",
"138.121.32.133:23492",
"131.255.35.193:36922",
"131.108.116.92:44949",
"191.240.149.161:8080",
"170.84.51.74:53281",

"189.89.246.242:50832",
"189.51.98.118:48704",
"189.51.98.182:56906",
"186.226.172.170:23500",
"177.75.143.211:35955",
"45.226.48.38:60143",
"187.16.109.209:9999",
"192.140.42.83:52852",
"200.233.147.133:8082",
"187.111.160.8:42579",
"189.45.42.148:53599",
"187.120.221.165:8888",
"186.226.183.170:42315",
"187.87.204.210:45597",
"186.249.213.65:52018",
"186.249.209.194:9999",
"200.170.144.185:8080",
"187.73.68.14:53281",
"45.70.218.102:45697",
"200.137.138.2:80",
"177.103.186.7:56030",
"189.113.217.35:53264",
"201.20.73.77:31071",
"170.82.73.140:53281",
"186.235.158.53:45403",
"131.255.35.193:36922",
"187.63.25.125:31110",
"177.92.17.186:23500",
"143.255.52.102:40687",
"201.59.201.92:40417",
"187.63.82.55:51769",
"186.211.248.214:44385",
"186.226.179.2:56089",
"186.233.98.173:23500",
"187.109.210.153:47351",
"177.86.158.102:38709",
"200.192.243.137:31497",
"187.111.192.202:52412",
"200.153.145.165:8080",
"200.233.220.166:59694",
"200.195.55.186:8080",
"177.53.59.96:55427",
"177.53.57.154:57984",
"191.240.156.154:36127",
"143.255.52.118:58909",
"186.206.151.154:3128",

"177.92.160.254:54868",
"177.221.176.80:35042",
"187.120.253.119:30181",
"187.45.106.176:8080",
"192.140.42.83:52852",
"201.62.56.49:35816",
"177.67.10.15:48314",
"143.255.52.118:58909",
"200.174.158.26:34112",


"189.89.243.142:42443",
"177.92.160.254:54868",
"177.221.176.80:35042",
"192.140.42.83:52852",
"201.62.56.49:35816",
"177.67.10.15:48314",
"143.255.52.118:58909",
"200.174.158.26:34112",
"45.230.176.232:23500",
"179.97.31.41:53100",
"168.227.229.102:33401",

"200.165.160.18:3128",
"189.52.165.134:1080",
"189.125.170.36:80",
"189.125.170.36:80",
"191.53.112.170:35618",
"170.84.51.74:53281",
"189.45.199.37:20183",
"187.115.10.50:20183",
"187.108.36.250:20183",
"191.243.54.245:41599",
"200.206.70.162:20183",


"177.92.67.230:53281",
"200.153.145.174:54748",
"200.186.53.98:58855",
"189.51.101.126:39108",
"138.121.32.26:23500",
"177.221.176.80:35042",
"200.142.120.90:42827",
"200.170.144.185:8080",
"200.137.138.2:80",
"138.121.32.133:23492",
"131.0.87.225:40758",
"168.194.201.6:8888",
"191.241.166.255:41288",
"177.53.8.83:53514",
"186.233.104.25:8080",
"179.127.166.239:80",
"200.186.53.14:58855",
"160.19.245.59:48234",
"200.0.46.50:37232",
"191.243.217.1:53281",
"170.84.49.229:53281",
"168.227.229.102:33401",
"186.216.81.21:31773",
"128.201.97.154:53281",
"138.97.116.175:57537",
"168.196.204.31:52821",
"131.255.33.25:36922",
"177.128.124.200:48582",
"168.194.86.22:53281",
"177.126.216.149:39353",
"200.222.31.146:51271",
"187.63.162.165:23500",
"131.161.68.37:31264",
"187.111.192.198:59114",
"186.227.112.68:6699",
"186.227.112.75:6699",
"186.193.37.21:52750",
"177.222.229.243:23500",
"200.212.2.80:45612",
"191.7.200.174:53230",
"186.219.210.209:54626",
"168.194.84.141:53281",
"191.241.167.251:41288",
"187.60.36.164:53597",
"177.47.194.98:21231",
"187.16.109.209:8888",
"191.241.166.254:41288",
"200.223.86.171:44525",
"177.105.232.228:36001",
"186.227.112.74:6699",
"168.196.207.201:52821",



#contem anonymous
"200.174.158.26:34112",
"177.94.206.67:60666",
"201.49.37.133:80",
"187.72.89.126:41846",
"177.53.59.96:55427",
"187.19.146.41:80",
"186.248.170.82:53281",
"177.75.143.211:35955",
"186.211.248.214:44385",
"189.51.101.126:39108",
"187.16.43.242:38278",
"200.150.86.138:44677",
"200.137.138.2:80",
"201.49.58.227:80",
"177.53.57.154:57984",
"201.59.201.92:40417",
"187.87.204.210:45597",
"186.226.179.2:56089",
"189.125.170.36:80",
"201.86.99.130:39900",
"187.111.160.8:42579",
"186.225.56.210:39018",
"200.153.145.174:54748",
"186.232.15.9:45849",
"187.111.192.146:51281",
"189.51.98.182:56906",
"200.205.21.66:8081",
"177.99.162.210:44456",
"186.235.158.53:45403",
"200.255.122.170:8080",
"200.255.122.174:8080",
"201.67.41.214:39849",
"187.72.56.151:80",
"200.206.50.66:42515",
"187.108.86.40:56183",


"177.99.162.210:44456",
"201.59.201.92:40417",
"186.232.15.9:45849",
"200.255.122.174:8080",
"187.72.89.126:41846",
"177.53.59.96:55427",
"189.127.106.16:53897",
"186.211.248.214:44385",
"200.174.158.26:34112",
"189.43.68.163:8080",
"189.45.42.148:53599",
"186.225.56.210:39018",
"187.16.43.242:38278",
"189.51.98.182:56906",
"200.255.122.170:8080",
"187.111.192.198:59114",
"200.205.21.66:8081",
"200.137.138.2:80",
"187.63.82.55:51769",
"177.92.17.186:23500",
"186.224.229.105:53943",
"187.111.192.146:51281",
"187.72.56.151:80",
"201.86.99.130:39900",
"200.233.220.166:59694",
"200.206.50.66:42515",
"201.49.58.227:80",
"177.53.57.154:57984",
"187.111.160.8:42579",
"200.150.86.138:44677",
"187.44.167.78:60786",
"187.19.146.41:80",
"187.108.86.40:56183",
"189.125.170.36:80",
"201.49.37.133:80",
"187.111.160.29:40098",
"177.75.143.211:35955",
"200.153.145.174:54748",
"201.67.41.214:39849",
"187.73.68.14:53281",
"189.51.101.126:39108",


"177.184.202.217:3128",
"192.141.12.70:8080",
"201.32.65.30:8080",
"177.185.93.77:8080",
"177.10.201.219:8080",
"187.62.209.155:8080",
"201.26.179.96:8080",
"186.237.221.27:8080",
"177.66.67.185:8080",
"181.223.84.177:8080",
"201.87.243.22:8080",
"177.184.207.17:8080",
"177.105.232.124:8080",
"191.243.221.130:3128",
"45.233.218.254:8080",
"177.136.32.190:8080",
"179.191.245.58:3128",
"138.219.223.166:3128",
"187.16.4.121:8080",
"187.45.123.118:8080",
"189.61.248.107:8080",
"200.240.244.7:8080",
"189.91.124.80:8080",
"186.250.119.137:8080",
"177.184.66.13:8080",
"181.191.85.114:8080",
"187.62.195.145:8080",
"187.87.76.251:3128",
"45.170.112.10:8080",
"177.220.188.213:8080",
"170.81.157.82:8080",
"200.215.171.238:8080",
"177.44.223.178:8080",
"168.228.120.22:8080",
"179.96.18.113:8080",
"186.192.98.250:8080",
"160.19.243.36:8080",
"138.94.91.2:8080",
"177.91.219.28:8080",
"138.118.173.21:3128",
"177.46.148.142:3128",
"170.247.156.71:8080",
"187.103.89.202:8080",
"170.233.123.146:8080",
"168.227.213.83:8080",
"191.252.196.79:3128",
"170.244.99.43:8080",
"186.195.91.4:8080",
"187.58.65.225:3128",
"45.166.244.175:8080",
"45.224.173.254:8080",
"177.66.221.5:8080",
"45.234.144.106:8080",
"177.125.61.226:3128",
"168.232.20.155:8080",
"168.181.196.71:8080",
"201.49.89.221:8080",
"138.185.22.130:8080",
"45.224.44.15:8080",
"138.118.34.25:8080",
"177.36.137.6:8080",
"187.18.125.34:3128",
"167.249.181.191:3128",
"200.159.250.2:3128",
"179.109.1.93:8080",
"177.101.253.43:8080",
"177.184.207.125:8080",
"45.235.87.65:53781",
"186.250.29.225:8080",
"177.184.83.235:20183",
"201.75.5.168:8080",
"187.19.204.23:20183",
"189.50.145.18:8080",
"200.5.32.211:8080",
"187.1.32.108:8080",
"45.169.172.2:3128",
"177.8.216.106:8080",
"177.20.235.241:8080",
"45.231.29.77:8080",
"186.193.20.59:3128",
"143.255.130.20:8080",
"179.124.137.189:8080",
"179.95.232.131:3128",
"179.189.27.28:8080",
"177.223.15.249:8080",
"45.232.244.105:8080",
"189.45.23.170:3128",
"177.202.59.58:8080",
"45.168.252.49:8080",
"170.80.85.1:8080",
"200.195.55.186:8080",
"45.228.147.22:8080",
"45.162.8.74:3128",
"168.232.64.52:8080",
"201.33.225.204:3128",
"187.103.74.137:8080",
"186.229.25.196:8080",
"186.201.208.180:8080",
"45.70.6.218:8080",
"200.170.144.185:8080",
"189.84.48.122:8080",
"168.194.250.5:8080",
"187.109.181.78:8080",
"186.193.26.106:3128",
"177.87.10.186:8080",
"179.156.172.154:8080",
"187.32.4.66:8080",
"170.244.106.238:8080",
"187.63.111.37:3128",
"179.127.35.10:8080",
"131.108.75.130:8080",
"138.122.13.149:8080",
"177.185.151.101:8080",
"45.70.193.102:8080",
"186.250.56.135:8080",
"190.93.176.70:8080",
"179.107.84.65:8080",
"189.30.181.98:8080",
"186.225.157.22:8080",
"179.252.22.210:8080",
"131.161.26.90:8080",
"191.241.36.162:8080",
"170.82.52.48:8080",
"177.124.10.53:8080",
"189.85.22.97:8080",
"170.79.95.128:8080",
"168.195.231.136:8080",
"45.70.195.175:8080",
"45.70.194.43:8080",
"45.228.119.16:8080",
"191.7.45.215:8080",
"177.55.189.88:8080",
"186.227.53.50:8080",
"138.219.133.22:8080",
"187.84.141.62:8080",
"201.18.98.18:8080",
"131.161.35.1:8080",
"177.206.181.85:8080",
"186.215.222.82:8080",
"200.202.229.218:8080",
"200.149.19.130:8080",
"131.161.176.101:8080",
"187.106.93.217:8080",
"170.254.151.98:3128",
"181.191.180.110:8080",
"181.213.69.57:8080",
"201.20.106.186:8080",
"160.238.176.197:8080",
"189.5.193.19:3128",
"201.20.107.94:8080",
"187.62.45.130:3128",
"177.129.207.23:8080",
"177.185.156.241:8080",
"45.170.68.15:8080",
"177.184.192.50:3128",
"45.226.20.6:8080",
"170.233.148.202:8080",
"168.0.140.183:8080",
"177.125.243.12:3128",
"201.49.58.227:80",
"186.229.25.18:8080",
"143.255.52.90:8080",
"177.185.159.62:8080",
"170.231.59.141:8080",
"131.255.8.102:8080",
"170.233.123.106:8080",
"200.229.227.201:8080",
"201.47.171.146:3120",
"200.141.135.234:8080",
"131.255.101.9:8080",
"187.16.34.138:8080",
"177.221.95.118:8080",
"177.66.54.199:8080",
"177.38.243.102:8080",
"187.45.152.78:8080",
"177.137.193.67:80",
"177.43.104.19:8080",
"45.230.215.45:8080",
"45.227.156.105:50013",
"201.71.186.6:8081",
"200.24.84.4:39136",
"200.225.140.130:56178",
"200.137.138.2:80",
"191.7.219.62:9191",
"191.240.157.186:53556",
"189.2.81.57:8080",
"187.62.195.39:8080",
"187.16.32.97:8080",
"187.108.38.10:20183",
"186.227.112.78:6699",
"186.226.179.2:56089",
"186.225.56.210:39018",
"186.224.229.105:53943",
"186.212.154.83:8080",
"186.193.229.38:8080",
"186.192.253.17:8000",
"179.97.53.154:3128",
"177.99.91.239:8080",
"177.87.79.90:8081",
"177.69.122.180:8080",
"177.67.8.223:48314",
"177.47.193.17:21231",
"177.38.232.40:30618",
"177.32.111.96:8080",
"177.200.89.22:8080",
"177.185.131.206:3128",
"177.136.185.200:80",
"177.125.43.26:8080",
"177.12.80.50:50556",
"177.107.52.130:3129",
"170.78.60.134:49965",
"170.247.17.90:8080",
"168.90.248.196:8080",
"168.195.228.114:43109",
"138.99.90.113:8080",
"138.204.179.162:44088",
"138.121.32.133:23492",
"138.0.210.97:80",
"131.255.35.193:36922",
"131.108.116.92:44949",
"177.74.112.162:8080",
"131.196.6.246:3128",
"177.124.57.214:8080",
"131.255.132.11:8080",
"45.168.74.6:8080",
"177.10.91.175:8080",
"191.240.149.161:8080",
"179.189.226.186:8080",
"200.155.36.188:3128",
"201.33.235.193:3128",
"201.20.77.237:8080",
"200.216.115.10:8080",

"191.240.149.161:8080",
"18.231.113.44:3128",
"177.136.32.190:8080",
"177.184.66.13:8080",
"177.46.148.142:3128",
"170.233.123.146:8080",
"191.252.196.79:3128",
"177.101.253.43:8080",
"45.235.87.65:53781",
"200.5.32.211:8080",
"200.195.55.186:8080",
"200.170.144.185:8080",
"168.195.231.136:8080",
"186.227.53.50:8080",
"201.49.58.227:80",
"186.229.25.18:8080",
"143.255.52.90:8080",
"170.233.123.106:8080",
"45.227.156.105:50013",
"201.71.186.6:8081",
"200.24.84.4:39136",
"200.225.140.130:56178",
"200.137.138.2:80",
"191.240.157.186:53556",
"186.227.112.78:6699",
"186.226.179.2:56089",
"186.225.56.210:39018",
"186.224.229.105:53943",
"177.67.8.223:48314",
"177.47.193.17:21231",
"177.38.232.40:30618",
"177.12.80.50:50556",
"170.78.60.134:49965",
"168.195.228.114:43109",
"138.204.179.162:44088",
"138.121.32.133:23492",
"138.0.210.97:80",
"131.255.35.193:36922",
"131.108.116.92:44949",
"170.84.51.74:53281",
"187.60.161.75:8081",
"177.131.95.200:8080",
"177.99.206.82:8080",
"200.223.86.171:44525",
"138.118.173.115:80",
"177.103.186.7:56030",
"179.185.114.206:80",
"177.46.149.22:32884",
"191.242.182.132:8081",
"189.57.214.162:33875",
"131.72.217.254:53281",
"45.166.86.6:8080",
"177.53.59.96:55427",
"186.194.120.72:8080",
"187.63.162.165:23500",
"177.67.219.1:61416",
"191.252.177.42:8080",
"143.137.220.46:33662",
"45.235.44.93:8080",
"54.207.60.214:8080",
"200.142.120.90:42827",
"177.46.141.143:36771",
"138.97.116.172:57537",
"187.16.226.93:3128",
"201.30.93.19:8080",
"191.240.154.246:8080",
"200.186.53.14:58855",
"187.17.145.237:30279",
"191.33.219.10:8080",
"138.121.32.26:23500",
"177.234.178.103:49066",
"179.125.177.31:8080",
"45.235.87.66:53781",
"186.225.250.26:60468",
"45.235.86.1:51996",
"170.239.46.177:58605",
"177.54.226.167:8080",
"201.86.99.130:39900",
"186.225.43.49:57701",
"191.54.62.255:3128",
"187.108.203.45:8080",
"177.92.160.254:54868",
"187.108.203.33:8080",
"45.235.87.4:51996",
"179.125.176.30:8080",
"186.250.55.149:43844",
"179.124.240.199:46318",
"200.206.50.66:42515",
"177.91.127.56:43014",
"186.233.98.158:34095",
"138.219.147.197:53281",
"138.36.20.43:34307",
"168.90.140.26:58790",
"177.223.16.141:8080",
"186.225.63.134:38459",
"187.108.203.41:8080",
"177.85.70.60:8080",
"177.46.147.89:35552",
"187.73.68.14:53281",
"200.233.134.85:43172",
"179.92.95.251:8080",
"187.120.253.119:30181",
"187.16.226.94:3128",
"45.4.237.72:42664",
"187.87.38.207:45644",
"191.7.193.50:61998",
"177.130.53.97:36354",
"189.51.98.118:48704",
"177.55.91.19:23500",
"189.113.217.35:53264",
"45.226.48.113:60143",
"138.36.107.24:41184",
"45.167.80.18:8080",
"45.164.42.22:8080",
"45.235.87.65:49192",
"45.234.200.18:53281",
"45.162.130.139:35909",
"45.162.82.6:3128",
"45.162.130.141:51113",
"45.162.130.139:34320",
"45.235.87.74:59725",
"45.235.87.65:59725",
"45.234.95.151:80",
"45.162.130.141:33039",
"45.235.44.84:3128",
"45.162.130.139:55852",
"45.162.130.139:54428",
"45.235.87.65:37213",
"45.163.72.158:8080",
"45.162.130.139:39127",
"45.168.189.219:3128",
"45.162.130.13:53120",
"45.234.68.4:54111",
"45.168.189.214:3128",
"45.234.95.148:3128",
"45.162.130.13:57253",
"45.162.130.16:32734",


"socks5h:200.233.147.133:8082",
"socks5h:168.194.201.6:9999",
"socks5h:187.120.221.165:9999",
"socks5h:187.16.109.209:9999",
"socks5h:186.249.213.113:9999",
"socks5h:189.112.125.209:9999",
"socks5h:186.249.209.194:9999",


"168.195.231.136:8080",
"200.153.145.174:54748",
"189.125.170.36:80",
"200.170.144.185:8080",
"186.225.56.210:39018",
"187.19.146.41:80",
"191.240.156.154:36127",
"187.73.68.14:53281",
"186.216.81.21:31773",
"177.53.8.83:53514",
"138.121.32.26:23500",
"179.124.240.210:56869",
"201.16.156.220:80",
"138.0.77.30:80",
"186.211.248.214:44385",
"191.36.244.230:51377",
"200.150.86.138:44677",
"138.204.179.162:44088",
"187.111.192.50:33620",
"191.241.226.230:53281",
"177.103.186.7:56030",
"186.224.229.105:53943",
"177.92.67.230:53281",
"187.120.253.119:30181",
"179.127.242.44:55299",
"200.192.243.137:31497",
"200.142.120.90:42827",
"187.111.160.8:42579",
"201.59.201.92:40417",
"179.189.225.58:41881",
"186.225.250.26:60468",
"138.36.107.24:41184",
"179.124.19.9:32525",
"177.92.160.254:54868",
"160.19.245.61:41191"
]

#--------------- END OF PROXIES TO TEST -----------------

for _ in range(qntOfTests):
    removeInvalidProxies(urlToTest)
    sleep(10)

if onlyHighAnonymity:
    filterHighAnonymity()
print("WORKING PROXIES")
print(proxies)
