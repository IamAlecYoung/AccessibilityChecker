from datetime import datetime

class GenerateCSV:
    
    def generate_CSV_titles(self):
        return "URL,Checked,Violations,Fails WCAGA, Fails WCAGAA, Fails WCAGAAA, Best practice, Other\n"

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
        fails_wcag_a = 0
        fails_wcag_aa = 0
        fails_wcag_aaa = 0
        best_practice = 0
        other_violations = 0

        for violation in violations:
            
            tags_in_violation = violation["tags"]
            
            if('wcag2a' in tags_in_violation or 'wcag21a' in tags_in_violation):
                fails_wcag_a += 1
            elif('wcag2aa' in tags_in_violation or 'wcag21aa' in tags_in_violation):
                fails_wcag_aa += 1
            elif('wcag2aaa' in tags_in_violation or 'wcag21aaa' in tags_in_violation):
                fails_wcag_aaa += 1
            elif('best-practice' in tags_in_violation):
                best_practice += 1
            else:
                other_violations += 1
             

        return "{},{},{},{},{}".format(
            fails_wcag_a,
            fails_wcag_aa,
            fails_wcag_aaa,
            best_practice,
            other_violations
        ) 