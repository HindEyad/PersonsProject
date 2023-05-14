# PersonsProject
 
Run and Test container through YAML file
This documentation offers a brief explanation on running and testing a Docker container using YAML file. By using a YAML file to define the Docker container's configuration and settings, you can easily spin up and manage Docker containers with different configurations.
This documentation will guide you through the process of creating a YAML file for a Docker container, running the container, and testing it. 
•	Creating YAML File:
Create a file “docker-compose.yml” that contains 3 main tags: (version, services, and networks)

1.	Version: according to preference of settings (in my case version 3.7)

2.	Services: contains an internal tag for each image (in my case frontend and backend).
Each image has the following dependencies:
 build: builds the image in its given path.
restart: auto restart if any crash occurs, this tag helps in efficiency of code.
ports: has the port of each image (in my case backend: 5000, frontend: 4000).
networks: contains name of network that will be run through it.
depends on backend: extra tag in frontend image which ensures that backend runs first.
3.	Networks: Contains tag name that contains tag driver. Name is the network name that files will run through, and driver is the driver type (in my case bridge)

•	Running the Docker Container on YAML File:
 In my case, I made the YAML file build my images itself if they are not already built
Write “Docker -compose up –build“ in the terminal
•	Testing the Container:
Write “Localhost:4000” in the search bar of any browser to view the GUI of my software

Public link of repository in docker hub:
 https://hub.docker.com/r/hindeyad/persons_project/tags
 backend: docker pull hindeyad/persons_project:backimage
 frontend: docker pull hindeyad/persons_project:frontimage
