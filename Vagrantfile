# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"
$enable_serial_logging=false

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider :virtualbox do |vb|
    vb.memory = 1024
    vb.cpus = 1
  end

  config.vm.synced_folder ".", "/home/vagrant/site"

  config.vm.network "forwarded_port", guest: 80, host: 8000
  config.vm.network "forwarded_port", guest: 8001, host: 8888

  config.vm.provision :shell, :path =>  File.expand_path("../ansible/bootstrap.sh", __FILE__)

end
