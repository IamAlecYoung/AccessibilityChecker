from datetime import datetime

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
