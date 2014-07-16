Simple Raspberry Pi GPIO Audio Player
========================

Add `@reboot sleep 10 && /home/pi/autorun && sleep 2 && echo -n p > /tmp/cmd &` to the end of `sudo crontab -e`

Copy "player.py" and "autorun" to the pi's home directory(/home/pi/).