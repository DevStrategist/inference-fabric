# fabric

a self-writing inference fabric. a fleet of devin agents designs, compiles, and
continuously rewrites a datacenter-scale serving stack. not a wrapper. an
operating system for inference.

## architecture

```
oracle/   stride conflict predictor, hugepage aware
loom/     agent scheduler mutator, driven by perf counters
pool/     cxl style memory mesh over nvlink domains
gate/     sandbox contract + red team harness
bench/    reproducible windows, 4096 line sweeps
```

devin agents own `loom/` and `bench/` end to end. humans own `oracle/` and
`gate/` until the fleet earns them.

## first result

coherence oracle caught a stride conflict the baseline scheduler missed
completely:

```
p99 tail latency   143ms baseline -> 127ms oracle   (-11.2%)
window             stride-heavy, 4096 line sweep
```

## the loop

1. bench/ opens a reproducible serving window
2. loom/ mutates scheduler params against real perf counters
3. oracle/ predicts stride conflicts before kernel launch
4. gate/ verifies every mutation never leaves the sandbox contract
5. repeat nightly. the fabric writes itself.
