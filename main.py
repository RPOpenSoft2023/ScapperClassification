from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

shoppingFood = ['Alcoholic Beverages', 'Tobacco Products']

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.screener.in/explore/')
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

all_ques_div = soup.findAll("div", {"class": "problem-tagbox-inner"})


index_wise_list = []

for i in range(66):
    list_at_i_index = []
    if (i == 0):
        continue
    # https://www.screener.in/company/compare/00000050/
    pageIndex = ''
    if i <= 9:
        pageIndex = "0"+str(i)
    else:
        pageIndex = str(i)
    pageUrl = f"https://www.screener.in/company/compare/000000{pageIndex}/"
    driver.get(pageUrl)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # pageIndicator = soup.find(
    #     'div', {"class": "flex-row flex-space-between margin-top-16 margin-bottom-36"})
    pageIndicator = soup.findAll(
        'div', {"class": "flex-baseline options"})
    numberOfPage = len(pageIndicator)
    # print(numberOfPage)
    if (numberOfPage == 0):
        numberOfPage = 1
    else:
        numberOfPage = int(pageIndicator[0].contents[-4].text)
        print(pageIndicator[0].contents[-4].text)

    # if (numberOfPage == 0):

    for page in range(numberOfPage):
        url = f"{pageUrl}/?page={page+1}"
        driver.get(url)
        time.sleep(3)
        companies = soup.findAll('a', {"target": "_blank"})
        for company in companies:
            compName = company.text
            list_at_i_index.append(compName)

    index_wise_list.append(list_at_i_index)
    print(list_at_i_index)
    # with open(f'sector', "a") as f:
    #     f.write('\n'.join(urls))
    #     f.write('\n')
    #     print("Problems urls successfully saved!")

df = pd.DataFrame(index_wise_list)
print(df)
df.to_csv('temp.csv')
# print(index_wise_list)
# pageIndex = '67'
# pageUrl = f"https://www.screener.in/company/compare/000000{pageIndex}/"
# driver.get(pageUrl)
# time.sleep(5)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# pageIndicator = soup.findAll(
#     'div', {"class": "flex-baseline options"})
# numberOfPage = len(pageIndicator)
# if (numberOfPage == 0):
#     numberOfPage = 0
# print(numberOfPage)
# # numberOfPage = int(pageIndicator[0].contents[-4].text)
# # print(pageIndicator[0].contents[-4].text)
# url = f"{pageUrl}/?page={1}"
# driver.get(url)
# time.sleep(3)
# company = soup.findAll('a', {"target": "_blank"})
# print(company[-1])
