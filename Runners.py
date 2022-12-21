from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from axe_selenium_python import Axe

#class Runners:

#def RunAndSaveToJSON(self, url: str, number: int):
def run_and_save_to_JSON(url: str, number: int):
    """
    Take in a URL, hit it with axe and return a 
    response as a json object
    :param url: The full url to analyse
    :param number: The number to save the results file as i.e. results1.json
    """
    # Setup the axe object
    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    axe = Axe(driver)
    axe.inject()
    # Run and store results
    results = axe.run()
    axe.write_results(results, "results{}.json".format(number))
    driver.close()


#def RunAndSaveToCSV(self, url: str, number: int):
def run_and_save_to_CSV(url: str, number: int):
    """
    Take in a URL, hit it with axe and return a 
    response as a CSV file
    :param url: The full url to analyse
    :param number: The number to save the results file as i.e. results1.csv
    """

#def RunAndReturnViolations(self, url: str):
def run_and_return_violations(url: str):
    """
    Take in a URL, hit it with axe and return a 
    response as a jviolation
    :param url: The full url to analyse
    """
    # Setup the axe object
    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    axe = Axe(driver)
    axe.inject()
    # Run and store results
    results = axe.run()
    driver.close()
    return results["violations"]
