# Howto create a headless RaspberryPi
- get the IP address of the server
- change the serever IP address in the sendAddress.py script
- Flash a Raspbian image on the memroy card
- add a ssh empty file in the boot partition
- add the wpa_supplicant.conf file in the boot partition
- change the hostname in the file etc/hostname in the rootfs partition
- copy the sendAddress.py script in the home/pi/ directory
- make it executable
- add the execution of the script in the .bashrc file (./sendAddress.py &)

Put the memory card in the raspberryPi
change the server IP address in the server script
Start the server socket_threaded_server.py
Start the raspberryPi
The IP address of the raspberryPi is displayed on the server
You can connect by ssh on it.
