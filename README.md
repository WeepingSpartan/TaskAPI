TASK : To build a random generator API and add a rate limiting service on top of it


To approach the problem, I have used a Django web framework to manage the users as well as design the frontend of the API.

The random generator (API A) was designed using the FastAPI framework and integrated into the Django Web framework


The two applications were run on different lcoalhost servers where the Django API would call results from API A and display it on the interface

![Django API is run on the http://localhost:7000](pic/1.png)




