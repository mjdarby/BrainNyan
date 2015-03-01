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

    Ahem. This is a BrainNy4n program. It will read like the ramblings of a mad
    man, but that is entirely normal.

    Tsun! I love a bit of tsun. Tsun is the way to be. If you're doubly so, are
    you tsuntsun? Tsun... Tsun is a state of mind!? Tsun is life!  Anta wouldn't
    understand~  Nyan, tsuntsun! A cat who is tsuntsun! Don't you think that's the
    best? If not, ANTA BWAKA! Nyancore is the best music genre. I'm tsun for
    grunge, but not so tsun for indie rock.

    My cat has something to say: Nyan! I think my cat is tsun for me. Then again,
    one might suppose cats are tsun for most things. If they weren't so tsun,
    maybe we'd hear less nyan and more purring. They always start off tsun, but
    with a bit of effort you can reduce the tsun levels with treats. But screw up,
    and they'll be back to super tsun faster than you can say nyan! Or even tsun!

    A dog goes wan wan and it makes my heart go wan wan kyun! So dere! Not baka at
    at all. If a dog hears a nyan, it goes all tsun! Nyan: Tsun. No nyan: Dere!
    Nyannyan is way out. All you get for that is tsun. Anta! Do you understand the
    power of the wan yet, baka? Wan: Dere! Baka: Nyan! Nyan comes from nekos! Nyan
    is not dere! Only dere is dere!

    Never fear the power of the neko. Though their tsun power is unrivalled,
    their tsun nature makes them woefully weak against puppies. Tsun is only good
    for one thing: Generating more tsun! Tsun can be beautiful, but only if you
    like tsun! If you like tsun, you will like nekos. Neko = Tsun! Tsun = Tsun!
    Nekos go nyan! Nyan = Neko! Wan = Dere! I'm losing my mind! Neko! Wan Neko!
    Tsun! Tsun! Tsun! Neko! Dere! Dere! Dere! Dere! Dere! Dere! Neko! Dere! Dere!
    Dere! Dere! Dere! Dere! Dere! Dere! Neko! Nyan! Nyan! Tsun! Neko! Nyan! Tsun!
    Tsun! Nyan! Neko!

By invoking BrainNyan thusly:

    ./brainnyan.py -i test.keywords test.text

We receive the following output:

    Hello World!

Truly, this is a modern wonder.

Things to do
============
* Figure out what happens if keywords are prefixes of each other (eg. Keywords 'n', 'ne', 'nek' and 'neko')
