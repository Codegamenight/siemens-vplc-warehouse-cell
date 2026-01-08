from ..vplc.fb import TON, SR

class Inputs:
    def __init__(self, start):
        self.start = start

class ConveyorCell:
    def __init__(self):
        self.run_latch = SR()
        self.timer = TON(2.0)

    def step(self, inp, dt):
        run = self.run_latch.update(inp.start, False)
        jam = self.timer.update(run, dt)
        return run, jam
