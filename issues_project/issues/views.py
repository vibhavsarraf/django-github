from django.shortcuts import render
from django.http import JsonResponse
from .lib.GithubUtility import GithubUtility
import json
from .lib.utils import getIssuesCount
import datetime
from django.utils import timezone


def fetchData(gitUtil):
    totalIssuesCount = gitUtil.getTotalIssuesCount()
    data = {}
    data['total'] = totalIssuesCount
    issues = gitUtil.getLast100Issues()
    curTime = timezone.now()
    prev24HourTime = curTime - datetime.timedelta(days=1)
    issuesWithin24HoursCount = getIssuesCount(issues, prev24HourTime, curTime)
    data['last24Hours'] = issuesWithin24HoursCount
    prev7DaysTime = curTime - datetime.timedelta(days=7)
    issues24HoursTo7Days = getIssuesCount(issues,
                                          prev7DaysTime,
                                          prev24HourTime)
    data['24HoursTo7Days'] = issues24HoursTo7Days
    issuesAfter7Days = totalIssuesCount - getIssuesCount(issues,
                                                         prev7DaysTime,
                                                         curTime)
    data['after7Days'] = issuesAfter7Days
    return data


'''
Return data about issues for a github repository.
@request.body should either contain "url" key or  "user" and "project" keys
'''


def issuesAPI(request):
    # try:
    data = request.body.decode('utf-8')
    gitUtil = GithubUtility(**json.loads(data))
    return JsonResponse(fetchData(gitUtil))
    # except Exception as e:
    # return JsonResponse({'error': str(e)})
