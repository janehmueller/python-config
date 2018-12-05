from datetime import timedelta
from functools import reduce
from unittest import TestCase

from python_json_config.transformers import to_timedelta


class GenericTransformersTest(TestCase):

    def test_to_timedelta(self):
        self.assertEqual(to_timedelta("1:0:0:0"), timedelta(days=1))
        self.assertEqual(to_timedelta("0:1:0:0:0"), timedelta(days=1))
        self.assertEqual(to_timedelta("0:1:0:1:-60"), timedelta(days=1))
        self.assertEqual(to_timedelta("0:1:24:1:-60"), timedelta(days=2))

        deltas = [
            to_timedelta("0:0:0:0:90"),
            to_timedelta("0:0:0:58:30"),
            to_timedelta("0:1:23:0:00"),
            to_timedelta("0:5:0:0:60"),
            to_timedelta("1:0:0:0:-60")
        ]
        delta_sum = reduce(lambda delta1, delta2: delta1 + delta2, deltas)
        self.assertEqual(delta_sum, timedelta(weeks=2))

