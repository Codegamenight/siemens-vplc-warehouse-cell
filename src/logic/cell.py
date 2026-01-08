from ..vplc.fb import TON, SR

class Inputs:
    def __init__(self, start=False, stop=False, pe1=False, pe2=False, estop=False):
        self.start = start
        self.stop = stop
        self.pe1 = pe1
        self.pe2 = pe2
        self.estop = estop

class Outputs:
    def __init__(self):
        self.motor_run = False
        self.fault_active = False
        self.fault_code = 0


class ConveyorCell:
    def __init__(self):
        self.motor_latch = SR()
        self.jam_timer = TON(2.0)  # Jam detection
        self.outputs = Outputs()

    def step(self, inp: Inputs, dt: float) -> Outputs:
        # Emergency stop has highest priority
        if inp.estop:
            self.outputs.motor_run = False
            self.outputs.fault_active = True
            self.outputs.fault_code = 999
            return self.outputs

        # Start/Stop logic
        self.outputs.motor_run = self.motor_latch.update(inp.start and not inp.stop, inp.stop)

        # Jam detection
        jam = self.jam_timer.update(self.outputs.motor_run and inp.pe1 and not inp.pe2, dt)
        if jam:
            self.outputs.fault_active = True
            self.outputs.fault_code = 101

        return self.outputs

