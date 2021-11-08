# Setting up your system

To learn and write `python` we need two things to get started:
1) An editor to edit source code files
2) A python interpreter which will run our source code files. This step contains compilation of our source code to byte code and interpreting this byte code (in one step).

The python interpreter is a normal executable and depending on your operation system called `python` or `python.exe`.

Let's install a python interpreter to get started ...

# TL;DR - Version
If you have prior knowledge and just want to get started quickly:
- Download anaconda from https://www.anaconda.com/products/individual
- Run an anaconda shell and make sure that `python --version` prints out the version number of your installed interpreter

```bash
 $ python3 --version
 Python 3.9.7
 ```

Congratulations, you are ready to learn `python` :)

If this was to fast for you or you want more information, have a look at the following chapter.

# Installing a python interpreter

There are different kind of python interpreters and python distributions available. 
I recommend using the Anaconda distribution.

This distribution does not only contain a python interpreter but it also delivers additional packages. We don't need these additional packages in this course (they are used for Machine Learning, Data Science, ...) but the anaconda distribution will also deliver us a minimal *Integrated Development Environment* (IDE). An IDE is used to edit source code files and supports use while developing and searching for errors (yes, there will be errors - nobody's perfect ;).

Next to the additional packages and an IDE, anaconda does also deliver us handy tools like an improved interactive python shell (named `ipython`) and `jupyter notebook`. We will talk about these tools in detail if we need them.

Call up this link and download and install the anaconda package: [Anaconda python](https://www.anaconda.com/products/individual)


After installing the interpreter you can check the python version.

Start a command line (e.g. bash for an unix systems or a cmd.exe command line for windows)
type in `python --version` witout the quotes
You should see a version output like this: "Python 3.8.3"

If you have problems installing anaconda check out the anaconda documentation website: https://docs.anaconda.com/anaconda/install/

## Why anaconda?
The anaconda package uses more disk space than a plain python interpreter installation but delivers us a lot of advanced modules "out of the box". Pythonistas also speak from "batteries included" for such cases. So we have everything we need installed in one package.

There are a lot of other python interpreters like IronPython, Jython, ... but the most common interpreter is the one from python.orgwhich is also used in the anaconda package. I won't talk about the others interpreters.


# Install an Integrated Development Environment (IDE)

By using the anaconda distribution we already have a small and functional IDE installed and we are ready to go. It is not needed to install another IDE to learn python. 

But if you want to work with a more fullblown IDE  and you know what you are doing, than I recommend one of these two IDEs:


[Visual Studio Code](https://code.visualstudio.com/Download "Download Visual Studio Code")
 Make sure that you also have the python extension installed. This is needed for additional features like debugging. 

[PyCharm Community](https://www.jetbrains.com/de-de/pycharm/download/#section=linux, "Pycharm Download"): If you are more into the Jetbrains products, check out PyCharm. A very rich and good Python IDE. 

[Overview](../overview.md) \| [Next (Variables)](../02_variables/variables.md)
