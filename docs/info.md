# 1-bit Full Adder - Tiny Tapeout Project

This project implements a **1-bit full adder** using Verilog for the Tiny Tapeout platform.  
It takes three input bits and produces a **sum** and **carry-out** output.

---

## How it works

The design uses the lower 3 bits of `ui_in` as inputs:

- `A = ui_in[0]`
- `B = ui_in[1]`
- `Cin = ui_in[2]`

### Output mapping:
- `Sum  -> uo_out[0]`
- `Cout -> uo_out[1]`

All other output bits are tied to zero.

---

### Logic implementation

The full adder is implemented using arithmetic addition:
{cout, sum} = a + b + cin;

This means:
- `sum` is the least significant bit of the result
- `cout` is the carry-out bit

---

## How to test

The design is verified using a **Verilog testbench + cocotb simulation**.

### Testbench setup

The testbench:
- Instantiates the module `tt_um_full_adder`
- Dumps waveforms to `tb.vcd`
- Drives inputs via `ui_in`
- Observes outputs on `uo_out`

### Inputs tested

All 8 possible combinations of:
- A (0/1)
- B (0/1)
- Cin (0/1)

### Expected behavior

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 | 0   | 0   | 0    |
| 0 | 0 | 1   | 1   | 0    |
| 0 | 1 | 0   | 1   | 0    |
| 0 | 1 | 1   | 0   | 1    |
| 1 | 0 | 0   | 1   | 0    |
| 1 | 0 | 1   | 0   | 1    |
| 1 | 1 | 0   | 0   | 1    |
| 1 | 1 | 1   | 1   | 1    |

---

## Testbench details

The provided testbench:
- Generates a VCD waveform file (`tb.vcd`)
- Instantiates `tt_um_full_adder`
- Provides clock (`clk`), reset (`rst_n`), and enable (`ena`)
- Connects input/output buses for simulation

Tooling used:
- Verilog simulation (Icarus / Verilator compatible)
- Cocotb Python testbench
- GTKWave for waveform analysis

---

## External hardware

No external hardware is required.

The design is fully digital and runs entirely inside the Tiny Tapeout ASIC environment.
