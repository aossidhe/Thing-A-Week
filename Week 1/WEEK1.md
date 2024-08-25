Welcome to my first weekly set of projects!

The first project is a D&D dice equation parser--basically a program to automatically compute D&D rolls. I wrote it in Python via Linux CLI. I've used Linux for programming before, but it's been ages and it was neat to get back into it. I chose Python for the language because it's a very common language and I've never used it, so it seemed like a good one to start to build new skills with. One of the first things I learned was that I don't like using Python. Whitespace-gnostic languages are dumb, and the loosey-goosey typing and horrible combination of both silent error handling and nigh-useless error logs/stack traces is awful to deal with. Python is often recommended as the best beginner language for someone learning to code, and after getting into it, I think that's either incredibly myopic or a cruel joke. Sure, you get to avoid worrying about strict typing, but that's actually a good thing to have to learn and prevents errors, especially when learning. Anyway, here's what I've got.

Currently the program works off CLI, either by 

	$ python3 roller.py [roll]

or by using it as an executable:

	$ ./roller.py [roll]

It's an abstract grammar parser that supports the following operations:

- Integers
- Addition and subtraction
- Multiplication and division (floored division, so it returns only the integer part of the quotient)
- Parentheses
- Dice rolls of the form kdn: k rolls of n-sided dice, where k and n are positive integers
    - Also supports the form dn, defaulting to one roll of an n-sided die
- Advantage in the form kan, which makes two sets of k rolls of n-sided dice and keeps the higher of the two
    - Supports the same defaulting behavior as a standard dice roll
- Disadvantage in the form kbn or kzn, which makes two sets of k rolls of n-sided dice and keeps the lower of the two
    - Supports the same defaulting behavior as a standard dice roll

The calculations obey order of operations, with dice rolls having a higher priority than multiplication/division. All inputs must be put in as a single string with no whitespace. Due to the way bash interprets strings, it may be necessary to wrap the argument in quotes, e.g. 

	$ ./roller.py "(1+2)d8"

will simplify to/calculate as

    $ ./roller.py "3d8"

There are a few more operations I'd like to add eventually, as well as some quality of life features like not needing to call the executable every time and accepting whitespaces, but this is a good proof of concept. I've never worked with grammar parsing before, and it was an interesting challenge that I think expanded my understanding of various computer science concepts.

The second thing in here is a quick video made for my friend’s upcoming engagement announcement; she and her fiancee are making a video where a bunch of their friends get the news that they’re getting married and rush out to see it. Super fun idea! I shot it in about fifteen minutes with the help of my aikido comrades, and then spent way too long editing it. It’s not perfect, and I still need to fix the audio and ADR in my friend saying I’ve got a call as he comes to hand me my phone, but I did quite a lot with Adobe Premiere, visual transitions, editing, masking, etc. Ultimately, I ended up going with a very simple cut, since it doesn’t have to be perfect, but I learned a lot about editing transitions, and I think if I were to remake this video it’d be a lot easier, not just in post but also in setting up and getting the shots to make the editing easier.

Finally, I’m hoping to create a website to host all these projects on, but the domain name service I went with suddenly and silently locked me out of everything, and I only just got it resolved yesterday evening, so that fell through. Maybe setting up the website will be (one of) my projects for next week.
