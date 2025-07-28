# Independent FoH Case

<aside>
💡

As of mid 2024, this road case has been built and lives in the studio. We need to decide whether it’s appropriate to bring it to BM where it will get destroyed, or reserve it for our non-dusty deployments.

</aside>

The goal of this project is to have a custom road case built for a set of FoH equipment to control TE Lighting that will be used when the MOTHERSHIP cannot accompany TE.

RFQ video showing MIDI controller placement 

[https://www.youtube.com/watch?v=zqpLRSTsEtA](https://www.youtube.com/watch?v=zqpLRSTsEtA)

**Status**: One case has been ordered and received - we’re ready to try it out at the next non-BM deployment! If it works, and after we know what we’d change, we can order the second one so we have enough side-by-side space for all Front of House positions.

## Scope assumptions

- Duplicate / separate equipment from the FoH controls inside MOTHERSHIP, except for the two Mac Minis which would need to be transferred between setups

## Goals Shared from 2023

Similar to the 2023 custom FoH desks built by Derek, it’s aims are:

- Carry-able by two people
- Quick deploy
- Minimal cable reconnections to set up
- Can utilize WiFi or wired networking to TE
- Powered by 110VAC; via host venue, generator, or long extension cord from TE
- Integrated storage for spare items (cords, controllers, hearing protection, manuals).
- A rain-resistant top case or cover
- Can be moved on playa in a single stack on wheels, either towed or stored in KHole
    - Yes, on playa. Because if MOTHERSHIP is inoperable for any reason, we still need a usable system for getting a FoH deployed each night.
- Closely mirror the FOH controls in MOTHERSHIP

## Improvements on the 2023 solution

Based on lessons learned from 2023, it will be different in the following ways:

- More durable
- No integrated legs. Sets on a surface at normal desk height. The supporting surface itself could be folding tables or a surface designed for this purpose built around Gorilla Carts (which could accommodate additional storage for VJ personal items and a generator).
- Anti-laptop. Inexpensive peripherals (keyboards, MIDI controls, displays) above the desk surface, Mac Minis embedded within the case.
- As many connections will be routed below the work surface layer as possible to discourage people from believing they need to unplug things. Therefore, USB hubs, ethernet switches, POE injector, etc will be below the desk surface, yet still accessible for inspection and troubleshooting.
- More formal markings and purpose-fit holders for the various pieces of equipment above the work surface
- Allows work surface reconfiguration (for ergonomics or new equipment in future years)
- Iteration on dust resistance at the cable ingress points
- Angled surfaces to support MIDI controllers
- It should support degraded operation modes where TE is more of a $2M puppet fixture with a via DMX, a la Framework
- Fold-down displays
- Power bar, more dust protected (some outlets internal, some above desk surface)
- Accommodates the following equipment in it’s first year (2024)
    - Desk 1
        - Lighting Mac Mini; Keyboard, touchpad or mouse, display
        - APC40 mkii2
        - 2x MF Twisters
        - 2x iPads with TouchOSC
        - Storage: Spare APC40 mkii
    - Desk 2
        - Laser Mac Mini; Keyboard, touchpad or mouse, display
        - Traktor F1
        - APC40 mkii
        - MF64 for finger drumming
        - APC Mini, located within reach of either operator, for color selection
        - Space for remote sound control (Armonia remote desktop via laptop or iPad)
        - Storage: Laptop for mobile troubleshooting around the car
- Evaluate the pros/cons of trying to host rendering in the FoH instead of on TE
    
    
    |  | **On-car rendering** | **FoH rendering** |
    | --- | --- | --- |
    | **Fallback option in the event of an lost data link** | LEDs continue to work even if FoH experiences network drop or power-out.
    
    Backup control possible via server room KVM or AutoVJ without interruption. | Car will glitch or go dark until an on-car rendering computer can be enabled. 
    
    This still requires a backup set of minimal computer peripherals (display, keyboard, mouse) at the server closet. |
    | **UI latency** | 20-500ms display latencies experienced on remote desktop
    
    Bome/MIDI latency seems usable and much less of an issue. | No UI latency |
    | **Sound reactive patterns** | Two short XLRs from mixer complete the link | New solution needed to get realtime audio from TE to the FoH rendering computer for sound-reactive patterns; either wireless, or long dual XLR |
    | **MIDI Controllers link to rendering engine** | Bome remote MIDI links have been difficult for volunteers to learn how to initially set up or re-enable after a glitch | Eliminates need for Bome / MIDI-over-ethernet links |
    | **Reliable minimum bandwidth requirements** | 4 Mbps minimum (2 VNC); wireless link is typically 250 Mbps with 5-30ms latency | 2-10ms latency
    
    Almost 100 Mbps minimum to transfer pixel data; will require dual redundant wired ethernet cables in protected cable raceway. 
    
    It’s not a 100% reliable solution: BM’23 and Framework both experienced networking issues over wired ethernet links (bad switch and fragile connection). 
    
    Long CAT6 has been shown to reduce bandwidth.  |
    | **Summary** | Can be run completely wireless, or use a single ethernet cord with wireless backup.
    
    UI latency is annoying, especially for inexperienced VJs who tend to fall back on more mouse and keyboard use over MIDI controllers. | Likely needs to always have at least 4 physical cables between TE and FoH. This increases setup time, which is already an issue when we roll out. Horrible cable mess and setup experiences in 2023 show that a custom snake and storage reel is a hard requirement. Loose cables or a raceway were shown to be a tripping risk and annoying to our audience.  |

# Design research

### Design philosophy

Mothership is for our pride in form over function. These cases are for function over form. We deploy this at commercial shows. I do not care about making the people around us say, “Ooooh that’s beautiful and alien.” I care that the cases are:

1. Durable and packable
2. Quickly deployable
3. Easy to troubleshoot under time pressure
4. Adaptable to the ergonomics of various operator heights and preferences
5. Adaptable to preferences we discover after more performances or when our equipment changes.

Since we do not plan to deploy these at Burning Man, I will not be prioritizing dust ingress protection. They will be water resistant when sealed. This decision matches commercially available GrandMA cases.

## Dimensions

From Slack:

> Standing performance is the default, director's chairs optional
> 
> - Top surface at ~~36"~~ 38", with risers to get control surfaces to 38"-44" for tall people
> - Nothing below 30" for knee clearance while seated in raised directors chairs
> - Minimum 24" desk depth for keyb, controllers, screen; 30" ideal

**Heights**

- Standard DJ table height: 1-1.1M (from 8 DJ riders); 39-43”
- Comfortable standing desk heights: 38”-44” (from team)
- Standard folding table/desk height: 29”

**Depths**

- Seen in several riders: 24-32”
- Standard US door width: 30”
- We have a deep layout: keyb/mouse, then APC40 flanked by twisters, backed by iPads and screen
- Decision: 29.5” deep

**Widths**

- 2 x 60” - most comfortable from real use at BM2023

**Cabinets**

- EU2200 heightd

**Monitors**

27” Monitors

|  LG Ultrafine 27UN850 | 24.1" x 14.4" x 1.8” |
| --- | --- |
| Dell S2722QC | 24.1”  x 15.8” x 2.2”
10.4 lbs |
| LG UltraGear 27GL83A | 24.2" x 14.4" x 2.2” |
| Dell S2721QS | 24.1”  x 15.8” x 2.2”
10.4 lbs |

**Features requested by Keegan:**

1. Full height from floor, on casters, for easy loading (one person roll, not two person lift). Keegan believes we will be able to demand this floor space in all venues (and will not be forced into situations where we are given a desk that we must set up at).
    1. Because I cannot guarantee we will be able to deploy this way everywhere (such as a nightclub booth, or when the host staging vendor forgets to honor this request and sets up a desk anyway, and we again are under time pressure), I will instead be designing a 2-piece design. The top is a coffin form factor that is sized to be placed on any desktop provided. It latches securely onto a bottom castered cabinet. The top contains all electronics and is not reliant on the bottom (unless we add rack mount gear in the future).
2. 6-casters on bottom. Planned.
3. Stow-away doors. Cabinets: Planned. Lid TBD.

Surface height adjustment: Embedded Varidesk Cube Plus 40

- I get it, it’s not slick. After looking at many other solutions and looking into design effort for a linear rail custom build, this is the best option for many reason. I’m happy to get into in a discussion. I will debrand it, that will help a little. Also if someone feels strongly, I’d welcome them making a custom top that’s less rounded, more alien/sleek.

Monitor mount: Ergotron LX. 

- Gas spring arm design allows most flexible positioning: Below viewlines (nearly flat), Below viewlines (GrandMA typical angle), Normal view angle (for set prep, not performance), Side of viewlines. I’m not open to static positioning (e.g [this](https://www.circlethreedesigns.com/monitor-fly-racks/2020/8/18/wfxhv2jemnytbc3e3h5kctglab98da)).
- An alternative is to use one of the newer magnetic mount very thin touch screen monitors. [17’ $800](https://eu.espres.so/products/espresso-pro-and-stand) (expensive - other normal monitor touch screen 21” for $350). Touch screen seems more interesting for lasers due to small UI elements in Chromatic vs Pangolin (for performance controls). Followup: The magnetic mount is too loose.

Vendors contacted:

| Vendor / Site | Via | Name | Answer |
| --- | --- | --- | --- |
| [royalcase.com](http://royalcase.com/) | Contact form
sales@royalcase.com
(844) 769-2538 | Hunter | Chose this vendor |
| [mentalcaseinc.com](http://mentalcaseinc.com/) | [matt@mentalcaseinc.com](mailto:matt@mentalcaseinc.com) | Matt | Declined on complexity / time (3 mo not enough) |
| [circlethreedesigns.com](http://circlethreedesigns.com/) | [info@CircleThreeDesigns.com](mailto:info@CircleThreeDesigns.com) |  | Declined on complexity |
| [roadcases.com](https://www.roadcases.com/) | [sales@roadcasesusa.com](mailto:sales@roadcasesusa.com) |  | Declined on complexity  |
| [allcases.com](http://allcases.com) | [william@allcases.com](mailto:william@allcases.com)  | Will | Was willing to do - slightly more expensive / longer lead time |