# The MIT License (MIT)
# Copyright (c) 2020 Mike Teachman
# Copyright (c) 2021 Eric Moyer
# https://opensource.org/licenses/MIT

# Platform-specific MicroPython code for the rotary encoder module
# Raspberry Pi Pico implementation

# Documentation:
#   https://github.com/MikeTeachman/micropython-rotary

from RPi import GPIO
from rotary import Rotary


class RotaryIRQ(Rotary):
    def __init__(
        self,
        pin_num_clk,
        pin_num_dt,
        min_val=0,
        max_val=10,
        reverse=False,
        range_mode=Rotary.RANGE_UNBOUNDED,
        pull_up=False,
        half_step=False,
        invert=False
    ):
        super().__init__(min_val, max_val, reverse, range_mode, half_step, invert)

        if pull_up:
            GPIO.setup(pin_num_clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(pin_num_dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        else:
            GPIO.setup(pin_num_clk, GPIO.IN)
            GPIO.setup(pin_num_dt, GPIO.IN)

        self._pin_num_clk = pin_num_clk
        self._pin_num_dt = pin_num_dt

        self._hal_enable_irq()

    def _enable_clk_irq(self):
        GPIO.add_event_detect(self._pin_num_clk, GPIO.BOTH, callback=self._process_rotary_pins)

    def _enable_dt_irq(self):
        GPIO.add_event_detect(self._pin_num_dt, GPIO.BOTH, callback=self._process_rotary_pins)

    def _disable_clk_irq(self):
        GPIO.remove_event_detect(self._pin_num_clk)

    def _disable_dt_irq(self):
        GPIO.remove_event_detect(self._pin_num_dt)

    def _hal_get_clk_value(self):
        return GPIO.input(self._pin_num_clk)

    def _hal_get_dt_value(self):
        return GPIO.input(self._pin_num_dt)

    def _hal_enable_irq(self):
        self._enable_clk_irq()
        self._enable_dt_irq()

    def _hal_disable_irq(self):
        self._disable_clk_irq()
        self._disable_dt_irq()

    def _hal_close(self):
        self._hal_disable_irq()
