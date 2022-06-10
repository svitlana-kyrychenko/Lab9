# Lab9
Running Spark

Put file with dataset in folder data

Order of running 

> run-cluster.sh
> 
> docker run --rm -it --network spark-network --name spark-submit -v "path":/opt/app bitnami/spark:3 /bin/bash
> 
> cd /opt/app
> 
> spark-submit --master local[*] --deploy-mode client main.py

Creating an installation

![image](https://user-images.githubusercontent.com/102665740/173160884-15a68429-b629-4cd2-97da-947e7e901667.png)

Result of running

![image](https://user-images.githubusercontent.com/102665740/173162785-b6dc4f32-40eb-4286-8eee-edbeb118f483.png)

To shutdown docker-compose

> shutdown-cluster.sh
