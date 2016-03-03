# CMStorm LED Control Tool
A simple application to control the Cooler Master CM Storm Devastator Keyboard LEDs via the System Tray in Ubuntu Linux.
<p align="center">
<img src = "https://raw.githubusercontent.com/Michael-Free/CMStorm-KeyboardControl/master/CMStormDevastator.png">
</p>
# About
In late 2015 I picked up the CM Storm Devastator Gaming Keyboard/Mouse Combo that was on sale.  It's a great keyboard, however the Scroll Lock button, which also turns on the the LED backlit keys, doesn't work in Ubuntu 14.04 LTS (which I am currently using).  

After doing some searching I found some solutions - but most seemed to be a bit of a comprimise, such as remapping the Scroll Lock key permanently. Some solutions would even turn the numberpad on the far-right in to a d-pad for the mouse on screen.  Later I found a simple command that would fix that problem, but it still felt 'cumbersome' to always have to log into a terminal and type on a command just to turn the LEDs on and off.

My frustration eventually resulted in me creating this simple helper app that allows a user to control their keyboard lighting in the Ubuntu Unity system tray (and other GTK-based environments). 

# Screenshots
<p align="center">
<img src = "https://raw.githubusercontent.com/Michael-Free/CMStorm-KeyboardControl/master/Screenshot.png">
</p>
# Requirements
- Cooler Master CMStorm Devastator Keyboard
- Python 3.4+
- Ubuntu Linux 14.04 LTS
- Unity, Gnome, or other GTK-based Desktop Environment.

# Installation
## Building recommended requirements 

    $ sudo apt-get install python3
    $ sudo apt-get install python3-pip

Please note that most of these dependencies are already met with a typical python3+ env... but just in case!

    $ sudo pip install gtk
    $ sudo pip install gi
    $ sudo pip install subprocess

## Method 1 - Git
#### Install/Download

    $ git clone https://github.com/Michael-Free/CMStorm-KeyboardControl.git
    $ cd CMStorm-KeyboardControl
    $ chmod +x cmstorm-led-ctrl.py

#### Test/Call CMStorm-KeyboardControl from Terminal

    $ python3 cmstorm-led-ctrl.py 

If all goes well you should see an icon that looks like an LED in your system tray. Click it and Toggle the On/Off Options and Select "Quit."

<p align="center">
<img src = "https://raw.githubusercontent.com/Michael-Free/CMStorm-KeyboardControl/master/Screenshot.png">
</p>

## Method 2 - Zip
#### Install/Download
Select the "Download ZIP" button at the top right of this page (http://cmstorm.michaelfree.net/) and Save the Zip file to the fold of your choice.  Once it is downloaded unzip the file:

    $ unzip CMStorm-KeyboardControl-master.zip
    $ cd CMStorm-KeyboardControl-master
    $ chmod +x cmstorm-led-ctrl.py

#### Test/Call CMStorm-KeyboardControl from Terminal

    $ python3 cmstorm-led-ctrl.py 

If all goes well you should see an icon that looks like an LED in your system tray. Click it and Toggle the On/Off Options and Select "Quit."

<p align="center">
<img src = "https://raw.githubusercontent.com/Michael-Free/CMStorm-KeyboardControl/master/Screenshot.png">
</p>

# Use Case
Manually running this script is still a comprimise, but the idea is to run this script at the time of login so you dont have to think about this ever again. 

From a Terminal Window:

    $ gnome-session-properties

A window like this should appear:

<img src="https://raw.githubusercontent.com/Michael-Free/CMStorm-KeyboardControl/master/gnome-session-00.png">

Click add:

<img src="">

# License
<p align="center">
<img src="http://www.gnu.org/graphics/heckert_gnu.small.png"><br>
The license to this software is governed directly by the <a href="http://www.gnu.org/licenses/gpl-3.0.en.html">GPL v3.0 License</a>.
</p>
# Reference 
- http://community.coolermaster.com/index.php/topic/11526-is-cm-storm-devastator-led-gaming-keyboard-compatible-with-linux/
- https://answers.launchpad.net/ubuntu/+source/linux/+question/241299
- http://blog.rumyhub.com/post/2015/01/31/ubuntu-fixing-cm-storm-devastator-keyboard-backlight-button.aspx
- http://ubuntuforums.org/showthread.php?t=2208222
- http://www.gnu.org/licenses/gpl-3.0.en.html
- https://pip.pypa.io/en/stable/installing/


