# EKS Cluster Architechture
- This architetcure provides a comprehensive overview of our AWS EKS (Elastic Kubernetes Service) cluster architecture, focusing on different resources that are strategically placed within specific node groups. By leveraging the robust features of AWS EKS, this architecture ensures optimal management, scalability, and resilience of application. The architecture  will detail the various Kubernetes objects employed and  their configurations.
  
- The architecture was designed by [Draw.io](https://app.diagrams.net/) .

- The architecture is composed of 3 layers : AWS layer , Kubernestes Physical layer and Kubernestes logical layer.

## AWS Layer
- The AWS layer of our architecture provides the foundational infrastructure that supports our Kubernetes cluster on AWS EKS (Elastic Kubernetes Service). This layer is crucial as it provides the compute resources, storage, and networking capabilities required to run our applications efficiently. Below is a detailed description of the AWS layer configuration, focusing on node groups and storage.

 **1-Generate SSH Key Pair**:
