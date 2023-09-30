# Python-Secure-Linux-Startup
Changes the MAC address and device name 

## How to automate
Step 1: Move the Script to a Permanent Location
First, move your Python script to a permanent location where it won't get accidentally deleted or moved. A common location is /usr/local/bin/. You may need root (sudo) permissions to do this:


sudo mv your_script.py /usr/local/bin/
Step 2: Create a Systemd Service

Create a Systemd service unit file to define how and when your script should run at startup:


sudo nano /etc/systemd/system/change_mac_and_device.service
In the text editor, add the following content:

[Unit]
Description=Change MAC Address and Device Name at Startup

[Service]
ExecStart=/usr/local/bin/your_script.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target


Replace /usr/local/bin/your_script.py with the actual path to your Python script.
Set the User to root to ensure it runs with the necessary privileges.
The Restart directive ensures that the script is restarted if it exits for any reason.
Save the file and exit the text editor.

Step 3: Enable and Start the Service

Enable the service to ensure it runs at startup and start it:


sudo systemctl enable change_mac_and_device.service
sudo systemctl start change_mac_and_device.service

Step 4: Verify the Service Status

You can check the status of the service to ensure it's running:


sudo systemctl status change_mac_and_device.service

If everything is set up correctly, your Python script will run at system startup, changing the MAC address and device name as configured.

