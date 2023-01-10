
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