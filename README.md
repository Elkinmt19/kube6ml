# **Kubernetes Deploy Machine learning (kube6ml)**

```python 
class KubernetesDeployMachineLearning(Kubeflow):
    def __init__(self):
        self.name = 'kube6ml'
        self.projects = [
            "k8s": [
                "k8s-getting-started"
            ]
        ]
    def __str__(self):
        return self.name

if __name__ == '__main__':
    project = KubernetesDeployMachineLearning()
```
