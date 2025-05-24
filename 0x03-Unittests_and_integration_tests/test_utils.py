#!/usr/bin/env python3
"""Defines the TestAccessNestedMap,
TestGetJson subclasses of Unittest.TestCase
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Any, Mapping, Tuple, Dict

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Defines testcases for `access_nested_map`
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping[str, Any],
        path: Tuple[str, ...],
        expected: Any
    ) -> None:
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
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping[str, Any],
        path: Tuple[str, ...],
        expected: str
    ) -> None:
        """Test that access_nested_map raises KeyError with expected message.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(
                nested_map,
                path
            )
        self.assertEqual(
            str(cm.exception),
            expected
        )


class TestGetJson(unittest.TestCase):
    """Defines test cases for `get_json`
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(
        self,
        url: str,
        expected: Dict,
        mock_get: Mock
    ) -> None:
        """Test get_json
        """
        mock_response = Mock()
        mock_response.json.return_value = expected
        mock_get.return_value = mock_response

        result = get_json(url)
        self.assertEqual(result, expected)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Test class for `memoize`
    """
    @parameterized.expand([
        ("basic_memoize_test", 42)
    ])
    def test_memoize(
        self,
        name: str,
        expected: int
    ) -> None:
        """Tests memoization
        """
        class TestClass:

            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        test_obj: TestClass = TestClass()
        with patch.object(
            test_obj,
            'a_method',
            wraps=test_obj.a_method
        ) as mock_method:
            # Call the property twice
            result1: int = test_obj.a_property
            result2: int = test_obj.a_property

            # Check that the property returns the expected value
            self.assertEqual(result1, expected)
            self.assertEqual(result2, expected)

            # Assert a_method was called only once (memoization working)
            mock_method.assert_called_once()
