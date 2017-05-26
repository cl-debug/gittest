#coding=UTF-8
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.cankaoxiaoxi.com/society/20170503/1953157.shtml")

print html