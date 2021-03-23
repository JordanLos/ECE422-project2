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

  - [ ] Response time plot

  - [ ] Application size plot

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

- [ ] Add alirezagoli to GitHub project
- [ ] Source Code 
- [ ] Design Artifaces
- [ ] Final Report
- [ ] Book Demo