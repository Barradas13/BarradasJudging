# Barradas Judge

A lightweight **open-source online judge** built to provide a local judge with any problems wanted.  
This project allows students and teachers to **practice programming problems from whichever problem they want to** directly through a simple web interface running locally.

---

## Overview

The Barradas Judge automatically organizes problems, PDFs, and gabaritos (answer files) from the json given, providing an independent environment to view statements and test solutions.


## Features

- Structure problems by **year, phase, and level**  
- **Search bar** to find problems quickly  
- Embedded PDF statements  
- Upload and simulate **code submissions**  
- Supports the languages:
  - C (`.c`)
  - C++ (`.cpp`)
  - Pascal (`.pas`)
  - Java (`.java`)
  - Python 3 (`.py`)
  - JavaScript (`.js`)

---

## Important informations

This project is based on 2 things:

 - The web application that offers an interface with the problems to solve;
 - A server which will receive code, run it and send the outputs.

If you want to run it 100% locally you can use the compose example of this repo, it has a judge image which will serve as the server to compile and execute the code.

If you want to run it locally just the web application you need to have a web url for an online judge, for exaple: https://ce.judge0.com/.

Note, you will need to prove a json file with the problems stuctures and pdf, zil urls, these urls need to be fully open to anyone on the internet and they must end with .pdf or .zip, for example you can use a github repository with github pages as you can see in: https://github.com/Barradas13/Exerc-cios1Info.

The Json must be converted to base64 so you can use: ``` base64 -w 0 input.json > base64.txt ``` and then copy the base64.txt and paste on .env.

The Json structure can be seen on ./static/exemplo.json

## Running Locally (Development)

### 1. Clone the Repository
```bash
git clone https://github.com/barradas13/barradasjudging.git
````

### 2. Install Dependencies

Using **Poetry**:

```bash
poetry install
```

### 3. Run the Application 

```bash
poetry run python3 app.py
```

Once running, the web interface will be available at:

```
http://localhost:5000
```

---