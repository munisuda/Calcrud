## Project goal - 
To automate the creation of events in needed users calendars, with a simple script using python, FastAPI and google calendar API for free.

## Prerequisites - 
Little to no knowledge in 
 - Python
 - FastAPI
- basics about endpoints 

## Environment Variables In .env.sample

- "calID" to be recieved from your own personal calendar which is used to create events

- "scopes" signifies what level of data would you want to access from the clients calendar (default SCOPE==https://www.googleapis.com/auth/calendar  unless needed otherwise)

- "timezone" is pretty self explanatory, use "Asia/Kolkata" for IST.