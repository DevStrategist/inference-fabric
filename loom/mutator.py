"""loom: agent-driven scheduler mutator.

each night the fleet opens a bench/ window, mutates scheduler parameters,
and keeps whatever survives gate/'s sandbox contract with better p99.
"""
import json, subprocess, sys

PARAM_SPACE = {
    "stride_hint":      [2 ** i for i in range(6, 22)],
    "evict_unshared":   [True, False],
    "hugepage_aware":   [True, False],
    "admission_alpha":  [0.1, 0.25, 0.5, 0.75, 0.9],
}

def run_window(cfg):
    out = subprocess.run(
        ["./bench/sweep", "--lines", "4096", *sum(
            (["--%s" % k, str(v)] for k, v in cfg.items()), [])],
        capture_output=True, text=True)
    return json.loads(out.stdout)["p99_ms"]

def mutate(best_cfg, best_p99):
    for key, vals in PARAM_SPACE.items():
        for v in vals:
            cfg = dict(best_cfg, **{key: v})
            p99 = run_window(cfg)
            if p99 < best_p99 * 0.98:   # keep only real wins
                return cfg, p99
    return best_cfg, best_p99

if __name__ == "__main__":
    cfg, p99 = mutate(json.loads(sys.argv[1]), float(sys.argv[2]))
    print(json.dumps({"cfg": cfg, "p99_ms": p99}))
