from typing import final
from datetime import datetime
import os, json
from pagestocheck import urls
from Global import GetTime
from GenerateJSON import OverrideReportGeneratorToGenerateJSON
from GenerateCSV import OverrideReportGeneratorToGenerateCSV, GenerateCSVTitles
from Runners import RunAndReturnViolations, RunAndSaveToJSON
from RetrieveLinks import ReturnRandomizedPages

file_to_print = ".csv"
#file_to_print = "json"

def main():
    """ Main program
    """
    print()
    print("[{}] Accessibility tester starting now".format(GetTime()))

    os.makedirs(os.path.abspath("Reports"),exist_ok=True)
    filepath = os.path.abspath("Reports/{}-AccessibilityCheck{}".format(datetime.now().strftime("%m-%d-%Y_%H-%M-%S"), file_to_print))
    with open(filepath, "w", encoding="utf8") as f:
        
        if(file_to_print == ".json"):
            f.write("[")
        elif(file_to_print == ".csv"):
            f.write(GenerateCSVTitles())

        print(urls)

        # If file with urls to focus on is present, use that
        # Otherwise, generate random pages
        pages_to_focus_on = urls
        if(len(urls) < 1):
            pages_to_focus_on = ReturnRandomizedPages()

        try:
            total=len(pages_to_focus_on)-1
            if(total < 0):
                print("[{}] No URLs provided".format(GetTime()))
                f.write(json.dumps({"Error": "[{}] No URLs provided".format(GetTime())}))
            else:
                for index, page in enumerate(pages_to_focus_on): 
                    try:
                        print("[{}] Checking accessibility on page [{}]".format(GetTime(), page))
                        
                        if(file_to_print == ".json"):
                            f.write(str(json.dumps(OverrideReportGeneratorToGenerateJSON(page, RunAndReturnViolations(page)), indent=4)))
                        elif(file_to_print == ".csv"):
                            f.write(str(OverrideReportGeneratorToGenerateCSV(page, RunAndReturnViolations(page))))
                            f.write("\n")

                        print("[{}] Completed check on page [{}]".format(GetTime(), page))
                    except Exception as e:
                        print(e)
                        print("[{}] Problem saving file for url {}".format(GetTime(), page))
                        f.write(json.dumps({"Error": "[{}] Problem saving file for url {}".format(GetTime(), page)}))

                    if(index != total):
                        f.write(",")
        except NameError:
            print("[{}] Problem with program somewhere".format(GetTime()))
            f.write(json.dumps({"Error": "[{}] Problem with program somewhere".format(GetTime())}))
        finally:
            if(file_to_print == ".json"):
                f.write("]")

    print("[{}] Accessibility tester complete".format(GetTime()))
    print()


if __name__ == '__main__':
    main()