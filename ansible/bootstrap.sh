#!/usr/bin/env bash

apt-add-repository -y ppa:ansible/ansible
apt-get update
apt-get -y install ansible software-properties-common

ansible-galaxy install -r /home/vagrant/site/ansible/requirements.yml
sudo -H -u vagrant bash -c "ansible-playbook -i /home/vagrant/site/ansible/inventory/vagrant /home/vagrant/site/ansible/vagrant.yml --connection=local"
