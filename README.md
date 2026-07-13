# GD Elo
A program that assigns a skill rating to Geometry Dash players by the levels they have completed.

![A website with a search bar, captioned GD Elo system](screenshots/Screenshot_20260712_200932.png)

(link)

## Features
- A backend that returns fetches user data straight from RobTop's Geometry Dash servers
- A algorithm that converts the user data returned from RobTop's servers into readable data.
- Another algorithm that uses the data from RobTop's servers to calculate a skill rating/ELO.
- A front end that looks nice.
- A leaderboard of the people with the highest ELO.

## How it works
The client (frontend) sends a request to the server (backend) containing the search query for a user. The backend then sends the name of the user to RobTop's servers, which returns statistics about the user. The username is then also sent to the AREDL API to get list points. The list points and the statistics are calculated into an Elo, which can be from like 1 to several billion probably.The stats and Elo are sent back to the client/frontend to be displayed on a webpage. 

## Credits
- GD Colon's [video on making his own Geometry Dash website](https://www.youtube.com/watch?v=tC-TZX0AAck) was very entertaining and somewhat informative.
- [Boomings.dev](https://boomlings.dev) and [GDDocs](https://wyliemaster.github.io/gddocs/#/) were great resources in learning about how to send requests.
- [AREDL API Documentation](https://api.aredl.net/v2/docs) was helpful in accessing the AREDL API.