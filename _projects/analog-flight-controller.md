---
slug: analog-flight-controller
order: 2
title: Analog flight controller
summary: Quadcopter PID loops computed in op-amps, not firmware.
context: Personal project
when: 2026
tools: KiCad, Simulink, ATtiny
status: In progress
current: Next rev shipping
repo: https://github.com/AaronDoubert/quadcopter-pid-boards
hero:
  src: afc-pcb.jpg
  alt: Rev B board, 90 by 210 mm, 4-layer.
  caption: Rev B — 90 × 210 mm, 4-layer, mounts on the frame.
shots:
  - src: afc-mounting.jpg
    alt: Board on the 5-inch frame with prop disks marked.
    caption: Board on the 5-inch frame; dashed circles are the prop disks. Every trimpot stays reachable.
  - src: afc-shim.jpg
    alt: The digital shim on a breadboard.
    caption: Digital shim on a breadboard — MPU-6050 into an ATtiny and DACs, probed with an Analog Discovery 3.
    photo: true
  - src: afc-roll-model.jpg
    alt: Roll axis as a Simscape circuit model.
    caption: Roll axis as a Simscape circuit model of the board.
  - src: afc-roll-step.jpg
    alt: Simulated roll step response.
    caption: Simulated roll step with the board model flying the quad.
---

Angle-to-rate loops on roll and pitch, rate-only on yaw, fed by an MPU-6050 through an
ATtiny1614 and MCP4822 DACs. Board history: v1 → rev A → rev B, plus an SMT variant.

<p class="note">Rev 3 is failing on the bench. Write up what failed and what the next rev
changes, and this paragraph goes away.</p>
