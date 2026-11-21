# bench results — window 0001

window: stride-heavy, 4096 line sweep, simulated 8x h100
baseline scheduler vs fabric oracle+loom pass 1

| metric              | baseline | fabric p1 | delta   |
|---------------------|----------|-----------|---------|
| p99 tail latency    | 143.2ms  | 127.1ms   | -11.2%  |
| p50 latency         | 61.4ms   | 58.9ms    | -4.1%   |
| stride conflicts    | 412      | 61        | -85.2%  |
| unshared evictions  | 9,318    | 2,204     | -76.3%  |
| snoop traffic /win  | 38.2GB   | 31.7GB    | -17.0%  |

loom mutation pass 2 is queued for tonight. oracle predicted 94 of the top
100 conflicting strides before launch; the 6 it missed were all non-pow2.

# bench results — window 0002 (loom pass 2)

window: stride-heavy + mixed batch, 4096 line sweep
loom mutated: stride_hint 4096->16384, admission_alpha 0.5->0.25

| metric              | fabric p1 | fabric p2 | delta   |
|---------------------|-----------|-----------|---------|
| p99 tail latency    | 127.1ms   | 118.4ms   | -6.8%   |
| stride conflicts    | 61        | 19        | -68.9%  |
| snoop traffic /win  | 31.7GB    | 26.9GB    | -15.1%  |

two passes, two wins. the loop is working.
