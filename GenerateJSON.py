from datetime import datetime

class GenerateJSON:

    def override_json_report_generator(self, url: str, violations: list):
        """
        Overwrite the inbuilt report method for axe_selenium method,
        instead generating as JSON
        """
        employee_string = {
            "URL": url, 
            "Checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Violations": str(len(violations)),
            "Problems": self.__generate_rule_violations(violations)
        }

        return employee_string

    def __generate_rule_violations(self, violations: list):
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
                "Element affected": self.__generate_elements_affected(violation["nodes"])
            })
        return returnobject

    def __generate_elements_affected(self, nodes: list):
        """ Generates the Target element details section
        """
        returnobject = []
        for node in nodes:
            returnobject.append({
                "Target": node["target"],
                "Details": {
                    "All": self.__multidimensional_array(node["all"]),
                    "Any": self.__multidimensional_array(node["any"]),
                    "None": self.__multidimensional_array(node["none"])
                }
            })
        return returnobject

    def __multidimensional_array(self, nodes: list):
        """
        Utilises the above method when it's a multidimensional array
        """
        string = []
        for node in nodes:
            string.append(node["message"])
        return string