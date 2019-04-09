import urllib.parse
import urllib.request
import json
import random
import fakeNewsGenerator as fng


webisteHeader = '<!DOCTYPE html><html lang="da"><head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>DR | TV, radio, nyheder og meget mere</title> <script src="Bootstrap.js"></script> <link rel="stylesheet" href="global.css"> <link rel="stylesheet" href="main.css"> <link rel="stylesheet" href="styles.css"/></head><body> <script src="topbarbundle.js"></script> <div class="page"> <div class="container"> <div class="full-bleed-banner"> <div class="full-bleed-banner__top"></div><div class="full-bleed-banner__left"></div><div class="full-bleed-banner__right"></div></div><nav class="focus-bar" aria-label="Fokus"> <div class="focus-bar__activities"> <ul class="top-spots"> <li> <a href="#" class="dr-frontpage__top-spot"> <img src="Images/fokusbaand/date-min-side.jpg" alt=""/> <div><span>DRTV: Date<br/>Min værste side</span></div></a> <script>if (!this.DR_adspaces) this.DR_adspaces=[]; DR_adspaces.push({c: "77363", b: "12349", a: "210"}); </script> </li><li> <a href="#" class="dr-frontpage__top-spot"> <img src="Images/fokusbaand/sorte-boks4.jpg" alt=""/> <div><span>Podcast:<br/>Den sorte boks</span></div></a> <script>if (!this.DR_adspaces) this.DR_adspaces=[]; DR_adspaces.push({c: "77445", b: "12401", a: "211"}); </script> </li><li> <a href="#" class="dr-frontpage__top-spot"> <img src="Images/fokusbaand/familien-lowander1.jpg" alt=""/> <div><span>DRTV:<br/>Familien Löwander</span></div></a> <script>if (!this.DR_adspaces) this.DR_adspaces=[]; DR_adspaces.push({c: "77370", b: "12294", a: "212"}); </script> </li><li class="top-spots__extra"> <a href="#" class="dr-frontpage__top-spot"> <img src="Images/fokusbaand/panda19.jpg" alt=""/> <div><span>Pandaerne<br/>kommer</span></div></a> <script>if (!this.DR_adspaces) this.DR_adspaces=[]; DR_adspaces.push({c: "77444", b: "12359", a: "354"}); </script> </li></ul> </div><div class="focus-bar__habits"> <ul class="top-spots"> <li> <a href="#" class="dr-frontpage__top-spot"> <img src="Images/fokusbaand/klassen_magnus2.png" alt=""/> <div><span></span></div></a> <script>if (!this.DR_adspaces) this.DR_adspaces=[]; DR_adspaces.push({c: "58972", b: "9675", a: "358"}); </script> </li><li> <a href="#" class="dr-frontpage__top-spot"> <img src="https://www.dr.dk/frontpage/content/src/img/ramasjang-logo.svg" alt=""/> <div></div></a> <script>if (!this.DR_adspaces) this.DR_adspaces=[]; DR_adspaces.push({c: "57000", b: "9360", a: "359"}); </script> </li><li> <a href="#" class="dr-frontpage__top-spot"> <img src="Images/fokusbaand/ultra.png" alt=""/> <div></div></a> <script>if (!this.DR_adspaces) this.DR_adspaces=[]; DR_adspaces.push({c: "73929", b: "9361", a: "360"}); </script> </li></ul> </div></nav> <section class="latest-bar" aria-label="Seneste"> <div class="latest-bar__primary"> <div class="latest-bar__article"> <p> <a href="https://www.dr.dk/nyheder.html">Seneste nyt:</a> <time datetime="2019-04-08T12:18:00.0000000&#x2B;00:00">45 min. siden</time> </p><h4><a href="#">DF g&#xE5;r med i ny EU-skeptisk alliance: &#x27;Nationalstaterne skal sidde i f&#xF8;rers&#xE6;det&#x27;</a></h4> </div><a href="https://www.dr.dk/nyheder.html" class="latest-bar__aside section-link dr-icon-link-boxed">Få hele nyhedsoverblikket</a> </div><div class="latest-bar__secondary"> <ul> <li><a href="index.html" class="section-link dr-icon-guide">TV-guiden</a></li><li><a href="index.html" class="section-link dr-icon-audio">Hør radio</a></li></ul> </div></section> <main class="main" id="content"> <div class="dredition"> <div class="dredition-front dredition-front--super"> <div class="dredition-main"> <div class="dredition-groups"> </div></div></div><div class="dredition-front dredition-front--620 dredition-top"> <div class="dredition-main"> <div class="dredition-groups">'
websiteFooter = '</div></div></div></div></main></div></div></body></html>'

def generateWebsite(fileName="index.html"):
    f = open("website/" + fileName, "w", encoding="utf-8")
    f.write(makeWebsite())
    f.close()

def makeWebsite():
    webiste = webisteHeader
    articles = fng.GenerateFakeArticles()

    i = 0
    length = len(articles) - 1
    while i < length:
        article1 = makeArticle(articles[i][0], getImage(articles[i][1]))
        i += 1
        article2 = makeArticle(articles[i][0], getImage(articles[i][1]))
        i += 1

        segment = makeSegment(article1, article2)
        webiste += segment
        
    webiste += websiteFooter
    return webiste


def makeArticle(title, image):
    start = '<div class="dredition-item dredition-desktop-style-50-100 dredition-mobile-style-small dredition-mobile-style-small-right dredition-image-skin--article"> <a class="dredition-item-inner" href="#"> <div itemscope itemtype="http://schema.org/ImageObject" class="dredition-item-image ratio-16-9"> <picture> <img data-image-format="16:9" itemprop="contentURL" src="'
    middle= '"></picture></div><div class="dredition-item-header"><h2><strong>'
    end = '</strong></h2></div></a></div>'
    
    return start + image + middle + title + end


def makeSegment(article1, article2):
    start = '<div class="dredition-group dredition-group-name--bb"> <div class="dredition-items">'
    end = '</div></div>'
    return start + article1 + article2 + end


def getImage(word):
    url = 'https://api.unsplash.com/search/photos?page=1&query=' + urllib.parse.quote(word) + '&client_id=2205579aac5b0001569184a150ea320eabb7e60123895a12245b723a557f5228#'
    content = ""
    with urllib.request.urlopen(url) as response:
        content = json.loads(response.read())

    number = random.randint(0,10)
    try:
        return content["results"][number]["urls"]["regular"]
    except:
        return content["results"][0]["urls"]["regular"]
