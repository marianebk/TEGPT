# 2023 Lighting Software & Integration

## Software Tasks

[2023 TE Software Tasks](2023%20Lighting%20Software%20&%20Integration%2061c9cd5c6e884c6db66d4f843a1b8812/2023%20TE%20Software%20Tasks%2072bd894800c84a25b2b5961920a039d8.csv)

[Low-level software tasks](2023%20Lighting%20Software%20&%20Integration%2061c9cd5c6e884c6db66d4f843a1b8812/Low-level%20software%20tasks%20f5264e3538bf417e86956d87124d1a89.csv)

# Roadmaps

- January 2023
    
    [Lighting Team Software Roadmap January 2023](https://www.notion.so/Lighting-Team-Software-Roadmap-January-2023-e66706aab0184a229e0aac1c69e667a1?pvs=21)
    
- EDC May 2023
    
    [EDC Software Status](2023%20Lighting%20Software%20&%20Integration%2061c9cd5c6e884c6db66d4f843a1b8812/EDC%20Software%20Status%2087a2e9a4cb7e4f7490de959da3f24d33.md)
    
    [Justin’s EDC Software Notes](2023%20Lighting%20Software%20&%20Integration%2061c9cd5c6e884c6db66d4f843a1b8812/Justin%E2%80%99s%20EDC%20Software%20Notes%20ac212e391d444956bf9432102c6aba3b.md)
    

# 2022 Documentation (to be migrated to Notion)

Still relevant!

- TE Lighting Design
    - https://docs.google.com/document/d/1YK9umrhOodwnRWGRzYOR1iOocrO6Cf9ZpHF7FWgBKKI/edit#heading=h.jwh2kgk98479
- Pattern Standards
    - https://docs.google.com/document/d/16FGnQ8jopCGwQ0qZizqILt3KYiLo0LPYkDYtnYzY7gI/edit#heading=h.zdrrcd758kl3

# Tutorials

[Low Level Software Tasks](https://docs.google.com/document/d/1vUw5XAjEezA1OhZ5tqew1Aw7z3jSoULjc8R_WXtoKGs/edit)

## Remote Access to the Production Rack

Use [Tailscale](https://tailscale.com/) + Remote Desktop to access the computers in the lighting rack.

1. Install [Tailscale](https://tailscale.com/). It’s free. 
2. Using a new browser profile (or an incognito tab), login to github as the user **titanicsend** (password [here](https://docs.google.com/spreadsheets/d/1JMT-oSenwYVS_fpXtLfjlVQqChUMWMs7pdlXXzdgqD4/edit#gid=0)).
3. Login to Tailscale using Github as your identity provider. If tailscale opened in a different browser profile, just copy the SSO link to the one where you’re logged in as **titanicsend.**
4. Browse “My devices” to see which machines are currently connected. Our main LX Studio box is `lighting-1`. Click the box name to copy the VPN IP address.
    
    ![Screen.png](2023%20Lighting%20Software%20&%20Integration%2061c9cd5c6e884c6db66d4f843a1b8812/Screen.png)
    
    - All use Apple Screen Sharing as the client, except for `laser-4`, which you can access from a Mac using the free [Microsoft Remote Desktop](https://apps.apple.com/us/app/microsoft-remote-desktop/id1295203466?mt=12).
    - If `lighting-1` is not accessible, but one of the other devices is, you can remote into one of them, then screenshare from that box into `lighting-1` and restart tailscale. Occassionally Tailscale cannot auto-login after some software update reboots, or if it hasn’t re-authenticated in many weeks.
5. Paste the IP into your Screen Sharing. All machines have username **te** and password **SK9822.** If that password isn’t working, please check for a change in the main password sheet ([TE Shared Accounts](https://docs.google.com/spreadsheets/d/1JMT-oSenwYVS_fpXtLfjlVQqChUMWMs7pdlXXzdgqD4/edit#gid=0)), and update it here. 

# Fall 2023 Events

[OSC from GrandMA Lighting Console - CANCELED the OSC idea](2023%20Lighting%20Software%20&%20Integration%2061c9cd5c6e884c6db66d4f843a1b8812/OSC%20from%20GrandMA%20Lighting%20Console%20-%20CANCELED%20the%20O%20acf1047c371644b59c800a0d7ab8d536.md)

[Software for LA show Oct 2023](2023%20Lighting%20Software%20&%20Integration%2061c9cd5c6e884c6db66d4f843a1b8812/Software%20for%20LA%20show%20Oct%202023%20458d516fef064ce98fbf8d7d4ba29044.md)