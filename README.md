# python-cisco
Cisco Network Automation - Software Defined Network - System Automation


INSTALLATION (Windows/Linux)

Installation

Just install the required modules/libraries to your python project directory if you do not have them

paramiko

For example:

pip install paramiko

Open ipler.txt and replace ip addresses with your network device ipaddresses. Open cisco_backup.py and replace the required information with yours. (ssh username, ssh password, cisco enable password, ftp server ip address, ftp account username and password)

Then, execute cisco_backup.py

If you like you can schedule that script when you would like to backup your devices config.

Also, you can use that script for all devices/servers/clients that you can connect via SSH.

That's all !
