# Modifying the Ultra96 board to meausure energy usage 

By default, the Ultra96v2 PYNQ image (v2.5) does not contain the necessary configuration to retrieve current/power readings from the power regulators.  After you image your SD card, you will need to make the following modifications to the system files on the SD card.

The imaged SD card should contain two partitions (possibly /dev/sda1 and /dev/sda2 on Linux).

On the partition containing an ''/etc'' folder, replace:
  * ''/etc/sensors.d/ultra96.conf'' with the ''ultra96.conf'' file provided in this repo folder.
 
On the partition containing ''BOOT.bin'', replace:
  * ''BOOT.bin'' with the ''BOOT.bin'' file provided in this repo folder.
  * ''image.ub'' with the ''image.ub'' file provided in this repo folder.

