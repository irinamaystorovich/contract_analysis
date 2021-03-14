# Docker Test

Note: 1) Docker container built successfully, 2) Docker container ran successfully, 3) could not figure out correct porting (will probably need help with this part). 



## Running the app on Docker:


### 1. Install Docker and Run Docker Desktop. [https://docs.docker.com/get-docker/] 


### 2. Build Docker Container. 

   * Download the directory and files.
   * Navigate to the correct directory using CLI (should contain **dockerfile** within).
   * Enter `docker build -f Dockerfile -t contract_app .`
   
   
### 3. Run Docker Container.

   * `docker run -p 5000:5000 contract_app`
   
   
### 4. Access the app through the link.
