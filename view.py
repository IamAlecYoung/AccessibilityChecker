import pyjsonviewer
import os

files = os.listdir("Reports")
files.sort(reverse=True)
sorted(files)

if(len(files) >= 1):
    # :Latest File found
    print("Opening latest file: Reports/{}".format(files[0]))
    pyjsonviewer.view_data(json_file="Reports/{}".format(files[0]))
else:
    # No file found
    print("No file found, opening blank JSON viewer")
    pyjsonviewer.view_data()