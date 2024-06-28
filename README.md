# EKS Cluster Architechture
- This architetcure provides a comprehensive overview of our AWS EKS (Elastic Kubernetes Service) cluster architecture, focusing on different resources that are strategically placed within specific node groups. By leveraging the robust features of AWS EKS, this architecture ensures optimal management, scalability, and resilience of application. The architecture  will detail the various Kubernetes objects employed and  their configurations.
  
- The architecture was designed by [Draw.io](https://app.diagrams.net/) .

- The architecture is composed of 3 layers : AWS layer , Kubernestes Physical layer and Kubernestes logical layer.

## AWS Layer
The AWS layer of our architecture provides the foundational infrastructure that supports our Kubernetes cluster on AWS EKS (Elastic Kubernetes Service). This layer is crucial as it provides the compute resources, storage, and networking capabilities required to run our applications efficiently. Below is a detailed description of the AWS layer configuration, focusing on node groups and storage.

### EKS Cluster Configuration

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
   - 
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

