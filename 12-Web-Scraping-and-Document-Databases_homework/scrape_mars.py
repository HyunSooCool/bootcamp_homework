from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

def init_browser():
    return Browser("chrome", executable_path = "/Users/hyunsookim/Downloads/chromedriver", headless=False) 
    
mars_db={}
def scrape_news():    
    browser = init_browser()
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
        
    time.sleep(1)
        
    html=browser.html
    soup=BeautifulSoup(html, "html.parser")
    browser.quit()

    news_title=soup.find("div",class_="content_title").text
    news_p = soup.find("div",class_="article_teaser_body").text

    mars_db['news_title'] = news_title
    mars_db['news_p'] = news_p

    return mars_db

def scrape_img():
    browser=init_browser()

    img_base_url ="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_base_url)

    time.sleep(1)

    image_html=browser.html
    soup=BeautifulSoup(image_html,"html.parser")
    browser.quit()

    featured_img_base_url="https://www.jpl.nasa.gov"
    
    featured_image_tag=soup.find("article")['style']
    #print(featured_image_tag)
    featured_image_list=list(featured_image_tag)
    #featured_image_list.index("/")
    featured_image=featured_image_tag[23:-3]

    featured_image_url = featured_img_base_url + featured_image

    mars_db["featured_image_url"] =featured_image_url

    return mars_db


def scrape_weather():
    browser=init_browser()

    weather_url ="https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)

    time.sleep(1)

    weather_html=browser.html
    soup=BeautifulSoup(weather_html,"html.parser")
    browser.quit()

    mars_weather=soup.find("p",class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    
    mars_db["mars_weather"] =mars_weather

    return mars_db

def scrape_facts():
    browser=init_browser()

    mars_facts_url ="https://space-facts.com/mars/"
    browser.visit(mars_facts_url)

    time.sleep(1)

    mars_facts_html=browser.html
    soup = BeautifulSoup(mars_facts_html,"html.parser")
    browser.quit()

    mars_facts = pd.read_html(mars_facts_url)
    mars_facts_df = mars_facts[0]
    mars_facts_df.columns = ['Description','Value']

    html_mars = mars_facts_df.to_html()
    mars_db['mars_facts'] =html_mars

    return mars_db

def scrape_hemispheres():
    browser=init_browser()

    mars_hemispheres_url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)

    time.sleep(2)

    mars_hemispheres_html=browser.html
    soup=BeautifulSoup(mars_hemispheres_html,"html.parser")
   

    hemisphere_base_url = "https://astrogeology.usgs.gov"

    description_list = soup.find_all("div",class_="description")
    url_list = soup.find_all("div",class_="description")

    link_url_list=[]
    for j in range(len(url_list)):
        link_url_list.append(hemisphere_base_url+url_list[j].find("a",class_="itemLink product-item")['href'])
    
    hemisphere_image_urls=[]
    for k in range(len(link_url_list)):
        hemisphere_image_dict={}
        full_image_url =link_url_list[k]
        browser.visit(full_image_url)
        time.sleep(2)

        full_image_html=browser.html
        soup=BeautifulSoup(full_image_html,"html.parser")

        hemisphere_base_url = "https://astrogeology.usgs.gov"
        
        title = description_list[k].find_all('h3')[0].text
        img_url = hemisphere_base_url + soup.find_all("img",class_="wide-image")[0]['src']
        
        hemisphere_image_dict["title"] = title
        hemisphere_image_dict["img_url"]=img_url
        
        hemisphere_image_urls.append(hemisphere_image_dict)

    mars_db["mars_hemispheres"] = hemisphere_image_urls

    return mars_db


