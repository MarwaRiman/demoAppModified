#Dockerfile , Image , container 
#Dockerfile is a blueprint for building images
#Image is a template for running containers
#Container is the actual running process where we have our package project 

FROM python:3.6 
#this pulls the python docker image from the docker hub that has python installed 
#add main.py file to the container and the destination is . (in our current directory)
ADD main.py . 
RUN pip install requests beautifulsoup4 
#for bigger projects where we have the requirements in txt file we install those requirements 

#specify below the entry command (where we want to start our application)
CMD [ "python", "./main.py" ]
# it runs python command in our container terminal 


