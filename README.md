BrainNyan
=========
BrainNyan is another super inefficient BF interpreter with a twist: The user can specify a mapping between a set of strings and the standard BF keywords to form their own 'dialect' of the language!

The interpreter is named after the first such dialect that I wrote.

Why?
====
BrainNyan was originally written in June 2011 as an exercise in C coding, using source control, and good taste. This repository was created to store the goodness that was BrainNyan. I promptly didn't commit the code and it was lost a few months later. This made it a _failed_ exercise in source control.

Almost four years later, I once again laid eyes on this lonely, empty repository. Even though I know the project was a little pointless, I couldn't bring myself to delete it. And so here it is! BrainNyan lives, thrown together in a couple of hours in Python, and saved from the dark realm into which all dead ideas go.

Usage
=====
BrainNyan is invoked like so:

    ./brainnyan.py [-i] <keyword mapping file> <code file>

BrainNyan will then run your code by first stripping out non-keywords and then converting the remainder into standard BF. This is then run through a simple interprerter to produce the required output.

The keyword mapping file contains a JSON object describing the mapping between your dialect's keywords and the BF keywords. See below for an example.

The code file contains your dialect's code, composed of your chosen keywords. All non-keywords are ignored by the interpreter.

If the -i option is specified, keywords are considered case insensitive, otherwise keywords are case sensitive.

Example
=======
The project contains the following test.keywords file:

    {
    "nyan": ">",
    "wan": "<",
    "neko": ".",
    "inu": ",",
    "tsun": "+",
    "dere": "-",
    "anta": "[",
    "baka": "]"
    }

And the following test.text file (lovingly translated from a BF example on Wikipedia):

    Tsun! Tsun, tsun. Tsuntsun? Tsun! Tsun. Tsun.  Anta!  Nyan!  Tsun! Tsun! Tsun! Tsun! Anta!  
    Nyan!  Tsun! Tsun! Nyan! Tsun! Tsun! Tsun! Nyan!  Tsun! Tsun! Tsun! Nyan!  Tsun! Wan Wan 
    Wan Wan Dere!  Baka! Nyan!  Tsun! Nyan!  Tsun! Nyan! Dere!  Nyan!  Nyan!  Tsun! Anta!  Wan 
    Baka! WanDere!  Baka! Nyan!  Nyan! Neko! Nyan! Dere! Dere! Dere! Neko! Tsun! Tsun! Tsun! 
    Tsun! Tsun! Tsun! Tsun!Neko!Neko! Tsun! Tsun! Tsun!Neko! Nyan!  Nyan! Neko! WanDere! Neko! 
    WanNeko! Tsun! Tsun! Tsun! Neko!Dere! Dere! Dere! Dere! Dere! Dere! Neko!Dere! Dere! Dere! 
    Dere! Dere! Dere! Dere! Dere! Neko! Nyan!  Nyan! Tsun!Neko! Nyan!  Tsun! Tsun! Nyan! Neko!

By invoking BrainNyan thusly:

    ./brainnyan.py -i test.keywords test.text
    
We receive the following output:

    Hello World!
    
Truly, this is a modern wonder.

Things to do
============
* Figure out what happens if keywords are prefixes of each other (eg. Keywords 'n', 'ne', 'nek' and 'neko')
