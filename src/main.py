from .vplc.scan import VPLC, ScanConfig
from .logic.cell import ConveyorCell, Inputs
from .comm.plc_transport import PLCConfig, MockTransport
from .comm.s7_dbmap import get_bool, set_bool, set_uint16

def main():
    transport = MockTransport(PLCConfig())
    
    # Create 4 cells
    cells = [ConveyorCell() for _ in range(4)]

    # Input states for each cell
    inputs = [Inputs(start=True) for _ in cells]

    def scan(dt):
        db = transport.read_db()
        prev_motor = False

        for i, cell in enumerate(cells):
            # Connect previous cell motor to current cell start
            if i > 0:
                inputs[i].start = prev_motor
            out = cell.step(inputs[i], dt)
            prev_motor = out.motor_run

            # Write outputs to DB
            set_bool(db, i*2, 0, out.motor_run)
            set_bool(db, i*2, 1, out.fault_active)
            set_uint16(db, i*2+2, out.fault_code)

            # Print state
            print(f"Cell{i+1} MOTOR={out.motor_run} FAULT={out.fault_active} CODE={out.fault_code}")

        transport.write_db(db)
        print("-"*40)

    plc = VPLC(ScanConfig(50), scan)
    plc.run()

if __name__ == "__main__":
    main()
