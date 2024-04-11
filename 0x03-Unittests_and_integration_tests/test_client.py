#!/usr/bin/env python3
"""Unittests and integration tests module
"""
import unittest
from unittest.mock import PropertyMock, patch

from parameterized import parameterized
client = __import__("client")


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json):
        """test_org method
        """
        my_client = client.GithubOrgClient(org)
        my_client.org
        my_client.org

        mock_get_json.assert_called_once()

    @parameterized.expand([
        ("google", True),
        ("abc", False)
    ])
    def test_public_repos_url(self, org: str, expected: bool):
        """test_public_repos_url method
        """
        with patch(
                "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": expected}
            my_client = client.GithubOrgClient(org)
            self.assertEqual(my_client._public_repos_url, expected)
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """test_public_repos method
        """
        payload = {
            "repo_url": "mimi",
            "repos": [
                {"name": "candle", "licence": None},
                {"name": "vanilla", "licence": None},
                {"name": "chocolate", "licence": None},
            ]
        }
        mock_get_json.return_value = payload["repos"]

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = payload["repo_url"]

            my_client = client.GithubOrgClient("")
            self.assertEqual(my_client.public_repos(None), [
                             "candle", "vanilla", "chocolate"])

            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("mimi")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, licence_key, expected):
        """test_has_license method
        """
        self.assertEqual(client.GithubOrgClient.has_license(
            repo, licence_key), expected)
