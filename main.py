from selenium import webdriver
from axe_selenium_python import Axe
from datetime import datetime
import time
import os, json

pageurl = "https://www.fife.ac.uk/"
urls = [
    pageurl,                                                                    # Main page
    pageurl+"contact-us/",                                                      # Forms with inputs
    pageurl+"news/",                                                            # General news, image headers
    pageurl+"news/fife-college-increases-degree-pathways-to-record-number/",    # Actual news content
    pageurl+"case-studies/",                                                    # Text overlay on image backgrounds
    pageurl+"courses/subject-areas/access-courses/",                            # General course overview
    pageurl+"courses/subject-areas/data-science/",                              # Largely different from the above
    pageurl+"courses/search-all-courses/NQESOL2",                               # Actual course overview
    pageurl+"studying-with-us/adam-smith-scholarships/apply-now/",              # Scholarship page
    pageurl+"about-us/getting-here/glenrothes-campus/",                         # Campus overview with maps
    pageurl+"studying-with-us/student-support-services/student-funding/"        # Page with table
]

def GetTime():
    """
    Just to get the formatted time for 
    the current function
    """
    return datetime.now().strftime("%H:%M:%S")

def RunAndSaveToJSON(url, number):
    """
    Take in a URL, hit it with axe and return a 
    response as a json object
    :param url: The full url to analyse
    :param number: The number to save the results file as i.e. results1.json
    :param printresults: Print results out to a json file.
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


def RunAndReturnViolations(url):
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
    return axe.report(results["violations"])


### -------------------------
### Main Program starting now
###

print()
print("[{}] Accessibility tester starting now".format(GetTime()))

os.makedirs(os.path.abspath("Reports"),exist_ok=True)
filepath = os.path.abspath("Reports/{}-AccessibilityCheck.txt".format(datetime.now().strftime("%m-%d-%Y_%H-%M-%S")))
with open(filepath, "w", encoding="utf8") as f:
    try:
        for index, page in enumerate(urls):
            print("[{}] Checking accessibility on page [{}]".format(GetTime(), page))

            #f.write(unicode(json.dumps(RunAndReturnViolations(page), indent=4)))
            f.writelines("[Run {}]Validation for {}\n--------------\n".format(index, page))
            f.write(RunAndReturnViolations(page))
            f.write("\n\n")
            
            print("[{}] Completed check on page [{}], inserted into results{}.json".format(GetTime(), page, index))
    
    except NameError:
        print("[{}] Problem saving file for url".format(GetTime()))
        f.write("ERROR: problem running script")

    #end = time.time()

print("[{}] Accessibility tester complete".format(GetTime()))
print()