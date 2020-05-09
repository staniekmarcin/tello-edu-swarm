# tello-edu-swarm

Package of scripts to create Tello EDU Swarm

## Configuration of Tello EDU

Connect PC to Tello EDU and run config_tello_swarm.py

```
python config_tello_swarm.py
```

Repeat this for every Tello EDU you want to use. This script will put Tello EDU into command mode and force given Access Point connection after reboot.

## Get Tello IP

If you know how to check Tello EDU IP then feel free to skip this instruction.
Otherwise connect PC to Access Point and run network_scan.py to scan network for online hosts.

```
python network_scan.py
```

## Running Swarm

When you got your Tellos ready and identified, modify commands_tello_swarm.txt file.
Use commands from https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf
e.g

```
battery?
takeoff
flip r
land
```

Run one of tello_swarm.py scripts.

```
python tello_swarm_2.py
```

Number in file name indicates number of Tello EDU used in Swarm.
