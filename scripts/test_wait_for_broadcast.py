#!/usr/bin/python

import sys
import logging

import antagent.ant as ant
import antagent.hw as hw

logging.basicConfig(
        level=logging.DEBUG,
        out=sys.stderr,
        format="%(asctime)s %(levelname)s %(message)s")

_LOG = logging.getLogger()

dev = hw.UsbHardware()
core = ant.Core(dev)
session = ant.Session(core)
try:
    channel = session.channels[0]
    network = session.networks[0]
    network.set_key("\xa8\xa4\x23\xb9\xf5\x5e\x63\xc1")
    channel.assign(channel_type=0x00, network_number=0)
    channel.set_id(device_number=0, device_type_id=0, trans_type=0)
    channel.set_period(0x1000)
    channel.set_search_timeout(255)
    channel.set_rf_freq(50)
    channel.set_search_waveform(0x0053)
    channel.open()
    print channel.read_broadcast(timeout=30).encode("hex")
finally:
    try: session.reset_system()
    except: _LOG.warning("Caught exception while resetting system.", exc_info=True)


# vim: ts=4 sts=4 et
