# NEXUS appointment checker
Are you frustrated that there are no interview appointments available?
Get notified when an appointment slot opens up at your preferred location(s).

Currently configured to generate a MacOS alert and send a Whatsapp message when available appointments are found at any of the selected locations.
The `Notifier` class can be extended to send notifications through other methods.

## Setup:
- clone the repo.
- create a python environment and install dependencies from `requirements.txt`.
- open .env_example and set the phone number(s) you want to notify. Save this as .env.
- run `main.py`.
- To make the program run on a schedule, I used crontab (MacOS, Linux), but other methods may be possible. Please do not abuse the API endpoint by sending too many requests in a short amount of time. You will probably get blocked by the server! 
