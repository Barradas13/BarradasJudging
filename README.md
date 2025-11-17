
# Barradas Judge

A lightweight **open-source online judge** designed to provide a fully local environment for testing programming problems from any source.  
This project allows students and teachers to **practice competitive programming and algorithm problems** through a simple local web interface.

---

## Overview

Barradas Judge automatically organizes problem statements, PDFs, and answer files from a provided JSON configuration.  
It creates an independent, self-contained environment where users can browse problems and test their solutions.

---

## Features

- Organized problem structure by **year, phase, and level**  
- **Search bar** for quick problem lookup  
- Embedded PDF viewers for statements  
- Upload and evaluate **code submissions**  
- Supports multiple languages:
  - C (`.c`)
  - C++ (`.cpp`)
  - Pascal (`.pas`)
  - Java (`.java`)
  - Python 3 (`.py`)
  - JavaScript (`.js`)

---

## Important Information

This project relies on two main components:

1. **The web application**, which displays the problems and handles submissions  
2. **A judge server**, which compiles and executes the code (Judge0 or any compatible API)

### Running fully locally
You can run the entire system locally using the `docker-compose` example provided in this repository.  
It includes a Judge0 container that acts as the execution backend.

### Running only the web application
If you want to run only the web interface locally, you must provide a **remote Judge0 API URL**, such as:

```

[https://ce.judge0.com/](https://ce.judge0.com/)

````

### Problem JSON file
You must provide a JSON file that describes the problem list and includes URLs for PDFs and ZIP files.  
These URLs must:

- Be publicly accessible on the internet  
- End with `.pdf` or `.zip`  
- Remain accessible at all times  

For example, you can host your problems on GitHub Pages, as shown here:  
`https://github.com/Barradas13/Exerc-cios1Info`

#### Converting the JSON to Base64
The JSON must be encoded in Base64 before being placed in the `.env` file:

```bash
base64 -w 0 input.json > base64.txt
````

Then copy the contents of `base64.txt` into your `.env` file.

The JSON structure example is available at:

```
./static/exemplo.json
```

---

## Running Locally (Development)

### 1. Clone the Repository

```bash
git clone https://github.com/barradas13/barradasjudging.git
```

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

## Docker (Optional)

A ready-to-use `docker-compose.yml` is included for running both the web app and Judge0 locally.

You will just need to adapt the json with the problems you want, at static there is a json with all obi problems, so if you are interested in OBI problems you sure will have some fun!