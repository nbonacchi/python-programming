# Python Programming
This repository contains the main resources for the Computer Programming course of the [Masters in Cognitive and Behavioral Neuroscience](https://www.ispa.pt/oferta-formativa/mestrado-neurociencias-cognitivas-e-comportamentais/) at [ISPA-IU](https://www.ispa.pt/)

#### **python-intro**
These worksheets will be covered in classes 2 and 3 of the course  

#### **python-data-science**
These worksheets will be covered in class 3 and 4 of the course  

### Setting up the environment
The **requirements.txt** file has the necessary python packages for both this and the python-data-science repository.

Before starting you should have both [**git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [**anaconda**](https://www.anaconda.com/products/individual) or [**miniconda**](https://docs.conda.io/en/latest/miniconda.html) installed on your machine.

To install the environment select an **environment name** (e.g. *aulas*) then open a terminal and substitute **\<env_name>** in the following commands with the name you selected:
```bash
$ conda create -n <env_name> python=3.9
$ conda activate <env_name>
$ git clone https://github.com/nbonacchi/python-programming.git
$ cd python-programming
$ pip install -r requirements.txt
```

### Launching the notebooks
To launch the notebooks run:
```bash
$ conda activate <env_name>
$ cd python-programming
$ jupyter-lab
```



### Credit
This course was adapted from the [Digital Skills and Training](https://www.ed.ac.uk/information-services/help-consultancy/is-skills) initiative of the [University of Edimburgh](https://www.ed.ac.uk/) Information Services. The original files for the course can be found [here](https://git.ecdf.ed.ac.uk/digital_skills/python-data-science) and [here](https://git.ecdf.ed.ac.uk/digital_skills/python-intro). Minor edits were done to the README.md files