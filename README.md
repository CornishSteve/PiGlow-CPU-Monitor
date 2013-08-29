PiGlow-CPU-Monitor
==================

Python script to display cpu usage of RaspberryPi via Pimoroni's PiGlow add on board


### Overview

This script illumiates each colour 'ring' of LED's on the PiGlow board in the following cycle:

White	(Inner Ring)
Blue
Green
Yellow
Orange
Red		(Outter Ring)

The delay between cycling colours and colour intensity are both governed by the current CPU load %.  When idle the colours are dim and change every 1.2 seconds, however when the CPU is under maxium load the colours are at their brightest and change every 0.1 seconds.


### Dependencies

This script is dependant on the following packages:

SMBus - is required to communicate over i2c with the PiGlow board
psutil - is required to get current CPU usage

These can be instaled by executing the following command:

sudo apt-get update
sudo apt-get install python-smbus python-psutil -y

You'll also need to enable the i2c driver by editing the '/etc/modules' file

sudo nano /etc/modules

And ensure the following lines are in the file:

i2c-dev
i2c-bcm2708

And you'll need to edit the '/etc/modprobe.d/raspi-blacklist.conf' file

sudo nano /etc/modprobe.d/raspi-blacklist.conf

You must comment out the blacklisted items by adding a '#' to the front of the lines:

#blacklist spi-bcm2708
#blacklist i2c-bcm2708

You'll need to reboot the Pi for the changes to take effect:

sudo reboot


### Credits

Jonathan Williamson (@pimoroni) - Thanks for creating the PiGlow board and all the assistance with writing the script

Jason Barnett (@Boeeerb) - Thanks for creating the piglow.py python module - without it this script just wouldnt work.
