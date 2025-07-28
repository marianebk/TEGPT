# TE Networking Lead Role Description

There’s no show without the network! You understand what gear needs to communicate and make it happen.

## **Your four most important responsibilities:**

1. Train a backup as you learn, so if you are sick or can’t go to a deployment, someone else knows what you know and TE can still be deployed.
2. The only way to do that is by keeping [the documentation](../Networking%20and%20Front%20of%20House%20Setup%20fe5360a00b594955b735e02115548ff4.md) updated.
3. The only way to keep the documentation updated is to do dry runs. You must spent time on your own opening these tools and messing around with them. You must pressure - no, force - other TE leads to bring up as many systems as possible well before the next deployment. You must do the dry run at a snail’s pace from the documentation so you know if the documentation is right. Then you can do it from memory quickly at a show, or troubleshoot efficiently. 

Dry runs require plugging in lots of different parts of TE and Mothership even they can’t be fully assembled. They require the front of house lead, laser lead, and LED lighting lead to be with you validating their applications.
4. Manage a networking [ToDo list](Network%20and%20FoH%20TODOs%20cec5af5464804e9da6ad5b392e710d26.md) with the software team members

## Who will support you?

Jeff, Justin Belcher, Will, Sina, and Liam have all learned this in prior years. Reach out and we will help - all you have to do is put in the time to practice, and use your favorite LLM as a networking professor.

Since 2023, the Front of House lead has been a separate role from Network lead, because it’s usually too much for one person - We’re recruiting Misha, David, Andy and anyone else who can but in the time to try connecting everything. Past FoH leads have been Jeff, Derek, and Sina.

### Duties of the Networking lead vs Front of House lead

| Area of Responsibility | Network lead | Front of House lead |
| --- | --- | --- |
| Understanding the purpose of all devices on the network; Establishing connectivity and traffic isolation | Responsible | Stakeholder |
| Documenting how to configure components | Network gear, remote desktop, VPN remote access | Lighting computer, DJ-Link, laser workstation, MIDI-over-ethernet |
| Integrating new systems and devices | The “solution provider” | The “customer” |
| Networking with guest systems such as GrandMA or Resolume | Shared responsibility | Shared responsibility |
| Mothership | Link: Wired or wireless, VPN or not, isolating traffic, remote desktop or LED data being sent over link | Workstation selection and MIDI controller layout. Single operator for both cars? Lasers controlled by Chromatik? |
| Inventory responsibility | Variety of network cable lengths, networking gear and racks, rack terminal access, AC (air conditioning) infrastructure,  | Computers, iPads, MIDI controllers, power and USB cables, monitors and mounts, mice/keyboards  |
| Training responsibility | Backup network admins | Volunteer VJs, nightly setup and strike |
| Software updates | OS, Network OS | Applications |

For example: Suppose one of our iPads dies. You might need to assign it a static IP address and make sure it can connect over wired ethernet and wifi. You’ll need to run software updates. You will need to make sure it can connect to the LED engine computer and Max/MSP OSC router, but not be overwhelmed by LED pixel data to LED controllers and not interfere with the DJ decks or lasers.

You don’t need to know where to configure those IP addresses and ports within Chromatic, MaxMSP, TouchOSC, and TouchDesigner. You don’t need to inventory it before shows or update it’s apps. You need to organize the dry run but not verify that each app (MoboLaser, TouchOSC, and Lumenair) is working on the iPad.

## Systems that are both selectively connected and isolated

1. Digital audio stack configuration (Armonia, D-Live)
2. Audio player metadata (DJ Link)
3. LED Lighting (Chromatik, LED controllers)
4. Lasers (Beyond, FB4s)
5. Front-of-House workstations (LEDs, Director/Conductor, Lasers, Audio mix, Projection/V1)
6. DMX FX (DJ lights, foggers, Mothership beacons)
7. Mothership LEDs and Lasers
8. WiFi or wired interconnections for the above

## Technical Skills

<aside>
💞

A note of encouragement. Everything listed below that **you have no clue about** - is something that one of us **had no clue about** and taught ourselves. All the people who’ve served in this role or been trained as a backup did NOT know these skills before we had to learn them for TE!

</aside>

1. Ubiquity networking gear - Switches, routers/gateways, access points, WiFi client bridge
2. VLANs - setting up multiple networks that are isolated from each other on the same piece of hardware (and occasionally opening a particular communication path between them).
3. Subnets - Assigning private IPs, CIDR (how subnet masks work)
4. VNC (RDP on windows) - accessing each computer on the network from any other. Playing janitor for people using these shared workstations.
5. Starlink - how to get internet to the car and sometimes also to crew
6. VPNs - we use a very simple single VPN to remotely access the network from anywhere
7. Keeping the shared password repository updated.
8. Keeping devices OS’s updated