# 📑 Document Indexing Algorithm
A Google-like document indexing algorithm, developed as a [Trybe](https://www.betrybe.com) Project.

## 💻 About this project
In this application the user can annex text files to later operate search functions on these files. Thus, the application has a files management module and a word search module.

Some files have been provided by [Trybe](https://www.betrybe.com) to accelerate the application development start, as some files in `./statics` that were used to test.

## 🛠️ Built with
<a href="https://docs.python.org/3/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>

## 🎯 Used skills
- Integrated class modularization
- Operations' asymptotic analysis

## 🏁 Getting started
### 🐍 Installing Python 3
You will need Python 3 in order to run the application. You can see how to install it [here](https://wiki.python.org/moin/BeginnersGuide/Download).
Once Python 3 is installed, you can follow the next steps to create a virtual enviroment and install the dependencies in it.

### 🌱 Creating virtual enviroment and installing dependencies
To create the virtual enviroment, run:
```
python3 -m venv .venv
```
To activate the virtual enviroment in a shell enviroment, run:
```
source .venv/bin/activate
```
To deactivate the virtual enviroment, you can simply run the command `deactivate`.

To install the dependencies in virtual enviroment, run:
```
python3 -m pip install -r dev-requirements.txt
```

## 🧪 Testing
To execute all tests, in virtual enviroment run:
```
python3 -m pytest
```
If some issue occurs, you can alternatively run `python3 -m pytest -s -vv`.

To execute one specifict test file, you can run the command with the file path. Example:
```
python3 -m pytest tests/file_path/file_name.py
```
To execute one specific test function, you can run the command with the flag `-k` and the function. Example:
```
python3 -m pytest -k function_name
```
