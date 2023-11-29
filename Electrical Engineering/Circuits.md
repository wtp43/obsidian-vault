---
dg-publish: true
tags: 
created: ""
---
---

# Circuits

### Reading Schematics
https://learn.sparkfun.com/tutorials/how-to-read-a-schematic/all

## Using a Multimeter
https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter/continuity

### Checking for Continuity
- When system is on: check that the voltage between VCC and GND is at the correct level 
- When system is off: check that there is no short between VCC and GND. If there is continuity (a short exists somewhere)

**Continuity and large capacitors:** During normal troubleshooting. you will be probing for continuity between ground and the VCC rail. This is a good sanity check before powering up a prototype to make sure there is not a short on the power system. But don't be surprised if you hear a short 'beep!' when probing. This is because there is often significant amounts of capacitance on the power system. The multimeter is looking for very low resistance to see if two points are connected. Capacitors will act like a short for a split second until they fill up with energy, and then act like an open connection. Therefore, you will hear a short beep and then nothing. That's ok, it's just the caps charging up.
