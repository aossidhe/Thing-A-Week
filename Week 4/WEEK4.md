# Week 4

## How to Use:

- Run `$ python3 program.py` to run an application that will allow you to generate character traits from a pre-defined database

### Delivered:

- GUI Improvements:
    - GUI is now slightly nicer-looking and reformats nicely when resized
    - Traits Retrieval:
        - Now defaults to 10 records to retrieve
        - The number of traits to retrieve can be edited manually, includes validation so typing in non-numbers doesn't break anything
        - Added incrementer/decrementer buttons
    - Traits Deleting:
        - Can now remove traits from the list 
        - Remove specific ones by selecting them and choosing "Remove selected"
        - Remove all of them by the "Clear all" button
    - Deleted Traits Recovery:
        - Stores deleted traits for retrieval in case of accidental deletion
        - Recovering them re-adds them to the default box and removes them from the deleted list
- Functionality Improvements:
    - Now automatically parses the .tsv file and creates the table if it doesn't exist
    - Will now create the `data` file in the correct directory (i.e. whichever one the program is in)

- Rebased Github a few times after VSCode decided to create/merge to a new branch or something, I don't know

### Practiced/Learned:

- Github rebasing/branch creation
- Python
    - Tkinter GUI
        - Lambda functions
        - Listbox usage
        - Array manipulation
    - Python in general
        - Order of declaring/using functions and variables
            - This was particularly weird, since the paradigm is new to me. Everything has to be declared synchronously, which means you have to set it up quite carefully. I'm sure there are better ways to separate out things into modules, etc, but so far this is a new paradigm and both foreign and an interesting challenge
        - How to work with Linux' file structure and use relative paths vs. absolute paths, etc.
    - sqlite3
        - Importing data
        - Creating tables


### Notes

- I was really excited to see how quickly I've picked up tkinter and been able to begin playing with it/creating new things. I was able to create the "deleted traits" window in ~20 minutes, just by applying things I'd already learned, and I got it working in under an hour (including looking up and implementing lambda functions). I'm pretty sure than now I could create a similar app to this in half an hour, depending on the complexity of the functionality I was aiming for.
- Having it automatically just work (assuming everything is installed) is really nice. I'll have to see about packaging it all up into an executable. That might be a good bit for this next week.
- I didn't push all this to GitHub until Tuesday, but eh. This is a self-challenge, so I'm not going to beat myself up over it.


### Possible Next Steps:

- Traits Generator:
    - Implement some parsing/modification to retrieved traits to modify pronouns (e.g. have a dropdown allowing choice of gender and adjust trait pronouns accordingly)
    - Add ability to save traits list
    - Allow for inserting custom traits/modifying existing ones
    - Add searching for traits
    - Prevent duplicates
    - Prevent conflicting traits
    - Add trait tags to generate specific types (e.g. "appearance", "hair", "family", etc.)
- Program Overall:
    - Improve GUI further, make it not look like something from 2001
    - Package it up into an executable so it doesn't have to be used through CLI and will come with all requirements pre-packaged
    - Add dice roller to the GUI (as the menu items would seem to suggest I have already; do not trust them, for they are deceitful!)
    - Add local AI image generation? Stable Diffusion, etc? Pretty ambitious but could be cool and on-theme