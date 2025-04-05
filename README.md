# ray_serve_fastapi_tutorial
A bunch of tutorials on Using and Serving [Guardrails-AI](https://www.guardrailsai.com/)


## How to Run
- Install Docker from [here](https://docs.docker.com/get-docker/)
- Run below script
    ```bash
    #!/bin/bash
    git clone https://github.com/abhishek9sharma/ray_serve_fastapi_tutorial.git
    cd  ray_serve_fastapi_tutorial
    make up_with_build 
    ```
- Using Jupyter Notebook
    - Browse the url http://localhost:8888/lab
    - Follow the instructions in the notebooks. They are self contained. 
    -  You need to set up some environment variables. The steps are mentioned below. 
        - The default setting of the tutorials is to use [OpenAI](https://openai.com/) services which requires an API key. To get the key, you need to sign up for an account on the [OpenAI website](https://openai.com/product). Once you have your API key, you can set it in your environment variables wherever mentioned in the notebooks.


- Using RAY and RAY Serve CLI

    Below comamnds should be run frome the cloned folder i.e. __ray_serve_fastapi_tutorial__

    - Change Directory to workspace ( if not using docker)
        -  ``` cd ray_serve_tutorial/workspace/ ```
    
    -  Install Environment
        
        ```
        chmod +x src/install_env.sh
        bash src/install_env.sh
        ```

    -  Activate the environment

        ```
        chmod +x src/install_env.sh
        bash src/install_env.sh
        ```


    -  Spin Up Ray Cluster
        
        - ``` ray start --head --dashboard-host 0.0.0.0  ```
        - Ray cluster should be visible at [http://localhost:8265/](http://localhost:8000/docs)

    -  Serving App
    
        - Serve Ray App From Code
            - run ```serve start --http-host 0.0.0.0 ```
            - run ``` serve run src.ray_fastapi:rayappadvanced --non-blocking ```
            - The app should be visible at [http://localhost:8000/docs](http://localhost:8000/docs)
        

        - Serve Ray App From Config file
            - ``` serve   shutdown``` You may have to run it from a different terminal
            -  ``` serve build src.ray_fastapi:rayappadvanced -o serve_config_app.yaml  ```
            - In the serve_config_app.yaml change port to 8001 in http_options
            -  ``` serve deploy serve_config_app.yaml  ```
            - The app should be visible at [http://localhost:8000/docs](http://localhost:8000/docs)
        


## References

- [https://docs.litellm.ai/](https://docs.litellm.ai/)
