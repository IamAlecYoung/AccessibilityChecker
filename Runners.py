from selenium import webdriver
from axe_selenium_python import Axe

def RunAndSaveToJSON(url: str, number: int):
    """
    Take in a URL, hit it with axe and return a 
    response as a json object
    :param url: The full url to analyse
    :param number: The number to save the results file as i.e. results1.json
    """
    # Setup the axe object
    driver = webdriver.Firefox()
    driver.get(url)
    axe = Axe(driver)
    axe.inject()
    # Run and store results
    results = axe.run()
    axe.write_results(results, "results{}.json".format(number))
    driver.close()


def RunAndSaveToCSV(url: str, number: int):
    """
    Take in a URL, hit it with axe and return a 
    response as a CSV file
    :param url: The full url to analyse
    :param number: The number to save the results file as i.e. results1.csv
    """

def RunAndReturnViolations(url: str):
    """
    Take in a URL, hit it with axe and return a 
    response as a jviolation
    :param url: The full url to analyse
    """
    # Setup the axe object
    driver = webdriver.Firefox()
    driver.get(url)
    axe = Axe(driver)
    axe.inject()
    # Run and store results
    results = axe.run()
    driver.close()
    return results["violations"]
