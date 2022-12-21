class StatePages:

    def __init__(self):
        self.__default_page_url  = "https://www.fife.ac.uk"  # "https://business.fife.ac.uk"
        self.__sitemap_link  = "/sitemap"
        self.__default_urls = []
        self.__exlude_urls = [
            "/news",
            "/coursesearch",
            "/courses/search-all-courses/",
        ]

    @property
    def default_page_url(self):
        """ Returns the main page to use
        """
        return self.__default_page_url
    @default_page_url.setter
    def set_default_page_url(self, url:str):
        """ Sets the main page to use
        """
        self.__default_page_url == url
        self.__sitemap_link == ""   # Reset
        self.__default_urls = []    # Reset
        self.__exlude_urls = []     # Reset


    @property
    def urls_to_use(self):
        """ Return the main urls to use, if set
        """
        return self.__default_urls
    @urls_to_use.setter
    def get_exluded_urls_to_use(self):
        """ Return the excluded urls to use, if set
        """
        return self.__exlude_urls

    @property
    def sitemap_to_use(self):
        """ Sets the urls to use
        """
        return self.__sitemap_link
    @sitemap_to_use.setter
    def sitemap_to_use(self, sitemap:str):
        """ Sets the urls to use
        """
        self.__sitemap_link == sitemap


    @property
    def exlude_urls_to_use(self, exclude_urls:list):
        """ Sets the exlude urls to use
        """
        self.__exlude_urls == exclude_urls
    @exlude_urls_to_use.setter
    def exlude_urls_to_use(self, exclude_urls:list):
        """ Sets the exlude urls to use
        """
        self.__exlude_urls == exclude_urls
