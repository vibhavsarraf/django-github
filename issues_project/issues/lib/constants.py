import os

githubGraphQLApi = 'https://api.github.com/graphql'
githubAccessToken = os.environ['GITHUB_TOKEN']
githubGraphQLHeaders = {"Authorization": "token %s" % (githubAccessToken)}
