# EDC Software Status

- [x]  Two-part upgrade to LX Framework
    - [x]  Upgrade to LX 0.4.2 (Status: pending merge from mcslee’s branch)
- [x]  Common pattern base class for VJ usability
    - [x]  Choose common parameters
    - [x]  Build a common base class to be used by all TE patterns (TEPerformancePattern)
    - [x]  Make common controls available to shader patterns
- [ ]  Beat Reactivity
    - [x]  Determine standard method for patterns to access LX tempo/beat information.  Add methods to base class?  (Discussed 4/11/23 as ready to use.)
    - [ ]  Example patterns
    - [ ]  Add to as many patterns as possible
- [ ]  **Major Pattern Refactor  **People can jump in here****
    - [ ]  Remove custom parameters from existing patterns and instead use TEPerformancePattern get functions such as `getSpeed()` `getSize()` etc.
    - [ ]  All patterns should pull color from `TEPerformancePattern.getCurrentColor()`
    - [ ]  Use beat reactivity wherever possible. *Examples: [*someone list examples here]*
    - [x]  Track progress on:
        
        [Pattern Prioritization](https://www.notion.so/f9a0be60ec344587b96f58e6e948f712?pvs=21)
        
- [x]  Parameter ordering for midi controllers (in progress) (not a prerequisite to pattern work)
    
    [Parameter layout on the MidiFighterTwister](EDC%20Software%20Status%2087a2e9a4cb7e4f7490de959da3f24d33/Parameter%20layout%20on%20the%20MidiFighterTwister%202ce7012a82d64ff5a123f8ce106e487b.md)
    
- [x]  Standardize use of Color by TEPerformancePattern (in progress)
- [x]  Buy hardware for FoH at EDC
    - [x]  APC40mkII
    - [x]  MidiFighter64
    - [x]  Midi over network extension (BomeBox)
    - [x]  2x MidiFighterTwisters (@INACTIVE Keegan 2 already has?) (ordered 4/2)
- [x]  Integration of DJ decks / LX / Lasers
    - [x]  Network adjustments to be Pioneer-friendly (@Jeff )
    - [x]  Color to lasers all the time, not just with AutoVJ running
- [ ]  Pre-show testing & adjustments
    - [x]  Confirm ability to use hardwire ethernet for EDC (@Jeff)
    - [x]  Test midi latency w/ BomeBox
        - [x]  Retain option to run LX computer at FoH if needed (@Jeff )
    - [ ]  Tune parameter ranges/exponents for playability, for each pattern
- [ ]  Showtime Checklist
    - [ ]  Add NoGapEffect to Master channel on .lxps
    - [ ]  User preferences: Select active pattern = true, focus channel on cue = true
    - [ ]  Map APC40 button to AutoVJ enable/disable
    - [ ]  Test that AutoVJ works with ShowKontrol / MaxMSP

- [ ]  ITEMS FOR AFTER EDC
    - [ ]  ~~Upgrade to Chromatik (new LX with latest features and easiest future updates)~~ → Now to do after EDC
    - [ ]  Upgrading to Chromatik will break the TE ui overlays for vertices and panels.  Need to export a .jar from the old version for troubleshooting the car
    - [ ]  ~~Ongoing eval of BeatLinkTrigger to cover functionality including that currently provided by ShowKontrol~~ → Now after EDC