#!/bin/bash
if [ -z "$1" ]
then
	printf "No arguments supplied.\nYou need to specify the path to the sd card. you can run the command 'sudo fdisk -l | grep /dev/' to find the path, it's the one with ~16 GiB capacity (e.g. ./restore_image /dev/sda)\n"
	exit 1
fi

mkdir sd

CONF_FILE="sd/etc/sensors.d/ultra96.conf"
BOOT_FILE="sd/BOOT.BIN"

sudo mount $12 sd

if [ -f "$CONF_FILE" ]
then
	sudo cp ultra96.conf sd/etc/sensors.d
	sleep 5
	sudo umount sd

elif [ -f "$BOOT_FILE" ]
then
	sudo cp BOOT.BIN sd
	sudo cp image.ub sd
	sleep 5
	sudo umount sd

else
	echo "could not find sd/etc/sensors.d/ultra96.conf or sd/BOOT.BIN in $12, make sure the sd card is flashed with the image correctly."
	sleep 5
	sudo umount sd

	exit 1
fi

sleep 5
sudo mount $11 sd

if [ -f "$CONF_FILE" ]
then
	sudo cp ultra96.conf sd/etc/sensors.d
	sleep 5
	sudo umount sd

elif [ -f "$BOOT_FILE" ]
then
	sudo cp BOOT.BIN sd
	sudo cp image.ub sd
	sleep 5
	sudo umount sd

else
	echo "coult not find sd/etc/sensors.d/ultra96.conf or sd/BOOT.BIN in $11, make sure the sd card is flashed with the image correctl."
	sleep 5
	sudo umount sd

	exit 1
fi

rm -rf sd

