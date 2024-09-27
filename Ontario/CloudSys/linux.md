# Linux Domain Questions

##### Question 1
Your EC2 Instance is running out of disk space. What actions will you take to mitigate that issue? 


##### Answer:
- EC2 Disk space means we are speaking of EBS volume
- We will first check if its a root volume or other volume: 
    - /root - OS
    - /application - for our application

- If its root volume then i will first check logs and clear some space if not the instance might shut down also
- If its application volume, then I will use EBS feature to take snapshot and increase disk space for the EC2 instance


##### Question 2
What is bastion host or gateway server? What role do they play?

##### Answer:
Bastion Server: 
A bastion server is used to manage access to an internal or private network - sometimes called gateway server or jumpbox or jump server

Private server or under VPC
Security, monitor incoming and outgoing traffic 

(1) -> (2) Bastion host -> (3) EC2 machine, if access

Benefit of bastion host: cut of external access, tear down bastion host


##### Question 3
Multiple EC2 instance in ASG is getting terminated and this is causing downtime on the application. EC2 Pricing and quota looks good

How would you start debugging this?

##### Answer:
EC2 -> Terminated
-> unhealthy 

Factor of unhealthy:
disk space being full
high cpu utilization (100%)
no memory left

Command: 
Solution
1. 
top -> cpu
process -> cpu utilization (application )

(dev) - (threading)

2. 
EBS -> 100% -> OS

/var/log   /tmp/etc

3. free memory left
free -mt
- swap memory left if its 0, then there is a problem using utilization of EC2 instance
- debug application 

ASG -> EC2 -> application -> Unhealthy 

checks ASG -> terminate 

Debug the application and debug the ec2 instance 

Answer: 
- Based on the information provided, I feel that ASG or AWS itself not having any particular issues, the termination of EC2 instance can be that the actual ec2 instance pushed towards becoming unhealthy. This happens for multiple reason

- High cpu utilization (application usage)
- Disk space
- No free swap memory that might be left

Solution: 
- log onto one of machine, see the highest utilization, reach out to developer
- increase the volume to free up the space
- look into different type of ec2 instance, suggest memory intensive ec2 instance, as part of the ASG



##### Question 4
Create a linux script that will push certain logs to S3 automatically. Explain only high level design which is enough. Share what all steps you would do to achieve this above script

Bonus: Also, the script should run in particular time

##### Answer:
High Level design
white board design

[]          <S3 bucket>
linux -> 

IAM role or access keys (for verification of access)

bash script 

* $ -> kernel
* /var/log/application_01/--
* aws cli command 
* AWS S3 cp <origin>(s3 bucket location)

Bonus:
linux cron job: 

Begin with iam role or access key, by default linux would not have access to s3 bucket
- once validated, she bang
- aws cli command
- copy files to the s3 bucket to the location specefied 

- I would use chron job


##### Question 5
Why logging is important? What is centralized logging and what tools helps to achieve centrallised logging? 

##### Answer:
Recording of application -> logs -> json or txt

Why is logging important? 
- Hard to debug/fix
[Ec2 instance] -> application (web api)

Logging  (/var/log/app.log)

lost EC2 instance 

[OOOOOOO - ec2 instances are here]

when application is deployed in a scalable manner, even log are created in a scalable manner. Introduce centralize logging 
- AWS -> S3 
        -> Cloud Watch
        -> Elastic search
        -> Splunk
        -> Data dog

Logging is important to track the behaviour of aapplication, scalable manner,
to get complete picture in terms of infor, debug warning, setup centralized logging
S3, cloudwatch, elastic search, splunk or datadoge (centralize logging, will have one place, faster and easier in production )


