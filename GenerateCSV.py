from datetime import datetime

class GenerateCSV:
    
    def generate_CSV_titles(self):
        return "URL,Checked,Violations,Critical(A),Serious(AA),Moderate(AAA),Other\n"

    def override_CSV_report_generator(self, url: str, violations: list):
        """
        Overwrite the inbuilt report method for axe_selenium method,
        instead generating as CSV
        """
        problems = self.__generate_rule_violations(violations)
        csvContent = "{},{},{},{}".format(
            url, 
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            str(len(violations)),
            self.__generate_rule_violations(violations)
        )

        return csvContent

    def __generate_rule_violations(self, violations: list):
        """ Generates the Rule element details section
        """

        critical_violations = 0
        serious_violations = 0
        moderate_violations = 0
        other_violations = 0

        for violation in violations:
            if(violation["impact"] == "critical"):
                critical_violations += 1
            elif(violation["impact"] == "serious"):
                serious_violations += 1
            elif(violation["impact"] == "moderate"):
                moderate_violations += 1
            else:
                other_violations += 1

        return "{},{},{},{}".format(
            critical_violations,
            serious_violations,
            moderate_violations,
            other_violations
        ) 