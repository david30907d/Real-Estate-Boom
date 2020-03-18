import requests, re
PAYLOAD = {
    "machineNo": "",
    "ipAddress": "27.242.129.44",
    "osType": 4,
    "model": "web",
    "deviceVersion": "Mac OS X 10.14.6",
    "appVersion": "80.0.3987.132",
    "deviceType": 3,
    "apType": 3,
    "browser": 1,
    "memberId": "",
    "domain": "www.sinyi.com.tw",
    "utmSource": "",
    "utmMedium": "",
    "utmCampaign": "",
    "utmCode": "",
    "requestor": 1,
    "utmContent": "",
    "utmTerm": "",
    "sinyiGroup": 1,
    "filter": {
        "exludeSameTrade": False,
        "objectStatus": 0,
        "retType": 2,
        "retRange": [
            "700",
            "701",
            "710"
        ],
        "totalPrice": "min-200",
        "houselandtype": [
            "B",
            "A"
        ]
    },
    "page": 1,
    "pageCnt": 20,
    "sort": "8",
    "isReturnTotal": True
}
TEXT = requests.get('https://www.sinyi.com.tw/').text
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
    "code": "0",
    "Connection": "keep-alive",
    "Content-Length": "529",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "sinyiwebapi.sinyi.com.tw",
    "Origin": "https://www.sinyi.com.tw",
    "Referer": "https//www.sinyi.com.tw/buy/list/200-down-price/building-apartment-type/Tainan-city/700-701-710-zip/Taipei-R-mrtline/03-mrt/year-desc/index",
    "sat": re.search(r"sat\"\:\"(.+?)\"", TEXT).group(1),
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "sid": "20200314101943900",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
resp = requests.post('https://sinyiwebapi.sinyi.com.tw/searchObject.php', json=PAYLOAD, verify=False, headers=HEADERS)
import json
result = []
if resp.status_code == 200:
    for obj in resp.json()['content']['object']:
        if ("18" in obj['tags'] or "19" in obj['tags']) or obj['groupCompany'] or '租' in obj['name'] or '大學' in obj['name']:
            lean_obj = {
                'name': obj['name'],
                'age': float(obj['age'].replace('年', '')),
                'uniPrice': float(obj['uniPrice'].replace('萬/坪', '').strip()),
                'shareURL': obj['shareURL']
            }
            result.append(lean_obj)
from operator import itemgetter
print(sorted(result, key=itemgetter('uniPrice')))