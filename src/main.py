from .vplc.scan import VPLC, ScanConfig
from .logic.cell import ConveyorCell, Inputs

def main():
    cell = ConveyorCell()

    def scan(dt):
        run, jam = cell.step(Inputs(start=True), dt)
        print(f"RUN={run} JAM={jam}")

    plc = VPLC(ScanConfig(50), scan)
    plc.run()

if __name__ == "__main__":
    main()

