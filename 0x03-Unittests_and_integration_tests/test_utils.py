#!/usr/bin/env python3
"""Defines the TestAccessNestedMap subclass of Unittest.TestCase
"""

import unittest
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Defines testcases for `access_nested_map`
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test method for `access_nested_map`
        """
        self.assertEqual(
            access_nested_map(
                nested_map,
                path
            ),
            expected
        )

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_nested_map_exception(self, nested_map, path, expected):
        """Test exceptions
        """
        try:
            self.assertRaises(
                access_nested_map(
                    nested_map,
                    path
                ),
                expected
            )
        except Exception:
            pass
