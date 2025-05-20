#!/usr/bin/env python3
"""Defines TestGithubOrgClient
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json) -> None:
        """Test that GithubOrgClient.org returns correct value
           and calls get_json once with correct URL
        """
        # Arrange dummy JSON response
        mock_get_json.return_value = {"some": "payload"}

        # Act
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(
            result,
            mock_get_json.return_value
        )

    def test_public_repos_url(self) -> None:
        """Test GithubOrgClient._public_repos_url
           returns expected URL from mocked org property
        """

        # Known payload to be returned by mocked org property
        fake_org_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "other_key": "other_value"
        }

        client = GithubOrgClient("google")

        with patch.object(
            GithubOrgClient,
            "org",
            new=property(lambda self: fake_org_payload)
        ):

            # Access the _public_repos_url property
            result = client._public_repos_url

            # Assert the property returns the repos_url
            # from mocked org payload
            self.assertEqual(
                result,
                fake_org_payload["repos_url"]
            )
