import urllib3, random
from random import sample
from bs4 import BeautifulSoup
import numpy as np
from pagestocheck import pageurl

class RetrieveLinks:

    __hefty_page = "{}/coursesearch".format(pageurl)
    __news_pages = "{}/news".format(pageurl)
    __site_map = "{}/sitemap/".format(pageurl)
    __templates_page = "/courses/search-all-courses/"
    __templates_url = "{}{}".format(pageurl, __templates_page)

    def __fetch_all_pages_from_sitemap(self, include_news:bool = True):
        """ Fetch all URLs from the Sitemap
            Returns ALL so long as they begin with
            the College URL or /
        """
        http = urllib3.PoolManager()
        conn = http.request("GET", self.__site_map)

        soup = BeautifulSoup(conn.data, "html.parser")
        links = soup.find_all('a')
        
        returnObject = []

        for tag in links:
            link = tag.get('href',None)
            if link is not None:
                if(link.startswith("/") or link.startswith(pageurl)):
                    
                    # Prepend full url to any without
                    if(link.startswith("/")):
                        link = "{}{}".format(pageurl, link)
                    
                    # If news to be included or not
                    if(link.startswith(self.__news_pages) and include_news == False):
                        continue
                    else:
                        returnObject.append(link)
        
        return returnObject


    def return_all_pages(self, include_news:bool = True):
        """Fetch and return ALL pages from sitemap
        """
        all_pages = self.__fetch_all_pages_from_sitemap(include_news=include_news)
        return all_pages

    def return_randomized_pages(self, num:int = 6, include_news:bool = True):
        """Fetch and return X pages from sitemap
            Defaults to returning 6
            
            :params int num: Number of elements to return
        """
        all_pages = self.__fetch_all_pages_from_sitemap(include_news=include_news)
        
        templated = [param for param in all_pages if param.startswith(self.__templates_url) == True]
        non_templated =  [param for param in all_pages if param.startswith(self.__templates_url) == False]

        randomised = []
        
        # Take random templated page
        randomised.append(random.choice(templated))
        
        # Ensure inserted number isn't greater than all pages count
        if(len(non_templated) < num):
            num = len(non_templated)
            
        # Take random X college pages
        for random_sampling in random.sample(non_templated, num):
            randomised.append(random_sampling)

        return randomised
