# **Python Programming**

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nbonacchi/python-programming/binder)

This repository contains the main resources for the Computer Programming 101 course using Python at [ISPA-IU](https://www.ispa.pt/).

The course is based on jupyter notebooks and divided into 2 main modules called:

- **python-intro**  
Introduction to Python variables, operators, boolean logic, data types, flow control, loops, and functions. With extra notebook containing classes, objects, and OOP basics.

- **python-data-science**
Introduction to basic Python libraries for data science, file IO, numpy, matplotlib and data visualization, pandas and data frames. With extra notebooks include a basic implementation of Conway's game of life, linear algebra and machine learning using scikit-learn, network analysys using networkx lib, regular expressions, signal processing using SciPy, text sentiment analysis and word clouds.

The course is designed to be self-paced and the notebooks are meant to be run either in vscode or in jupyter-lab.

</br>

## **Necessary dependencies**

To run the files for this course you need some software installed on your machine.  
Make sure you have *vscode*, *git*, and *uv* installed on your machine. You can download them from here:  
These instructions should work for all (win, mac, linux) operating systems.

**Git** is a free and open source distributed *version control system* that allows you to track changes in code, collaborate with others, and maintain different versions of a project.  
[More info on git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  
**Visual Studio Code** is a free open source code editor developed by Microsoft.  
[More info on vscode](https://code.visualstudio.com/docs/setup/setup-overview)  
**uv** is a fast Python package manager and environment tool.  
[More info on uv](https://docs.astral.sh/uv/)

### Installation steps

#### 1. Install the required software

- [**Download git**](https://git-scm.com/downloads) and follow the installer instructions for your platform.
- [**Download vscode**](https://code.visualstudio.com/download) and follow the instructions for your platform.
- [**Install uv**](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) for your platform.

#### 2. Install VS Code extensions

Open VS Code, go to the *Extensions* menu, and install:

- [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

</br>

## **Setting up the environment**

After installing the required software, follow these steps to set up your environment:

1. Open your terminal application (Anaconda Prompt, Terminal, PowerShell, etc.).
2. Change directory to where you want to store the course files (e.g., Documents):

   ```bash
   cd ~/Documents
   ```

   On Windows, you may use:

   ```bash
   cd %USERPROFILE%\Documents
   ```

3. Clone the repository:

   ```bash
   git clone https://github.com/nbonacchi/python-programming.git
   cd python-programming
   ```

4. Install Python 3.13 using uv and create a virtual environment:

   ```bash
   uv python install 3.13
   uv venv
   ```

5. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

6. Install the required Python packages:

   ```bash
   uv pip install -r requirements.txt
   ```

</br>

## **Launching the notebooks**

The easiest way to launch the notebooks is to use **vscode**.

1. Open vscode and click on the *file* menu and then *open folder*.
2. Select the folder with the course material (python-programming).
3. Click on the *view* menu and then *command palette*.
4. Type *python: select interpreter* and select the environment you created (the `.venv` folder).

Alternatively, you can run the notebooks from the command line.  
To launch the notebooks, activate your virtual environment and run:

```bash
# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate

jupyter-lab
```

</br>

#

# You can now run the notebooks and start learning python programming

</br>

## **Credit**

This course was adapted from the [Digital Skills and Training](https://www.ed.ac.uk/information-services/help-consultancy/is-skills) initiative of the [University of Edimburgh](https://www.ed.ac.uk/) Information Services. The original files for the course can be found [here](https://git.ecdf.ed.ac.uk/digital_skills/python-data-science) and [here](https://git.ecdf.ed.ac.uk/digital_skills/python-intro). 



