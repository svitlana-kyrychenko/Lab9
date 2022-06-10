# Lab9
Running Spark

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

result of running

![image](https://user-images.githubusercontent.com/102665740/173160943-f7f57635-0e37-43c5-8c00-f2ab1c4b13e3.png)
