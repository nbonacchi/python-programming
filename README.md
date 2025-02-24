
# **Python Programming**

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nbonacchi/python-programming/binder)

This repository contains the main resources for the Computer Programming 101 course using Python at [ISPA-IU](https://www.ispa.pt/).

The course is based on jupyter notebooks and divided into 2 main modules called:

- **python-intro**  
Introduction to Python variables, operators, boolean logic, data types, flow control, loops, and functions. With extra notebook containing classes, objects, and OOP basics.

- **python-data-science**
Introduction to basic Python libraries for data science, file IO, numpy, matplotlib and data visualization, pandas and data frames. With extra notebooks include a basic implementation of Conway's game of life, linear algebra and machine learning using scikit-learn, network analysys using networkx lib, regular expressions, signal processing using SciPy, text sentiment analysis and word clouds.

The course is designed to be self-paced and the notebooks are meant to be run in a jupyter environment.

</br>

## **Necessary dependencies**

To run the files for this course you need some software installed on your machine.  
Make sure you have *vscode* and both *git* and *miniconda* installed on your machine. You can download them from here:  
These instructions should work for all (win, mac, linux) operating systems.

Visual Studio Code is a free open source code editor developed by Microsoft.  
[More info on vscode](https://code.visualstudio.com/docs/setup/setup-overview)  
Git is a free and open source distributed version control system that allows you to track changes in code, collaborate with others, and maintain different versions of a project.  
[More info on git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  
Miniconda is a free minimal installer for *conda*, a package manager that allows you to easily install, run, and update python, its packages and their dependencies.  
[More info on miniconda](https://docs.conda.io/en/latest/miniconda.html).

### Windows

- [**Download vscode**](https://code.visualstudio.com/download) and foillow these [instructions](https://code.visualstudio.com/docs/setup/windows)  
- [**Download git**](https://git-scm.com/downloads/win) and follow the installer instructions.  
- [**Download miniconda**](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) and follow these [instructions](https://docs.anaconda.com/miniconda/install/).  

### MacOS

- [**Download vscode**](https://code.visualstudio.com/download) and foillow these [instructions](https://code.visualstudio.com/docs/setup/mac)  
- [**Download miniconda**](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh) and follow these [instructions](https://docs.anaconda.com/miniconda/install/).

### Linux

- [**Download vscode**](https://code.visualstudio.com/download) and foillow these [instructions](https://code.visualstudio.com/docs/setup/linux)  
- [**Download miniconda**](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) and follow these [instructions](https://docs.anaconda.com/miniconda/install/).

**Note:** Both Linux and MacOS come with git pre-installed.

</br>

## **Setting up the environment**

The **requirements.txt** file has the necessary python packages for both modules.

After all the necessary software is installed, you can now setup the environment to run the course.  
To install the environment you need to:

1) Choose an *environment name* (e.g. **aulas**)
2) Choose where you want to install the files (e.g. **C:\Users\username\Documents\aulas\\** or **~/home/username/Documents/aulas**)
3) Open an *anaconda terminal* (on windows) or a *terminal* (on mac or linux) and run the following commands:

```bash
cd .\Documents\aulas
conda create -n aulas python=3.10
conda activate aulas
git clone https://github.com/nbonacchi/python-programming.git
cd python-programming
pip install -r requirements.txt
```

Explanation of the commands:

- `cd .\Documents\aulas` changes the directory to the one where you want to install the course material.
- `conda create -n aulas python=3.10` creates a new conda environment with the name *aulas* and python version *3.10*.  
- `conda activate aulas` activates the environment, so all the installed packages are available.  
- `git clone https://github.com/nbonacchi/python-programming.git` downloads the repository with the course material.  
- `cd python-programming` changes the directory to the one with the course material.  
- `pip install -r requirements.txt` installs all the necessary packages specified in the **requirements.txt** file.

</br>

## Configure vscode to run python code and jupyter notebooks

Finally, you need to configure vscode to run python code and the jupyter notebooks.
To configure vscode to run python code and the jupyter notebooks you need to install the relevant extensions:

- [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

To install the extensions you need to open vscode and click on the *extensions* menu and then *marketplace*.  
After that you can search for the extensions you want to install and click on *install*.

Note: vscode has an ever growing number of extensions for all the programming languages.  
There are lot of features that can be customized to your liking.  
You can find more information about vscode extensions [here](https://code.visualstudio.com/docs/getstarted/keybindings).

You should now have the necessary extensions installed. We are almost ready to run the notebooks.

</br>

## **Launching the notebooks**

The easiest way to launch the notebooks is to use **vscode**.

1) Open vscode and click on the *file* menu and then *open folder*.
2) Select the folder with the course material (python-programming).
3) Click on the *view* menu and then *command palette*.
4) Type *python: select interpreter* and select the environment you created (e.g. *aulas*).

Alternatively you can run the notebooks from the command line.
To launch the notebooks, open an *anaconda terminal* (on windows) or a *terminal* (on mac or linux) and run:

```bash
conda activate aulas
cd ./Documents/aulas/python-programming
jupyter-lab
```

Explanation of the commands:

- `conda activate aulas` creates a new conda environment with the name *aulas* and python version *3.10*.
- `cd ./Documents/aulas/python-programming` changes the directory to the one with the course material.
- `jupyter-lab` launches the notebooks from the course material folder.

</br>

#

# You can now run the notebooks and start learning python programming

</br>

## **Credit**

This course was adapted from the [Digital Skills and Training](https://www.ed.ac.uk/information-services/help-consultancy/is-skills) initiative of the [University of Edimburgh](https://www.ed.ac.uk/) Information Services. The original files for the course can be found [here](https://git.ecdf.ed.ac.uk/digital_skills/python-data-science) and [here](https://git.ecdf.ed.ac.uk/digital_skills/python-intro). Minor edits were done to the README.md files
