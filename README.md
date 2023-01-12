
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
  pyinstaller --onefile --noconsole --add-data "/Users/********/.local/share/virtualenvs/AccessibilityChecker-stIi5yuP/lib/python3.10/site-packages/customtkinter:customtkinter/" --add-data "/Users/********/.local/share/virtualenvs/AccessibilityChecker-stIi5yuP/lib/python3.10/site-packages/axe_selenium_python:axe_selenium_python/" viewer.py
```

Package the program for distribution (Windows solution)
More info https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging#windows-pyinstaller-auto-py-to-exe
```bash
  pip show customtkinter        # Make note of the location to use below
  pip show axe_selenium_python  # Also this one
  pyinstaller --noconfirm --onedir --windowed --add-data "c:/users/alecyoung/.virtualenvs/accessibilitychecker-qrd-bgeu/lib/site-packages/customtkinter;customtkinter/" --add-data "c:/users/alecyoung/.virtualenvs/accessibilitychecker-qrd-bgeu/lib/site-packages/axe_selenium_python;axe_selenium_python/" viewer.py
```

***Note***: Within the ```--add-data ``` commands above, one of the biggest differences is that the directorys are seperated by a colon (:) on unix and a semicolon (;) on windows.