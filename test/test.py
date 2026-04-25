# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_full_adder(dut):
    dut._log.info("Starting Gate-level Hardend Simulation..")
    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await Timer(50,unit="ns")
    dut.rst_n.value = 1
    await Timer(50,unit="ns")
    
    test_cases = [
        (0,0,0,0,0),
        (1,1,0,0,1),
        (1,1,1,1,1),
        (1,0,0,1,0)
    ]

     dut._log.info("Test project behavior")

    # Set the input values you want to test
    for a,b,c,e_sum,e_cout in test_cases:
    dut.ui_in.value = (c << 2) | (b << 1) | a
    

    # Wait for one clock cycle to see the output values
    await Timer(20,units="ns")

   try:
       output_val = int(dut.uo_out.value)
       actual_sum =output_val & 1
       actual_cout =(output_val >> 1) & 1

    assert actual_sum == e_sum, f"Sum Error: A={a} B={b} C={c}"
    assert actual_cout == e_cout,f"Cout Error: A={a} B={b} C={c}"
    dut._log.info(f"Input: {a},{b},{c} -> Sum: {actual_sum}, Carry: {actual_carry} [PASS]")

except ValueError:
dut._log.error(f"Logic error: uo_out is {str(dut.uo_out.value)}"]
raise
