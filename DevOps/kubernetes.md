# Kubernetes Domain Questions

##### Question 1
What is Kubernetes kOPS?

##### Answer:
kOPS is automation tool used to setup a kubernetes cluster instead of kubeadmin to do it

kOPS is not something that will help you setup managed kubernetes cluster(EKS) or something but if you intended to to spin up a test cluster, or a small dev cluster then kOps can quickly do this 

kops will not only help you create, destroy, upgrade and maintain production-grade, highly available, Kubernetes cluster, but it will also provision the necessary cloud infrastructure 

It support AWS, DigitalOcean, GCE and OpenStack is Beta, Azure and AliCloud is in alpha


(kOps) -> [k8] -> {EBS, EC2, ASG, Route53}

##### Question 2
Explain replication controller in kubernetes? 

##### Answer:
A replication controller is responsible for running the specefied number of pods copies(replicas)- across the cluster

```
apiVersion: v1
kind: ReplicationController
metadata:
    name: nginx
spec:
    replicas: 3
    selector:
        app: nginx
    template: 
        metadata:
            name: nginx
            labels:
                app: nginx
            spec:
                containers: 
                - name: nginx
                  image: nginx
                  ports:
                  - containerPort: 80
```


[Rc.yaml] --------------- pod1  -> Node 1
[(3 replicas)]  -------------- pod2 -> Node 1
[            ]  -------------- pod3 -> Node 2

Replication controller does not scale horizontal. No auto-scale 

##### Question 3
What is pv and pvc in kubernetes ? What role do they play ?

##### Answer:
PV -> PresistentVolume
PVC -> PresistentVolumeClaim

{POD} -> [PVC] -> [pv] ---> (Volume(NFS,EBS, etc))

To get PV, we need to use the PVC in our deployment section(.yaml) request PVC to find that is required for PV for us, if its provisioned it will allot to that point. Just having one, will not work by default. PV and PVC work both hand in hand. PV can exist independent. 

##### Question 4
A pod is trying to access a volume but it gives error. We would like this pod to have access to this volume, What can we do to achieve the same? 

##### Answer:
Volume are provisioned as part of our kubernetes as part of our PVs 

pod gets attach to PVs via PVC

- The issue could appear with AccessMode of Volume
- Not all PV allow multiple pod access
- In K8s:
    - ReadWriteOnce
    - ReadOnlyMany
    - ReadWriteMany
    - ReadWriteOncePod
    - Example: NFS allow ReadWriteMany
    - EBS allow only ReadWriteOnce


    The error could be occuring because we are trying to attach a volume allow ReadWriteOnce, therefore causing issue, to fix this, make changes in PV and PVC, to make sure seperate volume is created. We make sure the volume we are trying to attach, has ReadWriteMany


##### Question 5
What is a side car container?

##### Answer:
logging -> application 
They are container that helps the application running in the pod, perform some common task, like logging, side car container, to app container to centralized application. 

This ensure, a common use cases, can be seperated and side car container that our deployment goes smooth, it will also remove complexity, smooth deploy, scale and manage the application. 

##### Question 6
We want to launch certain pod only specific node. These nodes should explicitly used only for this pod. Is it possible to control the deployment of pod such as given scenarios?

##### Answer:
- Yes this can be achieved as Taint in K8's
- We can add taint, to a node:
```
kubectl taint nodes nodex key=value:Effect
```
- Taints are a property of nodes that push pods away if they don't tolerate this taint
- Like labels, one or more Taints can be applied to a node
- This means that the node must not accept any pod that does not tolerate all of these taints 

##### Question 6
How does the K8's scheduler quickly assign worker nodes for the pods? Explain the internal working of K8's scheduler 

##### Answer:
Scheduler provision pod on different worker nodes. What sheduler has is information, metadata about worker node health, this info is filtered, when pod comes for scheduling during cycle, co-releate the data. It is very easy and faster to provision pod in kubernetes 

##### Question 6
You have 10 nodes with 500GB of disk attached to each node. Let us say node disk should reach 85% usage; then pod we have deployed should get evicted and re-deployed on a node with better disk health. Explain if this can be done? 

##### Answer:
I am assuming, saving a paticular node, when reaches utilization, use kubelet this is a node level config we have to do. 
Eviction hard and eviction soft
Here we can config eviction threshold, memory available, Inode available
Node has high utilization, qas methoda, paticular pod, once it decide which pod, termination will send this pod to shut down gracefully, if not force. Set up alerts for further debug

















