---
title: "Learning Notes on `AWS Technical Essentials` copied from Coursera"
draft: true
---

# Welcome to the Course

AWS Cloud Technical Essentials is a fundamental-level course. It’s designed to build your competence, confidence, and credibility with practical cloud skills that can help you innovate and advance your professional future. Here’s a quick overview of the skills that you will learn in each week of this first course. 

## Week 1: Getting Started with AWS Cloud 

 In this week, you will learn the definition of cloud computing and how to describe the cloud value proposition. You will learn how to differentiate between workloads that run on premises compared to workloads that run in the cloud, and how to create an AWS account. You will also get an overview of AWS, including how to differentiate between AWS Regions and Availability Zones, and the different ways that you can interact with AWS. Finally, you will learn best practices for using AWS Identity and Access Management (IAM). 

## Week 2: AWS Compute & Networking 

Week 2 is where you will learn how AWS compute services differ from other AWS services. The content for this week covers the basic components of Amazon Elastic Compute Cloud (Amazon EC2) architecture, and how to differentiate between a container and a virtual machine. You will also learn about the features and advantages of using serverless technologies, in addition to basic networking concepts and the features of Amazon Virtual Private Cloud (Amazon VPC). 

## Week 3: Storage & Databases on AWS 

This week, you will learn important concepts for AWS storage services—such as buckets and objects for Amazon Simple Storage Service (Amazon S3), and how Amazon Elastic Block Store (Amazon EBS) is used on AWS. You will also explore databases on AWS, and the use cases for each AWS storage service. 

##  Week 4: Monitoring, Optimizing, and Going Serverless on AWS 

In Week 4, you will learn about the benefits of monitoring on AWS, and how to optimize solutions on AWS. You will also learn about the function of Elastic Load Balancing (ELB), and how to differentiate between vertical scaling and horizontal scaling. 

---

# Course Roadmap

![alt text](./images/course_roadmap.png)

---

# What is AWS?
## What is the Cloud? 
In the past, companies and organizations hosted and maintained hardware such as compute, storage, and networking equipment in their own data centers. They needed to allocate entire infrastructure departments to take care of them, resulting in a costly operation that made some workloads and experimentation impossible.

As internet usage became more widespread, the demand for compute, storage, and networking equipment increased. For some companies and organizations, the cost of maintaining a large physical presence was unsustainable. To solve this problem, cloud computing was created.

Cloud computing is the on-demand delivery of IT resources over the internet with pay-as-you-go pricing. You no longer have to manage and maintain your own hardware in your own data centers. Companies like AWS own and maintain these data centers and provide virtualized data center technologies and services to users over the internet.

To help differentiate between running workloads on-premises versus in the cloud, consider the scenario where your developers need to deploy a new feature on your application. Before they deploy, the team wants to test the feature in a separate quality assurance (QA) environment that has the exact same configurations as production.

If you run your application on-premises, creating this additional environment requires you to buy and install hardware, connect the necessary cabling, provision power, install operating systems, and more. All of these tasks can be time-consuming and take days to perform. Meanwhile, the new product feature’s time-to-market is increasing and your developers are waiting for this environment. 

If you ran your application in the cloud, you can replicate the entire environment as often as needed in a matter of minutes or even seconds. Instead of physically installing hardware and connecting cabling, you can logically manage your physical infrastructure over the internet. 

Using cloud computing not only saves you time from the set-up perspective, but it also removes the undifferentiated heavy lifting. If you look at any application, you’ll see that some of the aspects of it are very important to your business, like the code. However, there are other aspects that are no different than any other application you might make: for instance the compute the code runs on. By removing repetitive common tasks that don’t differentiate your business, like installing virtual machines, or storing backups, you can focus on what is strategically unique to your business and let AWS handle the tasks that are time consuming and don’t separate you from your competitors. 

So where does AWS fit into all of this? Well AWS simply just provides cloud computing services. Those IT resources mentioned in the cloud computing definition are AWS services in this case. We’ll need to use these AWS services to architect a scalable, highly available, and cost effective infrastructure to host our corporate directory application. This way we can get our corporate directory app out into the world quickly, without having to manage any heavy-duty physical hardware. There are the six main advantages to running your workloads on AWS.

**The Six Benefits of Cloud Computing**: 

- Pay as you go. Instead of investing in data centers and hardware before you know how you are going to use them, you pay only when you use computing resources, and pay only for how much you use.

- Benefit from massive economies of scale. By using cloud computing, you can achieve a lower cost than you can get on your own. Because usage from hundreds of thousands of customers is aggregated in the cloud, AWS can achieve higher economies of scale, which translates into lower pay as-you-go prices.

- Stop guessing capacity. Eliminate guessing on your infrastructure capacity needs. When you make a capacity decision prior to deploying an application, you often end up either sitting on expensive idle resources or dealing with limited capacity. With cloud computing, these problems go away. You can access as much or as little capacity as you need, and scale up and down as required with only a few minutes notice.

- Increase speed and agility. IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization since the cost and time it takes to experiment and develop is significantly lower.

- Stop spending money running and maintaining data centers. Focus on projects that differentiate your business, not the infrastructure. Cloud computing lets you focus on your customers, rather than on the heavy lifting of racking, stacking, and powering physical infrastructure. This is often referred to as undifferentiated heavy lifting.

- Go global in minutes. Easily deploy your application in multiple Regions around the world with just a few clicks. This means you can provide lower latency and a better experience for your customers at a minimal cost.

---

# AWS Global Infrastructure

Infrastructure, like data centers and networking connectivity, still exists as the foundation of every cloud application. In AWS, this physical infrastructure makes up the AWS Global Infrastructure, in the form of Availability Zones and Regions.

Here are a few examples of Region codes:

us-east-1: This is the first Region created in the east of the US. The geographical name for this Region is N. Virginia.

ap-northeast-1: The first Region created in the northeast of Asia Pacific. The geographical name for this Region is Tokyo.

AWS Regions are independent from one another. This means that your data is not replicated from one Region to another, without your explicit consent and authorization.

## CHOOSE THE RIGHT AWS REGION
Consider four main aspects when deciding which AWS Region to host your applications and workloads: latency, price, service availability, and compliance.

- **Latency**. If your application is sensitive to latency, choose a Region that is close to your user base. This helps prevent long wait times for your customers. Synchronous applications such as gaming, telephony, WebSockets, and IoT are significantly affected by higher latency, but even asynchronous workloads, such as ecommerce applications, can suffer from an impact on user connectivity.
- **Price**. Due to the local economy and the physical nature of operating data centers, prices may vary from one Region to another. The pricing in a Region can be impacted by internet connectivity, prices of imported pieces of equipment, customs, real estate, and more. Instead of charging a flat rate worldwide, AWS charges based on the financial factors specific to the location.
- **Service availability**. Some services may not be available in some Regions. The AWS documentation provides a table containing the Regions and the available services within each one.
- **Data compliance**. Enterprise companies often need to comply with regulations that require customer data to be stored in a specific geographic territory. If applicable, you should choose a Region that meets your compliance requirements.

## AVAILABILITY ZONES

![alt text](./images/availability_zones.png)

Inside every Region is a cluster of Availability Zones (AZ). An AZ consists of one or more data centers with redundant power, networking, and connectivity. These data centers operate in discrete facilities with undisclosed locations. They are connected using redundant high-speed and low-latency links.AZs also have a code name. Since they’re located inside Regions, they can be addressed by appending a letter to the end of the Region code name. For example:

us-east-1a: an AZ in us-east-1 (Northern Virginia Region)

sa-east-1b: an AZ in sa-east-1 (São Paulo Region in South America)

If you see that a resource exists in us-east-1c, you know this resource is located in AZ c of the us-east-1 Region.

## SCOPE AWS SERVICES

Depending on the AWS Service you use, your resources are either deployed at the AZ, Region, or Global level. Each service is different, so you need to understand how the scope of a service may affect your application architecture.When you operate a Region-scoped service, you only need to select the Region you want to use. If you are not asked to specify an individual AZ to deploy the service in, this is an indicator that the service operates on a Region-scope level. For region-scoped services, AWS automatically performs actions to increase data durability and availability.On the other hand, some services ask you to specify an AZ. With these services, you are often responsible for increasing the data durability and high availability of these resources.


## MAINTAIN RESILIENCY

To keep your application available, you need to maintain high availability and resiliency. A well-known best practice for cloud architecture is to use Region-scoped, managed services. These services come with availability and resiliency built in.When that is not possible, make sure the workload is replicated across multiple AZs. At a minimum, you should use two AZs. If one entire AZ fails, your application will have infrastructure up and running in at least a second AZ to take over the traffic.

![alt text](./images/application_in_2_AZs.png)

---


# Security and the AWS Shared Responsibility Model

When you begin working with the AWS Cloud, managing security and compliance is a shared responsibility between AWS and you. To depict this shared responsibility, AWS created the shared responsibility model. This distinction of responsibility is commonly referred to as security of the cloud, versus security in the cloud.

![alt text](./images/shared_responsibility_model.png)

## WHAT IS AWS RESPONSIBLE FOR?
AWS is responsible for security of the cloud. This means AWS is required to protect and secure the infrastructure that runs all the services offered in the AWS Cloud. AWS is responsible for:

Protecting and securing AWS Regions, Availability Zones, and data centers, down to the physical security of the buildings

Managing the hardware, software, and networking components that run AWS services, such as the physical server, host operating systems, virtualization layers, and AWS networking components

The level of responsibility AWS has depends on the service. AWS classifies services into three different categories. The following table provides information about each, as well as the AWS responsibility.


![alt text](./images/aws_responsibilities.png)

Note: 
- Container services refer to AWS abstracting application containers behind the scenes, not Docker container services. This enables AWS to move the responsibility of managing that platform away from customers.


## WHAT IS THE CUSTOMER RESPONSIBLE FOR?


You’re responsible for security in the cloud. When using any AWS service, you’re responsible for properly configuring the service and your applications, as well as ensuring your data is secure.The level of responsibility you have depends on the AWS service. Some services require you to perform all the necessary security configuration and management tasks, while other more abstracted services require you to only manage the data and control access to your resources. Using the three categories of AWS services, you can determine your level of responsibility for each AWS service you use.

![alt text](./images/customer_responsbilities.png)


Due to the varying level of effort, it’s important to consider which AWS service you use and review the level of responsibility required to secure the service. It’s also important to review how the shared security model aligns with the security standards in your IT environment, as well as any applicable laws and regulations.It’s important to note that you maintain complete control of your data and are responsible for managing the security related to your content. Here are some examples of your responsibilities in context.

- Choosing a Region for AWS resources in accordance with data sovereignty regulations
- Implementing data protection mechanisms, such as encryption and managing backups
- Using access control to limit who has access to your data and AWS resources

---

# Protect the AWS Root User

## What’s the Big Deal About Auth?
When you’re configuring access to any account, two terms come up frequently: authentication and authorization. Though these terms may seem basic, you need to understand them to properly configure access management on AWS. It’s important to keep this mind as you progress in this course. Let’s define both terms.

## Understand Authentication
When you create your AWS account, you use a combination of an email address and a password to verify your identity. If the user types in the correct email and password, the system assumes the user is allowed to enter and grants them access. This is the process of authentication.Authentication ensures that the user is who they say they are. Usernames and passwords are the most common types of authentication, but you may also work with other forms, such as token-based authentication or biometric data like a fingerprint. Authentication simply answers the question, **“Are you who you say you are?”**

## Understand Authorization
Once you’re inside your AWS account, you might be curious about what actions you can take. This is where authorization comes in. Authorization is the process of giving users permission to access AWS resources and services. Authorization determines whether the user can perform an action—whether it be to read, edit, delete, or create resources. Authorization answers the question, **“What actions can you perform?”**

## What Is the AWS Root User?
When you first create an AWS account, you begin with a single sign-in identity that has complete access to all AWS services and resources in the account. This identity is called the AWS root user and is accessed by signing in with the email address and password that you used to create the account.

## Understand the AWS Root User Credentials
The AWS root user has two sets of credentials associated with it. One set of credentials is the email address and password used to create the account. This allows you to access the AWS Management Console. The second set of credentials is called access keys, which allow you to make programmatic requests from the 
AWS Command Line Interface (AWS CLI) or AWS API
.  Access keys consist of two parts:

1. An access key ID, for example, A2lAl5EXAMPLE
2. A secret access key, for example, wJalrFE/KbEKxE

Similar to a username and password combination, you need both the access key ID and secret access key to authenticate your requests via the AWS CLI or AWS API. Access keys should be managed with the same security as an email address and password.

## Follow Best Practices When Working with the AWS Root User
Keep in mind that the root user has complete access to all AWS services and resources in your account, as well as your billing and personal information. Due to this, securely lock away the credentials associated with the root user and do not use the root user for everyday tasks.  To ensure the safety of the root user:

- Choose a strong password for the root user.
- Never share your root user password or access keys with anyone.
- Disable or delete the access keys associated with the root user.
- Do not use the root user for administrative tasks or everyday tasks.

**When is it OK to use the AWS root user?**
There are some tasks where it makes sense to use the AWS root user. Check out the links at the end of this section to read about them.
Link: [aws_tasks-that-require-root](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks)

## Delete Your Keys to Stay Safe
If you don't already have an access key for your AWS account root user, don't create one unless you absolutely need to. If you do have an access key for your AWS account root user and want to delete the keys:

Go to the 
 My Security Credentials page
 in the AWS Management Console and sign in with the root user’s email address and password.

Open the Access keys section.

Under Actions, click Delete.

Click Yes.

## The Case for Multi-Factor Authentication
When you create an AWS account and first log in to that account, you use single-factor authentication. Single-factor authentication is the simplest and most common form of authentication. It only requires one authentication method. In this case, you use a username and password to authenticate as the AWS root user. Other forms of single-factor authentication include a security pin or a security token.However, sometimes a user’s password is easy to guess. 

For example, your coworker Bob’s password, IloveCats222, might be easy for someone who knows Bob personally to guess, because it’s a combination of information that is easy to remember and describes certain things about Bob (1. Bob loves cats, and 2. Bob’s birthday is February 22).

If a bad actor guessed or cracked Bob’s password through social engineering, bots, or scripts, Bob might lose control of his account. Unfortunately, this is a common scenario that users of any website often face.

This is why using MFA has become so important in preventing unwanted account access. MFA requires two or more authentication methods to verify an identity, pulling from three different categories of information.

Something you know, such as a username and password, or pin number

Something you have, such as a one-time passcode from a hardware device or mobile app

Something you are, such as fingerprint or face scanning technology

Using a combination of this information enables systems to provide a layered approach to account access. Even though the first method of authentication, Bob’s password, was cracked by a malicious user, it’s very unlikely that a second method of authentication, such as a fingerprint, would also be cracked. This extra layer of security is needed when protecting your most sacred accounts, which is why it’s important to enable MFA on your AWS root user.

## Use MFA on AWS
If you enable MFA on your root user, you are required to present a piece of identifying information from both the something you know category and the something you have category. The first piece of identifying information the user enters is an email and password combination. The second piece of information is a temporary numeric code provided by an MFA device.Enabling MFA adds an additional layer of security because it requires users to use a supported MFA mechanism in addition to their regular sign-in credentials. It’s best practice to enable MFA on the root user.

## Review Supported MFA Devices
AWS supports a variety of MFA mechanisms, such as virtual MFA devices, hardware devices, and Universal 2nd Factor (U2F) security keys. For instructions on how to set up each method, check out the Resources section.

![alt text](./images/mfa_devices_supported.png)

---

# Introduction to AWS Identity and Access Management

## WHAT IS IAM?
IAM is a web service that enables you to manage access to your AWS account and resources. It also provides a centralized view of who and what are allowed inside your AWS account (authentication), and who and what have permissions to use and work with your AWS resources (authorization).With IAM, you can share access to an AWS account and resources without having to share your set of access keys or password. You can also provide granular access to those working in your account, so that people and services only have permissions to the resources they need. For example, to provide a user of your AWS account with read-only access to a particular AWS service, you can granularly select which actions and which resources in that service they can access.


## GET TO KNOW THE IAM FEATURES

To help control access and manage identities within your AWS account, IAM offers many features to ensure security.

- IAM is global and not specific to any one Region. This means you can see and use your IAM configurations from any Region in the AWS Management Console.

- IAM is integrated with many AWS services 
by default


- You can establish password policies in IAM to specify complexity requirements and mandatory rotation periods for users.

- IAM supports MFA.

- IAM supports identity federation, which allows users who already have passwords elsewhere—for example, in your corporate network or with an internet identity provider—to get temporary access to your AWS account.

- Any AWS customer can use IAM; the service is offered at no additional charge.

## WHAT IS AN IAM USER?

An IAM user represents a person or service that interacts with AWS. You define the user within your AWS account. And any activity done by that user is billed to your account. Once you create a user, that user can sign in to gain access to the AWS resources inside your account.You can also add more users to your account as needed. For example, for your cat photo application, you could create individual users in your AWS account that correspond to the people who are working on your application. Each person should have their own login credentials. Providing users with their own login credentials prevents sharing of credentials.

## IAM USER CREDENTIALS

An IAM user consists of a name and a set of credentials. When creating a user, you can choose to provide the user:

- Access to the AWS Management Console
- Programmatic access to the AWS Command Line Interface (AWS CLI) and AWS Application Programming Interface (AWS API)

To access the AWS Management Console, provide the users with a user name and password. For programmatic access, AWS generates a set of access keys that can be used with the AWS CLI and AWS API. IAM user credentials are considered permanent, in that they stay with the user until there’s a forced rotation by admins.When you create an IAM user, you have the option to grant permissions directly at the user level.This can seem like a good idea if you have only one or a few users. However, as the number of users helping you build your solutions on AWS increases, it becomes more complicated to keep up with permissions. For example, if you have 3,000 users in your AWS account, administering access becomes challenging, and it’s impossible to get a top-level view of who can perform what actions on which resources.If only there were a way to group IAM users and attach permissions at the group level instead. Guess what: There is!

## WHAT IS AN IAM GROUP?

An IAM group is a collection of users. All users in the group inherit the permissions assigned to the group. This makes it easy to give permissions to multiple users at once. It’s a more convenient and scalable way of managing permissions for users in your AWS account. This is why using IAM groups is a best practice.If you have a an application that you’re trying to build and have multiple users in one account working on the application, you might decide to organize these users by job function. You might want IAM groups organized by developers, security, and admins. You would then place all of your IAM users in the respective group for their job function.This provides a better view to see who has what permissions within your organization and an easier way to scale as new people join, leave, and change roles in your organization.Consider the following examples.

- A new developer joins your AWS account to help with your application. You simply create a new user and add them to the developer group, without having to think about which permissions they need.

- A developer changes jobs and becomes a security engineer. Instead of editing the user’s permissions directly, you can instead remove them from the old group and add them to the new group that already has the correct level of access.

Keep in mind the following features of groups.

- Groups can have many users.
- Users can belong to many groups.
- Groups cannot belong to groups.


The root user can perform all actions on all resources inside an AWS account by default. This is in contrast to creating new IAM users, new groups, or new roles. New IAM identities can perform no actions inside your AWS account by default until you explicitly grant them permission.The way you grant permissions in IAM is by using IAM policies.

## WHAT IS AN IAM POLICY?

To manage access and provide permissions to AWS services and resources, you create IAM policies and attach them to IAM users, groups, and roles. Whenever a user or role makes a request, AWS evaluates the policies associated with them. For example, if you have a developer inside the developers group who makes a request to an AWS service, AWS evaluates any policies attached to the developers group and any policies attached to the developer user to determine if the request should be allowed or denied.

## IAM POLICY EXAMPLES

Most policies are stored in AWS as JSON documents with several policy elements. Take a look at the following example of what providing admin access through an IAM identity-based policy looks like.

```json
{

"Version": "2012-10-17",    
     "Statement": [{        
          "Effect": "Allow",        
          "Action": "*",        
          "Resource": "*"     
     }]
}
```

In this policy, there are four major JSON elements: Version, Effect, Action, and Resource.

- The Version element defines the version of the policy language. It specifies the language syntax rules that are needed by AWS to process a policy. To use all the available policy features, include "Version": "2012-10-17" before the "Statement" element in all your policies.

- The Effect element specifies whether the statement will allow or deny access. In this policy, the Effect is "Allow", which means you’re providing access to a particular resource.

- The Action element describes the type of action that should be allowed or denied. In the above policy, the action is "*". This is called a wildcard, and it is used to symbolize every action inside your AWS account.

- The Resource element specifies the object or objects that the policy statement covers. In the policy example above, the resource is also the wildcard "*". This represents all resources inside your AWS console.

Putting all this information together, you have a policy that allows you to perform all actions on all resources inside your AWS account. This is what we refer to as an administrator policy.

Let’s look at another example of a more granular IAM policy.


```json
{"Version": "2012-10-17",    
     "Statement": [{        
          "Effect": "Allow",        
          "Action": [            
               "iam: ChangePassword",            
               "iam: GetUser"            
               ],        
          "Resource": "arn:aws:iam::123456789012:user/${aws:username}"    
     }]
}
```

After looking at the JSON, you can see that this policy allows the IAM user to change their own IAM password (iam:ChangePassword) and get information about their own user (iam:GetUser). It only permits them to access their own credentials because the resource restricts access with the variable substitution ${aws:username}.

## UNDERSTAND POLICY STRUCTURE

When creating a policy, it is required to have each of the following elements inside a policy statement.

![alt text](./images/iam_policy_3_essential_elements.png)

---

# Role Based Access in AWS

Throughout these last few lessons, there have been sprinklings of IAM best practices. It’s helpful to have a brief summary of some of the most important IAM best practices you need to be familiar with before building out solutions on AWS.

## LOCK DOWN THE AWS ROOT USER

The root user is an all-powerful and all-knowing identity within your AWS account. If a malicious user were to gain control of root-user credentials, they would be able to access every resource within your account, including personal and billing information. To lock down the root user:

Don’t share the credentials associated with the root user.

Consider deleting the root user access keys.

Enable MFA on the root account.

## FOLLOW THE PRINCIPLE OF LEAST PRIVILEGE

Least privilege is a standard security principle that advises you to grant only the necessary permissions to do a particular job and nothing more. To implement least privilege for access control, start with the minimum set of permissions in an IAM policy and then grant additional permissions as necessary for a user, group, or role.

## USE IAM APPROPRIATELY

IAM is used to secure access to your AWS account and resources. It simply provides a way to create and manage users, groups, and roles to access resources within a single AWS account. IAM is not used for website authentication and authorization, such as providing users of a website with sign-in and sign-up functionality. IAM also does not support security controls for protecting operating systems and networks.

## USE IAM ROLES WHEN POSSIBLE

Maintaining roles is easier than maintaining users. When you assume a role, IAM dynamically provides temporary credentials that expire after a defined period of time, between 15 minutes and 36 hours. Users, on the other hand, have long-term credentials in the form of user name and password combinations or a set of access keys.User access keys only expire when you or the admin of your account rotates these keys. User login credentials expire if you have applied a password policy to your account that forces users to rotate their passwords.

## CONSIDER USING AN IDENTITY PROVIDER

If you decide to make your cat photo application into a business and begin to have more than a handful of people working on it, consider managing employee identity information through an identity provider (IdP). Using an IdP, whether it be an AWS service such as AWS IAM Identity Center (Successor to AWS Single Sign-On) or a third-party identity provider, provides you a single source of truth for all identities in your organization.You no longer have to create separate IAM users in AWS. You can instead use IAM roles to provide permissions to identities that are federated from your IdP.For example, you have an employee, Martha, that has access to multiple AWS accounts. Instead of creating and managing multiple IAM users named Martha in each of those AWS accounts, you can manage Martha in your company’s IdP. If Martha moves within the company or leaves the company, Martha can be updated in the IdP, rather than in every AWS account you have.

## CONSIDER AWS IAM IDENTITY CENTER

If you have an organization that spans many employees and multiple AWS accounts, you may want your employees to sign in with a single credential.AWS IAM Identity Center is an IdP that lets your users sign in to a user portal with a single set of credentials. It then provides them access to all their assigned accounts and applications in one central location.AWS IAM Identity Center is similar to IAM, in that it offers a directory where you can create users, organize them in groups, and set permissions across those groups, and grant access to AWS resources. However, AWS IAM Identity Center has some advantages over IAM. For example, if you’re using a third-party IdP, you can sync your users and groups to AWS IAM Identity Center.This removes the burden of having to re-create users that already exist elsewhere, and it enables you to manage those users from your IdP. More importantly, AWS IAM Identity Center separates the duties between your IdP and AWS, ensuring that your cloud access management is not inside or dependent on your IdP.

---

# Week 1's Quiz: 

[A GitHub Week 1 Quiz](https://github.com/salimt/Courses-/blob/master/AWS%20Cloud%20Solutions%20Architect%20Professional/c01-%20AWS%20Cloud%20Technical%20Essentials/w1-%20Amazon%20Web%20Services%20(AWS)/Week%201%20Quiz%20_%20Coursera.pdf)

---

# Default Amazon Machine Image (AMI) for Amazon EC2

When using the user data scripts, remember to replace the <INSERT REGION HERE> with whatever AWS region you are operating in, and ensure you remove both brackets as well.

## Amazon Linux 2023 user data script: 

```bash
          #!/bin/bash -ex
          wget 
https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/DEV-AWS-MO-GCNv2/FlaskApp.zip
          unzip FlaskApp.zip
          cd FlaskApp/
          yum -y install python3-pip
          pip install -r requirements.txt
          yum -y install stress
          export PHOTOS_BUCKET=${SUB_PHOTOS_BUCKET}
          export AWS_DEFAULT_REGION=<INSERT REGION HERE>
          export DYNAMO_MODE=on
          FLASK_APP=application.py /usr/local/bin/flask run --host=0.0.0.0 --port=80 
```

---

## 2.1 Compute as a Service on AWS

## Understanding Servers
The first building block you need to host an application is a server. Servers often times can handle Hypertext Transfer Protocol (HTTP) requests and send responses to clients following the client-server model, though any API based communication also falls under this model. A client being a person or computer that sends a request, and a server handling the requests is a computer, or collection of computers, connected to the internet serving websites to internet users. These servers power your application by providing CPU, memory, and networking capacity to process users’ requests and transform them into responses. For context, common HTTP servers include:

Windows options, such as Internet Information Services (IIS).

Linux options, such as Apache HTTP Web Server, Nginx, and Apache Tomcat.

To run an HTTP server on AWS, you need to find a service that provides compute power in the AWS Management Console. You can log into the console and view the complete list of AWS compute services.


![alt text](./images/different_compute_options_in_AWS.png)

## Choose the Right Compute Option
If you’re responsible for setting up servers on AWS to run your infrastructure, you have many compute options. You need to know which service to use for which use case. 

At a fundamental level, there are three types of compute options: 
- virtual machines
- container services, and 
- serverless. 


If you’re coming to AWS with prior infrastructure knowledge, a virtual machine can often be the easiest compute option in AWS to understand. This is because a virtual machine emulates a physical server and allows you to install an HTTP server to run your applications. To run these virtual machines, you install a hypervisor on a host machine. This hypervisor provisions the resources to create and run your virtual machines.

In AWS, these virtual machines are called Amazon Elastic Compute Cloud or Amazon EC2. Behind the scenes, AWS operates and manages the host machines and the hypervisor layer. AWS also installs the virtual machine operating system, called the guest operating system.Some AWS compute services use Amazon EC2 or use virtualization concepts under the hood, therefore it is best to understand this service first before moving on to container services and serverless compute. 

A **hypervisor** is software or firmware that creates and manages virtual machines (VMs) by separating a computer's physical hardware from its operating system and applications. It allows multiple OS environments to run on a single physical machine, each with its own resources like CPU, memory, and storage. Hypervisors are fundamental to virtualization, enabling efficient use of hardware and providing flexibility, scalability, and isolation.

> Behind the scenes, AWS operates and manages the host machines and the hypervisor layer. AWS also installs the virtual machine operating system, called the guest operating system.

Some AWS compute services use Amazon EC2 or use virtualization concepts under the hood, therefore it is best to understand this service first before moving on to container services and serverless compute. 

---

## 2.2 Introduction to Amazon Elastic Compute Cloud (AWS EC2)


 Amazon EC2 is a web service that provides secure, resizable compute capacity in the cloud. It allows you to provision virtual servers called EC2 instances. Although AWS uses the phrase “web service” to describe it, it doesn’t mean that you are limited to running just web servers on your EC2 instances. You can create and manage these instances through the AWS Management Console, the AWS Command Line Interface (CLI), AWS Software Development Kits (SDKs), or through automation tools and infrastructure orchestration services.In order to create an EC2 instance, you need to define:

- **Hardware** specifications, like CPU, memory, network, and storage.
- **Logical** configurations, like networking location, firewall rules, authentication, and the operating system of your choice.

When launching an EC2 instance, the first setting you configure is which operating system you want by selecting an Amazon Machine Image (AMI).

### What Is an AMI?

In the traditional infrastructure world, the process of spinning up a server consists of installing an operating system from installation disks, installation drives, or installation wizards over the network. In the AWS Cloud, this operating system installation is no longer your responsibility, and is instead built into the AMI that you choose.Not only does an AMI let you configure which operating system you want, you can also select storage mappings, the architecture type (such as 32-bit, 64-bit, or 64-bit ARM), and additional software installed.

### What Is the Relationship Between AMIs and EC2 Instances?

> A cake is an instantiation of the cake recipe
> An EC2 instance is an instantiation of the AMI image

EC2 instances are live instantiations of what is defined in an AMI, much like a cake is a live instantiation of a cake recipe. If you are familiar with software development, you can also see this kind of relationship between a Class and an Object.

A Class is something you model and define, while an object is something you interact with. In this case, the AMI is how you model and define your instance, while the EC2 instance is the entity you interact with, where you can install your web server, and serve your content to users.When you launch a new instance, AWS allocates a virtual machine that runs on a hypervisor. Then the AMI you selected is copied to the root device volume, which contains the image used to boot the volume. In the end, you get a server you can connect to and install packages and any additional software. In this case, you install a web server along with the properly configured source code of your employee directory app. 


![alt text](./images/ami_ec2_rootvolume.png)

One advantage of using AMIs is that they are reusable. 

You might choose a Linux-based AMI and configure the HTTP server, application packages, and any additional software you may need to run your application. 

If you wanted to create a second EC2 instance with the same configurations, how can you easily do that? One option is to go through the entire instance creation and configuration process and try to match your settings to the first instance. However, this is time consuming and leaves room for human error. 

The second, better option, is to create an AMI from your running instance and use this AMI to start a new instance. This way, your new instance will have all the same configurations as your current instance, because the configurations set in the AMIs are the same.

![alt text](./images/create_ami_from_running_instance.png)

### Where Can You Find AMIs?
You can select an AMI from the following categories.

- Quick Start AMIs that are premade by AWS and allow you to get started quickly.
- AWS Marketplace AMIs that provide popular open source and commercial software from third-party vendors.
- My AMIs that are created from your EC2 instances.
- Community AMIs that are provided by the AWS user community.
- Build your own custom image with EC2 Image Builder.

---

## 2.3: Container Services on AWS

AWS offers a broad spectrum of compute offerings that give you the flexibility to choose the right tool for the right job. The three main categories of compute are virtual machines, containers, and serverless. There is no one-size-fits-all service because it depends on your needs.The key is to understand what each option has to offer in order to build a more appropriate cloud architecture for your use case. In this unit, you learn about containers and how to run them on AWS.Containers can host a variety of different workloads, including web applications, lift and shift migrations, distributed applications, and streamlining of development, test, and production environments.

### WHAT IS A CONTAINER?

While containers are often referred to as a new technology, the idea started in the 1970s with certain Linux kernels having the ability to separate their processes through isolation. At the time, this was configured manually, making operations complex.With the evolution of the open source software community, containers evolved. Today, containers are used as a solution to problems of traditional compute, including the issue of getting software to run reliably when it moves from one compute environment to another.


A container is a standardized unit that packages up your code and all of its dependencies. This package is designed to run reliably on any platform, because the container creates its own independent environment. This makes it easy to carry workloads from one place to another, such as from development to production or from on-premises to the cloud.

### WHAT IS DOCKER?

When you hear the word container, you may associate it with Docker. **Docker is a popular container runtime** that simplifies the management of the entire operating system stack needed for container isolation, including networking and storage. Docker makes it easy to create, package, deploy, and run containers.

![alt text](./images/containers_and_virtual_machines.png)


Containers share the same operating system and kernel as the host they exist on, whereas virtual machines contain their operating system. Since each virtual machine has to maintain a copy of an operating system, there’s a degree of wasted space.A container is more lightweight. They spin up quicker, almost instantly. This difference in startup time becomes instrumental when designing applications that need to scale quickly during input/output (I/O) bursts.While containers can provide speed, virtual machines offer you the full strength of an operating system and offer more resources, like package installation, a dedicated kernel, and more.

### ORCHESTRATE CONTAINERS

In AWS, containers run on EC2 instances. For example, you may have a large instance and run a few containers on that instance.While running one instance is easy to manage, it lacks high availability and scalability. Most companies and organizations run many containers on many EC2 instances across several Availability Zones.If you’re trying to manage your compute at a large scale, you need to know:

- How to place your containers on your instances.
- What happens if your container fails.
- What happens if your instance fails.
- How to monitor deployments of your containers.


This coordination is handled by a container orchestration service. AWS offers two container orchestration services: Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS).

### MANAGE CONTAINERS WITH AMAZON ELASTIC CONTAINER SERVICE (AMAZON ECS)

Amazon ECS is an end-to-end container orchestration service that allows you to quickly spin up new containers and manage them across a cluster of EC2 instances.

![alt text](./images/one_ec2_multiple_containers.png)


To run and manage your containers, you need to install the Amazon ECS Container Agent on your EC2 instances. This agent is open source and responsible for communicating back to the Amazon ECS service about cluster management details. You can run this agent on both Linux and Windows AMIs. An instance with the container agent installed is often called a container instance.

![alt text](./images/ecs_agent_to_orchestrate_containers.png)


Once the Amazon ECS container instances are up and running, you can perform actions that include, but are not limited to, launching and stopping containers, getting cluster state, scaling in and out, scheduling the placement of containers across your cluster, assigning permissions, and meeting availability requirements.

To prepare your application to run on Amazon ECS, you create a task definition. The task definition is a text file, in JSON format, that describes one or more containers. A task definition is similar to a blueprint that describes the resources you need to run that container, such as CPU, memory, ports, images, storage, and networking information.

Here is a simple task definition that you can use for your corporate director application. In this example, the runs on the Nginx web server.


### Task definition
```json
{    

     "family": "webserver",    

     "containerDefinitions": [ {        

          "name": "web",        

          "image": "nginx",        

          "memory": "100",        

          "cpu": "99"    

     } ],    

     "requiresCompatibilities": [ "FARGATE" ],    

     "networkMode": "awsvpc",    

     "memory": "512",    

     "cpu": "256"

}
```

```
## Amazon ECS (Elastic Container Service):
- What it is: A fully managed container orchestration service provided by AWS.
- Technology: ECS is an AWS-native service and does not use Kubernetes. Instead, it uses its own orchestration technology.
- Docker integration: ECS works directly with Docker containers, so if you're familiar with Docker, it's relatively straightforward to use ECS. AWS handles a lot of the complex setup, such as networking and container placement, for you.

## How ECS Works:
- Container Instances (EC2 instances): In ECS, when you launch a cluster of EC2 instances, each instance runs the ECS agent. This agent is responsible for running and managing the containers on that instance. These EC2 instances are called container instances.
- Tasks: A task is an instantiation of a container or group of containers. It’s how ECS defines a running containerized application. For example, if you launch an application with multiple containers, ECS defines it as a task.
- Fargate: ECS can also use Fargate, which is a serverless compute engine. With Fargate, you don't even need to manage EC2 instances; AWS runs the containers for you in a completely managed environment.

## Key Points:
- Native to AWS: ECS is built directly on AWS, and AWS takes care of much of the complexity (like networking, scaling, and load balancing) for you.
- No Kubernetes: ECS uses AWS-native orchestration, not Kubernetes.
- Terminology: Containers running on ECS are called tasks.
```

```
## Amazon EKS (Elastic Kubernetes Service):
- What it is: A fully managed service that runs Kubernetes clusters on AWS.
- Technology: EKS uses Kubernetes, an open-source container orchestration tool originally developed by Google. While ECS is AWS-native, EKS leverages Kubernetes' widespread adoption and flexibility.
- Docker integration: EKS runs Docker containers, but it uses Kubernetes to manage and orchestrate them, instead of AWS-native orchestration technology.

## How EKS Works:
- Worker Nodes (EC2 instances): In EKS, the EC2 instances are called worker nodes, and they run your containers. These worker nodes are part of a Kubernetes cluster.
- Pods: In Kubernetes (and therefore in EKS), a pod is the smallest deployable unit. A pod can contain one or more containers that are tightly coupled. Think of a pod as the Kubernetes equivalent of a task in ECS.
- Control Plane: EKS manages the Kubernetes control plane for you. The control plane is responsible for making scheduling decisions, scaling, and managing the state of the Kubernetes cluster (worker nodes, pods, etc.).

## Key Points:
- Kubernetes-based: EKS runs on Kubernetes, which means you get access to the full set of Kubernetes features, such as advanced scheduling, load balancing, service discovery, and much more.
- More Complex but Flexible: Since Kubernetes is a flexible and powerful orchestration tool, you get more control over how your containers run, but it also comes with more complexity compared to ECS.
- Terminology: Containers running in EKS are part of a pod, not a task.
```


### USE KUBERNETES WITH AMAZON ELASTIC KUBERNETES SERVICE (AMAZON EKS)

Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services. By bringing software development and operations together by design, Kubernetes created a rapidly growing ecosystem that is very popular and well established in the market.If you already use Kubernetes, you can use Amazon EKS to orchestrate these workloads in the AWS Cloud.Amazon EKS is conceptually similar to Amazon ECS, but there are some differences.

An EC2 instance with the ECS Agent installed and configured is called a container instance. In Amazon EKS, it is called a worker node.

An ECS Container is called a task. In the Amazon EKS ecosystem, it is called a pod.

While Amazon ECS runs on AWS native technology, Amazon EKS runs on top of Kubernetes.

If you have containers running on Kubernetes and want an advanced orchestration solution that can provide simplicity, high availability, and fine-grained control over your infrastructure, Amazon EKS is the tool for you.


### Terminology Comparison

| ECS | EKS |
|---|---|
| EC2 Instances where containers are run `EC2 Container Instances` | EC2 Instances where containers run `Worker Nodes` |
| A `task` refers to a set of one or more containers that are scheduled together | A `pod` - the smallest deployable unit and equivalent of `task` in ECS - consists of one or more containers that share resources |
| Summary: In ECS, the EC2 instances where containers run are called container instances because they have the ECS agent installed to manage `tasks` | Summary: In EKS (Kubernetes), the EC2 instances are called worker nodes, and they are part of the broader Kubernetes cluster. Kubernetes distributes containers (in the form of pods) to these nodes. |

![alt text](./images/a_EKS_worker_node.png)

---

## 2.4 Serverless and AWS Lambda

### REMOVE THE UNDIFFERENTIATED HEAVY LIFTING

If you run your code on Amazon EC2, AWS is responsible for the physical hardware and you are responsible for the logical controls, such as guest operating system, security and patching, networking, security, and scaling.

If you run your code in containers on Amazon ECS and Amazon EKS, AWS is responsible for more of the container management, such as deploying containers across EC2 instances and managing the container cluster. 

However, when running ECS and EKS on EC2, you are still responsible for maintaining the underlying EC2 instances.

If you want to deploy your workloads and applications without having to manage any EC2 instances, you can do that on AWS with serverless compute.


### GO SERVERLESS

Every definition of serverless mentions four aspects.

- No servers to provision or manage.
- Scales with usage.
- You never pay for idle resources.
- Availability and fault tolerance are built-in.

With serverless, spend time on the things that differentiate your application, rather than spending time on ensuring availability, scaling, and managing servers.AWS has several serverless compute options, including AWS Fargate and AWS Lambda.

### EXPLORE SERVERLESS CONTAINERS WITH AWS FARGATE

Amazon ECS and Amazon EKS enable you to run your containers in two modes.

- Amazon EC2 mode
- AWS Fargate mode


AWS Fargate is a purpose-built serverless compute engine for containers. Fargate scales and manages the infrastructure, allowing developers to work on what they do best: application development.It achieves this by allocating the right amount of compute, eliminating the need to choose and handle EC2 Instances and cluster capacity and scaling. Fargate supports both Amazon ECS and Amazon EKS architecture and provides workload isolation and improved security by design.

AWS Fargate abstracts the EC2 instance so you’re not required to manage it. However, with AWS Fargate, you can use all the same ECS primitives, APIs, and AWS integrations. It natively integrates with AWS Identity and Access Management (IAM) and Amazon Virtual Private Cloud (VPC). Having native integration with Amazon VPC allows you to launch Fargate containers inside your network and control connectivity to your applications.

### RUN YOUR CODE ON AWS LAMBDA

If you want to deploy your workloads and applications without having to manage any EC2 instances or containers, you can use AWS Lambda.AWS Lambda lets you run code without provisioning or managing servers or containers. You can run code for virtually any type of application or backend service, including data processing, real-time stream processing, machine learning, WebSockets, IoT backends, mobile backends, and web apps, like your corporate directory app!

AWS Lambda requires zero administration from the user. You upload your source code and Lambda takes care of everything required to run and scale your code with high availability. There are no servers to manage, bringing you continuous scaling with subsecond metering and consistent performance.

### HOW LAMBDA WORKS

There are three primary components of a Lambda function: the trigger, code, and configuration.The code is source code, that describes what the Lambda function should run. This code can be authored in three ways.

You create the code from scratch.

You use a blueprint that AWS provides.

You use same code from the AWS Serverless Application Repository, a resource that contains sample applications, such as “hello world” code, Amazon Alexa Skill sample code, image resizing code, video encoding, and more.

When you create your Lambda function, you specify the runtime you want your code to run in. There are built-in runtimes such as Python, Node.js, Ruby, Go, Java, .NET Core, or you can implement your Lambda functions to run on a custom runtime.The configuration of a Lambda function consists of information that describes how the function should run. In the configuration, you specify network placement, environment variables, memory, invocation type, permission sets, and other configurations. To dive deeper into these configurations, check out the resources section of this unit.Triggers describe when the Lambda function should run. 

A trigger integrates your Lambda function with other AWS services, enabling you to run your Lambda function in response to certain API calls that occur in your AWS account. This makes you quicker to respond to events in your console without having to perform manual actions.All you need is the what, how, and when of a Lambda function to have functional compute capacity that runs only when you need it to.Amazon’s CTO, Werner Vogels, says, “No server is easier to manage than no server.” This quote summarizes the convenience you can have when running serverless solutions, like AWS Fargate and AWS Lambda. 

In the next unit, you apply all the information you’ve learned about Amazon EC2, Amazon ECS and Amazon EKS, and AWS Fargate and learn the use cases for each service.

AWS Lambda function handler

The AWS Lambda function handler is the method in your function code that processes events. When your function is invoked, Lambda runs the handler method. When the handler exits or returns a response, it becomes available to handle another event.You can use the following general syntax when creating a function handler in Python:

def handler_name(event, context):  ... return some_value

NAMING

The Lambda function handler name specified at the time you create a Lambda function is derived from the following:the name of the file in which the Lambda handler function is locatedthe name of the Python handler functionA function handler can be any name; however, the default on the Lambda console is lambda_function.lambda_handler. This name reflects the function name as lambda_handler, and the file where the handler code is stored in lambda_function.py.If you choose a different name for your function handler on the Lambda console, you must update the name on the Runtime settings pane.

BILLING GRANULARITY

AWS Lambda lets you run code without provisioning or managing servers, and you pay only for what you use. You are charged for the number of times your code is triggered (requests) and for the time your code executes, rounded up to the nearest 1ms (duration). AWS rounds up duration to the nearest millisecond with no minimum execution time. With this pricing, it can be very cost effective to run functions whose execution time is very low, such as functions with durations under 100ms or low latency APIs. For more information, see 
AWS News Blog
. 

SOURCE CODE

This video used a small amount of sample code illustrating a pattern for lazily generating assets using AWS Lambda and Amazon S3. If you’re looking to deploy a service to resize images to production, consider using the new release  
 Serverless Image Handler 
which is a robust solution to handle image manipulation and can be deployed via an AWS CloudFormation template.

You can find a tutorial on creating the AWS Lambda function as well as the code used in the AWS Lambda demo here: see 

---

## 2.5 Networking on AWS

### WHAT IS NETWORKING?

Networking is how you connect computers around the world and allow them to communicate with one another. In this trail, you’ve already seen a few examples of networking. One is the AWS global infrastructure. AWS has created a network of resources using data centers, Availability Zones, and Regions.

### KNOW THE NETWORKING BASICS


Think about sending a letter. When sending a letter, there are three pieces of information you need.
- Sender
- Receiver
- Payload content

Let’s go further. Each address must contain information such as:

- Name of sender and recipient
- Street
- City
- State or province
- Zip, area, or postal code
- Country


You need all parts of an address to ensure that your letter gets to its destination. Without the correct address, postal workers are not able to properly deliver the message. In the digital world, computers handle the delivery of messages in a similar way. This is called **routing**.

### WHAT ARE IP ADDRESSES?

In order to properly route your messages to a location, you need an address. Just like each home has a mail address, each computer has an IP address. However, instead of using the combination of street, city, state, zip code, and country, the IP address uses a combination of bits, 0s and 1s. 

 It’s called 32-bit because you have 32 digits of 0s and 1s. 

### WHAT IS IPV4 NOTATION?

Typically, you don’t see an IP address in this binary format. Instead, it’s converted into decimal format and noted as an Ipv4 address. 

In the diagram below, the 32 bits are grouped into groups of 8 bits, also called octets. Each of these groups is converted into decimal format separated by a period. 

![alt text](./images/ipv4_notation.png)

In the end, this is what is called an Ipv4 address. This is important to know when trying to communicate to a single computer. But remember, you’re working with a network. This is where CIDR Notation comes in.


### USE CIDR NOTATION

192.168.1.30 is a single IP address. If you wanted to express IP addresses between the range of 192.168.1.0 and 192.168.1.255, how can you do that? 

One way is by using Classless Inter-Domain Routing (CIDR) notation. CIDR notation is a compressed way of specifying a range of IP addresses. Specifying a range determines how many IP addresses are available to you. 

CIDR notation looks like this: 

```
192.168.1.0/24
```

It begins with a starting IP address and is separated by a forward slash (the “/” character) followed by a number. The number at the end specifies how many of the bits of the IP address are fixed. In this example, the first 24 bits of the IP address are fixed. The rest are flexible. 


```
# first 24 of the 32 bits are fixed 
192.168.1.0/24

# 192 - Fixed 
# 168 - Fixed
# 1 - Fixed
# last 8 bits - Flexible 

# each of the last 8 bits can take 0 or 1 - so two choices. 
# hence 2^8 = 256 IP addresses possible
```

When working with networks in the AWS Cloud, you choose your network size by using CIDR notation. In AWS, the smallest IP range you can have is `/28`, which provides you `16 IP addresses`. The largest IP range you can have is a `/16`, which provides you with `65,536` IP addresses.


---


```

# Q) What should be the right CIDR range to choose for my VPC? What factors dictate that? 
When should I choose a CIDR /24 or CIDR/28 and CIDR/16 range of ip addresses?

Ans: 
Factors that decide the range of the IP addresses: 
1. Size of the Network
2. Subnets
3. Growth and Scalability
4. Private vs Public Subnets
5. Peering and Inter-VPC Connectivity
6. Service Endpoints & NAT Gateways

Summary: 
/16: Best for large networks with many subnets, services, or where future scaling is critical.
/24: Suitable for mid-sized networks with a moderate number of subnets.
/28: Best for small networks, testing environments, or scenarios with very few resources.

Note: On `Subnets`

AWS reserves 5 IP addresses in every subnet, so in smaller CIDR blocks like /28 (where 16 IP addresses are available), you only have 11 usable IPs. Remaining 5 get used for subnets

```

---

## 2.6. Introduction to VPC


3 Requirements to set up a VPC: 
1. The name of your VPC.
2. A Region for your VPC to live in. Each VPC spans multiple Availability Zones within the Region you choose.
3. A IP range for your VPC in CIDR notation. This determines the size of your network. Each VPC can have up to four /16 IP ranges.

![alt text](./images/vpc_azs_region.png)

### Create a Subnet: 

After you create your VPC, you need to create subnets inside of this network. Think of subnets as smaller networks inside your base network—or virtual area networks (VLANs) in a traditional, on-premises network. In an on-premises network, the typical use case for subnets is to isolate or optimize network traffic. In AWS, subnets are used for high availability and providing different connectivity options for your resources. 

> Subnet is a subset of VPC. The size of Both Subnets and VPCs are indicated with CIDR notation.
> A VPC CIDR range is always bigger than its subnet CIDR range. 

When you create a subnet, you need to choose three settings.
1. The VPC you want your subnet to live in, in this case VPC (`10.0.0.0/16`).
2. The Availability Zone you want your subnet to live in, in this case AZ1.
3. A CIDR block for your subnet, which must be a subset of the VPC CIDR block, in this case 10.0.0.0/24.

 When you launch an EC2 instance, you launch it inside a subnet, which will be located inside the Availability Zone you choose.  

Below is an image of an EC2 instance residing inside a public subnet   

![alt text](./images/public_and_private_subnetets_inside_vpc.png)

How to maintain high availability with a VPC?

- When you create your subnets, keep high availability in mind. In order to maintain redundancy and fault tolerance, create at least two subnets configured in two different Availability Zones.   

**Reserved IPs** For AWS to configure your VPC appropriately, AWS reserves five IP addresses in each subnet. These IP addresses are used for routing, Domain Name System (DNS), and network management.  

What are those 5 Reserved IPs at every Subnet? 

![alt text](./images/5_reserved_ip_addresses.png)

> For example, consider a VPC with the IP range 10.0.0.0/22. The VPC includes `1,024 total IP addresses`. This is divided into four equal-sized subnets, each with a `/24` IP range with `256 IP addresses`. Out of each of those IP ranges, there are only 251 IP addresses that can be used because AWS reserves five.  

Since AWS reserves these five IP addresses, it can impact how you design your network. A common starting place for those who are new to the cloud is to create a VPC with a IP range of /16 and create subnets with a IP range of /24. This provides a large amount of IP addresses to work with at both the VPC and subnet level. 

---

### Gateways

#### Internet Gateway 

- To enable internet connectivity for your VPC, you need to create an internet gateway. 

> Think of this gateway as similar to a modem. Just as a modem connects your computer to the internet, the internet gateway connects your VPC to the internet. Unlike your modem at home, which sometimes goes down or offline, an internet gateway is highly available and scalable. 

- After you create an internet gateway, you then need to attach it to your VPC.  

#### Virtual Private Gateway  


A virtual private gateway allows you to connect your AWS VPC to another private network. Once you create and attach a VGW to a VPC, the gateway acts as anchor on the AWS side of the connection. On the other side of the connection, you’ll need to connect a customer gateway to the other private network. A customer gateway device is a physical device or software application on your side of the connection. 

> Once you have both gateways, you can then **establish an encrypted VPN connection between the two sides**. 


#### NAT Gateway

NAT Gateway stands for Network Address Translation Gateway. The name "NAT" is derived from the process of Network Address Translation, which allows a device (like an EC2 instance) with a private IP address to communicate with external systems (like the internet) by **translating its private IP into a public IP** for **outbound traffic**.


**Why is it called "NAT Gateway"?**
Network Address Translation (NAT): This is the key process behind the name. NAT allows instances in a private subnet (with only private IP addresses) to send traffic to the internet by translating their private IP addresses to a public IP address as they pass through the NAT Gateway.
Gateway: It acts as a "gateway" or bridge between instances in a private subnet and external destinations, like the internet.

**Primary Function: Outbound Internet Traffic**
A NAT Gateway is primarily designed to allow outbound internet access from instances in a private subnet, while preventing inbound traffic from the internet.
When an instance in a private subnet needs to download updates or communicate with a service on the internet, it sends the request to the NAT Gateway. The NAT Gateway then makes the request on behalf of the instance using its own public IP and routes the response back to the instance.


**Important Characteristics**:
- Outbound-only:
     - NAT Gateway is designed for outbound traffic only from private subnets to the internet. It does not allow incoming traffic initiated from the internet to reach instances in private subnets.

- Security:
     - Since instances behind a NAT Gateway do not have public IP addresses, they are not directly reachable from the internet, enhancing security.


**Summary**:
NAT Gateway enables instances in private subnets to connect to the internet (e.g., to download updates or communicate with external APIs), but does not allow inbound internet traffic. It serves as a way to hide the private IP addresses of those instances from external systems while enabling them to make outgoing connections.

---

**Outbound vs. Inbound Traffic Breakdown**
Outbound Traffic refers to traffic initiated by an instance (in your private subnet) that goes out to the internet. When you send a request to download an update or access an external API, this is outbound traffic because the instance is initiating the connection.

Inbound Traffic refers to traffic initiated from the internet towards your instance. For example, a web server accepting a request from an external user would be receiving inbound traffic.

**Key Concept: Stateful Connections and Outbound Session**
NAT Gateways maintain **stateful connections**. When your instance starts a connection to the internet, the NAT Gateway tracks that connection. Any return traffic (like the update file) is automatically allowed because it is part of an ongoing session initiated by your instance.
NAT Gateway does not allow new incoming connections initiated by the external source. It only forwards responses to requests that were initiated by the private instance (which keeps the session active).


## What is built in `Public` and `Private` Subnets

```
Example Architecture Setup for Amazon.com or Facebook.com:


**Public-facing Load Balancer (ALB or NLB) in a public subnet**:

- The Load Balancer receives all incoming traffic (e.g., user requests to Amazon.com).
It distributes the traffic to a pool of web servers based on load and availability.

**Web Servers**:
- The web servers can be in either a public or private subnet. If they are in a public subnet, they have a public IP address but only accept traffic from the Load Balancer.
If they are in a private subnet, they do not have a public IP and can only receive traffic forwarded by the Load Balancer.


**Backend Components (databases, APIs, etc.) in private subnets**:
- These are isolated and only accessible from the web servers or other internal systems.
- They cannot be accessed directly from the internet, ensuring sensitive data and services are protected.

**NAT Gateway (optional for backend services)**:
- Any backend instances in the private subnet that need to initiate outbound traffic (e.g., for updates, API calls) do so through a NAT Gateway.

Summary:
- Web Servers (like Amazon.com and Facebook.com) do need to allow inbound traffic for users to access their websites. However, this traffic is typically handled in a controlled and secure manner, often through Load Balancers and strict security group rules.
- Backend systems, on the other hand, are usually hosted in private subnets and do not allow any unsolicited inbound traffic from the internet. They may make outbound requests through NAT Gateways or other secure channels.


The **key security principle** here is that inbound traffic is tightly controlled and usually mediated by a public-facing Load Balancer, while private subnets and backend systems remain isolated and protected from direct exposure to the internet.
```

---

## 2.7: Amazon VPC Routing and Security

### The Main Route Table

When you create a VPC, AWS creates a route table called the main route table. A route table contains a set of rules, called routes, that are used to determine where network traffic is directed. AWS assumes that when you create a new VPC with subnets, you want traffic to flow between them. Therefore, the default configuration of the main route table is to allow traffic between all subnets in the local network.

![alt text](./images/main_route_table_(of_a_vpc).png)


There are two main parts to this route table.

- The **destination**, which is a range of IP addresses where you want your traffic to go. In the example of sending a letter, you need a destination to route the letter to the appropriate place. The same is true for routing traffic. In this case, the destination is the IP range of our VPC network.

- The **target**, which is the connection through which to send the traffic. In this case, the traffic is routed through the local VPC network.

### Custom Route Tables

- Custom Route Tables are Route Tables for specific subnets 
     - granular way to route your traffic for specific subnets.  

> If you associate a custom route table with a subnet, the subnet will use it instead of the main route table. By default, each custom route table you create will have the `local` route already inside it, allowing communication to flow between all resources and subnets inside the VPC. 


![alt text](./images/custom_route_tables.png)


### Secure Your Subnets with Network ACLs


A NACL (Network Access Control List) is *a stateless firewall* at the subnet level in AWS that controls inbound and outbound traffic to and from subnets. 

> Network ACL’s are considered stateless, so you need to include both the inbound and outbound ports used for the protocol. If you don’t include the outbound range, your server would respond but the traffic would never leave the subnet.   

![alt text](./images/network_acl_inbound_and_outbound_rules.png)

> Note the `non modifiable` rules in both `inbound` and `outbound`

### Secure Your EC2 Instances with Security Groups

![alt text](./images/NACL_vs_sec_group_rules.png)

> Default Security Group Behaviour: Denies all inbound traffic by default, allows all outbound by default

If you have a web server, you may need to accept HTTP and HTTPS requests to allow that type of traffic in through your security group. You can create an inbound rule that will allow port 80 (HTTP) and port 443 (HTTPS) as shown below. 

![alt text](./images/inbound_sg_rules_for_http_https.png)

#### Port 80 vs Port 443: 

```
Q) 1. What does port 80 and port 443 signify? 
2. What does HTTP request and HTTPS request ? How are these 2 requests different

> Port 80 (HTTP): When your browser makes an HTTP request over port 80, the communication is unencrypted. 
- Anyone intercepting the data between the browser and server can read the content in plaintext.
- HTTP requests are typically used on websites where security is not a concern (e.g., static informational sites).

E.g.: `http://` websites

> Port 443 (HTTPS): When your browser makes an HTTPS request over port 443, the communication is encrypted using SSL/TLS. This means:
- The data is securely encrypted and can only be decrypted by the server and client.
- HTTPS requests are used on websites where security is important (e.g., banking, e-commerce, login forms).

E.g.: `https://` websites
```

![alt text](./images/http_vs_https.png)


![alt text](./images/networking_sg_rules_for_a_multi_tier_system.png)

> This example allows you to define three tiers and isolate each tier with the security group rules you define. In this case, you only allow internet traffic to the web tier over HTTPS, Web Tier to Application Tier over HTTP, and Application tier to Database tier over MySQL. This is different from traditional on-premises environments, in which you isolate groups of resources via VLAN configuration. In AWS, security groups allow you to achieve the same isolation without tying it to your network. 

---

## 10 Common network troubleshooting steps for Amazon VPC

Below is a list of configurations you should check if you ever have `a public EC2 instance with a web application` that is not loading as expected.

1. Internet gateway
> Is IGW attached to VPC?
> Without the internet gateway, no traffic will be allowed in or out of the VPC.

2. Route tables

> Does the route table of the subnet that has the EC2 application have destination as `0.0.0.0/0` and target as `igw` ? This route allows outbound traffic to the internet and makes the subnet a `public` subnet


3. Security groups

> By default all inbound traffic is blocked. 




---



# Additional References:

- [My ChatGPT Interactions on Networking in AWS](https://chatgpt.com/share/67077451-51e0-800f-ad65-98c6b109e330)
- [My ChatGPT Interactions on Computing in AWS](https://chatgpt.com/share/6703b5e9-1154-800f-8c1d-03f16c3ae6e0)