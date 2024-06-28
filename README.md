# EKS Cluster Architechture
- This architetcure provides a comprehensive overview of our AWS EKS (Elastic Kubernetes Service) cluster architecture, focusing on different resources that are strategically placed within specific node groups. By leveraging the robust features of AWS EKS, this architecture ensures optimal management, scalability, and resilience of application. The architecture  will detail the various Kubernetes objects employed and  their configurations.
  
- The architecture was designed by [Draw.io](https://app.diagrams.net/) .

- The architecture is composed of 3 layers : AWS layer , Kubernestes Physical layer and Kubernestes logical layer.

## AWS Layer
The AWS layer of our architecture provides the foundational infrastructure that supports our Kubernetes cluster on AWS EKS (Elastic Kubernetes Service). This layer is crucial as it provides the compute resources, storage, and networking capabilities required to run our applications efficiently. Below is a detailed description of the AWS layer configuration, focusing on node groups and storage.

### EKS Cluster Configuration

#### Managed Node Groups


- **Cluster Name:** ${CLUSTER_NAME}
- **Region:** ${AWS_REGION}
- **Kubernetes Version:** 1.29
- **Availability Zones:** eu-west-3a, eu-west-3b, eu-west-3c

1. **nodegroup1**
   - **Instance Types:** t3.medium
   - **Availability Zones:** eu-west-3a, eu-west-3b, eu-west-3c
   - **Spot Instances:** true
   - **Desired Capacity:** 3
     
2. **mng-ondemand-prod**
   - **Instance Types:** t3a.xlarge, t2.xlarge, m6i.xlarge, m5.xlarge, m5a.xlarge
   - **Availability Zones:** eu-west-3a, eu-west-3b, eu-west-3c
   - **Min/Max Size:** 1/4
   - **Desired Capacity:** 1
   - **Volume Size:** 300 GiB


3. **backup-mng-ondemand-prod**
   - **Instance Types:** t3a.xlarge, t2.xlarge, m6i.xlarge, m5.xlarge, m5a.xlarge
   - **Availability Zones:** eu-west-3a, eu-west-3b, eu-west-3c
   - **Min/Max Size:** 0/4
   - **Desired Capacity:** 0


4. **mng-spot-prod-16g**
   - **Instance Types:** t3a.xlarge, t3.xlarge, t2.xlarge, m6i.xlarge, m5.xlarge, m5a.xlarge
   - **Availability Zones:** eu-west-3a, eu-west-3b, eu-west-3c
   - **Min/Max Size:** 2/12
   - **Desired Capacity:** 5
   - **Spot Instances:** Enabled

5. **mng-spot-prod-32g**
   - **Instance Types:** r6i.xlarge, r5.xlarge, r5a.xlarge
   - **Availability Zones:** eu-west-3a, eu-west-3b, eu-west-3c
   - **Min/Max Size:** 1/8
   - **Desired Capacity:** 2
   - **Spot Instances:** Enabled

6. **mng-spot-prod**
   - **Instance Types:** t3a.xlarge, t2.xlarge, m6i.xlarge, m5.xlarge, m5a.xlarge
   - **Availability Zones:** eu-west-3a, eu-west-3b, eu-west-3c
   - **Min/Max Size:** 4/12
   - **Desired Capacity:** 6
   - **Spot Instances:** Enabled

#### Storage

In our architecture, we have implemented several Kubernetes StorageClass objects to manage persistent storage efficiently. These storage classes define how storage is dynamically provisioned and managed within our EKS cluster, using Amazon EBS (Elastic Block Store) as the underlying storage provider. Below are the details of the configured storage classes:

1.**gp2-delete-sc** 
  - **Type:** gp2 (General Purpose SSD)
  - **Reclaim Policy:** Delete (deletes the volume when the PVC is deleted)

2.**gp2-retain-sc1**
  - **Type:** gp2 (General Purpose SSD)
  - **Reclaim Policy:** Retain (retains the volume when the PVC is deleted)
## Kubernetes Layer

3.**gp2-delete-sc** 
  - **Type:** gp3 (General Purpose SSD)
  - **Reclaim Policy:** Delete (deletes the volume when the PVC is deleted)

4.**gp2-retain-sc1**
  - **Type:** gp3 (General Purpose SSD)
  - **Reclaim Policy:** Retain (retains the volume when the PVC is deleted)

## Kubernets Layer
This part provides an overview of the Kubernetes layer within our architecture. The Kubernetes layer is organized into Two main layers:  the Kubernetes physical layer, and the Kubernetes logical layer. This section focuses on  describing the use of different resources, control plane, and worker nodes placed in node groups. Each worker node contains different namespaces, each namespace hosts deployments with pods and services, and other namespaces contain StatefulSets for databases, PVCs, PVs from EBS, and services.

### Control Plane

The control plane manages the Kubernetes cluster, ensuring the state of the cluster matches the desired state as defined by the configurations. It includes components such as the API server, etcd, scheduler, and controller manager.

### Worker Nodes

Worker nodes run the actual workloads, including applications and services. These nodes are part of isix differnet  node groups, each serving specific purposes within the cluster:

1. **NodeGroup1:** General purpose, spot instances, volume size 100Gi.
2. **mng-ondemand-prod:** On-demand instances for databases, volume size 300Gi, tainted for elasticsearch master nodes.
3. **backup-mng-ondemand-prod:** Backup node group for databases, on-demand instances, volume size 300Gi.
4. **mng-spot-prod-16g:** Spot instances with 16Gi volume size.
5. **mng-spot-prod-32g:** Spot instances with 32Gi volume size.
6. **mng-spot-prod:** General purpose spot instances, volume size 300Gi.

### Namespaces

Namespaces are used to isolate resources within the Kubernetes cluster. Each namespace contains various Kubernetes resources, organized for specific functionalities:

- **Application Namespaces:** Contain deployments with pods and services for stateless applications.
- **Database Namespaces:** Contain StatefulSets, PVCs, and PVs for stateful applications like databases.

### Deployments and Pods

Deployments manage stateless applications, ensuring that the specified number of replicas are running at any given time. Each deployment creates and manages pods, which are the smallest deployable units in Kubernetes.

### Services

Services provide a stable IP address and DNS name for accessing the pods, enabling communication within the cluster and with external clients.

### StatefulSets

StatefulSets manage stateful applications, ensuring the deployment and scaling of a set of pods with unique identities and persistent storage. This is particularly useful for applications like databases.

### Persistent Volume Claims (PVCs) and Persistent Volumes (PVs)

PVCs are requests for storage by users, and PVs are the actual storage resources in the cluster. PVCs bind to PVs to provide persistent storage for pods. In our setup, PVs are provisioned using Amazon EBS.

#### Storage Classes

We use different storage classes for different types of volumes:
- **gp2-delete-sc**: Storage class with gp2 volumes and a delete reclaim policy.
- **gp2-retain-sc**: Storage class with gp2 volumes and a retain reclaim policy.
- **gp3-delete-sc**: Storage class with gp3 volumes and a delete reclaim policy.
- **gp3-retain-sc**: Storage class with gp3 volumes and a retain reclaim policy.

