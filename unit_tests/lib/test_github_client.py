# Import system libraries
import os
import sys

# Import 3rd party libraries
import pytest

# Import custom libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
import lib.github_client as github_client

def test_is_valid_github_url():
    assert github_client._is_valid_github_url(None) == False
    assert github_client._is_valid_github_url('') == False
    assert github_client._is_valid_github_url(1) == False
    assert github_client._is_valid_github_url([]) == False
    assert github_client._is_valid_github_url({}) == False
    assert github_client._is_valid_github_url('https://github.com/jeffreyleeon/code-analyst') == True
    assert github_client._is_valid_github_url('https://github.com/jeffreyleeon/code-analyst/') == True
    assert github_client._is_valid_github_url('https://github.com/jeffreyleeon/code-analyst/some-behind') == True
    assert github_client._is_valid_github_url('http://github.com/jeffreyleeon/code-analyst/') == False
    assert github_client._is_valid_github_url('https://somedomain.com/jeffreyleeon/code-analyst/') == False
    assert github_client._is_valid_github_url('https://somedomain/jeffreyleeon/code-analyst/') == False
    assert github_client._is_valid_github_url('https://somedomain.com//code-analyst/') == False
    assert github_client._is_valid_github_url('https://somedomain.com/jeffreyleeon/') == False
    assert github_client._is_valid_github_url('https://somedomain.com///') == False

def test_github_client_init():
    with pytest.raises(Exception):
        github_client.GithubClient(None)
    with pytest.raises(Exception):
        github_client.GithubClient('')
    with pytest.raises(Exception):
        github_client.GithubClient(1)
    with pytest.raises(Exception):
        github_client.GithubClient([])
    with pytest.raises(Exception):
        github_client.GithubClient({})
    github_client.GithubClient('https://github.com/jeffreyleeon/code-analyst')
    github_client.GithubClient('https://github.com/jeffreyleeon/code-analyst/')
    with pytest.raises(Exception):
        github_client.GithubClient('http://github.com/jeffreyleeon/code-analyst/')
    with pytest.raises(Exception):
        github_client.GithubClient('https://github.com//code-analyst/')
    with pytest.raises(Exception):
        github_client.GithubClient('https://github.com/jeffreyleeon/')
    with pytest.raises(Exception):
        github_client.GithubClient('https://github.com///')
