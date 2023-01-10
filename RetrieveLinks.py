from re import template
import urllib3, random
from random import sample
from bs4 import BeautifulSoup
import numpy as np
from urllib.parse import urlsplit, urlunsplit

class RetrieveLinks:

    def __fetch_all_pages_from_sitemap(self, sitemap:str):
        """ Fetch all URLs from the Sitemap
            Returns ALL so long as they begin with
            the College URL or /
        """
        http = urllib3.PoolManager()
        conn = http.request("GET", sitemap)

        soup = BeautifulSoup(conn.data, "html.parser")
        links = soup.find_all('a')
        
        returnObject = []
        pageurl = self.__get_sitemap_base_url(sitemap)

        for tag in links:
            link = tag.get('href',None)
            if link is not None:
                if(link.startswith("/") or link.startswith(pageurl)):
                    
                    # Prepend full url to any without
                    if(link.startswith("/")):
                        link = "{}{}".format(pageurl, link)
                        
                    returnObject.append(link)
        
        return returnObject


    def __get_sitemap_base_url(self, sitemap:str):
        """Return the base url"""
        split_url = urlsplit(sitemap)
        return "{}://{}".format(
            split_url.scheme,
            split_url.netloc
        ) 

    def __generate_all_pages(self, sitemap:str, templated_pages:list=[]):
        """Generate all pages, shared between components"""
        all_pages = self.__fetch_all_pages_from_sitemap(sitemap=sitemap)
        
        # Only return pages where they are not templated
        non_templated = []
        if not templated_pages:
            non_templated = all_pages
        else:
            for pages in all_pages:
                page_not_shown_in_either_template = True
                for templates in templated_pages:
                    page_not_shown_in_either_template = page_not_shown_in_either_template and not pages.startswith(templates)
                if(page_not_shown_in_either_template is True):
                    non_templated.append(pages)

        for template in templated_pages:
            templated = [param for param in all_pages if param.startswith(template) == True]
            non_templated.append(random.choice(templated))

        # This method acts like a set to only return unique results
        return sorted(list(dict.fromkeys(non_templated)))


    def initial_return_all_pages_using_sitemap(self, sitemap:str, templated_pages:list=[]):
        """Return all pages, with the option of removing all templated """

        all_results = self.__generate_all_pages(sitemap, templated_pages)
        return all_results


    def initial_return_randomized_pages_using_sitemap(self, sitemap:str=None, templated_pages:list=[], num:int = 6):
        """Fetch and return X pages from sitemap
            Defaults to returning 6
            
            :params int num: Number of elements to return
        """

        all_results = self.__generate_all_pages(sitemap, templated_pages)

        randomised = []       
        # Ensure inserted number isn't greater than all pages count
        if(len(all_results) < num):
            num = len(all_results)
            
        # Take random X college pages
        for random_sampling in random.sample(all_results, num):
            randomised.append(random_sampling)

        return randomised

    def further_randomise_and_return_results(self, current_pages:list=[], random_amount:int=0):
        """Takes in a list and returns a randomised selection"""
        if not current_pages:
            return current_pages
        
        if len(current_pages == random_amount or random_amount == 0):
            return current_pages
        
        randomised = []
        for random_sampling in random.sample(current_pages, random_amount):
            randomised.append(random_sampling)

        return randomised