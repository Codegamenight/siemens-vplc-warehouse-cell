class TON:
    def __init__(self, pt_s):
        self.pt_s = pt_s
        self.et_s = 0.0
        self.q = False

    def update(self, inp, dt):
        if inp:
            self.et_s += dt
            if self.et_s >= self.pt_s:
                self.q = True
        else:
            self.et_s = 0.0
            self.q = False
        return self.q

class SR:
    def __init__(self):
        self.q = False

    def update(self, s, r):
        if r:
            self.q = False
        elif s:
            self.q = True
        return self.q
