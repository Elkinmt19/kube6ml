# **Kubectl commands**

Some useful `kubectl` commands are the followings:

```bash
kubectl cluster-info 
```
To get the information related to the cluster, this command shows us the nodes running in our cluster and also shows us their IP addresses.

```bash
kubectl get <kubernetes-object> 
```
This command gives us information about specific objects of our kubernetes cluster, this objects can be nodes, deployments, namespaces, services and so more.

```bash
kubectl run <pod_name> --image=<container_image>
```
This command allows us to create a single pod using a specific container image.

```bash
kubectl describe <kubernetes-object> <object-name> 
```
This command gives descriptive information about a specific kubernetes object.

```bash
kubectl delete <kubernetes-object> <object-name> 
```
This command deletes a specific kubernetes object or resource. This command can also be used with the `--all` flag in order to delete all the existing resources at once, typing (`kubectl delete all --all`).

```bash
kubectl create deployment <deployment-name> --image=<container_image>
```
This command allows us to create a deployment using a specific container image.

```bash
kubectl scale deployment <deployment-name> --replicas=<number-of-replicas>
```
This command allows us to scale in or out a specific deployment.

```bash
kubectl expose deployment <deployment-name> --type=<service-type> --port=<external-port> --target-port=<internal-port>
```
This command allows us to create kubernetes services, this services can be:
- CluterIP
- NodePort
- LoadBalancer

```bash
kubectl set image deployment <deployment-name> <deployment-name>=<new-container-image>
```
This command allows us to make a new release or rollout deployment setting a new container image into a specific kubernetes deployment.

```bash
kubectl rollout status deploy <deployment-name>
```
This command allows us to see the status of a rollout deployment.

```bash
kubectl apply -f <yaml-config-file>
```
This command allows us to create resources in our kubernetes cluster from yaml configuration files.

```bash
kubectl -n <namespace-name> port-forward --address 0.0.0.0 service/<service-name> <local-port>:<target-port>
```
This command allows us map the port of the WSL 2 VM to the port of our local machine.