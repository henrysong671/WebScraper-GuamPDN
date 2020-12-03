import requests
import re
from bs4 import BeautifulSoup


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sourceFile = open("source.txt", "w")

    url = 'https://www.guampdn.com/search/?q=Peter+Onedera'
    page = requests.get(url)

    parsedHTML = BeautifulSoup(page.content, 'html.parser')
    articleList = []
    articleListSorted = []
    checkWords = ['story', 'opinion']

    for link in parsedHTML.findAll("a"):
        articleList.append(link.get('href'))

    for x in articleList:
        k = [w for w in checkWords if w in x]
        if len(k) == len(checkWords):
            articleListSorted.append('https://www.guampdn.com' + x + '\n')

    for articleListSorted in articleListSorted:
        sourceFile.write(articleListSorted)

    sourceFile.close()
    source = open("source.txt", "r")
    output = open("output.txt", "a")

    for articleListSorted in articleListSorted:
        postURL = source.readline()

        output.write(postURL)

        pageReq = requests.get(postURL)
        parsedPage = BeautifulSoup(pageReq.content, 'html.parser')
        foundParagraphs = parsedPage.find_all('p', class_='gnt_ar_b_p')
        for x in foundParagraphs:
            # print(x.text)
            # print('\n')
            output.write(x.text.encode('utf8'))
            output.write('\n')

        # print('\n\n')
        output.write('\n\n')




