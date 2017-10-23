#!/usr/bin/env python3
import sys
from pathlib import Path
import unittest
import itertools, re

sys.path.insert(0, str(Path(__file__).parent.parent))

from collections import OrderedDict

dict = OrderedDict

import cbrf
from cbrf import *


class Tests(unittest.TestCase):

	def testSimple(self):
		from cbrf import CentroBank
		cb=CentroBank()
		currencies = ("USD", "EUR")

		for c in currencies:
			print(cb.byISO[c])


if __name__ == "__main__":
	unittest.main()
