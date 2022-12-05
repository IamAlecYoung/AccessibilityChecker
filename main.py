from typing import final
from selenium import webdriver
from axe_selenium_python import Axe
from datetime import datetime
import os, json
from pagestocheck import urls

def GetTime():
    """
    Just to get the formatted time for 
    the current function
    """
    return datetime.now().strftime("%H:%M:%S")


def RunAndSaveToJSON(url: str, number: int):
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


def OverrideReportGeneratorToGenerateJSON(url: str, violations: list):
    """
    Overwrite the inbuilt report method for axe_selenium method,
    instead generating as JSON
    """
    employee_string = {
        "URL": url, 
        "Checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Violations": str(len(violations)),
        "Problems": GenerateRuleViolations(violations)
    }

    return employee_string

def GenerateRuleViolations(violations: list):
    """ Generates the Rule element details section
    """
    returnobject = []
    for violation in violations:
        returnobject.append({
            "Rule": violation["id"],
            "Description": violation["description"], 
            "HelpURL": violation["helpUrl"],
            "Impact": violation["impact"],
            "Tags": violation["tags"],
            "Element affected": GenerateElementsAffected(violation["nodes"])
        })
    return returnobject


def GenerateElementsAffected(nodes: list):
    """ Generates the Target element details section
    """
    returnobject = []
    for node in nodes:
        returnobject.append({
            "Target": node["target"],
            "Details": {
                "All": MultidimensionalArray(node["all"]),
                "Any": MultidimensionalArray(node["any"]),
                "None": MultidimensionalArray(node["none"])
            }
        })
    return returnobject


def MultidimensionalArray(nodes: list):
    """
    Utilises the above method when it's a multidimensional array
    """
    string = []
    for node in nodes:
        string.append(node["message"])
    return string


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


def main():
    """ Main program
    """
    print()
    print("[{}] Accessibility tester starting now".format(GetTime()))

    os.makedirs(os.path.abspath("Reports"),exist_ok=True)
    filepath = os.path.abspath("Reports/{}-AccessibilityCheck.json".format(datetime.now().strftime("%m-%d-%Y_%H-%M-%S")))
    with open(filepath, "w", encoding="utf8") as f:
        f.write("[")
        
        try:
            total=len(urls)-1
            if(total < 0):
                print("[{}] No URLs provided".format(GetTime()))
                f.write(json.dumps({"Error": "[{}] No URLs provided".format(GetTime())}))
            else:
                for index, page in enumerate(urls): 
                    try:
                        print("[{}] Checking accessibility on page [{}]".format(GetTime(), page))
                        f.write(str(json.dumps(OverrideReportGeneratorToGenerateJSON(page, RunAndReturnViolations(page)), indent=4)))
                        print("[{}] Completed check on page [{}]".format(GetTime(), page))
                    except:
                        print("[{}] Problem saving file for url {}".format(GetTime(), page))
                        f.write(json.dumps({"Error": "[{}] Problem saving file for url {}".format(GetTime(), page)}))

                    if(index != total):
                        f.write(",")
        except NameError:
            print("[{}] Problem with program somewhere".format(GetTime()))
            f.write(json.dumps({"Error": "[{}] Problem with program somewhere".format(GetTime())}))
        finally:
            f.write("]")

    print("[{}] Accessibility tester complete".format(GetTime()))
    print()

if __name__ == '__main__':
    main()