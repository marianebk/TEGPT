# WAN client-mode bridge

Hardware: https://www.amazon.com/gp/product/B0B4ZSR2PX/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1 (OpenWRT)
Location: TE Rack
Network: WAN
Notes: This gives the network rack it’s internet access. 

It’s configured as a client-mode WiFi interface, connected to EN1 (Internet / WAN) on the EdgeRouter.

It can connect to the WiFi at the warehouse or at event sites; It can connect to Starlink as a WiFi client, or even tether the entire rack to a portable LTE hotspot (such as a mobile phone’s Personal Hotspot feature, a MiFi device, or other LTE modem).