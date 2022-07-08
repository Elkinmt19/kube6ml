# **Kubernetes Deploy Machine learning (kube6ml)**

```python 
class KubernetesDeployMachineLearning(Kubeflow):
    def __init__(self):
        self.name = 'kube6ml'
        self.projects = [
            "k8s": [
                "k8s-getting-started",
                "k8s-flask-nginx"
            ]
        ]
    def __str__(self):
        return self.name

if __name__ == '__main__':
    project = KubernetesDeployMachineLearning()
```

## Getting Started
In order to be able to use the different project that this repo has, first it is important to setup an appropriated environment. The main purpose of this project is to develop and implement ML pipelines using `Kubernetes`, because of this it is important to setup a Kubernetes cluster to work.

There are different ways to setup a Kubernetes cluster locally in a computer or laptop, here there are some guides to perform this installation:

- [Kubernetes on Windows](./windows_setup.md)
