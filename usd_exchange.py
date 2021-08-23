url = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW"
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome(executable_path="c:\dev\chromedriver")
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

values=[]
#print(soup)
table0 = soup.find_all("tr", {"class":"down"})
a = table0[0].findAll('td')
values.append(a[0].text[:-1]) 

table = soup.find("table", {"class": "tbl_exchange"})
a = table.findAll('tr')
'''
매매기준율
<th class="th_ex2"><span>현찰 사실때</span></th>
<th class="th_ex3"><span>현찰 파실때</span></th>
<th class="th_ex4"><span>송금 보내실때</span></th>
<th class="th_ex5"><span>송금 받으실때</span></th>
<th class="th_ex6"><span>T/C 사실때</span></th>
<th class="th_ex7"><span>외화수표 파실때</span></th>
'''

for tr in a :
    try:
        values.append(tr.find('td').text) 
    except:
        print("")

driver.quit()
to_store = []
to_store.append(float(values[3].replace(",","")))
to_store.append(float(values[4].replace(",","")))
to_store.append(float(values[1].replace(",","")))
to_store.append(float(values[2].replace(",","")))
to_store.append(float(values[0].replace(",","")))
print(to_store)
