TASK : To build a random generator API and add a rate limiting service on top of it


To approach the problem, I have used a Django web framework to manage the users as well as design the frontend of the API.

The random generator (API A) was designed using the FastAPI framework and integrated into the Django Web framework


The two applications were run on different lcoalhost servers where the Django API would call results from API A and display it on the interface

![Django API is run on the http://localhost:7000](pic/1.png)

Django API is run on the http://localhost:7000 

To run django server on localhost: 
go to task folder using 

```
cd task/
python3 manage.py runserver 7000
```

![FastAPI is run on the http://localhost:8000](pic/2.png)

FastAPI is run on the http://localhost:8000

To run fastapi server 
```
uvicorn main:app --reload
```

![](pic/3.png)

![](pic/4.png)


The above signup and login page was made on the Django API using the default django libraries aka Authentication and Signup forms.


![](pic/5.png)


The random number is called from the fastapi interface onto the django webpage.


![](pic/6.png)
After refreshing the page (GET Request) 5 times, the rate limiting functionality of the Django interface and returns a "403 Forbidden" error message. This functionality happens whenever a user tries to access a random number more than 5 times, and locks the user out for a minute before it resets.  

![](pic/7.png)
The above picture shows the fastapi interface getting call requests from our django interface to call the random number onto the webpage


![Django API is run on the http://localhost:7000](pic/8.png)

As above, when accessing the /docs of the fastapi interface, we can try out the random function and execute it to receive and random number.






