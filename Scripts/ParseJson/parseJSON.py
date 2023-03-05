#from imp import get_tag
import json

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

read_filepath = "fullaudit.json"
write_filepath = "audit_parse.txt"

with open(read_filepath, 'r') as content:
    imported_json = json.load(content)


with open(write_filepath, "w", encoding="utf8") as f:
   
    # print out the values
    for site in imported_json:

        # Any Error'd sites
        if "Error" in site:
            continue

        # Any items in problems, otherwise go to next element
        if not site["Problems"]:
            continue

        # Does the element have ANY WCAG violations
        if not any(Is_Value_A_Voilation(problem['Tags']) == True for problem in site["Problems"]):
            continue

        # Ignore that cc-btn
        # for problems in site["Problems"]:
        #     if "Element affected" in problems:
        #         for item in problems["Element affected"]:
        #             if "Target" in item:    # No Target element
        #                 if ".cc-btn" in item["Target"]:
        #                     break

        f.write('%-40s\n' % (site["URL"]))
            
        for problem in site["Problems"]:
            # Only print out WCAG violations
            if Is_Value_A_Voilation(problem["Tags"]) is False:
                continue

            f.write("\t%-s (%-s) %-40s \n" % (Get_WCAG_Value(problem["Tags"]), Get_Tag_Value(problem["Tags"]), problem["Description"]))
            f.write("\t(%-s) %-40s \n" % (Get_Tag_Value(problem["Tags"]), problem["Description"]))
            f.write("\t%-40s\n" % (problem["HelpURL"]))

            # if "Element affected" in problems:
            #     for item in problems["Element affected"]:
            #         if "Target" in item:
            #             f.write("\t%-40s\n" % (item["Target"]))

            f.write("\t%-40s\n" % (""))