import requests


class Issue:
    def __init__(self, issue):
        self.issue_id = ""
        self.long_name = ""
        self.key = ""
        self.logged_work = 0

        if "fields" in issue:
            fields = issue["fields"]
            if "summary" in fields:
                self.long_name = fields["summary"]

        self.issue_id = issue["id"]
        self.key = issue["key"]


class IssueModule:
    def __init__(self, url, username, pw):
        self.active_issue = None
        self.issues_key = {}
        self.issues_id = {}
        self.jira_url = url
        if self.jira_url == "":
            self.jira_url = "https://jira.adeo.no/rest/api/2/"
        self.username = username
        self.pw = pw
        self.work_log = {}
        self.log_id = 0

    def get_issues(self):
        response = requests.get(self.jira_url + "search?jql=assignee=" + self.username)
        for issue in response.json()["issues"]:
            self.issues_key[issue["key"]] = Issue(issue)
            self.issues_id[issue["id"]] = Issue(issue)
        print("Updated issues")

    def list_issues(self):
        for index, issue in self.issues_key.items():
            print(index + "\t" + issue.long_name)

    def set_active_issue(self, issue):
        if issue not in self.issues_key and issue not in self.issues_id:
            print("Did not find the target issue: %s" % issue)
            print("Check key or id provided")
        else:
            self.active_issue = self.issues_key[issue]

    def show_active_issue(self):
        if self.active_issue is None:
            print("No active issues")
        else:
            print(self.active_issue.key + "\t" + self.active_issue.long_name)

    def get_active_issue(self):
        return self.active_issue
