# Greed Specification

> He who is not contented with what he has,
> would not be contented with what he would like to have.
> 
> &mdash; Socrates &mdash;
## Overview
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Rules
Greed is played according to the following rules.

- Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
- The player (#) can move left or right along the bottom of the screen.
- If the player touches a gem they earn a point.
- If the player touches a rock they lose a point.
- Gems and rocks are removed when the player touches them.
- The game continues until the player closes the window.

## Interface
<img src="greed-screenshot.png" width="60%" alt="Greed Game Screenshot">

## Project Structure

---

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- greed               (source code for game)
  +-- directoring       (director class for game)
  +-- casting           (specific game classes)
  +-- services          (services game classes)
  +-- shared            (game definition classes)
  +-- __main__.py       (entry point for program)
+-- design.png          (UML Class design)
+-- README.md           (general info)
```

## Requirements
Your program must also meet the following requirements.

- The program must have a README file.
- The program must have at least eight classes.
- Each module, class and method must have a corresponding comment.
- The game must remain generally true to the order of play described earlier.

## Development Setup
In order to have a consistent experience in all platforms you must create a virtual environment
and download the corresponding libraries
- Create Virtual Environment: ```py -m venv venv --prompt GreedGame```
- Activate Virtual Environment: ```.\venv\Scripts\activate```(windows) ```source ./venv/bin/activate```(MacOS / Linux)
- Install required libraries: ```pip install -r requirements.txt```

## Run the App
After you have finished the Development Environment Setup and with an activated
environment, you can run the app with the command ```py Greed```

## Team Members
- Cate Schmidt  <ch21103@byui.edu>
- Danny Hernandez -> her17048@byui.edu
- Reynaldo Armenta Bravo -> arm19008@byui.edu
- Anthuan Morera Zaldivar -> mor21098@byui.edu
- Alan Montoya -> mon21033@byui.edu

## Have Some Fun
Make the game your own by enhancing it any way you like. Here are a few ideas.

- Enhanced gems and rocks (multiple kinds, different points).
- Enhanced player movement (up and down in a limited range)
- Enhanced game play and game over messages.
- Enhanced gem, rock and player representation (colors or better symbols)