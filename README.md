# ray_serve_fastapi_tutorial
A simple tutorial on deploying fastapi apps using ray_serve


## How to Run

### Setting Up
- Install Docker from [here](https://docs.docker.com/get-docker/)

    * Note: If you do not want to use Docker you can run the notebook/scripts directly on your machine also using [jupyter lab](https://jupyter.org/install)

- Run below script
    ```bash
    #!/bin/bash
    git clone https://github.com/abhishek9sharma/ray_serve_fastapi_tutorial.git
    cd  ray_serve_fastapi_tutorial
    make up_with_build 
    ```


### Running the Jupyter Notebook 
This notebook demonstrates how to deploy a _Hello World_ FastAPI app Using _Ray Serves Python API_
    
- If you have installed Docker, provided you have run the command ```make up_with_build ``` mentioned before, you can browsethe below link
    - http://localhost:8888/lab/tree/workspace/notebooks/serving_fastapi_ray.ipynb

- If you are using [jupyter lab](https://jupyter.org/install) 
    - run the command```jupyter lab ``` 
    - browse the url http://localhost:8888/lab or http://localhost:8889/lab
- Follow the instructions in the notebook [serving_fastapi_ray.ipynb](/workspace/notebooks/serving_fastapi_ray.ipynb). It is self contained. 


### Ray CLI
Below steps demonstrate how to deploy a _Hello World_ FastAPI app Using _Ray Serves CLI_

- Below comamnds should be run frome the cloned folder i.e. __ray_serve_fastapi_tutorial__

- Change Directory to workspace ( if not using docker)
    -  ``` cd ray_serve_tutorial/workspace/ ```

-  Install Environment
    
    ```
    chmod +x src/install_env.sh
    bash src/install_env.sh
    ```

-  Activate the environment

    ```
    source ray_env/bin/activate
    ```

-  **Spin Up Ray Cluster**
    
    - ``` ray start --head --dashboard-host 0.0.0.0  ```
    - Ray cluster should be visible at [http://localhost:8265/](http://localhost:8265)
    - Status can also be verified using ``` ray status  ```

-  **Serving App**

    - __Serve Ray App From CodeLocation__
        - Run below commands
            -  ```serve start --http-host 0.0.0.0 --http-port 8001 ```
            - ``` serve run src.ray_fastapi:rayappadvanced --non-blocking ```
        - The app should be visible at [http://localhost:8001/docs](http://localhost:8001/docs) and serve at [http://localhost:8001/hello](http://localhost:8001/hello)
    

    - __Serve Ray App From Config file__
        - Run below commands
            - ```serve   shutdown -y``` 
            -  ```serve build src.ray_fastapi:rayappadvanced -o serve_config_app.yaml  ```
            - ```serve start --http-host 0.0.0.0 --http-port 8001 ```
            -  ```serve deploy serve_config_app.yaml  ```
        - The app should be visible at [http://localhost:8001/docs](http://localhost:8001/docs) and serve at [http://localhost:8001/hello](http://localhost:8001/hello)
    
    
    - __Serve Replica Autoscaling__
        - Run app with autoscalilng config
            - Run command ```serve shutdown -y ```
            - Remove the __num_replicas__ in __serve_config_app.yaml__
            - Add below config (You can refer [serve_config_app_autoscale.yaml](/workspace/notebooks/serve_config_app_autoscale.yaml))
                        
                        max_ongoing_requests: 5
                        autoscaling_config:
                            target_ongoing_requests: 2
                            min_replicas: 2
                            max_replicas: 5

            - Redeploy app using below commands 
               - ```serve start --http-host 0.0.0.0 --http-port 8001 ```
               -  ```serve deploy serve_config_app.yaml  ```
        - Simulate AutoScaling 
            - Start ```locust -f src/locust_test.py --web-port 8004```. 
            - It should be visible at [http://localhost:8004/](http://localhost:8004/)
            - Load test  [http://localhost:8001](http://localhost:8001/) with requests using locust. You can use below settings
                - Number of Users 100
                - Ramp Up 10
                - Host http://localhost:8001/
            - You can see auto_scaling of replicas increasing at [http://localhost:8265/#/serve/applications/app1/RayAppAdvanced](http://localhost:8265/#/serve/applications/app1/RayAppAdvanced) after some time




## References

- https://docs.ray.io/en/latest/index.html
- https://maxpumperla.com/learning_ray
