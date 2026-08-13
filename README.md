# Geometry Dash Elo System
A program that assigns a skill rating to Geometry Dash players by the levels they have completed.

![A website with a search bar, captioned GD Elo system](screenshots/Screenshot_20260712_200932.png)

[Download here]()
This was originally supposed to be a web app, but I couldn't find anywhere to host the backend that didn't get blocked by Cloudflare.

## Features
- Fetches data about users from RobTop's Geometry Dash servers and the All Rated Extreme Demon List servers
- Proocesses data to be readable by humans
- Generates skill rating from the data

## How it works
The program sends a request to RobTop's servers for information on the player requested by the user of the program. The servers send back what appears as gibberish, and the program processes it into something that is readable. The readable data is either processed even more to calculate the ELO, or is returned directly to the user

## How to run locally
I'm assuming this is refering to running the code through like the .py files instead of the executable files.
### Requirements:
- Python 3.14.6
- Requests 2.34.2 (library)
- Tkinter (usually is already installed, but sometimes it isn't, as was the case on my system)
- All the other libraries in the requirements.txt file. I don't understand what they do or why I needed them, but I assume they were installed alongside the requests library.
### Instructions
Run the python file (.py). Double click it. If the dependancies are installed on your system, it should work

## Credits
- GD Colon's [video on making his own Geometry Dash website](https://www.youtube.com/watch?v=tC-TZX0AAck) was very entertaining and somewhat informative.
- [Boomings.dev](https://boomlings.dev) and it's older (more outdated) sibling [GDDocs](https://wyliemaster.github.io/gddocs/#/) were great resources in learning about how to send requests.
- [AREDL API Documentation](https://api.aredl.net/v2/docs) was helpful in accessing the AREDL API.
- [Bro Code's Tkinter Tutorial]() was very helpful in making the GUI, as I didn't know much about Tkinter when starting the project.
