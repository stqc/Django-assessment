# Task Management API Django Assessment

## Breif Overview

- Users can register with username and password (no email added)
- Users can login with username and password on the ``/api/token/`` route and get ``access_token `` and ``referesh_token`` (For the scope of this test the JWT is sent in the header)
- Users can create their tasks, and update them
- A user can only see their own task and update their own tasks
- A user can view their completed and incompleted tasks seprately using the `` is_completed `` example: ``/api/tasks/is_completed=true``
- Swagger documentation can be accessed at the ``/api/swagger/`` route

## Set up instructions

- Clone the repository 
- run `` pip install -r requirements.txt ``
- db is included in the repository for convenience but if you wish to reset the db or update schema please use 
    - `` python3 manage.py makemigrations ``
    - `` python3 manage.py migrate ``
- Finally to run the server `` python3 manage.py runserver ``


DB can also be viewed in the admin panel using the following user details ``/admin/``
  
  ``username: prateek``
  ``password: root``

another test user with some tasks include 
 `` username: user-1 ``
 `` password: test ``

 NOTE: JWT token expiry settings have not been changed and assumes default values (5 minutes for access_token and 1 day for refresh_token)

