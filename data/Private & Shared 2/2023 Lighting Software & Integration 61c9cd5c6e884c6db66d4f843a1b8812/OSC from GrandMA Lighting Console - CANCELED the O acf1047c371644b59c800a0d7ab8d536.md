# OSC from GrandMA Lighting Console - CANCELED the OSC idea

# Overview

- Send OSC messages from GrandMA to Chromatik
- Add an ethernet dongle to Lighting-1 so it can participate in the same network as GrandMA
    - **Make sure subnets do not conflict

# GrandMA SETUP

Documentation for configuring OSC output:

[OSC (Open Sound Control) - grandMA3 User Manual - Help pages of MA Lighting International GmbH](https://help2.malighting.com/Page/grandMA3/remote_inputs_osc/en/1.9)

# Data to send from GrandMA to LX

### Color

OSC Messages to send to LX (Yes the primary color is 3 and secondary is 4!)

| **Item** | **OSC Address** | **Data Type** | **Value Range** |
| --- | --- | --- | --- |
| Primary Color Hue | /lx/palette/swatch/color/3/primary/hue | float | 0-1 |
| Primary Color Saturation | /lx/palette/swatch/color/3/primary/saturation | float | 0-1 |
| Primary Color Brightness | /lx/palette/swatch/color/3/primary/brightness | float | 0-1 |
| Secondary Color Hue | /lx/palette/swatch/color/4/primary/hue | float | 0-1 |
| Secondary Color Saturation | /lx/palette/swatch/color/4/primary/saturation | float | 0-1 |
| Secondary Color Brightness | /lx/palette/swatch/color/4/primary/brightness | float | 0-1 |

### Strobes

- Could add an effect to the master channel and trigger with OSC

### Speed

- Justin’s thoughts: define a single place to receive the OSC speed message (in normalized range 0-1).  Then figure out ourselves how to distribute that to all the patterns.  For example we could set up a Macro Knobs as the input point:
    - Add a Knobs modulator:
        
        ![Untitled](OSC%20from%20GrandMA%20Lighting%20Console%20-%20CANCELED%20the%20O%20acf1047c371644b59c800a0d7ab8d536/Untitled.png)
        
    - Which initially looks like this:
        
        ![Untitled](OSC%20from%20GrandMA%20Lighting%20Console%20-%20CANCELED%20the%20O%20acf1047c371644b59c800a0d7ab8d536/Untitled%201.png)
        
    - Rename it to something relevant:
        
        ![Untitled](OSC%20from%20GrandMA%20Lighting%20Console%20-%20CANCELED%20the%20O%20acf1047c371644b59c800a0d7ab8d536/Untitled%202.png)
        
    - Then hover over knob1 to see the OSC address at the bottom of the screen:
        
        ![Untitled](OSC%20from%20GrandMA%20Lighting%20Console%20-%20CANCELED%20the%20O%20acf1047c371644b59c800a0d7ab8d536/Untitled%203.png)
        
    - …Then we map K1 to something relevant on our side, such as speed knobs on patterns