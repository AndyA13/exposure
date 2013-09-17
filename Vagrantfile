Vagrant.configure("2") do |config|

  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.network :forwarded_port, host: 8000, guest: 8000

  config.vm.synced_folder "salt/roots/", "/srv/"

  config.vm.network :private_network, ip: "10.10.10.11"

  config.vm.provision :salt do |salt|

    salt.minion_config = "salt/minion"
    salt.run_highstate = true

    salt.verbose = true
    salt.install_type = :daily

  end

end