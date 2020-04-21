# ECS781P_190617866
MiniProject
Following objectives are met through the prototype of this web app development
The project will have the form of an application, developed in Python and Flask. 
The mini project will work on the following aspects of Cloud applications: 
•	REST-based service interface. 
•	Interaction with external REST services. 
•	Use of on an external Cloud database for persisting information. 
•	Support for cloud scalability, deployment in a container environment. 
The data file is obtained in JSON and converted to CSV. CSV File is being loaded in Cassandra database to store the data.
Python Flask is used to fetch the data as per the requirements of the user.
The requirements.txt will give details about required software.
Docker file will give details about directory. Cassandra driver is used to communicate with application to fulfil the REST requirements.

GET, PUT, POST, DELETE and UPDATE services are used for this prototype. 
GET   Fetch details of world universities
POST  Allow user to add the university records
PUT Confirms the update
DELETE - Delete the record which are redundant

Applications :
Python 2.7
Flask 1.1
SQL Alchemy (Local database)
Jupyter Notebook
Cassandra (Local and AWS instance)

Important installations:
•	sudo apt−get update
•	sudo apt install docker.io
•	sudo apt install python3pip
•	pip3 install Flask
•	sudo snap install microk8s -classic
•	sudo docker pull cassandra:latest
•	sudo docker run --name cassandra-test -p 9042:9042 -d cassandra:latest
•	wget -O “ source.csv”.csv  “ location ”
•	sudo docker cp source.csv cassandra-test:/home/source.csv
•	sudo docker exec -it cassandra-test cqlsh
