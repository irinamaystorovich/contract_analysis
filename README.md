


#Contract Analysis solution

#allows to extract entities, dates, action items from the document

#uses Docker, Flask, OCR

-------------------------------------------------------------------------------------------
# Docker Test

Note: 1) Docker container built successfully, 2) Docker container ran successfully, 3) could not figure out correct porting (will probably need help with this part). 

## Running the app on Docker:


### 1. Install Docker and Run Docker Desktop. [https://docs.docker.com/get-docker/] 


### 2. Build Docker Container. 

   * Download the directory and files.
   * Navigate to the correct directory using CLI (should contain **dockerfile** within).
   * Enter `docker build -f Dockerfile -t contract_app .`

   * (Error: "In the default daemon configuration on Windows, the docker client must be run with elevated privileges to connect." refer to [https://stackoverflow.com/questions/40459280/docker-cannot-start-on-windows])
   
   
### 3. Run Docker Container.

   * `docker run -p 5000:5000 contract_app`
   
   
### 4. Access the app through the link.

----------------------------------------------------------

# Flask
 
# change pdf file path 
1. Run app.py
2. Press link 
