[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nbonacchi/python-programming/binder)
# **Python Programming**
This repository contains the main resources for the Computer Programming 101 course using Python at [ISPA-IU](https://www.ispa.pt/).

The course is based on jupyter notebooks and divided into 2 main modules called:

### **python-intro**
Introduction to Python variables, operators, boolean logic, data types, flow control, loops, and functions. 

Extra notebook containing classes, objects, and OOP basics.
### **python-data-science**
Introduction to basic Python libraries for data science, file IO, numpy, matplotlib and data visualization, pandas and data frames. 

Extra notebooks include a basic implementation of Conway's game of life, linear algebra and machine learning using scikit-learn, network analysys using networkx lib, regular expressions, signal processing using SciPy, text sentiment analysis and word clouds.

<br>

## **Setting up the environment**
The **requirements.txt** file has the necessary python packages for both this and the python-data-science repository.

Before starting you should have both [**git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [**anaconda**](https://www.anaconda.com/products/individual) or [**miniconda**](https://docs.conda.io/en/latest/miniconda.html) installed on your machine.

To install the environment select an **environment name** (e.g. *aulas*) then open a _terminal_ and type:
```bash
$ conda create -n aulas python=3.10
$ conda activate aulas
$ git clone https://github.com/nbonacchi/python-programming.git
$ cd python-programming
$ pip install -r requirements.txt
```

<br>

## **Launching the notebooks**
To launch the notebooks run:
```bash
$ conda activate aulas
$ cd python-programming
$ jupyter-lab
```

<br>

## **Credit**
This course was adapted from the [Digital Skills and Training](https://www.ed.ac.uk/information-services/help-consultancy/is-skills) initiative of the [University of Edimburgh](https://www.ed.ac.uk/) Information Services. The original files for the course can be found [here](https://git.ecdf.ed.ac.uk/digital_skills/python-data-science) and [here](https://git.ecdf.ed.ac.uk/digital_skills/python-intro). Minor edits were done to the README.md files
