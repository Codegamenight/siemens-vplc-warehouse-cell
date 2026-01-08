import time

class ScanConfig:
    def __init__(self, scan_ms=50):
        self.scan_ms = scan_ms

class VPLC:
    def __init__(self, cfg, step_fn):
        self.cfg = cfg
        self.step_fn = step_fn

    def run(self):
        dt = self.cfg.scan_ms / 1000.0
        while True:
            self.step_fn(dt)
            time.sleep(dt)
