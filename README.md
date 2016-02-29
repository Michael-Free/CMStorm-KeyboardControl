# CMStorm-KeyboardControl
A simple application to control the Cooler Master CM Storm Devastator LEDs via the System Tray in Ubuntu Linux.
<p align="center">
![alt tag](https://raw.githubusercontent.com/Michael-Free/CMStorm-KeyboardControl/master/CMStormDevastator.png)
</p>
# About
In late 2015 I picked up the CM Storm Devastator Gaming Keyboard/Mouse Combo that was on sale.  It's a great keyboard, however the Scroll Lock button, which also turns on the the LED backlit keys, doesn't work in Ubuntu 14.04 LTS (which I am currently using).  

After doing some searching I found some solutions - but most seemed to be a bit of a comprimise, such as remapping the Scroll Lock key permanently. Some solutions would even turn the numberpad on the far-right in to a d-pad for the mouse on screen.  Later I found a simple command that would fix that problem, but it still felt 'cumbersome' to always have to log into a terminal and type on a command just to turn the LEDs on and off.

My frustration eventually resulted in me creating this simple helper app that allows a user to control their keyboard lighting in the Ubuntu Unity system tray (and other GTK-based environments). 

# Requirements
- Cooler Master CMStorm Devastator Keyboard
- Python 3.4+
- Ubuntu Linux 14.04 LTS
- Unity, Gnome, or other GTK-based Desktop Environment.

# Reference 
- http://www.tomshardware.com/answers/id-2611456/turn-storm-devastator-leds.html
- http://community.coolermaster.com/index.php/topic/11526-is-cm-storm-devastator-led-gaming-keyboard-compatible-with-linux/
- https://answers.launchpad.net/ubuntu/+source/linux/+question/241299
- http://blog.rumyhub.com/post/2015/01/31/ubuntu-fixing-cm-storm-devastator-keyboard-backlight-button.aspx
- http://ubuntuforums.org/showthread.php?t=2208222
