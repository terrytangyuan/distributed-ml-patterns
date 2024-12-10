# Distributed Machine Learning Patterns

[![LinkedIn](https://raw.githubusercontent.com/terrytangyuan/terrytangyuan/master/imgs/linkedin.svg)](https://www.linkedin.com/in/terrytangyuan)
[![Bluesky](https://raw.githubusercontent.com/terrytangyuan/terrytangyuan/master/imgs/bluesky.svg)](https://bsky.app/profile/terrytangyuan.xyz)
[![GitHub](https://raw.githubusercontent.com/terrytangyuan/terrytangyuan/master/imgs/github.svg)](https://github.com/terrytangyuan)
[![Twitter](https://img.shields.io/twitter/follow/TerryTangYuan?style=social)](https://twitter.com/TerryTangYuan)
[![Mastodon](https://raw.githubusercontent.com/terrytangyuan/terrytangyuan/master/imgs/mastodon.svg)](https://fosstodon.org/@terrytangyuan)

<img align="right" src="images/english-front-cover.png" alt="book-front-cover" width="50%" height="50%">

This repository contains references and code for the book *Distributed Machine Learning Patterns* from [Manning Publications](https://bit.ly/2RKv8Zo) by [Yuan Tang](https://github.com/terrytangyuan).

:fire: **[Korean](images/korean-cover.jpg) and [Chinese](images/chinese-cover.pdf) versions are available from Tsinghua University Press and Hanbit Media!**

[Manning](https://bit.ly/2RKv8Zo), [Amazon](https://www.amazon.com/dp/1617299022/), [Barnes & Noble](https://www.barnesandnoble.com/w/distributed-machine-learning-patterns-yuan-tang/1140209010), [Powell’s]( https://www.powells.com/book/distributed-machine-learning-patterns-9781617299025), [Bookshop](https://bookshop.org/p/books/distributed-machine-learning-patterns-yuan-tang/17491200)


In *Distributed Machine Learning Patterns* you will learn how to:

* Apply patterns to build scalable and reliable machine learning systems.
* Construct machine learning pipelines with data ingestion, distributed training, model serving, and more.
* Automate machine learning tasks with [Kubernetes](https://kubernetes.io/), [TensorFlow](https://www.tensorflow.org/), [Kubeflow](https://www.kubeflow.org/), and [Argo Workflows](https://argoproj.github.io/argo-workflows/).
* Make trade off decisions between different patterns and approaches.
* Manage and monitor machine learning workloads at scale.

This book teaches you how to take machine learning models from your personal laptop to large distributed clusters. You’ll explore key concepts and patterns behind successful distributed machine learning systems, and learn technologies like TensorFlow, Kubernetes, Kubeflow, and Argo Workflows directly from a key maintainer and contributor. Real-world scenarios, hands-on projects, and clear, practical advice DevOps techniques and let you easily launch, manage, and monitor cloud-native distributed machine learning pipelines.

## About the topic

Scaling up models from personal devices to large distributed clusters is one of the biggest challenges faced by modern machine learning practitioners. Distributing machine learning systems allow developers to handle extremely large datasets across multiple clusters, take advantage of automation tools, and benefit from hardware accelerations. In this book, Yuan Tang shares patterns, techniques, and experience gained from years spent building and managing cutting-edge distributed machine learning infrastructure.

## About the book

*Distributed Machine Learning Patterns* is filled with practical patterns for running machine learning systems on distributed Kubernetes clusters in the cloud. Each pattern is designed to help solve common challenges faced when building distributed machine learning systems, including supporting distributed model training, handling unexpected failures, and dynamic model serving traffic. Real-world scenarios provide clear examples of how to apply each pattern, alongside the potential trade-offs for each approach. Once you’ve mastered these cutting-edge techniques, you’ll put them all into practice and finish up by building a comprehensive distributed machine learning system.

## About the reader

For data analysts, data scientists, and software engineers familiar with the basics of machine learning algorithms and running machine learning in production. Readers should be familiar with the basics of Bash, Python, and Docker.

## About the author

Yuan is a principal software engineer at [Red Hat](https://www.redhat.com/), working on [OpenShift AI](https://www.redhat.com/en/technologies/cloud-computing/openshift/openshift-ai). Previously, he has led AI infrastructure and platform teams at various companies. He holds leadership positions in open source projects, including [Argo](https://argoproj.github.io/), [Kubeflow](https://github.com/kubeflow), and [Kubernetes](https://github.com/kubernetes/community/tree/master/wg-serving). He's also a maintainer and author of many popular [open source projects](https://github.com/sponsors/terrytangyuan). In addition, Yuan [authored](https://terrytangyuan.github.io/cv#publications) three technical books and published numerous impactful papers. He's a regular [conference speaker](https://terrytangyuan.github.io/cv#talks), technical advisor, leader, and mentor at [various organizations](https://terrytangyuan.github.io/cv#services). 

## Supporting Quotes

*"This is a wonderful book for those wanting to understand how to be more effective with Machine Learning at scale, explained clearly and from first principles!"*

**-- Laurence Moroney, AI Developer Relations Lead at Google**

*"This book is an exceptionally timely and comprehensive guide to developing, running, and managing machine learning systems in a distributed environment. It covers essential topics such as data partitioning, ingestion, model training, serving, and workflow management. What truly sets this book apart is its discussion of these topics from a pattern perspective, accompanied by real-world examples and widely adopted systems like Kubernetes, Kubeflow, and Argo. I highly recommend it!"*

**-- Yuan Chen, Principal Software Engineer at Apple**


*"This book provides a high-level understanding of patterns with practical code examples needed for all MLOps engineering tasks. This is a must-read for anyone in the field."*

**-- Brian Ray, Global Head of Data Science and Artificial Intelligence at Eviden**


*"This book weaves together concepts from distributed systems, machine learning, and site reliability engineering in a way that’s approachable for beginners and that’ll excite and inspire experienced practitioners. As soon as I finished reading, I was ready to start building."*

**-- James Lamb, Staff Data Engineer at SpotHero**


*"Whatever your role is in the data ecosystem (scientist, analyst, or engineer), if you are looking to take your knowledge and skills to the next level, then this book is for you. This book is an amazing guide to the concepts and state-of-the-art when it comes to designing resilient and scalable, ML systems for both training and serving models. Regardless of what platform you may be working with, this book teaches you the patterns you should be familiar with when trying to scale out your systems."*

**-- Ryan Russon, Senior Manager of Model Training at Capital One**


*"AI is the new electricity, and distributed systems is the new power grid. Whether you are a research scientist, engineer, or product developer, you will find the best practices and recipes in this book to scale up your greatest endeavors."*

**-- Linxi "Jim" Fan, Senior AI Research Scientist at NVIDIA, Stanford PhD**

*"This book discusses various architectural approaches to tackle common data science problems such as scaling machine learning processes and building robust workflows and pipelines. It serves as an excellent introduction to the world of MLOps for data scientists and ML engineers who want to enhance their knowledge in this field."*

**-- Rami Krispin, Senior Data Science and Engineering Manager**

*"无论是新手还是专家，这本书都将引领你构建强大的机器学习系统，进而掌握分布式机器学习、自动化工具和大规模工作负载管理的要点。让你的机器学习之旅更上一层楼！"*

**-- 高策，TensorChord CEO，Kubeflow 社区维护者**

*"这是一本关于在分布式环境下开发、运行和管理机器学习系统的全面手册。作者详尽地阐述了从数据分区、采集、模型训练到服务和工作流程管理等一系列关键主题。通过使用现实世界中的案例，本书深入浅出地讲解了人工智能与机器学习领域用到的核心软件、系统和平台，涵盖了 PyTorch、TensorFlow、Kubeflow、Argo Workflows 和 Kubernetes 等。无论是算法工程师、系统工程师还是架构师，都能从中获得开发和维护分布式机器学习系统所需的全方位知识。我将此书极力推荐给所有对机器学习有着浓厚兴趣和实践需求的专业人士！"*

**-- 陈源，NVIDIA 主任工程师**

*"很高兴看到这本书能在国内出版。随着 ChatGPT 等工具和技术的爆火，AI技术迎来了又一波爆发期。与此同时，Kubernetes 等云原生技术作为基础设施的事实标准也再次在本轮技术热潮中成为首选项。这本书介绍了很多结合云原生和分布式技术进行机器学习的方法和案例，推荐对这方面感兴趣的读者进行阅读。"*

**-- 张晋涛，Kong Inc., Microsoft MVP, CNCF Ambassador**
