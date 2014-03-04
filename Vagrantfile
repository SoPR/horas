# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Define box
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  # Setup synced folders for local development
  config.vm.synced_folder "./", "/home/vagrant/horas"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 8000 on the guest machine.
  config.vm.network :forwarded_port, guest: 8000, host: 8000

  # Shell provisioning
  config.vm.provision "shell", path: "https://raw.github.com/SoPR/horas-install/master/install-dev-tools.sh"
  config.vm.provision "shell", path: "https://raw.github.com/SoPR/horas-install/master/install-datastores.sh"
  config.vm.provision "shell", path: "https://raw.github.com/SoPR/horas-install/master/configure-git.sh"
  config.vm.provision "shell", path: "https://raw.github.com/SoPR/horas-install/master/profile-settings.sh"
  config.vm.provision "shell", path: "https://raw.github.com/SoPR/horas-install/master/install-django-requirements.sh"

end
