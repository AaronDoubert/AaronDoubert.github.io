---
slug: electronics-labs
order: 5
title: Metal detector and audio equalizer
summary: A two-555 beat-frequency metal detector and a 3-band audio EQ.
context: ECE 20007
when: Spring 2026
tools: LTspice, bench
status: Complete
hero:
  src: ece-detector.jpg
  alt: Metal detector on the breadboard.
  caption: Metal detector on the breadboard.
  photo: true
shots:
  - src: ece-detector-b.jpg
    alt: Second half of the detector circuit.
    caption: Second half of the detector circuit.
    photo: true
  - src: ece-scope.jpg
    alt: Mixer output on the scope.
    caption: Mixer output on the scope, from my lab notebook.
    photo: true
  - src: ece-eq-sch.jpg
    alt: Three-band audio equalizer schematic.
    caption: 3-band audio equalizer schematic.
  - src: ece-eq-bode.jpg
    alt: Measured response of one equalizer band.
    caption: Measured response of one band.
---

The detector oscillated at 71 kHz against a 50 kHz target and the square-wave mixing didn't
beat cleanly, so the concept was proved in LTspice instead. The 3-band equalizer is the
cleaner piece of the two.
