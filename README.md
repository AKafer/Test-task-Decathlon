<h1> Solution for test task Decathlon </h1>

## Task

### The input of the program is a CSV-like text file (see the attachment). The task is to output an JSON file with all athletes in ascending order of their places, containing all the input data plus total score and the place in the competition (in case of equal scores, athletes must share the places, e.g. 3-4 and 3-4 instead of 3 and 4). Draw an algorythm diagram using a tool you prefer. Input file should be uploaded using browser. Be sure to keep the code design simple, but allowing to easily change or add more input sources and/or output file formats. About Decathlon competition: http://en.wikipedia.org/wiki/Decathlon

## Implementation details:

### Implemented django server.

### Used DRF and JS.

### Algorythm diagram is shown in file Algorythm.pdf.

### All calculation logic is located in the file views.py in the api folder.

# How to install a project

### Clone a repository and change to it on the command line:

```
git clone https://github.com/AKafer/Test-task-Decathlon.git
cd Test-task-Decathlon/
```

### Create and activate virtual environment:

```
python -m venv venv
source venv/Scripts/activate
```

### Install dependencies from requirements.txt:

```
pip install -r requirements.txt
```

### Run migrations:

```
cd todolist
python manage.py migrate
```

### Start project:

```
python manage.py runserver
```

## How to use:

```
1. Choose a csv file with Decathlon results
2. Press button DOWNLOAD JSON
3. You will get json file and results will be shown in a table
```

## Technology stack: Python 3, Django 4.1, DRF, JS, jQuery, DataTables

## Project author - SERGEI STOROZHUK
