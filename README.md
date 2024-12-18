# Rocket-League-EV3-LEGO
control rocket league bot with lego EV3

# Instructions
**Installing Python for EV3 and Rocket League**  
1) Install the ev3dev2 firmware to the EV3 Brick [Tutorial](https://www.ev3dev.org/docs/getting-started/)
2) Install the `python-ev3dev2` library to your computer (> pip install python-ev3dev2).
3) Install the `rlbot` library to your computer (> pip install rlbot).

**Installing RLBOT and create a bot**  
4) Install RL Bot console [here](https://rlbot.org/)
5) Install a bot template [here](https://github.com/ddthj/GoslingUtils)
6) Replace the `ExampleBot.py` inside the GoslingUtils-Master with my `ExampleBot.py`

**Downloading the code to the EV3 Brick**  
7) Connect EV3 Brick to the same wifi network as your computer.
8) Download my `ev3.py` and open in to download it to the ev3 brick.

**Set up the connection between pc and ev3**  
9) In `ev3.py` and `ExampleBot.py` change HOST to your local ipv4 adress (cmd > ipconfig).
10) In `ev3.py` and `ExampleBot.py` change PORT to any open communication port (65432).
11) In `GoslingUtils > ExampleBot.cfg` edit the name of the bot to your custom name.

**Load the bot**  
12) After you replaced the Example bots code and renamed it, open RLBotGUI.
13) Click on **Bots > add > Load Folder** and select the `GoslingUtils-Master` folder.
14) If the bot is added succesfuly you should see your bots name in the bot list.

**Starting a game**  
15) Select your bot and click on **Launch Rocket League and Start Match**.
16) Make sure your EV3 has wifi connection and run the `ev3.py` on your EV3 brick.
17) When your console get spammed with data or your EV3 display shows 'Connected' you are good to go!

**Stopping**  
18) The order doesnt matter, but id turn off the program on the EV3 first, then shut down RLBotGUI.

# Help
If your EV3 brick doesn't connect to your pc:  
- You might have entered the wrong PORT or HOST (check port and host in `ev3.py` and `ExampleBot.py`)  
- Your sensors might not be set up correct (check inputs and sensors in `ev3.py`)  
- Your EV3 or computer might not have a stable internet connection.  
If you don't receive any in the RLBotGUI at all, you should run `ev3.py` on your computer with the EV3 connected so the errors will show up on the pc so you can fix them.

# Caveats
- cpufreq overclocking is **NOT** required.
- USB can be used instead of WIFI but it requires changes in the code.