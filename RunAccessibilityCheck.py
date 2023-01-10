from typing import final
from datetime import datetime
import os, json
from Global import GetTime
#from GenerateJSON import override_json_report_generator
#from GenerateCSV import override_CSV_report_generator, generate_CSV_titles
from GenerateJSON import GenerateJSON
from GenerateCSV import GenerateCSV
from Runners import run_and_return_violations, run_and_save_to_JSON
from RetrieveLinks import RetrieveLinks

class RunAccessibilityCheck:

    @staticmethod
    def get_file_type(self, file_to_print:str=".json"):
        return os.path.abspath("Reports/{}-AccessibilityCheck{}".format(datetime.now().strftime("%m-%d-%Y_%H-%M-%S"), file_to_print))

    def run(self, pages_to_check:list=[], file_to_print:str=".json", random_pages_to_return:int=0):
        """ Main program
        """
        print()
        print("[{}] Accessibility tester starting now".format(GetTime()))

        os.makedirs(os.path.abspath("Reports"),exist_ok=True)
        filepath = self.get_file_type(self, file_to_print=file_to_print)
        with open(filepath, "w", encoding="utf8") as f:
            
            if(file_to_print == ".json"):
                f.write("[")
            elif(file_to_print == ".csv"):
                f.write(GenerateCSV().generate_CSV_titles())

            pages_to_focus_on = pages_to_check

            try:
                total=len(pages_to_focus_on)-1
                if(total < 0):
                    print("[{}] No URLs provided".format(GetTime()))
                    f.write(json.dumps({"Error": "[{}] No URLs provided".format(GetTime())}))
                else:
                    for index, page in enumerate(pages_to_focus_on): 
                        try:
                            print("[{}] {}/{} Checking accessibility on page [{}]".format(GetTime(), index, total, page))
                            
                            if(file_to_print == ".json"):
                                f.write(str(json.dumps(GenerateJSON().override_json_report_generator(page, run_and_return_violations(page)), indent=4)))
                            elif(file_to_print == ".csv"):
                                f.write("{}{}".format(str(GenerateCSV().override_CSV_report_generator(page, run_and_return_violations(page))), "\n"))

                            print("[{}] {}/{} Completed check on page [{}]".format(GetTime(), index, total, page))
                        except Exception as e:
                            print(e)
                            print("[{}] Problem saving file for url {}".format(GetTime(), page))
                            f.write(json.dumps({"Error": "[{}] Problem saving file for url {}".format(GetTime(), page)}))

                        if(file_to_print == ".json" and index != total):
                            f.write(",")
            except NameError:
                print("[{}] Problem with program somewhere".format(GetTime()))
                f.write(json.dumps({"Error": "[{}] Problem with program somewhere".format(GetTime())}))
            finally:
                if(file_to_print == ".json"):
                    f.write("]")

        print("[{}] Accessibility tester complete".format(GetTime()))
        print()