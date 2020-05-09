# tello-edu-swarm

Package of scripts to create Tello Edu Swarm

## Configuration of Tello EDU

Connect your PC to Tello EDU and run config_tello_swarm.py

```
python config_tello_swarm.py
```

Repeat this for every Tello EDU you want to use in your Swarm. This script will put you Tello EDU into command mode and force given Access Point connection after reboot.

## Get Tello IP

If you know how to check Tello IP then feel free to skip this instruction.
Otherwise connect you PC to Access Point and run network_scan.py to scan your network for online hosts.

```
python network_scan.py
```

## Running Swarm

When you got your Tellos ready and identified you can modify commands_tello_swarm.txt file.
Use commands from https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf
Run one of tello_swarm.py scripts.

```
python tello_swarm_2.py
```

Number in file name indicates number of Tell EDU you want to use in your Swarm.
