# ray_serve_fastapi_tutorial
A simple tutorial on deploying fastapi apps using ray_serve


## How to Run
- Install Docker from [here](https://docs.docker.com/get-docker/)
- Run below script
    ```bash
    #!/bin/bash
    git clone https://github.com/abhishek9sharma/ray_serve_fastapi_tutorial.git
    cd  ray_serve_fastapi_tutorial
    make up_with_build 
    ```
-  You may need to set up some environment variables. The steps are mentioned below. 
    - The default setting of the tutorials is to use [OpenAI](https://openai.com/) services which requires an API key. To get the key, you need to sign up for an account on the [OpenAI website](https://openai.com/product). Once you have your API key, you can set it in your environment variables wherever mentioned in the notebooks.

### Jupyter Notebook demonstrating how to deploy a _Hello World_ FastAPI app Using _Rays' Python API_
    
- Browse the url http://localhost:8888/lab
- Follow the instructions in the notebook. It is self contained. 


### Steps to deploying a FastAPI app Using Ray CLI

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
        - run ```serve start --http-host 0.0.0.0 ```
        - run ``` serve run src.ray_fastapi:rayappadvanced --non-blocking ```
        - The app should be visible at [http://localhost:8001/docs](http://localhost:8001/docs)
    

    - __Serve Ray App From Config file__
        - ```serve   shutdown``` 
        -  ```serve build src.ray_fastapi:rayappadvanced -o serve_config_app.yaml  ```
        -  ```serve deploy serve_config_app.yaml  ```
        - The app should be visible at [http://localhost:8001/docs](http://localhost:8001/docs)
    
    - __Serve Replica Autoscaling__
        - Start ```locust -f workspace/src/locust_test.py --web-port 8004```
        - Shutdown serve  ```serve shutdown ```
        - Remove the __num_replicas__ in __serve_config_app.yaml__
        - Add below config 
                
                    max_ongoing_requests: 5
                    autoscaling_config:
                        target_ongoing_requests: 2
                        min_replicas: 2
                        max_replicas: 5

        - Redeploy app using ```serve deploy serve_config_app.yaml  ```
        - You can see auto_scaling of replica when u bombard the endpoint [http://localhost:8001](http://localhost:8001/) with requests
    



## References

- https://docs.ray.io/en/latest/index.html
- https://maxpumperla.com/learning_ray
