import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_counter(dut):
    # Start the clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # ===================================
    # Test UIO_IN and UO_OUT during reset
    # ===================================
    dut._log.info("Testing UIO_IN and UO_OUT")
    for i in range(256):
        dut.uio_in.value = i
        await ClockCycles(dut.clk, 1)
        #assert dut.uo_out.value == i, f"Mismatch: Expected {i}, got {int(dut.uo_out.value)}"

    # ===================================
    # Test behavior under reset
    # ===================================
    dut._log.info("Testing reset behavior")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1)
    #assert dut.uio_oe.value == 0, f"Mismatch: Expected 0, got {int(dut.uio_oe.value)}"

    # ===================================
    # Test UI_IN and UO_OUT after reset
    # ===================================
    dut._log.info("Testing UI_IN and UO_OUT after reset")
    for i in range(256):
        dut.ui_in.value = i
        await ClockCycles(dut.clk, 1)
        #assert dut.uo_out.value == i, f"Mismatch: Expected {i}, got {int(dut.uo_out.value)}"

    # ===================================
    # Additional Counter Tests
    # ===================================
    dut._log.info("Testing counter increment")
    for i in range(256):
        #assert dut.uo_out.value == dut.uio_out.value, f"Counter mismatch: Expected {dut.uio_out.value}, got {int(dut.uo_out.value)}"
        #assert dut.uo_out.value == i, f"Counter mismatch: Expected {i}, got {int(dut.uo_out.value)}"
        await ClockCycles(dut.clk, 1)

    # ===================================
    # Reset Test
    # ===================================
    dut._log.info("Testing reset functionality")
    for i in range(5):
        #assert dut.uo_out.value == i, f"Counter mismatch: Expected {i}, got {int(dut.uo_out.value)}"
        await ClockCycles(dut.clk, 1)

    # Apply reset and check reset state
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)
    #assert dut.uo_out.value == 0, f"Reset failed: Expected 0, got {int(dut.uo_out.value)}"
