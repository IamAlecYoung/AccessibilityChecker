#from imp import get_tag
import imp
import json

csv_title = ""

class WCAGViolation:
    def __init__(self, wcag, type, rule, impact, description):
        self.wcag = wcag
        self.type = type
        self.rule = rule
        self.impact = impact
        self.description = description

    def __eq__(self, other):
        return self.wcag == other.wcag

    def __hash__(self):
        return hash(self.wcag)

    def __repr__(self):
        return '<WCAGViolation {}>'.format(self.wcag)


def Is_Value_A_Voilation(tag_list:list):
    """True if tags contains a WCAG value """
    if('wcag2a' in tag_list 
    or 'wcag21a' in tag_list
    or 'wcag2aa' in tag_list 
    or 'wcag21aa' in tag_list
    or 'wcag2aaa' in tag_list 
    or 'wcag21aaa' in tag_list):
        return True
    else:
        return False

def Get_Tag_Value(tag_list:list):
    """Prettify the tag value"""
    if('wcag2a' in tag_list or 'wcag21a' in tag_list):
        return 'WCAG A'
    elif('wcag2aa' in tag_list or 'wcag21aa' in tag_list):
        return 'WCAG AA'
    elif('wcag2aaa' in tag_list or 'wcag21aaa' in tag_list):
        return 'WCAG AAA'
    elif('best-practice' in tag_list):
        return "Best practice"
    else:
        return "Unknown"

def Get_WCAG_Value(tag_list:list):
    """Get the accessibility number tag value"""
    wcag_elements = [tag for tag in tag_list if tag.startswith("wcag")]
    if wcag_elements:
        wcag_error = [tag for tag in wcag_elements if not tag.endswith("a")]
        return wcag_error

def Get_Unique_Titles(line_row:list):
    # first passthrough to get titles
    # -------------------------------
    unique_titles = set()
    for site in imported_json:
        # Any Error'd sites
        if "Error" in site:
            continue

        # Any items in problems, otherwise go to next element
        if not site["Problems"]:
            continue

        for problem in site["Problems"]:
            # Only print out WCAG violations
            if Is_Value_A_Voilation(problem["Tags"]) is False:
                continue

            tag_a_value = Get_WCAG_Value(problem["Tags"])
            tag_result_val = Get_Tag_Value(problem["Tags"])
            result = WCAGViolation(tag_a_value[0], tag_result_val, problem["Rule"], problem["Impact"], problem["Description"])

            unique_titles.add(result)
    
    return unique_titles


read_filepath = "07-06-2023_20-24-29-AccessibilityCheck.json"
write_filepath = "audit_parse.txt"

print("Starting program")

with open(read_filepath, 'r') as content:
    imported_json = json.load(content)

with open(write_filepath, "w", encoding="utf8") as f:
   
    unique_titles = Get_Unique_Titles(imported_json)
    csv_title = "{}{}".format("Site",unique_titles)
    
    for violation in unique_titles:

        # Does the element have ANY WCAG violations
        pages_affected = []

        # Iterate over EVERY record each time in the loop...
        for site in imported_json:

            # Any Error'd sites
            if "Error" in site:
                continue

            # Any items in problems, otherwise go to next element
            if not site["Problems"]:
                continue
            
            for problems in site['Problems']:
                if violation.wcag in problems['Tags']:
                    pages_affected.append(site['URL'])

        # Print out the results
        # --------------------- 
        f.write('%-40s (Occurances %d)\n' % (violation.wcag, len(pages_affected)))
        f.write("%-s (%-s) %-40s \n" % (violation.rule, violation.type, violation.description))

        for affected in pages_affected:
            f.write('\t%-40s,\n' % (affected))
        
        f.write('\n')

print("Ending program")