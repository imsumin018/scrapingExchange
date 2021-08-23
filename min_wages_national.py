from bs4 import BeautifulSoup
import requests

class NationWageSiteInfo:
    def __init__(self):
        self.nation_list = [] #info at first page
        self.visit_link_list = [] #links to visit

def get_nation_list():
    res = NationWageSiteInfo()
    url = "https://countryeconomy.com/national-minimum-wage"
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    a = soup.find_all(class_="table-responsive")

    req = requests.get(url)
    req.raise_for_status()
    req.encoding=None   # None 으로 설정
    # HTML 소스 가져오기
    html = req.text
    # HTTP Header 가져오기
    header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok

    soup = BeautifulSoup(html, 'html.parser')
    print(len(soup.text))

    for row in soup.select('tbody tr'):
        row_text = [x.text for x in row.find_all('td')]
        print(row_text)
        res.nation_list.append(row_text)
        #print(', '.join(row_text))  # You can save or print this string however you want.
        for x in row.find_all('td'):
            a_link = x.find_all('a', href=True)
            if len(a_link)>0:
                #print(a_link[0]['href'])
                res.visit_link_list.append(a_link[0]['href'])
    return res

first_page_result = get_nation_list()
print(first_page_result.nation_list)
print(first_page_result.visit_link_list)
