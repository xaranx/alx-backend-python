
#!/usr/bin/env python3
"""Unittests and integration tests module
"""
from typing import Any, Mapping, Sequence
import unittest
from unittest.mock import patch
from parameterized import parameterized

access_nested_map = __import__("utils").access_nested_map
memoize = __import__("utils").memoize
utils = __import__("utils")


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected: Any):
        """test_access_nested_map method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Mapping):
        """test_get_json method
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(utils.get_json(url), payload)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """TestMemoize class
    """

    def test_memoize(self):
        """test_memoize method
        """

        class TestClass:
            """TestClass class
            """
            def a_method(self):
                """a_method method
                """
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as test_a_method:
            test_a_method.return_value = 42

            my_object = TestClass()
            my_object.a_property
            my_object.a_property

            test_a_method.assert_called_once()

