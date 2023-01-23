
# Python accessibility checker

Quick and dirty python project to check accessibility on a list of college pages.

Takes the list of pages in pagestocheck.py and generates a report on accessibility violations present on each as a JSON list.

#### Select sites to use

Change the URLS listed in the pagestocheck.py file and run again to run against new pages


## Run Locally

Clone the project

```bash
  git clone git@ssh.dev.azure.com:v3/alecyoung/AccessibilityChecker/AccessibilityChecker
```

Go to the project directory

```bash
  cd ./AccessibilityChecker
```

Install dependencies and enter shell

```bash
  pipenv install --dev
  pipenv shell
```

Run the program

```bash
  python3 viewer.py
```

Package the program for distribution (Non-Windows)
```bash
  pip show customtkinter        # Make note of the location to use below
  pip show axe_selenium_python  # Also this one
  pyinstaller --onefile --noconsole --add-data "/Users/alecyoung/.local/share/virtualenvs/AccessibilityChecker-stIi5yuP/lib/python3.10/site-packages/customtkinter:customtkinter/" --add-data "/Users/alecyoung/.local/share/virtualenvs/AccessibilityChecker-stIi5yuP/src/axe-selenium-python/axe_selenium_python:axe_selenium_python" --icon=test.ico viewer.py
```

Package the program for distribution (Windows solution)
More info https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging#windows-pyinstaller-auto-py-to-exe
```bash
  pip show customtkinter        # Make note of the location to use below
  pip show axe_selenium_python  # Also this one
  pyinstaller --noconfirm --onedir --windowed --add-data "c:/users/alecyoung/.virtualenvs/accessibilitychecker-qrd-bgeu/lib/site-packages/customtkinter;customtkinter/" --add-data "c:\users\alecyoung\.virtualenvs\accessibilitychecker-qrd-bgeu\src\axe-selenium-python\axe_selenium_python;axe_selenium_python/" viewer.py
```

***Note***: Within the ```--add-data ``` commands above, one of the biggest differences is that the directorys are seperated by a colon (:) on unix and a semicolon (;) on windows.

## Super important
The version of axe-core is suuuuuuper outdated on pypi for the axe-selenium-python library (last updated 2018 at time of writing).
There is an updated version of the package available from here:
https://github.com/mozilla-services/axe-selenium-python/blob/master/axe_selenium_python/package.json

Installing from the Github repo doesn't work well since the package-lock.json dependencies points to a 404 address (https://nexus.corp.indeed.com)
/Users/alecyoung/.local/share/virtualenvs/AccessibilityChecker-stIi5yuP/src/axe-selenium-python/axe_selenium_python

To fix, go to the find the relevant package and SHA256 from https://registry.npmjs.org/axe-core (For latest package, check https://www.npmjs.com/package/axe-core)
Go to the above directory and edit the package-lock.json with the updated info.
```bash
"node_modules/axe-core": {
      "version": "4.6.2",
      "resolved": "https://registry.npmjs.org/axe-core/-/axe-core-4.6.2.tgz",
      "integrity": "sha512-b1WlTV8+XKLj9gZy2DZXgQiyDp9xkkoe2a6U6UbYccScq2wgH/YwCeI2/Jq2mgo0HzQxqJOjWZBLeA/mqsk5Mg==",
      "engines": {
        "node": ">=4"
      }
  }
```

Then, in that directory, run
```bash
npm install
```

Make sure the /Users/alecyoung/.local/share/virtualenvs/AccessibilityChecker-stIi5yuP/src/axe-selenium-python/axe_selenium_python/**node_modules** directory now exists 
