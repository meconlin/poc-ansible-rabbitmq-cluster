POC Ansible install of HA RabbitMQ Cluster
=========

Installs rabbitmq https://www.rabbitmq.com/ (Configurable...HA and Clustering ready).   

Extends an existing role to:
- installs and configures clustered RabbitMQ on N nodes in your inventory file
- will apply HA policy  ```ha-all`` to all queues created
- sync mode is automatic
- cluster_partition_handling is set to pause_minority

It can install either into a Vagrant or AWS.  
An example python celery application exists in /exampleapps to experiment with.

Playing with Vagrant
-------

Spin up a 3 node HA Cluster for testing...  
Install Ansible role on your host:  

Place ansible role into your preferred global roles directory
```
$git clone https://github.com/mrlesmithjr/ansible-rabbitmq.git
```

Place sym links inside the roles dir of this project   
```
$mkdir /roles
$cd roles
$ln -s /Users/mark/workspace/myglobalroles/ansible-rabbitmq ansible-rabbitmq
```


Now spin up your environment...  
````
vagrant up
````
Re-run vagrant playbook ```playbook.yml```...  
```
vagrant provision
```
OR
```
ansible-playbook playbook.yml -i vagrant-inventory.ini --private-key=/Users/mark/.ssh/vagrant -v
```

When you are done testing, tear it all down...  
````
./cleanup.sh
````


Playing with AWS
---
You will have to launch nodes you can access with your key and that share a security group that allows them to see each other

TODO:
- mark to define AWS security group rules for RabbitMQ clustering

Run the AWS playbook
```
ansible-playbook -i aws-stage-inventory.ini --private-key=/Users/mark/.ssh/gg_rsa --user=mconlin aws-stage-main.yml
```
