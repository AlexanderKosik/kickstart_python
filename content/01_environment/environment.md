# Setting up your system

To learn and write Python code, we need two things to get started:

1) An editor to edit source code files

2) A Python interpreter which will run our source code files. This step compiles our source code to byte code and interprets this byte code (all in one step).

The Python interpreter is a normal executable and depending on your operation system called `python` or `python.exe`.

Let's install a Python interpreter to get started ...

# TL;DR - Version
If you have prior knowledge and just want to get started quickly:
- Download Anaconda from [here](https://www.anaconda.com/products/individual "Anaconda Download") and install it
- Run an Anaconda shell and make sure that `python --version` prints out the version number of your installed interpreter

```bash
 $ python --version
 Python 3.8.8
 ```

Congratulations, you are ready to learn Python! :blush:

If this was too fast for you or you want more information, have a look at the following chapter.

# Installing a Python interpreter

There are different kinds of Python interpreters and Python distributions available.
I recommend using the Anaconda distribution.

This distribution not only contains a Python interpreter, but also delivers additional packages. We don't need these additional packages in this course (they are used for Machine Learning, Data Science, etc.) but the Anaconda distribution will also deliver us a minimal *Integrated Development Environment* (IDE). An IDE is used to edit source code files and supports us while developing and searching for errors (yes, there will be errors - nobody's perfect ;)

As well as providing additional packages and an IDE, Anaconda also presents us with handy tools like an improved interactive Python shell (named `ipython`) and `jupyter notebook`. We will talk about these tools in detail if we need them.

Click this link to download and install the Anaconda package: [Anaconda Python](https://www.anaconda.com/products/individual)

I will explain the installation step-by-step for a Unix operation system. If you have Windows or MacOS and need further help, check out the [Anaconda documentation](https://docs.anaconda.com/anaconda/install/).

1) Start by making the downloaded shell script executable:
```bash
$ chmod +x Anaconda3-20xx.xx-Linux-x86_64.sh
```
2) Execute the shell script and follow the instructions:
```bash
$ ./Anaconda3-20xx.xx-Linux-x86_64.sh
```
3) If you have chosen the default settings during installation, the conda environment is not activated by default.

To activate the Anaconda environment, follow this step as stated in the installation description:
```bash
You have chosen to not have conda modify your shell scripts at all.
To activate conda's base environment in your current shell session:

eval "$(/home/xxx/anaconda3/bin/conda shell.YOUR_SHELL_NAME hook)"
```
So in my case I use the zsh shell, so I execute this command:
```bash
eval "$(/home/alex/anaconda3/bin/conda shell.zsh hook)"
```
4) Check that your conda environment is activated. You will see a `(base)` before your prompt and call `python --version` to check your Python version
```bash
─alex@XPS-13  ~ ‹node-›  ‹›
╰─$ eval "$(/home/alex/anaconda3/bin/conda shell.zsh hook)"            
(base) ╭─alex@XPS-13  ~ ‹node-›  ‹›
╰─$ python --version
Python 3.8.8
```

Congratulations! Now you are ready to go! :smiley:

> Hint: If you use Windows, just press *start*, then search for and open the Anaconda prompt. This will automatically activate your Anaconda environment and you are ready to go.

## Why Anaconda?
The Anaconda package uses more disk space than a plain Python interpreter installation, but supplies us with a lot of advanced modules "out of the box". Pythonistas refer to it as a "batteries included" distribution, since we have everything we need installed in one go.

There are a lot of other Python interpreters like IronPython, Jython, but the most common interpreter is the one from python.org which is also used in the Anaconda package. If you like, you can explore these at your own leisure.


# Install an Integrated Development Environment (IDE)

By using the Anaconda distribution, we already have a small and functional IDE installed and we are ready to go. It is not necessary to install another IDE to learn Python. However, if you want to work with a more full-blown IDE and you know what you are doing, then I recommend one of the following two IDEs:


[Visual Studio Code](https://code.visualstudio.com/Download "Download Visual Studio Code")
 Make sure that you also have the Python extension installed. This is needed for additional features like debugging.

[PyCharm Community](https://www.jetbrains.com/de-de/pycharm/download/#section=linux, "Pycharm Download"): If you are more into the Jetbrains products, check out PyCharm. A very rich and good Python IDE. 

# Exercises
[Exercises for week 1](../../exercises/week1/week1.md)

[Overview](../overview.md) \| [Next (Let's go)](../02_ready/ready.md)
