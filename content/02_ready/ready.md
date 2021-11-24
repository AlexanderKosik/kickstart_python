# Ready to go
Now that we have an installed Python environment we are ready to go. You can only learn programming by doing. Programming is like learning to ride a bike. You can read many books about bikes, but you will only know what it is really like to ride a bike if you try it out for yourself.

This means your starting point is reading the chapters carefully but also you *must* also become active and try things out and explore for yourself. This exploration is an active process where you create a mental model of how things work. This mental model must be tested, extended, falsified and corrected. This might take some time and it is exhausting but it is worth the effort and you can unterstands things better.

We will start by using and exploring an interactive Python session as a calculator.

# Python as a calculator
For our first exploration we will use a Python REPL. REPL stands for: Read - Evaluate - Print - Loop. Starting Python in an interactive REPL mode helps us exploring things and sharpening our mental model.

We start a Python REPL by opening an interactive interactive Python session:
``` python
$ python3
```
You will see a Python Prompt:
![Interactive Python session](ressources/ipython.png "Interactive Python session")

Lets try to calculate how much money a year we make if we get a monthly salary of $3250 and bonus of $4500 once a year:
``` python
>>> 3250 * 12 + 4500
43500
``` 
As you see Python behaves like a normal calculator and prints the result of our expression immediatly. Let's continue with another example.

Lets try to calculate how long it takes for light beam to travel from the sun to the earth. We can do this by dividing the distance between the sun and the earth by the speed of light **c**.
Mean distance between sun and earth: 149600000 km
Speed of light: 300000 km per second

``` python
>>> 149600000 // 300000 
498
``` 

The two backslashes between our numbers is called an `operator`. In the example above we used a so called `truncating division` by using `\\`. This will deliver us an integer value and the result is rounded down. Compare what changes if you use a "normal division" by using the `\` operator 

``` python
>>> 149600000 / 300000 
498.6666666666667
``` 

By using a `\` we get a floating point value as a result. The result we get is in seconds. If we want to results in minutes we must divide our last result by 60.

In an interactive sessions the last result of a calculation is stored automatically. We can access it by using `_`. Pay attention: This does only apply to interactive sessions!

``` python
>>> 149600000 / 300000 
498.6666666666667
>>> _ / 60
8.311111111111112
``` 

So a light beam takes a little bit more than 8 minutes from the sun to the earth.

# Literals
So far we have explored two data types in Python: an integer representing a whole number and floating point numbers. A direct denotation of data values in programs is known as a **literal**, or more verbose an **integer literal** or rather **floating point literal**. 

# Different number representations
If you read the examples from above it might be hard to figure out the exact numbers without counting decimal places. Is it 1.4 million kilometers to the sun, 14.9 million kilometers or 149.6 million kilometers?!
Python delivers us a possibility to make it easier for humans to read these numbers by using a `_` as a delimiter:

``` python
>>> 149_600_000 // 300_000 
498
``` 

Even though you can technically use the `_` delimiter in every position it is highly encouraged to only use it as a thousands separator.

You can create integer values by also using a scientific representation using `E` or also a lower case `e`. Let's calculate the the travel of a light beam using meters instead of kilometers:
``` python
>>> 149_600_000 * 1E3 // 3E8
498
``` 

# Operators in Python
Python recognizes the following operators, but not all of them are relevant for us now:
```
+ - * / % ** // << >> &
| ^ ~ < <= > >= <> != ==
```

Exercise: 
1) Can you figur out what the `%` and `**` operators do?
2) Play around with some mathematical operators. Can you calculate how many days you are alive? Can you represent the result in days, hours and also in minutes?

# Giving things a name
Let's talk about Identifiers
case sensitivity

# statements, expressions


bool
# if else
string

# immutable/mutable

# further readings: pep8
# chapter reference



