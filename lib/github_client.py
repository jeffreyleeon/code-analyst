import re

def _is_valid_github_url(url):
    try:
        return re.search(r'https://github.com/[\S]+/[\S]+', url) is not None
    except Exception:
        return False

class GithubClient(object):

    def __init__(self, github_url=None):
        if github_url is None:
            raise Exception('GithubClient: please provide valide github url.')
        if _is_valid_github_url(github_url) is False:
            raise Exception('GithubClient: url {} is not a valid github url, please follow pattern {}'.format(
                url,
                'https://github.com/jeffreyleeon/code-analyst'
            ))
        self.url = github_url
