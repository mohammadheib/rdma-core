# SPDX-License-Identifier: (GPL-2.0 OR Linux-OpenIB)
# Copyright (c) 2023 Red Hat, Inc, All rights reserved.  See COPYING file

import unittest

BROADCOM_VENDOR_ID = 0x14E4
BNXT_RE_DEVS = {
	0x1605,  # BCM57454
	0x1606,  # BCM57454
	0x1614,  # BCM57454
	0x16C0,  # BCM57417
	0x16C1,  # BMC57414
	0x16CE,  # BMC57311
	0x16CF,  # BMC57312
	0x16D6,  # BMC57412
	0x16D7,  # BMC57414
	0x16D8,  # BMC57416
	0x16D9,  # BMC57417
	0x16DF,  # BMC57314
	0x16E2,  # BMC57417
	0x16E3,  # BMC57416
	0x16E5,  # BMC57314
	0x16ED,  # BCM57414
	0x16EB,  # BCM57412
	0x16EF,  # BCM57416
	0x16F0,  # BCM58730
	0x16F1,  # BCM57452
	0x1750,	 # BCM57508
	0x1751,	 # BCM57504
	0x1752,	 # BCM57502
	0x1803,	 # BCM57508 NPAR
	0x1804,	 # BCM57504 NPAR
	0x1805,	 # BCM57502 NPAR
	0x1807,	 # BCM5750x VF
	0x1809,  # BCM5750x Gen P5 VF HV
	0xD800,  # BCM880xx VF
	0xD802,  # BCM58802
	0xD804,  # BCM8804 SR
}


def is_bnxt_dev(ctx):
    dev_attrs = ctx.query_device()
    return dev_attrs.vendor_id == BROADCOM_VENDOR_ID and \
            dev_attrs.vendor_part_id in BNXT_RE_DEVS


def skip_if_bnxt_dev(ctx):
    if is_bnxt_dev(ctx):
        raise unittest.SkipTest('Skip this test for bnxt devices.')
