import urllib3, random
from random import sample
from bs4 import BeautifulSoup
import numpy as np
from pagestocheck import pageurl

site_map = "{}/sitemap/".format(pageurl)
templates_page = "/courses/search-all-courses/"
templates_url = "{}{}".format(pageurl, templates_page)

def RetrieveALLPages():
    http = urllib3.PoolManager()
    conn = http.request("GET", site_map)

    soup = BeautifulSoup(conn.data, "html.parser")
    links = soup.find_all('a')
    
    returnObject = []

    for tag in links:
        link = tag.get('href',None)
        if link is not None:
            if(link.startswith("/") or link.startswith(pageurl)):
                if(link.startswith("/")):
                    link = "{}{}".format(pageurl, link)
                returnObject.append(link)
    
    return returnObject


def ReturnAllPages():
    all_pages = RetrieveALLPages()
    return all_pages

def ReturnRandomizedPages(num:int = 6):
    all_pages = RetrieveALLPages()
    
    templated = [param for param in all_pages if param.startswith(templates_url) == True]
    non_templated =  [param for param in all_pages if param.startswith(templates_url) == False]

    randomised = []
    
    # Take random templated page
    randomised.append(random.choice(templated))
    
    # Take random X college pages
    for random_sampling in random.sample(non_templated, num):
        randomised.append(random_sampling)

    return randomised

    
ReturnRandomizedPages()
