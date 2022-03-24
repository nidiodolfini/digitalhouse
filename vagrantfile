Vagrant.configure("2") do |config|
  config.vm.define "server" do |server|
  config.vm.box = "ubuntu/focal64"
  config.vm.boot_timeout = 900
  config.vm.synced_folder ".", "/vagrant", disabled: true
  server.vm.provider "virtualbox" do |vb|
      # Display the VirtualBox GUI when booting the machine
      vb.gui = false
        # Customize the amount of memory and cpus on the VM:
      vb.memory = 2048
      vb.cpus = 2
    end
  server.vm.hostname = "server"
  server.vm.network "public_network"
end
