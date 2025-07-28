# Networking and Front of House Setup

<aside>
🆘 Need help? **Network**: Ask Chris K, Eric Wu, Jeff, Sina, Justin Belcher, or Will Drevo
**FoH**: Ask David C, Misha, Sina, Derek, Jeff, Look, or Will Drevo

</aside>

<aside>
🧹 **Staying Organized**
It’s critical that if you make changes, you keep the various documents up-to-date. Communicate with the current TE Network lead - That’s @cnk  (**Chris Kleinknecht)** for 2025.

</aside>

[Network and FoH TODOs](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Network%20and%20FoH%20TODOs%20cec5af5464804e9da6ad5b392e710d26.csv)

## Overview
Purpose

Our networks are used for:

1. **LED control**. Over 110 LED controllers controlling >85,000 LEDs receiving pixel information from a Mac Studio running the Chromatik pattern engine.
2. **Laser control**. 12 projectors controlled by Pangolin Beyond running on an Intel NUC.
3. **~~Projection mapping**. A Mac Studio, sometimes ingesting live webcam data, driving 4 short throw projectors in the Ice Lounge.~~
4. **Audio control**. Remote management of Allen & Heath headless digital rack mixer and Dante data for several X8 amps.
5. **Pioneer DJ Link**. Up to 5 CDJ-3000s and a V10 mixer, connected to each other as well as ShowKontrol to feed tempo, beat, phrase, and track waveform preview data to other systems.
6. **Front-Of-House**. A dedicated high speed point-to-point disk link that extends the on-car LAN to the control booth where the LED VJ, Laser operator, and Sound Engineer all control their systems over remote desktop connections.
7. **Crew WiFi**. Ubiquity APs around the car for crew laptops to access the systems above flexibly around the car, and to share our upstream internet (Starlink) in remote locations.

### Physical Layout

The majority of the network concerns are coexisting on one LAN, with the following exceptions:

1. DJ Link devices live on an isolated [VLAN](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4.md). The ShowKontrol computer has two NICs, one on the LAN and one on the DJ Link VLAN.
2. Audio Control is on a separate network due to that vendor’s adorable habits, timelines, and peculiarities. He uses it some years. 
3. Upstream internet (venue WiFi, Starlink, Personal HotSpot or wired upstream) is considered WAN.

There are [45 wired ports distributed in 5 weatherproof patch panels](https://docs.google.com/spreadsheets/d/14Lj-hovCMH-IyVQV6PKU_ADQEh9bYlXcRrHoYI6OkcE/edit?gid=1391190856#gid=1391190856) located around the car’s perimeter. These are used for connecting to LED controllers, lasers, WiFi APs, the P2P wireless FoH link, and DJ equipment (❗must be only plugged in to a DJ VLAN port).

The ports around the car are connected to a 48-port enterprise switch mounted vertically against a wall in the server closet. The server closet is adjacent to the “k-hole” elevated crawlspace and has filtered air conditioning. 

Most of our valuable network equipment sits in one removable rack. The rack is removable for convenient R&D/maintenance as well as for avoiding theft, vibration in transit, and extreme weather. For shows, the network rack is placed in the server closet. The enterprise network switch on the server closet wall is then bridged to the identical switch in the removable rack by connecting the four rightmost SFP ports together. This is called a link aggregation group; using multiple ethernet cables provides redundancy and increases bandwidth. This LAG configuration also is configured to preserve VLAN tagging across the two devices. 

### Remote Access

All computers have TailScale VPN installed for [remote desktop access](https://www.notion.so/2023-Lighting-Software-Integration-61c9cd5c6e884c6db66d4f843a1b8812?pvs=21). This is primarily to be used between shows when the rack is removed from the car but powered. In an emergency, it could theoretically be used for remote troubleshooting during a performance if the car has internet access.

During a show, the main computers (lighting-1, showkontrol-3, laser-4) are meant to be controlled from the Front of House via OSX Screen Sharing (or Microsoft Remote Desktop). 

### Product Documentation and Firmware

All manuals and firmware are kept on [a Google Drive](https://drive.google.com/drive/folders/1z8Ywqvw5b2SNnMwsjORi_HgAesaxSp2K) which is local-access (mirrored) to all of the computers.
 

### Redundancy

| Computer and software | Backup system |
| --- | --- |
| `lighting-1` [Chromatik](https://chromatik.co/) | `lighting-2` Chromatik
`lighting-10-FOH`- FOH Chromatik
`mship-led` - Mothership Chromatik - in an emergency, should be plugged into TE LAN and render pixels over the 150’ Cat6 snake |
| `laser-4` Pangolin Beyond | `lighting-2` Parallels (license must be transferred or cached offline before the show) |
| `showkontrol-3` ShowKontrol or BTL | `lighting-2` ShowKontrol or BLT |
| UDM Pro as router and [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) server | None - reconfigure network to use MotherShip’s UDM Pro and pray.  |
| UDM Pro’s role as the UniFi controller (AP Config, switch adoption) | UniFi mobile app on our phones, or the UniFi App on Lighting-2 |
| 48-port enterprise network Switch | Other network switch running in a collapsed/flatter LAN. Pioneer DJ LINK VLAN may need physical isolation - reconnect DJ LINK LAN with a separate 8-port switch direct to showkontrol-3’s secondary NIC |
| WAN Wifi Client | A spare OpenWRT or DD-WRT device (blue LinkSys) can be swapped in. Unlikely to be critical at BM with our current Starlink-as-primary WAN config. |
| FoH P2P Link | Spare NanoBeam / PowerBeam
White 150’ 4 x Cat6 Snake  |
| [BomeBox](https://www.bome.com/products/bomebox) | Spare BomeBox in bins, also Bome Network can be the USB device hub |

### Startup Automation

- All computers are set up to boot following loss of power, and auto-login to the primary user
- `lighting-1` Starts Chromatik automatically
- `showcontrol-3` has startup scripts to launch ShowKontrol and our Max OSC router
- Lasers never start automatically as a safety measure

## Network Diagram

[https://www.figma.com/board/n8JNRv2LgfDIu3n6dCUoQN/Titanic's-End-%3C-%3E-Mothership-System?node-id=0-1](https://www.figma.com/board/n8JNRv2LgfDIu3n6dCUoQN/Titanic's-End-%3C-%3E-Mothership-System?node-id=0-1)

## Network Device List and Functional Descriptions

The definitive record of **IP address allocation** is kept in the Networking Google Sheet: https://docs.google.com/spreadsheets/d/14Lj-hovCMH-IyVQV6PKU_ADQEh9bYlXcRrHoYI6OkcE/edit?gid=1303362726#gid=1303362726 (because it supports a more robust offline mode than Notion). IP Addresses are assigned by the DHCP Service of the UDM Pro routers (this can assign reserved IPs outside the main DHCP dynamic pool range), or done via manual IP setup for critical devices such as `lighting-1` 

### Network Devices

[Network Devices](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Network%20Devices%20eb21f16f99184518ba0b8d5a2ec8b80b.csv)

[Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%204f37b94aff9d4254878b5712cea7d1f0.csv)

### Show Coordination

A key tenant of our system is that we cannot guarantee a trained VJ is present at all times that DJs are performing. To support this, we have systems to vary the visual show like a more-intelligent screensaver.

The LEDs use a custom developed module for Chromatik we call Auto-VJ. The lasers can use “Virtual LJ”, which is a dumb playlist that advances the pattern every X beats on the current page of cues. Both of these rely on knowing the current tempo (BPM) so they can roughly change things to the music.

Phrases are the sections of a song that do not have major thematic changes within them. In EDM, they’re almost always 32 beats long, and occasionally 16. If a DJ uses Pioneer Rekordbox’s “Phrase Analysis” feature, our show can be much more intelligent since it knowns when to change the lighting to match key moments and the current mood. The common phrase types is can differentiate are UP (buildups, verses), DOWN (breakdowns, bridges), and CHORUS (peak moments). Many times our DJs do not perform phrase analysis, so the key role of a trained VJ is to make major changes happen on phrase changes, especially “the drops”. Showkontrol and Beat Link Trigger are the two options we choose between for each show. They are displayed on the middle monitor, in front of our Lighting Director role (if we are staffing one), directly between the LED Operator and Laser Operator.

The “middlewares” called ShowKontrol and Beat Link Trigger allow us to:

1. See the music waveform previews that are shown to the DJs on the CDJ decks. 
2. Receive BPM changes, beat markers, downbeat (beat 1 of 4) events, and phrase changes from the DJ decks and convert them to OSC messages that can be sent over the network.

OSC messages from Showkontrol or Beat Link Trigger are first routed to [a Max/MSP script](https://github.com/titanicsend/LXStudio-TE/blob/main/te-app/resources/scripts/TE_OSC_Dispatcher.maxpat) running on the same computer,  `showkontrol-3`. This serves as an OSC router and can filter messages before sending them on to Chromatik (LEDs) or Pangolin Beyond (Lasers).

- [ ]  @Justin to add link to any documentation (github? LX Repo? New Repo?  There are still some undocumented details like when to use the other MAx MSP Projects/patches I see there)

### VLANs

### Understanding VLANs

- A VLAN is a set of ports that can all talk to each other in isolation from the other ports on the switch. You can route traffic between VLANs using a router or VLAN config. Technically a VLAN is a broadcast domain, so something like a DHCP server, which responds to broadcast packets requesting an IP address, can only field requests that exist within it’s VLAN.
- A Link Aggregation Group (LAG) is a set of ports that act as a single cable. We LAG the 4 highest numbered ports between our two enterprise 48-port switches.
- VLAN member ports are either tagged or untagged. A configured VLAN can still isolate traffic even if it doesn’t add tags, just by designating only certain physical ports as untagged members or non-members.
    - A VLAN tag is a number (like “200”) that is added to an ethernet frame.
    - Tagging is used to combine many VLANs’ traffic over a single cable (or the LAG), then split it back out to separate VLANs on the other side of that link.
- An untagged port means that traffic that exits that port will have its VLAN tag ripped off
- A tagged port will add the VLAN number to all ethernet frames that leave that port
- A computer’s network interface can be configured in Windows/OSX to add a VLAN tag, but this is uncommon and we don’t use it this way.
- To add a VLAN tag at switch port ingress, you must both:
    1. Define the port to be a member of that VLAN on the switch’s VLAN config admin page,
    2. Set up the Port VLAN ID (PVID) to add the tag
- We do PVIDs and untagged membership, then define the LAG as a trunk that tags traffic between the switches. Non-VLAN traffic is essentially “VLAN 1” and is always untagged. It flows untagged through the LAG alongside tagged VLAN frames.

### Current VLANs

| Tag | Meaning |  |
| --- | --- | --- |
| 1 | The Default VLAN, as if you didn’t define any. “TE LAN” usually refers to this, and is 10.0.0.0/9 (10.0.0.1 - 10.127.255.255, the latter of which is the broadcast IP address).

Most traffic uses this by default, notably:
1. Communication between TE rack computers / Mothership computers, such as remote desktop, OSC, SSH, etc.
2. Computers reaching the internet via Starlink or the rack’s WiFi Client
3. [Chroma.tech](http://Chroma.tech) controller pixel data - our highest bandwidth and traffic backlog risk point |  |
| 2 | **TE Crew**. Configure this only if TE camp member devices may be interfering with our TE LAN show. Assign APs to this VLAN and get them the fuck off and TE LAN stuff (perhaps by changing the WiFi password for SSID “TE LAN”) |  |
| 3 | **Audio**. Configure only if Pascal needs this, to isolate management traffic to the main D-Live audio mixer, Powersoft amp’s Armonia app, or DANTE or AES67 digital audio streams.  |  |
| 5 | **Lasers**. Configure this if the lasers seem to have network issues (Purple status bars at the bottom of Pangolin - see below*). You’ll need to use a second USB Ethernet interface on the laser computer - continue to use the main ethernet port for VLAN 1. |  |
| 200 | **Pioneer DJ-LINK**, in auto-IP (AKA [APIPA](https://en.wikipedia.org/wiki/Link-local_address)) mode (the default way we use them). This is the most critical VLAN to keep isolated; if Pioneer equipment is plugged into a normal VLAN 1 port, this **will** fuck the LEDs. **Always used.** Connect only to a secondary ethernet interface on the Showkontrol / Beat Link Trigger computer and the DJ gear. Clearly label any ethernet cables and ports out on the car used for the VLAN. |  |
| 400 | **Pioneer DJ-LINK**, in DHCP mode (rarely needed). There may be a need to know an exact IP address for each player, done via a DHCP IP reservation to each player’s MAC address. You’ll need to switch the connected ports from VLAN 200 to 400. Also see VLAN 200’s warnings above.  |  |

* Note that red or yellow backgrounds are laser-content related delays, not networking issues. Purple text means a network reliability problem:

![43252641_2192230200852116_5082074749400514560_n.jpg](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/43252641_2192230200852116_5082074749400514560_n.jpg)

### Step-by-Step

1. Access either switch’s admin interface. Logged in to Chrome as titanicsend@gmail.com, find it easily here: Or, to access directly by IP address, always remember [every IP is here](https://docs.google.com/spreadsheets/d/14Lj-hovCMH-IyVQV6PKU_ADQEh9bYlXcRrHoYI6OkcE/edit?gid=1303362726#gid=1303362726) and [every password is here](https://docs.google.com/spreadsheets/d/1JMT-oSenwYVS_fpXtLfjlVQqChUMWMs7pdlXXzdgqD4/edit?gid=0#gid=0).
    
    ![Monosnap lighting-2 2024-08-06 12-34-30.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_lighting-2_2024-08-06_12-34-30.png)
    
2. Review the existing VLAN IDs
    
    ![Monosnap lighting-2 2024-08-06 12-40-26.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_lighting-2_2024-08-06_12-40-26.png)
    
3. Assign physical ports to particular VLANs as either untagged members (U) or not members. For example, here is the membership for the default network, VLAN 1. Compare it to the membership for the isolated Pioneer DJ-LINK, VLAN 200.
    
    ![Monosnap lighting-2 2024-08-06 12-43-48.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_lighting-2_2024-08-06_12-43-48.png)
    
    ![Monosnap lighting-2 2024-08-06 12-47-06.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_lighting-2_2024-08-06_12-47-06.png)
    
4. If a VLAN needs a DHCP server, make sure it’s able to reach the UDM Pro (main router in the TE rack). This means there’s an assigned untagged member port connected to it, and the VLAN ID of the “network” is assigned in the Ubiquity Network app on the router as well.
    
    ![Monosnap lighting-2 2024-08-06 15-19-12.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_lighting-2_2024-08-06_15-19-12.png)
    

## Front of House (FoH)

The Front of House is a booth or table where the LED VJ, Laser VJ, and sound engineer can remotely control the show from a position embedded in the rear of the audience. On many shows this will be from our second art car, Mothership. Other times we’ll be given a desk (like at Coachella or Framework) and we have a traditional touring-rated lighting desk for that. We sometimes invite audience participation from FoH with MIDI controllers.

<aside>
⚠️ Common gotcha: **Train people that the normal state for all computers is WiFi-off, ethernet cable connected.** Someone see’s a WiFi interface turned off (on iPads, laptops, or anything else at FoH) and decides to turn them on, perhaps even correctly joining WiFi “TE LAN”. If the wired ethernet interface on the same machine is also connected, some of our configurations will cause very bad loopbacks spamming the network. We’ve considered disabling the WiFi interfaces on FoH devices, but this makes it very difficult to perform emergency walk-around maintenance in other situations.

</aside>

### There are two modes for connecting FoH ↔ Car (only use one at a time!)

1. **Ethernet cable mode (e.g.: EDC, playa backup)**
    1. The Car’s LAN (any non-VLAN port of the large 48-port switches) is directly connected to the smaller FoH switch via a very long ethernet cable, AKA a snake. 
2. **PTP WiFi bridge mode (e.g.: Burning Man)**
    - We use Ubiquiti AirMAX dishes, one on each side. (one on the car, and one at front of house)
        1. The car has a NanoBeam 5AC (30 deg antenna) mounted high - this is in “AP Mode”, but it is not a router.
        2. The FoH booth uses either the larger PowerBeam 5AC dish (10 deg antenna), or our spare 30 deg NanoBeam (such as on Mothership). It is NOT in AP mode. It’s wired connection is connected to the FoH network switch. 
    - **Additional information to understand and configure this link**
        - The antennae powered by the white PoE injectors that go between the antenna and its wired network.
        - As a bridge, these have no router. They do not perform [NAT](https://en.wikipedia.org/wiki/Network_address_translation) - think of them as a direct replacement for a long ethernet cable, but they happen to have IP addresses and some configuration on each end. They still have a SSID (”TE FoH”) and password for encrypting the link’s traffic, set on the AP side (the car’s dish).
        - Their Point-2-Point wireless link uses the 5 GHz band but is not WiFi-compatible (it’s a proprietary AirMAX RF modulation). With line-of-site, the link is capable of a symmetric 450 Mbps.
        - These also have a separate, normal WiFi radio reserved for management/admin. These radios are only active and making a visible network within the first 10 minutes from the dish being powered up. The SSID’s can be found as “PBE-XXX-XXetc” for the PowerBeam, and “NBE-XX-XXetc” for the NanoBeams. Connect to one from a phone running the UISP app to configure that device. The username is ‘ubnt’ and passwords are in [the password sheet](https://docs.google.com/spreadsheets/d/1JMT-oSenwYVS_fpXtLfjlVQqChUMWMs7pdlXXzdgqD4/edit?gid=0#gid=0).
        - These devices are not part of Ubiquity’s UniFi consumer line. They’re part of the UISP line. To configure them, download the UISP app. Alternately, they can be managed by the cloud-based UISP service.
        - The channel width is set on the AP side of the link (the car’s dish). Generally we’ve found 40MHz channel width to be best — if you’re on a bad width you’ll see the frequency change frequently in the UISP app connected to the P2P client (the FoH side of the link). Try different channels and widths with the UISP mobile app managing the AP side to see what gets you the best capacity. This is easiest with two phones, one connected to the management interface of each dish.
        

## FoH Pre-show Packing Checklist

- **FoH physical Desk setup**
    - [ ]  A MOTHERSHIP, or if Mothership is not coming to the event, the independent rolling FoH standing workstation
    - [ ]  Two folding tables in case Mothership is incapacitated on-playa
        - [ ]  Two folding chairs
        - [ ]  A rain tarp
        - [ ]  You will borrow a Honda EU2200 small mobile generator from camp if this contingency is activated
    - [ ]  Long surge protector/power strip - label as “FoH”
    - [ ]  Two additional normal power strips (label with orange tape “FoH” to prevent them getting “borrowed”)
    - [ ]  A 100’ power extension cord for various emergencies
    
- **Devices**
    - [ ]  Starlink, including power cord and ethernet adapter
    - [ ]  Server Rack. Top to bottom:
        - [ ]  Wifi client bridge
        - [ ]  UDM Pro (router) labeled "TE UDM Pro: 10.0.0.1" TE-LAN (and labeled VLANs)
        - [ ]  48 port switch labeled with "10.0.0.2" on the far left (and labeled VLANs)
        - [ ]  Lighting-2, showkontrol-3 in one unit1U
        - [ ]  Lighting-1, laser-4, generative AI GPU laptop
        - [ ]  Bottom drawer: “Terminal”: KVM, USB Keyboard, USB mouse, flat HDMI display + USB power cable for it
        - [ ]  Verify every device powers up when the single power cord is plugged in (even the hidden KVM! Check it’s small power switch)
    - [ ]  FoH Mac Mini - primary lighting operator’s computer. `lighting-10-FOH`
        - [ ]  Power cord, **large** external monitor with monitor power cord, HDMI cord, wired fancy RGB mechanical keyboard and mouse
        - [ ]  **Large** ShowKontrol External Monitor with monitor power cord, HDMI cord or DisplayPort and appropriate adapter/hub, wired keyboard and mouse
    - [ ]  FoH Laser laptop `laser-14-FOH` - or - Intel Nuc `mship-laser` with all power cords and a wired keyboard/mouse
        - [ ]  ASUS Touch Screen external monitor and power cord - MUST use both HDMI and Thunderbolt connections for touch to work
        - [ ]  Secondary Espresso thin touch 17” display and stand
    - [ ]  *Another* spare external monitor (for `lighting-10-FOH` or `laser-14-FOH` or `mship-led` or `mship-laser`)
    - [ ]  USB-C Thunderbolt → Ethernet + HDMI dongle for any FoH laptops
    - [ ]  (x2) Power adaptors for any laptops. One will get borrowed.
    - [ ]  16-port white ethernet switch labeled "TE-LAN" and "FOH desk" + its power cable
    - [ ]  Double check: total of six monitors: 4 for lighting/LED/director, 1 touch screen for laser, 1 for backup
    
- **If bringing Mothership**
    - [ ]  UDM Pro (router) labeled "MSHIP-LAN" and "10.128.0.1/16" + its power cable
    - [ ]  16-port white ethernet switch labeled "MSHIP-LAN" and "10.128.0.0/16" + power cable
    - [ ]  Mothership Mac Studio - `mship-led`
        - [ ]  Power cord, medium or large external monitor, HDMI cord, wired RGB mechanical keyboard and mouse
    - [ ]  AT LEAST 65 flexible, positionable monitor mounts. Really. For BM’24, we don’t have Mothership in hand with a desk surface as of yet, so we need to bring multiple options. Assume some flat desk space and clearance for a “clamp-able” back desk edge.
    - If beacon control not being done from Chromatik:
        - [ ]  iPad with DMX app LumenAir and active license
    
- **Midi Control**
    - [ ]  (x3) APC40 Mkii (lighting, lasers, and spare)
        - [ ]  Riser Block
    - [ ]  (x3) APC Mini Mkii (Director / Conductor, `mship-laser`, and spare)
    - [ ]  (x3) MidiFighterTwister (Cue, Aux, spare)
        - [ ]  iPads (x2), USB-C power+ethernet dongles, right-angle charging cables, stands
    - [ ]  (x2) NI Traktor Kontrol F1 (laser, spare)
    - [ ]  (x2) Bome Box and spare, as well as two USB-A to micro-USB for backup power to the BomeBox (for if PoE not working)
    - [ ]  8-port powered USB-A hub
    - [ ]  MidiFighter64
    - [ ]  *[PTP wireless bridge mode only - IE, on playa not at Framework/EDC]*
        - Ubiquiti PTP Dishes (3 total - two medium, 1 large), each with a PoE injector

- **Cables**
    - This list may duplicate some items above but is comprehensive
    - AC
        - [ ]  Specific AC cords for Mac Studio, Mac Mini, and Intel Nuc
        - [ ]  AC adaptor for USB hub
        - [ ]  AC → USB-C for iPad ethernet dongles
        - [ ]  (x3) AC → PoE Injectors for dish antennas
        - [ ]  AC for all monitors
        - [ ]  AC for all laptops + spare
    - USB
        - Type-B to type-A
            - [ ]  (2x) Right angle MidiFighterTwister  ←→  powered USB hub
            - [ ]  (2x) APC40  ←→  powered USB hub
            - [ ]  (2x) APCMini  ←→  (1) powered USB hub and (1) `mship-laser`
            - [ ]  Powered USB hub ←→ Bome Box
            - [ ]  MidiFighter64 ←→  powered USB hub
            - [ ]  (2x) spares
    - Ethernet cables
        - [ ]  (3x) FoH Computers ←→ ethernet switch
        - [ ]  Bome box ←→ ethernet switch
        - [ ]  (4x) P2P link dish → PoE → FoH switch at both FoH and TE
        - [ ]  150’ white braided-exterior 4x Cat6 EtherCon tactical loom snake.
            - [ ]  (x2) Cat5 → 4x XLR breakout, male and female - Commonly used for laser eStop
            - [ ]  (x8) EtherCon to traditional RJ-45 adapter ends
        - [ ]  (2x) 180’-200’ Cat5 snake backups / link-up cords
        - [ ]  Several small Ethernet female-female chaining adapters
        - [ ]  (5x) 6’ and 10-14’ spare cords
- **If show is using mobile foggers**
    - [ ]  Wireless DMX triggers
- **If DJ lighting is not provided by venue**
    - [ ]  (2x) ADJ Stealth Wash Zoom moving head fixtures
        - [ ]  (2x) Wireless DMX-over-WiFi adapters
        - [ ]  iPad loaded with DMX app such as LumenAir with active license verified
    - [ ]  (4x) Nanlite light tubes with chargers
- M**obile apps**
    - Lighting/Network lead’s phone (all are for wireless link troubleshooting):
        - [ ]  UISP, UniFi, WiFiman, Starlink
        - [ ]  Nanlite control if you feel like it (effects for Nanlite tubes)
    - FOH iPads:
        - [ ]  All the above, plus LumenAir (DMX/ArtNet like Beacons/DJ Lights) and TouchOSC

## Show Setup Procedures

### Build / Setup

- [ ]  *Please edit and correct this list AS YOU GO, AS LONG AS YOU READ IT TO THE END FIRST*
- [ ]  **SEE ALSO** TE BM 2023 Software Runbook / Troubleshooting
    
    [TE BM 2023 Runbook / Troubleshooting](https://docs.google.com/presentation/d/1to4eDjwxo6PlV5Hcj9IzWTWRQrwOwAkF-6hyYwhbESs/edit#slide=id.g23c0395a3d7_0_16)
    

### **At Titanics End - Car**

- [ ]  **Install Network rack in the car’s server closet** - Important: check with Build Manager about the order of installation vs Audio Racks to prevent heavy rework
- [ ]  **Connect main network rack to side rack**. Connect 4 ethernet cords between the rightmost (gold) SFP ethernet ports on the Rack’s 48 port switch and the 48 port switch mounted in the closet’s outer wall.  Of the three, we sometimes use one via an optical cable. The show is still fully good to go if any 2 of these are working.
- [ ]  **Power the AC unit** and ensure it’s exhaust is correctly routed
- [ ]  **Power both the car-mounted ethernet switch and the rack in the server closet.** The generator powers the outlets in the back of the closet, or a Power Lead may have powered the car via shore power while building or at camp. If this isn’t ready but you’re ready to boot and test things, run your own extension cord to any source. You should see lights on ports for both of the network racks. This will also power any PoE devices distributed around the car’s 5 ethernet junction boxes.
- [ ]  **Connect the DJ booth to the network.** Inside the network closet, in the back, you’ll see a white Ethernet cord called “Dj Booth” written on tape on that coord. Ensure it’s plugged into the SIDE network switch (on the right as you look into the closet and turn your head right) using one of the bottom 4 ports - these are VLAN’ed to the Pioneer DJ network.
- [ ]  **Chain Laser ethernet.** When lasers are mounted, chain their Ethernet. For EDC, we successfully ran chains of 3 (left), 6 (above DJ), 3 (right). It’s most convenient to also do safety keys, TRUE1 power chains, and eStops (chained DMX 3-pin or XLR) at this time.
    - [ ]  Confirm whether you are using a separate Laser VLAN - if so, check that the ports the lasers connect to are designated as untagged members (see VLAN section above)
    - [ ]  Route eStop (XLR) cables from various chains to the central eStop splitter which is likely to be installed in the server rack.
- [ ]  When an audio team member (Jordan / Kian / Liam / Brendan / Aakash / Pascal) can help, connect 2x XLR line-outs from the rack mixer in the closet to the USB audio interface in the network rack.
- [ ]  Connect any sound output from computers used for timed shows (such as Mothership’s bootup sequence) to the D-LIVE Mixer’s line-in
- [ ]  Mount and connect at least two UniFi WiFi APs around the car, near the ethernet port boxes (most shows: front of the car). You’ll find the APs in the little white drawstring you found the SFP/LAG link ethernet cables in above.
- [ ]  Mount and plug in ethernet for the TE’s P2P dish - we typically mount this disk to a speaker bracket arm’s round tube (suggest routing Ethernet cable to a rear network junction box).
- [ ]  Mount Starlink up high on TE (beefy zip ties to frame). Connect StarLink’s ethernet adapter cord to port 9 (WAN icon) on the main enterprise router (UniFi Dream Machine Pro, top of rack).

### **At Front of House (Mothership, or other FoH desk)**

- [ ]  Setup the FoH network
    - [ ]  Connect the following to the TE LAN network switch:
        - [ ]  FoH dish using PoE adaptor to the TE LAN switch. Use the official Ubiquity PoE injectors for these antennas - they CANNOT be powered via typical PoE.
            - [ ]  Or, a designated cable (labeled A, B, C, or D) from the Cat6 tactical white snake
            - [ ]  Or, and I’m sorry you seem to be so fucked, one of the spare 180’ Cat5 cables
        - [ ]  `lighting-10-FOH`
        - [ ]  iPad dongles’ wired ethernet
            - [ ]  Connect USB-C power to the iPad dongles.  The power supply to each iPad must be ≥ 40 watts because the dongle uses 20W itself. This is more than a stock iPad power supply.
        - [ ]  Bome Box ethernet. It doesn’t matter which BomeBox ethernet port you choose.
            - [ ]  Connect the powered USB hub to the Bome box
                - [ ]  Connect all midi devices we want to send to LX to the USB hub (x2 MF Twisters, APC40, APC Mini, and for some shows the MF64)
                - [ ]  Connect the powered USB hub to AC power
            - [ ]  If PoE is not possible, power the Bome Box off the microUSB port (can be a spare from it’s own powered USB hub):
            
            ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled.jpeg)
            
        - [ ]  MSHIP LAN’s UDM Pro router - WAN port (globe icon)
    - [ ]  Connect the following to the MSHIP LAN network switch:
        - [ ]  MSHIP LAN’s UDM Pro router - Any LAN port
        - [ ]  `mship-led`
        - [ ]  `mship-laser`
            - [ ]  Connect MIDI devices over USB to the laser computer (Traktor F1, APC Mini, and for some shows and APC40 or MF64, etc)
            - [ ]  Wire Mothership’s laser eStops (DMX) in a chain to an easily accessible eStop on the laser desk
        - [ ]  Mothership [Chroma.tech](http://Chroma.tech) LED controllers
        - [ ]  Mothership lasers’ ethernet **input** side of laser data ports (important for BM’24): 2 of TE4, TE6, or TE8
        - [ ]  Beacon ArtNet ethernet cables
    - [ ]  Connect all power cables and screens.

### **LED and Laser Integration testing**

- [ ]  Power Mothership - all computers should auto-boot
- [ ]  Power the rack in the car and wait 2 minutes
- [ ]  Confirm all devices have their WiFi OFF (Laptops, iPads). This can cause network disruption.
- [ ]  Confirm iPads and any FoH laptops are charging to avoid surprises later.
- [ ]  Verify remote desktop from FoH to all TE Rack computers: lighting-1, lighting-2, showkontrol-3, lasers-4, GPU laptop
- [ ]  Verify auto-startup scripts started the correct build of Chromatik in auto-DJ mode on `lighting-1`, ShowKontrol and MaxMSP on `showkontrol-3`
- [ ]  Verify internet connectivity via Starlink or WiFi client.
    - [ ]  If bandwidth is a potential issue, consider doing the following after changing the StarLink WiFi password so general camp members aren’t streaming or competing for bandwidth.
    - [ ]  If Starlink’s wired Ethernet connection isn’t working, you can configure the GL iNet client mode router to connect to the Starlink as a wireless client and bridge internet to the car’s UDM router’s port 8 (WAN2). Connecting to an existing WiFi network via this WAN2 client mode router is the default setup we use in the Santa Rosa Studio.
- [ ]  The lighting lead should have had a team already connect the various structural modules’s 16 and 5 port switches to power (16-port), PoE port (5-ports), and connect ethernet to all power/controller backpacks
- [ ]  Verify MIDI controllers have connected to the BomeBox Network apps
    
    ### MIDI Controller setup
    
    The LED and Laser computers for each car receive color coordination MIDI and brightness fader data from the Lighting Director’s APC Mini; The LED and laser computers on TE also connect to the remote MIDI controllers located on MOTHERSHIP.
    
    ![MIDI Network.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/MIDI_Network.png)
    
     
    
    ## Bome and MIDI Setup steps
    
    - [ ]  Confirm Power light is lit on the BomeBox.  Confirm midi surfaces have some lit LEDs.
    
    ### The Director’s APC Mini - Color and Brightness faders
    
    To split the Director’s color messages out to all four computers requires that we create a Virtual Port on the BomeBox for each consumer, and split the Director’s APC Mini outgoing MIDI to all computers.
    
    1. TE’s LED computer, `lighting-1`, sends bidirectionally; it is “configured” (button colors set) by `lighting-1`. It must have bidirectional routes added on the BomeBox (named “FoH”) to and from a virtual port named “**Director**”. Chromatik setup code depends on this name.
    2. TE’s Laser computer, `laser-4`, receives Director MIDI via the virtual MIDI port named **Director-to-laser-4**
    3. Mothership’s LED computer, `mship-led`, receives Director MIDI via the virtual MIDI port named **Director-to-mship-led**
    4. Mothership’s laser computer, `mship-laser`, receives Director MIDI via the virtual MIDI port named **Director-to-mship-laser**
    
    ### Setup Steps
    
    1. On the BomeBox, create these four virtual MIDI ports:
        
        ![Monosnap Bome Network 2024-08-14 22-56-23.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_Bome_Network_2024-08-14_22-56-23.png)
        
    2. Again on the FoH BomeBox, add bidirectional routes for **Director**, and Controller-to-Virtual Port routes for the others. Here is the subset of routes you will need to create - you’ll likely see other routes automatically in this list.
        
        <aside>
        ❗ Each APC Mini mkii will appear as two devices. Always select and map the one that appears as either “**APC mini mk2 [1]**” or “**APC mini mk2 Control**”
        
        </aside>
        
        ![Monosnap Bome Network 2024-08-14 23-02-53.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_Bome_Network_2024-08-14_23-02-53.png)
        
    3. Now, switching to each of the computers that need to receive these colors, use the Bome Network app to connect to the “FoH” BomeBox, and enable (connect to) the matching virtual port. Using the network diagram above, make sure each Bome Network app is connected to the particular MIDI controllers it needs.
        
        ![Monosnap Laser-4-3 via client router on V 2024-08-14 15-35-15.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_Laser-4-3_via_client_router_on_V_2024-08-14_15-35-15.png)
        
    
    After the Director’s Virtual routes are created, connect each computer to the MIDI controllers it needs.
    
    ### Try this first: Step-by-step example for `mship-laser`
    
    ![Monosnap Laser-4-3 via client router on V 2024-08-14 15-27-41.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/37fcbd33-b424-4db3-8be1-b3777599b3a9.png)
    
    ![Monosnap Laser-4-3 via client router on V 2024-08-14 23-35-51.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/67a070b0-ec14-4665-aa01-bbbd56b91c31.png)
    
    ![Monosnap Laser-4-3 via client router on V 2024-08-14 15-34-05.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/59c82ff2-2f67-4f00-b0f5-d0e97cd7d9b7.png)
    
    ![Monosnap Laser-4-3 via client router on V 2024-08-14 16-15-59.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_Laser-4-3_via_client_router_on_V_2024-08-14_16-15-59.png)
    
    - [ ]  Verify on `mship-laser` that the primary APC Mini for Mothership is working as intended in Beyond.
    - [ ]  Confirm that the Director’s APC Mini is selecting colors in Beyond from the QuickFX Row.
        
        ![Monosnap Laser-4-3 via client router on V 2024-08-14 23-58-18.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_Laser-4-3_via_client_router_on_V_2024-08-14_23-58-18.png)
        
    
    ### laser-4: TE’s Lasers
    
    ![Monosnap Laser-4-3 via client router on V 2024-08-14 23-22-09.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_Laser-4-3_via_client_router_on_V_2024-08-14_23-22-09.png)
    
    - Important: if using Bome Network to link any FoH USB MIDI controllers connected directly to `mship-laser` to the car’s `laser-4`, you must configure the Microsoft Remote Desktop client to “Play audio through the remote computer”
        - Screenshot
            
            ![Monosnap Untitled 2024-08-14 23-53-16.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_Untitled_2024-08-14_23-53-16.png)
            
    - [ ]  `laser-4`(on TE) has its Bome Network app connected to the FoH: Traktor Kontrol F1 via BomeBox
    - [ ]  Verify via Microsoft Remote Desktop to lasers-4 that the Traktor F1 and any other laser MIDI controllers are working as intended in Beyond.
    - [ ]  Confirm the Director’s APC Mini is selecting colors in Beyond from the QuickFX Row.
        
        ![Monosnap Laser-4-3 via client router on V 2024-08-14 23-58-18.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_Laser-4-3_via_client_router_on_V_2024-08-14_23-58-18.png)
        
    
    ### Lighting-1: TE’s LEDs
    
    - [ ]  BomeBox named “FoH” connects the 4 LED MIDI controllers to Bome Network app on `lighting-1`
    - [ ]  🎛️ Connect MIDI controllers to Chromatik
        
        <aside>
        ⚠️ If the FOH ↔ Car connection changes, such as switching from the dish to a wired connection or vice versa.  It is HIGHLY RECOMMENDED to restart both the physical BomeBox and the Bome software on Lighting-1 and on any other Bome hardware/software instances.
        
        </aside>
        
        - Verify Bome network connection from BomeBox to `lighting-1` *(toggle for screenshot…)*
            - [ ]  Confirm Bome Network software is running on `lighting-1`.  When running there is a Bome icon in the menu bar:
                
                ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled.png)
                
            - [ ]  Click the Bome icon → Show
                
                ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%201.png)
                
            - [ ]  The FoH device should show Connected. Give it a minute. If it does not connect, try pressing the Pair button on the Bomebox.
                
                ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%202.png)
                
            - [ ]  When Connected, click the FoH device and check the status of the MIDI devices.  All connected devices should say “open” under the name.  If they say something different like “one-way”, “in-ok-but-out-not-okay”, etc, toggle the midi surface off and back on again.  It should say Open when it comes back.
                
                ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%203.png)
                
            - [ ]  If something really crazy happened, the routes may need to be adjusted on the bomebox.  To adjust midi routing click the globe icon on the BomeBox > FoH device screen.  This should not need adjustment after it has been set once at the TE factory, unless new midi controller types are added or a new bomebox is installed.
            - [ ]  The MIDI surfaces should now be available in lighting-1’s OS with the bomebox name prepended to the midi name, like “FoH: APC40 mkII”.
        
        <aside>
        ⚠️ To get the correct midi surface behavior in Chromatik, the **FoH: <MIDI device name>** name must be correct. If the midi surfaces are directly connected to the Chromatik Computer (such as running Chromatik on a laptop/MacMini at FoH) rename them in the OSX Audio Midi Setup application and add “FoH: “ to the name so they will be handled correctly in Chromatik.  To do this: Command + Space → Audio MIDI Setup, then Window → Show Midi Studio. Then double-click a device and change the Device Name.
        
        </aside>
        
        - [ ]  Verify Chromatik recognizes the devices.  The green buttons should match on your screen:
        - *Toggle for screenshot*
        (Note: The following For BM’24 you should also see the FoH: APC Mini - Director control surface)
            
            ![Monosnap lighting-1 2024-08-07 01-15-02.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Monosnap_lighting-1_2024-08-07_01-15-02.png)
            
        - [ ]  MidiFighterTwister: Cue vs Aux
            - [ ]  The left-hand MFT should show blue background lights to indicate it is following the Primary focused channel.
            - [ ]  The right-hand MFT should show red background lights to indicate it is following the Aux focused channel.
            - [ ]  **To toggle primary/aux**, press the top button on the right side of the MFT.  Or click the button next to “Aux” in the MIDI SURFACES list in Chromatik.
            - [ ]  When using two MFTs, both should be set to Bank 0.
            - Diagram of the MidiFighterTwister side buttons: *(toggle for screenshot…)*
                
                ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%204.png)
                
        - [ ]  How to tell if midi controllers are working
            - [ ]  Move the faders on the APC40.  The channel faders in Chromatik should follow.
            - [ ]  Be sure the Master Fader is up.
            - [ ]  Focus a channel and a TEPerformancePattern within that channel.  Move the MFT knobs to confirm the parameters are changed.
                - [ ]  Open Perform mode (Click Design/Perform in top right, or press top right button “SESSION” on APC40mkII.  Click Aux (⚫ / Arm / Record) on a channel to cue and focus it.  Confirm that the right-hand Midi Fighter Twister with red lights changes the aux-focused channel.
        - [ ]  Troubleshooting
            - Assuming you see the Midi Surface in Chromatik,
            - Verify the green squares to enable the midi surfaces are on, as shown in the screenshot
                
                ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%205.png)
                
            - Verify proper MIDI devices names including BomeBox Prefix.  The names need to match the definitions in src/main/java/titanicsend/midi/MidiNames.java. If the BomeBox prefix changes, update it here and recompile *(toggle for screenshot…)*
                
                ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%206.png)
                
    
    ### mship-led: Mothership’s LEDs
    
    @Andrew Look - to lighten the load on @Justin, as well as to spread the knowledge, please use the example checklists above and document how you’d like Chromatik on Mothership to receive the colors from the Director (if that’s in scope for 2024)
    

*Now continuing past MIDI Controller setup to BPM and OSC setup…*

- [ ]  Setup the iPads to display the Cue (Left) and Aux (right) parameters in Perform mode
    - [ ]  Confirm OSC output and iPad output are enabled in the Control Bank
        - *Toggle for screenshot*
            
            ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%207.png)
            
    - [ ]  The MaxMSP patch on showkontrol-3 must be receiving OSC from lighting-1
        - [ ]  Check the MaxMSP patch is running (TE_OSC_Dispatcher)
        - *Toggle for screenshot*
            
            ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%208.png)
            
        - [ ]  Check that showkontrol-3’s IP address matches Chromatik’s OSC Output address  has the IP address configured in Chromatik’s OSC destination. The (Left sidebar) Model → CONTROL PANEL, when in Production mode, will set this IP to the value in src/main/java/titanicsend/lasercontrol/PangolinHost.java
        - *Toggle for screenshot*
            
            ![Untitled](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Untitled%209.png)
            
        - [ ]  Launch TouchOSC on both ipads, and tap CUE on the left (iPad 1), and AUX on the right (iPad 2)
        - [ ]  If the TouchOSC diplays are not responding when parameters are changed, verify that their IP addresses match what is configured in the MaxMSP patch. Currently they are 10.100.0.201 and 10.100.0.202. If connected via the wired ethernet dongles, they will get these IP addresses from the main car’s router. If connected via WiFi (not recommended), you will need to manually assign these IPs with subnet mast 255.128.0.0 and router 10.0.0.1.

### Pioneer DJ Link / ShowKontrol / Beat Link Trigger

- [ ]  Verify the Pioneer DJ Link network is communicating with our ShowKontrol
    - [ ]  Verify ShowKontrol or BLT running on `showkontrol-3` can see the Pioneer equipment on auto-assigned IP addresses on VLAN 200
    - [ ]  Verify all decks are communicating via DJ Link. Verify all decks can access a library of music plugged into one deck’s USB. Load a track in each deck and verify that maximizing the fader assigned to each deck will change that deck to display “Master”.
    - [ ]  Verify all decks are running the latest firmware.
        
        [CDJ-3000 Firmware Update Guide](https://support.pioneerdj.com/hc/en-us/articles/4413929605529-CDJ-3000-Firmware-Update-Guide-)
        
    - [ ]  Verify each deck has a manually-assigned player number that matches the channel it is plugged into on the mixer.  Verify there are no player number conflicts.
    - [ ]  Verify ethernet connection to each CDJ and the mixer.
    - [ ]  In each CDJ/Mixer menu, confirm IP address is as expected
- [ ]  Verify ShowKontrol is sending tempo and OSC messages to LEDs and Lasers
    - [ ]  Play a track on the CDJs and verify the tempo is updated in Chromatik and Beyond
    - [ ]  TBD: Get tempo into Pangolin QuickShow on `mship-laser` via Midi Timecode
    - [ ]  TBD: Instead distribute tempo and beat to Pangolin Beyond on `laser-4` via Ableton Link
        - [ ]  JKB Note: BeatLinkTrigger has Ableton LInk and we could configure it to share for Pangolin

### DJ Lights (set up and control)

The DJ lights are two moving head wash lights controlled over Artnet using DMX Wifi Dongles (Stealth Wash Zoom - Eliminator)

- These lights are used to light up the DJ deck and area. Expand these headings for pictures.
    
    ![1000029006.jpg](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/1000029006.jpg)
    

## Set up

- Make sure the moving head lights are installed physically on the bridge beam at the same time as the lasers. Otherwise installation becomes very difficult and requires heavy machinery.
- Moving head lights require one global truss C clamp each. Ensure that you secure the metal safety harness around the beam as a backup in case the C clamp fails. (See below)
- Click for pic
    
    ![1000029011.jpg](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/1000029011.jpg)
    
- Space out the lights on the beam to make sure you can make an X pattern down to the DJ decks so that the DJ isn't blinded by the lights. See photo below for configuration
- Click for pic
    
    ![1000029022.png](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/1000029022.png)
    
- Make sure each moving head light has a PK knight WiFi dongle connected to it and they are powered (see below)
- Click for pic
    
    ![1000029008.jpg](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/1000029008.jpg)
    
- DJ Light House **Left should be on DMX address 101 and the Right should be on 121**
    - This can be checked on the DJ lights’ screen on the device itself by pressing the menu button (see below)
        
        ![1000029009.jpg](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/1000029009.jpg)
        
- The **VJ iPad 2** is the main control surface for the lights
    - The Illuminator app on the iPad will is needed to control the lights
- Open the Illuminator app and make sure the Artnet interface is enabled
    - Go to connections → Artnet should “on” and inside the artnet menu the Universe 1 should be “on” too
- The lights should be connected to the app and controllable by the app
- Keep in mind that the lights are grouped under the  “DJ Washes” group (see below)
- The recommended setting is WHITE/AMBER, indicated below in the yellow button called “Default settings”. Generally any other color wasn't bright enough to fully illuminate the DJ. It is recommended to set the lights to the default setting at the beginning of the the show and leave it for the rest of the night
    
    ![1000029019.jpg](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/1000029019.jpg)
    

## Troubleshooting

1. If you are not sure what are the IPs of the device, you can find them on the Ubiquity interface
    1. as of now, they should be Right (10.6.2.102) and Left (10.6.2.101)
2. The lights should be flashing slowly and the colors on both dongle should match (as of now Red)
3. The Eliminator stealth wash zoom lights are technically INDOOR rated. In the case they stop working, you can setup nanlites behind the DJ decks with the tripod stands included in the nanlites bag. Make sure to adjust the lights downwards not to blind the DJs!

## Verify!

- LXStudio broadcasting pixel data
    - [ ]  Power up a fixture or two and corresponding Angio controllers
    - [ ]  Turn on lighting-1
    - [ ]  Confirm fixtures start showing a pattern within X seconds
- All Angio controllers working
    - [ ]  Turn on light show as above
    - [ ]  Power up all Angio controllers
    - [ ]  TODO: Should we write a lighting-1 script that pings all controllers that are supposed to exist and produces a report? @Eli McNutt
    - [ ]  TODO: Is there a way that script can also verify all controllers’ firmware and config? @Eli McNutt
- MIDI
    - [ ]  Turn on light show as above
    - [ ]  Switch channels on APC, make sure the GUI changes with it
    - [ ]  Switch channels on GUI, make sure APC lights change with it
    - [ ]  Switch to MF64 pattern
    - [ ]  Push buttons on MF64, make sure light show effects get triggered
    - [ ]  TODO: How to test Twisters?
    - [ ]  TODO: How to test NIs?
- Backup FoH wifi (for loss of both P2P dish link and no ability to run an ethernet cable)
    - [ ]  Confirm MIDI working as above
    - [ ]  Disconnect FOH switch from PowerBeam
    - [ ]  Confirm MIDI controls stop working
    - [ ]  Turn on FOH backup AP client
    - [ ]  Wait N seconds
    - [ ]  Confirm MIDI controls start working
    - [ ]  Confirm lighting-10 remote desktop working
    - [ ]  Turn FOH AP off again
    - [ ]  Confirm MIDI controls stop working
    - [ ]  Reconnect FOH switch to PowerBeam
    - [ ]  Confirm MIDI controls and lighting-10 start working
- ShowKontrol
    - [ ]  Sending OSC messages on BPM change, beat, and phrase change to MAX/MSP script
    - [ ]  Max/MSP script is running
    - [ ]  BPM changes are being received by computers laser-4 and lighting-1 (Chromatik)
- Laser control
    - [ ]  `laser-4` is reachable via remote dekstop from FOH
    - [ ]  Pangolin Beyond has it’s internet license activated (must have internet access)
    - [ ]  `laser-4` sees all powered on lasers (8 FB4 cards for BM’24) after the keys/interlock/e-Stop START button is pushed
    - [ ]  `mship-laser` sees all powered on lasers (8 FB4 cards for BM’24) after the keys/interlock/e-Stop START button is pushed
    - [ ]  MIDI: Bome Network is running on `laser-4` and (`mship-laser` or `laser-14`), and Remote Direct Midi is working for Traktor Kontrol F-1 (cues, blackouts) and APC-40 (if using)
    - [ ]  Director colors are being received and used by Beyond on `laser-4`
    
- Recovery from a loss of the point-to-point wireless link
    - [ ]  Power down the FoH dish, typically a PowerBeam
    - [ ]  Power up the FoH Client WiFi Bridge device
    - [ ]  Verify it’s connected to the car’s UniFy AP’s (UFO style) crew network

### Strike

- [ ]  Disconnect Angio Switches on modules. Coil and cord-wrap ethernet cables to be coiled near the module’s switches.

### Troubleshooting Checklist: Loss of FoH ↔ Car Connectivity

- [ ]  Check link lights on FoH switches
- [ ]  Check LED indicator for link strength on the P2P link’s antenna dish
- [ ]  Using a mobile phone, connect to P2P Dish’s management WiFi radio (NME-XX-XXXX or PBE-XX-XXXX)
    - [ ]  If you can’t see this open network, it’s been more than 10 minutes since that side of the link was powered on. Power cycle the NanoBeam or PowerBeam.
    - [ ]  Use the UISP iPhone App. Credentials are in [the sheet](https://docs.google.com/spreadsheets/d/1JMT-oSenwYVS_fpXtLfjlVQqChUMWMs7pdlXXzdgqD4/edit?gid=0#gid=0); username ubnt and typical “Network layer” password
    - [ ]  Verify the SSID, WiFi link password, and link’s strength
    - [ ]  Use site survey to look for RF interference and test antenna orientation
    - [ ]  If possible, perform the same for the NanoBeam on the car.
- [ ]  MIDI troubleshooting
    - [ ]  Remote into `lighting-1` and verify the Bome Network Tool is running
    - [ ]  Verify the Bome Network Tool is connected to the BomeBox via the LAN / P2P link
    - [ ]  Verify that the MIDI Surfaces (e.g. APC40) entries are **enabled** in the rightmost MIDI sidebar of the Chromatik
    - [ ]  Verify the device names are identical in the Chromatik codebase’s MIDI classes to what’s shown in the Bome Network Tool’s virtual device forwarding list
    - [ ]  Connect to the BomeBox’s web interface (OpenWRT fork) using a FoH-local computer. You can access the static IP (typically [http://10.8.0.20](http://10.8.0.20) and no password) or if it’s new BoomeBox you’re swapping in, use a local Bome Network Tool on a FoH laptop to perform discovery of it’s local IP.
    - [ ]  Check BomeBox config settings and see that bidirectional MIDI routes are enabled between each MIDI device and the Bome Network Tool.
    - [ ]  If the FOH link to car was swapped between dish/wired, restart the BomeBox software on `lighting-1` AND power cycle the BomeBox.

## Other pages related to Networking and Front of House

[Independent FoH Case](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/Independent%20FoH%20Case%206925a111786c44e589f3d80d1799ee10.md)

[MIDI setup: APCminiMk2 over Bomebox](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/MIDI%20setup%20APCminiMk2%20over%20Bomebox%2002cb560b23864732b0521857b4ae426e.md)

[BM 2024 Notes - JKB](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/BM%202024%20Notes%20-%20JKB%20e0306593c3e940c6b8b3959c83f10732.md)

[TE Networking Lead Role Description](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/TE%20Networking%20Lead%20Role%20Description%2013d7fd75b80080ed9bd6e59d0e116554.md)

[2025-05-17 - Summary](Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4/2025-05-17%20-%20Summary%201f67fd75b80080cca990d9f5dc795b02.md)