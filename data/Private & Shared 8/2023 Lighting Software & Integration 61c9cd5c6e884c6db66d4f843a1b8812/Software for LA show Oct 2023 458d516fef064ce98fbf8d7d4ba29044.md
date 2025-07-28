# Software for LA show Oct 2023

# Goal: TE DMX Channels

This is what we are attempting to build:

[https://docs.google.com/document/d/1j3uxW5kF_P8jmKfZRRQ6kExiIuevVXSpsOZN1wsyfRs/edit](https://docs.google.com/document/d/1j3uxW5kF_P8jmKfZRRQ6kExiIuevVXSpsOZN1wsyfRs/edit)

Patterns to reserve for Fish/Chris

Bass lighting. 

Arc edges

# Jeff Tasks

- [ ]  

# Look Tasks

- [ ]  Our APC40 driver: disable APC40’s Device controls (8 knobs on the right) from being mapped to active device. Test if it’s still mappable.
- [ ]  

# Tasks

- [x]  RECEIVE DMX INPUT
    - [x]  Update to latest Chromatik which includes an ArtNet input utility.
    - [x]  Add custom DMX modulators to handle the new input types (@Justin: Done)
- [x]  EFFECTS FOR DMX CONTROL
    - [x]  Speed input mapped to all the current patterns. (@Jon: Done, in PR #404)
    - [x]  Strobe effect
        - [x]  Whole-car strobe AKA “sync strobe”… will work with stock Strobe effect
        - [x]  Random Strobe (@Jon: working on this. Should have something tomorrow (10/12))
- [x]  OTHER CHANGES
    - [x]  Remove Color-Per-Channel to avoid problems (@Andrew Look, @Justin )
- [x]  ADDITIONAL TESTING
    - [x]  Consider PR #405 which fully deletes ColorCentral
    - [x]  Study our use of Views, does it conflict with the new LX Views?  Possible important changes will be needed here to avoid conflict.
        
        **Initial behavior looks fine.  We could use additional testing here.*
        
        - *Note the new LX Views utility under Left Pane > Model:*
            
            ![Untitled](Software%20for%20LA%20show%20Oct%202023%20458d516fef064ce98fbf8d7d4ba29044/Untitled.png)
            
- [ ]  PRE-SHOW
    - [x]  Pre-show: add the DMX modulators to a show file.
    - [ ]  Set up LXP file with patterns & channels for show (@Andrew Look)
- [ ]  OPTIONAL IDEAS
    - [ ]  (Optional) Add a global singleton with one button to create all the DMX modulators needed for the show, so they can easily be re-created.