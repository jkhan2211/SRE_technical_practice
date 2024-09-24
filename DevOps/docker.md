# Docker Domain Questions

##### Question 1
How to check logs from my docker container and how to filter only last 200 lines from container log?

##### Answer:
Docker command will help us here:

Docker command:

```
docker container log <container_name>
```

```
docker container log webapp
```

Filtering logs from my docker container command:

```
docker container log -tail 200 <container_name>
docker container log --tail 200 <container_name>
```
* Important: the command i have used in the past is the docker container log container_name command to investigate, you can filter out the last 200,100 line including the tail 200 argument, to filter out the last 200 lines



##### Question 2
What will happen to container logs, if you re-start container, will it be lost or not? 

##### Answer:
Because container are stateless, you will lose log if the container is deleted, if we have a use case to presist log, we should use external log storage layer.

But, if container are stopped, and started or restarted than we won't lose any logs, they would be in, (docker container log) we may not see the old logs, if the application restart, we may see new files, but the older files will also exist, in an older timestamp memory

```
/var/logs/app.log
```

##### Question 3
You encounter a docker image with size 2.7 gb. Will this be a cause of concern? if yes how to tackle this? 

##### Answer:
- Bigger docker image would result in a longer build time (2.7 gb)
- Docker image download error or API rate limit issue
- Application will also become bulkier

Solution:
- Smaller Image Base(Alpine Image)
- Multi-Stage Builds feature when building docker image
- Remove package binaries after installing and dont install package that isnt required 

Another solution: to lock package with version



##### Question 4
What is the difference between docker image vs docker layers? 
##### Answer:
- Each layer is an image itself
- They have auto-generated ids during image build time or container time
- Each layer stores the changes compared to the image based on 
- An image can consist of a single layer(that's often the case when the squash command was used)

```
FROM rails:onbuild
ENV RAILS_ENV dev
ENTRYPOINT ["bundle", "exec", "logica"]
```

##### Question 5
Explain CMD and ENTRYPOINT in docker, are these same or different? 

##### Answer:

Only CMD
```
FROM ubuntu:latest
CMD["echo","This is CMD"]
```

Only ENTRYPOINT
```
FROM ubuntu:latest
ENTRYPOINT["echo","This is ENTRYPOINT"]
```

ENTRYPOINT and CMD
```
FROM ubuntu:latest
ENTRYPOINT["echo"]
CMD["This is entrypoint]
```

- Both run during docker runtime 
- Either one of them are suggested for best practice 
- Using both of them in the same dockerfile is also possible


##### Question 6
Given 2 different docker file below. Which one do you think will have lesser size when built?
```
#syntax=docker/dockerfile:1
FROM node:12-alpine
RUN apk add --no-cache python2 g++ make
WORKDIR /appCOPY ..RUN yarn install--
productionCMD ["node","src/index.js"]
```
------------------------------------------------------------------
```
#syntax=docker/dockerfile:1
FROM node
RUN apk add --no-cache python2 g++ make
WORKDIR /appCOPY ..RUN yarn install--
productionCMD ["node","src/index.js"]
```

##### Answer:
Image 1 has lesser size, light weight images or OS(packages that is required for function of application)


