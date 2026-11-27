---
slug: ailerons-flaps
order: 1
title: PART ailerons and flaps
summary: Hinge-moment sizing and printed construction for a 95 m/s airframe.
context: Purdue Aerial Robotics
when: Fall 2026
tools: Onshape, Python
status: In progress
current: PART · Fall 2026
hero:
  src: cs-flap.jpg
  alt: Flap shell, inside face, showing the internal triangular ribs.
  caption: Flap shell, inside face — triangular ribs carrying load into the hinge line.
shots:
  - src: cs-flap-horn.jpg
    alt: Flap horn end with control horn, hinge bushing and an M2 screw.
    caption: Horn end — control horn, hinge bushing, M2 screw into a heat-set insert.
  - src: cs-flap-xray.jpg
    alt: Flap with the skin made see-through, showing ribs, inserts and horn.
    caption: Skin made see-through — ribs, inserts and horn together.
  - src: cs-aileron-xray.jpg
    alt: Aileron with the skin made see-through.
    caption: Aileron, skin see-through — ribs, bronze hinge bushing, heat-set inserts.
  - src: cs-aileron-hinge.jpg
    alt: Aileron hinge end with bushing and M2 screws.
    caption: Aileron hinge end — bushing and M2 screws into heat-set inserts.
  - src: cs-aileron.jpg
    alt: Aileron construction.
    caption: Aileron construction.
  - src: cs-flap-section.jpg
    alt: Flap end view showing the hinge eye and overlapping skin.
    caption: Flap end view — hinge eye and overlapping skin.
  - src: cs-in-wing.jpg
    alt: Aileron placed in the wing structure.
    caption: Aileron placed in the wing structure.
    full: true
---

<h3>Servo sizing</h3>

Hinge moments from a linearized thin-airfoil flap model (Roskam Part VI) at FAR 23 load
factors — n = 10/3 rolling, n = 2 flaps down. Ruddervator modelled as a flat plate at its
total angle to the flow, including an 8 m/s gust.

<table>
  <thead>
    <tr><th>Surface</th><th>Worst case</th><th class="n">Servo torque</th></tr>
  </thead>
  <tbody>
    <tr><td>Aileron</td><td>95 m/s, 25° trailing edge down</td><td class="n">13.5 kgf·cm</td></tr>
    <tr><td>Ruddervator</td><td>95 m/s, 25°, 8 m/s gust</td><td class="n">10.2 kgf·cm</td></tr>
    <tr><td>Flap</td><td>40 m/s, 40° down</td><td class="n">4.1 kgf·cm</td></tr>
  </tbody>
</table>

<h3>Construction</h3>

Printed shells with internal triangular ribs, turning on a bronze sleeve bushing at the hinge
line. Control horn bolts on with M2 screws into heat-set inserts.
