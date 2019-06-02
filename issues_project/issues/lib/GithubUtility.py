from .utils import runGithubQuery
from .Issue import Issue
from django.utils.dateparse import parse_datetime


class GithubUtility:
    def _parseGithubUrl(self, url):
        try:
            info = url[url.rfind('github.com'):].split('/')
            self.user = info[1]
            self.project = info[2]
        except IndexError:
            raise Exception('Wrong Url format given to GithubUrl constructor')

    def __init__(self, url=None, user=None, project=None):
        if url:
            self._parseGithubUrl(url)
        else:
            if(not user or not project):
                raise Exception('Improper GithubUrl constructor call')
            self.user = user
            self.project = project

    def getTotalIssuesCount(self):
        query = '''
        {
            repository(owner: "%s", name: "%s") {
                issues(states: OPEN) {
                    totalCount
                }
            }
        }
        ''' % (self.user, self.project)
        resp = runGithubQuery(query)
        return resp['data']['repository']['issues']['totalCount']
        # url = self.githubApiUrl + self.user + '/' + self.project + '/issues'
        # return fetchIssues(url).__len__()

    def getLast100Issues(self):
        query = '''
        {
            repository(owner: "%s", name: "%s") {
                issues(last: 100, states: OPEN) {
                    nodes {
                        createdAt
                    }
                }
            }
        }
        ''' % (self.user, self.project)
        resp = runGithubQuery(query)
        results = resp['data']['repository']['issues']['nodes']
        issues = []
        for issue in results:
            issues.append(Issue(parse_datetime(issue['createdAt'])))
        return issues
