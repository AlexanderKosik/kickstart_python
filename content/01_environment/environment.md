# Setting up your system

To learn and write `python` we need two things to get started:

1) An editor to edit source code files

2) A python interpreter which will run our source code files. This step contains compilation of our source code to byte code and interpreting this byte code (in one step).

The python interpreter is a normal executable and depending on your operation system called `python` or `python.exe`.

Let's install a python interpreter to get started ...

# TL;DR - Version
If you have prior knowledge and just want to get started quickly:
- Download anaconda from [here](https://www.anaconda.com/products/individual "Anaconda Download") and install it
- Run an anaconda shell and make sure that `python --version` prints out the version number of your installed interpreter

```bash
 $ python --version
 Python 3.8.8
 ```

Congratulations, you are ready to learn `python` :blush:

If this was to fast for you or you want more information, have a look at the following chapter.

# Installing a python interpreter

There are different kind of python interpreters and python distributions available. 
I recommend using the Anaconda distribution.

This distribution does not only contain a python interpreter but it also delivers additional packages. We don't need these additional packages in this course (they are used for Machine Learning, Data Science, ...) but the anaconda distribution will also deliver us a minimal *Integrated Development Environment* (IDE). An IDE is used to edit source code files and supports use while developing and searching for errors (yes, there will be errors - nobody's perfect ;).

Next to the additional packages and an IDE, anaconda does also deliver us handy tools like an improved interactive python shell (named `ipython`) and `jupyter notebook`. We will talk about these tools in detail if we need them.

Call up this link and download and install the anaconda package: [Anaconda python](https://www.anaconda.com/products/individual)

I will explain the installation step by step for a unix operation system. If you have Windows or MacOS and need further help, check out the [anaconda documentation](https://docs.anaconda.com/anaconda/install/). 

1) Start by changing making the downloaded shell script executable:
```bash
$ chmod +x Anaconda3-20xx.xx-Linux-x86_64.sh
```
2) Execute the shell script and follow along the instructions
```bash
$ ./Anaconda3-20xx.xx-Linux-x86_64.sh
```
3) If you have chosen the default settings during installation the conda environment is not activated by default.

To activate the anaconda environment, follow this step as stated in the installation description:
```bash
You have chosen to not have conda modify your shell scripts at all.
To activate conda's base environment in your current shell session:

eval "$(/home/xxx/anaconda3/bin/conda shell.YOUR_SHELL_NAME hook)"
```
So in my case I use the zsh shell, so I execute this command:
```bash
eval "$(/home/alex/anaconda3/bin/conda shell.zsh hook)"
```
4) Check that your conda environment is activated. You will see a `(base)` before your prompt and call `python --version` to check your python version
```bash
─alex@XPS-13  ~ ‹node-›  ‹› 
╰─$ eval "$(/home/alex/anaconda3/bin/conda shell.zsh hook)"            
(base) ╭─alex@XPS-13  ~ ‹node-›  ‹› 
╰─$ python --version
Python 3.8.8
```

Congratulations! Now you are ready to go! :smiley:

> Hint: If you use windows just press *start* and search and open the anaconda prompt. This will automatically activate your anaconda environment and you are ready to go.

## Why anaconda?
The anaconda package uses more disk space than a plain python interpreter installation but delivers us a lot of advanced modules "out of the box". Pythonistas also speak from "batteries included" for such cases. So we have everything we need installed in one package.

There are a lot of other python interpreters like IronPython, Jython, ... but the most common interpreter is the one from python.orgwhich is also used in the anaconda package. I won't talk about the others interpreters.


# Install an Integrated Development Environment (IDE)

By using the anaconda distribution we already have a small and functional IDE installed and we are ready to go. It is not needed to install another IDE to learn python. 

But if you want to work with a more fullblown IDE  and you know what you are doing, than I recommend one of these two IDEs:


[Visual Studio Code](https://code.visualstudio.com/Download "Download Visual Studio Code")
 Make sure that you also have the python extension installed. This is needed for additional features like debugging. 

[PyCharm Community](https://www.jetbrains.com/de-de/pycharm/download/#section=linux, "Pycharm Download"): If you are more into the Jetbrains products, check out PyCharm. A very rich and good Python IDE. 

# Exercises
[Exercises for week 1](../../exercises/week1/week1.md)

[Overview](../overview.md) \| [Next (Variables)](../02_variables/variables.md)
