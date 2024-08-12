# Attenuator-With-RPI
## What Is This?
This is a program to control an attenuator (ATT-6000 protocol) through serial port using a Raspberry Pi and Python.

## Connections
<img alt="This is the attenuator that will be used" src="/imgs/top_view_att.jpg" width="500" height="250">
<img alt="Raspberry Pi 4 pinout (https://nerdytechy.com/raspberry-pi-4-gpio-pinout/)" src="/rpi4_pinout.jpg" width="500" height="300">
<img alt="Side view of connections to attenuator" src="/imgs/side_view_att_connections.jpg" width="500" height="300">
<img alt="Top view of connections to attenuator" src="/imgs/top_view_att_connections.png" width="500" height="300">
<img alt="Top view of connections to Raspberry Pi" src="/imgs/top_view_rpi_connections.png" width="500" height="300">
<img alt="Block Diagram of all connections" src="/imgs/block_diagram_connections.png" width="500" height="300">

## UI
<img alt="Here is an example of using this program" src="/imgs/ui.png" width="500" height="300">

## Common Issues

 1. > SerialException: could not open port /dev/ttyS0: [Errno 13] Permission denied: '/dev/ttyS0'
    
    To fix this error, either run the python file with `sudo` ex. (`sudo
    python3 Main.py`) or run `sudo chmod 666 /dev/ttyS0` in the terminal.
    
 2. Remember to connect Tx (RPI) to Rx (Att), and Rx (RPI) to Tx (Att). Also, set the baudrate to 115200.
 3. Enable Serial Port in raspi-config by going to the terminal and type `sudo raspi-config`, then select `3 Interface Options`, `I6 Serial Port`, select `No` to "Login Shell accessible over serial," select `Yes` to "Serial port hardware to be enabled," select `Ok`, then `Finish`, and press `Yes` to "reboot now." Or press the Raspberry Pi Logo, go to `Preferences`, then press `Raspberry Pi Configuration`, go to tab `Interfaces`,  and select `Serial Port`.
  

## Requirements
- Raspberry Pi 
- Attenuator (ATT-6000 protocol)
- Python
- PyQt5
- Pyserial

How to install Python 3.9 and pip. (Linux)
```sh
sudo apt-get install python3.9 python3-pip
```

How to install PyQt5, and Pyserial with pip. (Linux)
```sh
pip install PyQt5
pip install pyserial
```

## Attenuator Description
>Serial communication protocol analysis
The overall structure of the CNC attenuator ATT-6000 protocol adopts the command line mode, and the communication baud rate is 115200bps. 
The PC sends out the command, the machine parses and executes it, and then returns the result to the PC. 
The command is limited to lowercase letters a~z and the number 0 ~9, 
the end symbol of each command is a newline character (hexadecimal representation is "0x0a" or'/n')
Communication commands include three types of commands: w command
wv0 command: set the output attenuation
The format is: wv0xxxx + 0x0a, a total of 8 bytes;
Where "xxxx" is the attenuation value represented by 4 numbers, such as:
wv01150\n: indicates that the write attenuation is: 11.5DB (the maximum attenuation is: 0-3175, the step is 25)
Converted into hexadecimal: that is 0X77 0X76 0X30 0X31 0X31 0X35 0X30 0X0a
0X77 0X76 0X30 0X31 0X31 0X35 0X30 0X0a
w          v         0        1        1        5        0       \n

## Clone This Repository
Copy paste this into the terminal.
```sh
git clone https://github.com/Alex-Czerniewski/Attenuator-With-RPI/
```
