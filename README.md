Jungle Game (Python 2.7)
========================

A simple text-only Python game based on exercise 45 in Zed Shaw's free online book [Learn Python the Hard Way](http://learnpythonthehardway.org/book/).

This exercise is supposed to teach us (beginners) more about object-oriented programming concepts. In a previous exercise (43), we started building a game with skeleton classes provided by Zed. This time, we start from scratch and design our own text game (like [Zork](http://en.wikipedia.org/wiki/Zork) or [Adventure](http://en.wikipedia.org/wiki/Colossal_Cave_Adventure)). 

In ex. 43, everything was coded in a single .py file. Now, in ex. 45, we are tasked with using multiple files (modules).

This has been a GREAT learning exercise for working with objects. I had never understood OOP until three weeks ago. Now I understand a lot more. Granted, this is only a simple game, but in working with variables, lists, and functions in this game, I've learned a ton about how to traverse the classes in my code.

## The Game

You are a biologist who needs to find a rare fruit tree in the dangerous tropical jungle and return to your starting point with a sample of the fruit intact. You can travel through 31 locations to fulfill your quest. Along the way you will need to solve a few puzzles, including how to get past some jungle predators.

## Current Status

At this point, most "adventures" do not run yet. However, you can step through all of the locations, and nothing throws an error. 

In location 27 (game starting point), you can pick up and drop several items. You can carry them to other locations and drop them there, and pick them up later. You can put items into the raft. Can't do much else yet.

* To run the game: main.py

* You can quit cleanly by typing: exit

## Game History

Feb. 4, 2014 - Started the exercise. Drew game map on paper. Listed all items and locations to be used in game. Thought up puzzles and how to solve them.

Feb. 6 - Coded skeleton classes for all game locations. Made a dictionary (map) for all game locations. Made Engine class to run the game. 

Feb. 7 - Created skeleton classes for all game items. These are things that can be picked up, carried, and used. First commit to GitHub. 

Feb. 8 - Added function use_item() to Location() class. Not finished yet, but it allows the player to pick up, drop, and examine items that are found in the game. Also worked out a new function -- defaults() -- for handling directional movement from one location to another. That required a rewrite of the Engine() class.

Feb. 9 - Lots of work on taking and dropping items, carrying them to different locations, and making the raft an item that can only be carried alone, not with other items. Lots of trial and error. Reorganized functions in main Location() class.

Feb. 11 - More work on items. Now they can be put into the raft; the raft cannot be carried when things are inside it; the things can be seen if they are inside the raft. The put_items() function was time-consuming.

Feb. 12 - Zed says spend a week on this. My week is up. However, before I return to Zed's exercise 45, I want to get the raft into the water. I've got walkthrough capability for all scenes (some do not have descriptions written) and all objects can be picked up, carried, dropped, or put into the raft. Items can be taken out of the raft. The machete can be used in two locations.

