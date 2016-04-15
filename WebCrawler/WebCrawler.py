"""This python script is used for crawing through web page"""

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''
    
def extractHyperlink(pageData):
    
    startLink = pageData.find('<a href=')
    if startLink == -1:
        return None,0
    else:
        startPos =  pageData.find('"',startLink)
        endPos = pageData.find('"', startPos + 1)
        url = pageData[startPos + 1:endPos]
        return url,endPos
    
def getAllHyperLink(pageData):
    while True:
        link,endPos = extractHyperlink(pageData)
        if link:
            print link
            pageData = pageData[endPos:]
        else:
            break


getAllHyperLink(get_page('http://interviewquestionbank.net'))
