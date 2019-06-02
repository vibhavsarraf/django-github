import requests
from .Issue import Issue
from .constants import githubGraphQLApi, githubGraphQLHeaders


def runGithubQuery(query):
    request = requests.post(githubGraphQLApi,
                            json={'query': query},
                            headers=githubGraphQLHeaders,)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(
            'GraphQl query failed, status: {}'.format(request.status_code)
        )


def getIssuesCount(issues, begin, end):
    return len(list(
        filter(lambda x: x.created_at > begin and x.created_at <= end,
               issues)
    ))
