### Setup

==Cybera==

1. `Client_VM` 

   ```bash
   # Setup
   sudo apt update
   sudo apt -y install python-pip
   pip install requests
   # Starter Kit
   wget https://raw.githubusercontent.com/hamzehkhazaei/ECE422-Proj2-StartKit/master/http_client.py
   ```

2.  `Swarm` VM's

   ```bash
   # All VM's
   sudo apt update
   sudo apt -y install docker.io
   
   # Swarm Manager Only
   wget https://raw.githubusercontent.com/hamzawey/ECE422-Proj2-StartKit/master/docker-compose.yml
   ```

### Running

1. `Swarm Manager`

   ```bash
   sudo docker swarm init
   ## Use Output for Workers, if necessary
   sudo docker stack deploy --compose-file docker-compose.yml app_name
   ```

2. `Swarm workers`

   ```bash
    sudo docker swarm join \
     	--token xxxxxxxxxxxxxxxxxx \
       swarm_manager_ip:2377
   ```

3. `Client_VM`

   ```bash
   python3.5 http_client.py SWARM_MANAGER_IP 1 1
   ```

### Starter Kit Files

`Figures`: 

- Just Images. Probably dont need

`docker-images`

​	`Dockerfile`

- Don't know how Docker files work but looks simple enough

​	`myapp.py`

- just counts the number of times the server has been visited
- has a number that makes the computation randomly difficult (i.e  take arbirtrary amounts of compute resources)

​	`requirements.txt`

- just says `flask` and `redis`

`docker-compose.yml`

- dont know how docker works

`http_client.py`

- ==argv==[ `swarm_master_ip`, `no_users`, `think_time`]
- Multithreaded server that makes requests every `think_time`
- creates `no_users` number of threads to make requests.

### To Do

- Automate setting up the servers. I don't want to open a 3 terminals and run all these commands everytime
- Dont have room for 2 medium 1 small VM. 
- Only need to autoscale the web microserve bottleneck (I think thats the `http_client` -==MAKE SURE!==)
- How to measure response times?
- Do we need to spawn more clusters? I don't think we can get more compute resources

### ToDo

- [ ] Script to scale up
- [ ] read response times
- [ ] Visualize different things

### Scaling

`$ docker service scale app_name_web=5`

**How many replicas can we make))**

- Bash script, timing response using curl
- python curl to get responsone time
- run docker to get workdload
- application size

# Demo

https://eclass.srv.ualberta.ca/pluginfile.php/7017526/mod_resource/content/1/Demo%20Marking%20Guide.pdf

https://eclass.srv.ualberta.ca/pluginfile.php/7017525/mod_resource/content/1/Project%20Description.pdf

- [ ] Show Swarm cluster and deployed app micro service.

- [ ] Bell shaped workload

  - [ ] Auto-scale disabled
    - response times varies with workload

  - [ ] Autoscale enabled
    - respone time should stay within acceptable range despite workload
    - Show app size changes with workload (show number of containers) for each microservice

- [ ] Visualization

  - [ ] Workload Plot

    - Poll redis

  - [ ] Response time plot
  
    ​	- using curl
  
  - [ ] Application size plot
  
    ​	- Maybe using sock?

# Design Artifacts

- [ ] A high-level architectural view of your application in which auto-scalability features have been shown. 
- [ ] A state diagram that shows the state, events, and actions in the auto-scaler. 
- [ ] The pseudocode of the auto-scaling algorithm along with reasons behind the parameter settings in the algorithm; important parameters may include lower and higher thresholds, the length of the monitoring interval, scaling policies, etc.

# Report

- [ ] Title and Author name (this is required for your report) 
- [ ] Abstract 
- [ ] Introduction 
- [ ] Technologies, methodologies, tools etc. that you used for accomplishing the project and the reason you chose them.
- [ ] Design artifacts with explanation (i.e., whatever you have in your Design folder) 
- [ ] Deployment instructions and user guides 
- [ ] Other related information 
- [ ] Conclusion 
- [ ] Reference

# Submission ==April 18?==

- [x] Add alirezagoli to GitHub project
- [ ] Source Code 
- [ ] Design Artifaces
- [ ] Final Report
- [ ] Book Demo



# Docker Notes

File Sturecture

```bash
.
├── docker-compose.yml
├── docker-images
│  └── web-app
│     ├── Dockerfile
│     ├── myapp.py
│     └── requirements.txt
├── figures
│  ├── app.png
│  ├── sg.png
│  └── vis.png
├── http_client.py
├── ProjectNotes.md
└── README.md
```

`docker-compose.yml`

- Use a `Dockerfile` to dfine the app environment
- define the services in `docker-compose.yml`

==How to Scale Apps with Swarm==: https://docs.docker.com/get-started/swarm-deploy/

### Docs

[Offical](https://docs.docker.com/engine/swarm/)

==Swarm==

- multiple docker hosts in swarm mode. 

==Task==

- A running container being managed by the swarm (not a standalone)

==Node==

- A docker engine within the swarm. Can be a manager or a worker.
- Workers receive an execute tasks from managers
- Manager can also act as workers.

==Service==

- Specifies which container image to use and what commands to run on it.
- Definition of tasks to execute on nodes

**Tutorial**

### Docker commands

`docker swarm join-token worker`: Generates Docker Token for swarms





- How to SSH In

1. Make sure TunnelBlick is running: [link](https://wiki.cybera.ca/display/RAC/Rapid+Access+Cloud+Virtual+Private+Network)

2. SSH by `ssh -i /path/to/ece422.pem ubuntu@<ip address>`

   ​	Ip address is here <img src="/Users/jordanlos/Library/Application Support/typora-user-images/image-20210417022455202.png" alt="image-20210417022455202" style="zoom:25%;" />

   

