from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
    driver = __setup_edge_browser()
    driver.get(url) 
    wait = WebDriverWait(driver, timeout=30)
    wait.until(EC.presence_of_element_located(By.ID, "cc-btn-dismiss"))
    axe = Axe(driver)
    axe.inject()
    # Run and store results
    results = axe.run()
    axe.write_results(results, "results{}.json".format(number))
    driver.close()

#def RunAndReturnViolations(self, url: str):
def run_and_return_violations(url: str):
    """
    Take in a URL, hit it with axe and return a 
    response as a jviolation
    :param url: The full url to analyse
    """
    # Setup the axe object
    driver = __setup_edge_browser()
    driver.get(url)
    #wait = WebDriverWait(driver, timeout=30)
    #wait.until(EC.presence_of_element_located(By.ID, "cc-btn-dismiss"))
    axe = Axe(driver)
    axe.inject()
    # Run and store results
    results = axe.run()
    driver.close()
    return results["violations"]


def __setup_edge_browser():
    edge_driver="/Users/alecyoung/Downloads/edgedriver_mac64_m1/msedgedriver"
    desired_cap = {
        "os" : "OS X",
        "os_version" : "Big Sur",
        "browser" : "Edge",
        "browser_version" : "109.0"
    }
    driver = webdriver.Edge(executable_path=edge_driver, capabilities=desired_cap)
    return driver

def __setup_firefox_browser():
    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(Options=firefox_options)
    return driver