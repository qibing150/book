""" 
使用原生爬虫爬取电子书信息， 每一本书的信息都需要爬取，
包括书名、作者、内容简介...等。 
参考地址：http://d81fb43e-d.parkone.cn/ """
import re
from urllib import request

class Book():


    url = 'http://d81fb43e-d.parkone.cn/book/'
    root_pattern = ''
    #书名
    bookname_pattern = '<h2>([\s\S]*?)</h2>'
    #作者
    name_pattern = '<a href="/author/[\s\S]*?">([\s\S]*?)</a>'
    #出版社
    press_pattern = '<span>出版社:([\s\S]*?)</span>'
    #简介
    brief_pattern = '<p class="description">([\s\S]*?)</p>'
    #出版日期
    publication_pattern = '<p>出版日期:([\s\S]*?)</p>'


    def __fetch_content(self):
        url = Book.url+str(i)
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
        
           
    def __analysis(self, htmls):
        anchors = []
        bookname = re.findall(Book.bookname_pattern, htmls)
        name = re.findall(Book.name_pattern, htmls)
        press = re.findall(Book.press_pattern, htmls) 
        publication = re.findall(Book.publication_pattern, htmls)
        brief = re.findall(Book.brief_pattern, htmls)

        anchor = {'书名':bookname,'作者':name,'出版社':press,'出版日期':publication,'简介':brief}
        anchors.append(anchor)
        print(anchors)

    
    def go(self):
        htmls = self.__fetch_content() 
        self.__analysis(htmls)

for i in range(1,254):
    book = Book()
    book.go() 

    