<h1> Solution for test task Decathlon </h1>

## Task

### The input of the program is a CSV-like text file (see the attachment). The task is to output an JSON file with all athletes in ascending order of their places, containing all the input data plus total score and the place in the competition (in case of equal scores, athletes must share the places, e.g. 3-4 and 3-4 instead of 3 and 4). Draw an algorythm diagram using a tool you prefer. Input file should be uploaded using browser. Be sure to keep the code design simple, but allowing to easily change or add more input sources and/or output file formats. About Decathlon competition: http://en.wikipedia.org/wiki/Decathlon

## Implementation details:

### Implemented django server.

### Used DRF and JS.

### Algorythm diagram is shown in file Algorythm.pdf.

### All calculation logic is located in the file views.py in the api folder.

# How to install a project

## 1. At local computer

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

### Run site in browser:

```
http://127.0.0.1:8000/
```

## 2. In a docker container

### Clone a repository and change to it on the command line:

```
git clone https://github.com/AKafer/Test-task-Decathlon.git
cd Test-task-Decathlon/
```

### Make docker image:

```
docker build -t decathlon .
```

### Run container:

```
docker run --name dec -it -p 8000:8000 decathlon
```

### Run migrations:

```
docker exec -it dec bash
python manage.py migrate
```

### Run site in browser:

```
http://localhost:8000/
```

## How to use:

```
1. Choose a csv file with Decathlon results
2. Press button DOWNLOAD JSON
3. You will get json file and results will be shown in a table
```

### Needed format for csv file (example):

```
Edan Daniele;12.61;5.00;9.22;1.50;60.39;16.43;21.60;2.60;35.81;5.25.72
Lehi Poghos;13.04;4.53;7.79;1.55;64.72;18.74;24.20;2.40;28.20;6.50.76
Coos Kwesi;13.75;4.84;10.12;1.50;68.44;19.18;30.85;2.80;33.88;6.22.75
Severi Eileifr;13.43;4.35;8.64;1.50;66.06;19.05;24.89;2.20;33.48;6.51.01
```

## Technology stack: Python 3, Django 4.1, DRF, JS, jQuery, DataTables

## Project author - SERGEI STOROZHUK
