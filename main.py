import requests
from datetime import datetime
from bs4 import BeautifulSoup


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Opens file to contain html links to all articles
    sourceFile = open("source.txt", "w")

    # URL of search results of a query
    url = 'https://www.guampdn.com/search/?q=Peter+Onedera'
    page = requests.get(url)

    parsedHTML = BeautifulSoup(page.content, 'html.parser')
    articleList = []
    articleListSorted = []

    # search words for html links
    urlKeyWords = ['story', 'opinion']

    # find all <a href=''> in html code
    for link in parsedHTML.findAll("a"):
        articleList.append(link.get('href'))

    # adds all of the HTML links with the key words into a list
    for x in articleList:
        k = [w for w in urlKeyWords if w in x]
        if len(k) == len(urlKeyWords):
            articleListSorted.append('https://www.guampdn.com' + x + '\n')

    # write all of the links we want to a .txt file, for future reference
    for articleListSorted in articleListSorted:
        sourceFile.write(articleListSorted)

    sourceFile.close()
    source = open("source.txt", "r")
    output = open("output.txt", "w")

    today = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    output.write("Last Updated: " + today + " (GMT+10)")
    output.write('\n')

    # look through each article
    for articleListSorted in articleListSorted:
        # inputs url from .txt file
        postURL = source.readline()

        output.write(postURL)

        try:
            # get and parse article HTML
            pageReq = requests.get(postURL)
            parsedPage = BeautifulSoup(pageReq.content, 'html.parser')

            # search for any HTML tags <p class='gnt_ar_b_p'> (i.e. the actual text of the article)
            foundParagraphs = parsedPage.find_all('p', class_='gnt_ar_b_p')

            # print all text instances of <p class=gnt_ar_b_p>
            for x in foundParagraphs:
                # print(x.text)
                # print('\n')
                output.write(x.text.encode('utf8'))
                output.write('\n')

            # print('\n\n')
            output.write('\n\n')
        except requests.exceptions.MissingSchema:
            break




