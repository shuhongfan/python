"""
@Time ： 2021/11/30 14:36
@Auth ： 021321752215舒洪凡
@File ：31.py
@IDE ：PyCharm
"""

from selenium import webdriver
from time import sleep
import xlwt  # 进行excel操作
#谷歌驱动 告诉电脑在哪打开浏览器
driver=webdriver.Chrome(executable_path="D:\Develop\chromedriver.exe")
#打开网页
driver.get("https://www.jd.com")
#通过xpath找到输入框输入要搜索的
driver.find_element_by_xpath("//*[@id='key']").send_keys("华为手机")
#通过xpath找到搜索按钮点击
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
driver.implicitly_wait(5)#隐式休息5s
hrefs=[]
names=[]
prices=[]
commits=[]
shops=[]
for j in range(1,11):
    for i in range(1, 31):
        href = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-img']/a").get_attribute("href")#get_attribute获得对应属性的属性值
        information = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-name p-name-type-2']")
        price = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-price']")
        commit = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-commit']/strong")
        shop = driver.find_element_by_xpath(
            "//ul[@class='gl-warp clearfix']/li[" + str(i) + "]//div[@class='p-shop']")
        hrefs.append(href)
        names.append(information.get_attribute("textContent").replace('\n', '').replace('\t', ''))
        prices.append(price.get_attribute("textContent").replace('\n', '').replace('\t', '').replace('￥',''))
        commits.append(commit.get_attribute("textContent").replace('\n', '').replace('\t', ''))
        shops.append(shop.get_attribute("textContent").replace('\n', '').replace('\t', ''))
    driver.find_element_by_xpath("//*[@id='J_bottomPage']/span[1]/a[9]").click()
    sleep(2)
    print("第"+str(j)+"页")
print("爬取完毕！")
#存数据
book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
sheet = book.add_sheet('京东', cell_overwrite_ok=True)  # 创建工作表
col = ("链接","名称","价格","评价","商店")
for i in range(0, 5):
    sheet.write(0, i, col[i])  # 列名
for i in range(0,300):
    sheet.write(i+1,0,hrefs[i])
for i in range(0,300):
    sheet.write(i+1,1,names[i])
for i in range(0,300):
    sheet.write(i+1,2,prices[i])
for i in range(0,300):
    sheet.write(i+1,3,commits[i])
for i in range(0,300):
    sheet.write(i+1,4,shops[i])
book.save("京东.xls")  # 保存
print("关闭浏览器，保存数据")

