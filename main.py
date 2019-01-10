from cmd import Cmd
from timerModule import TimerModule
from issueModule import IssueModule
from workLogModule import WorkLogModule
import sys


class Main(Cmd):
    def __init__(self, usr, pw):
        super().__init__()
        self.time_spent_on_issue = {}
        self.timer_module = TimerModule()
        self.issue_module = IssueModule("https://jira.adeo.no/rest/api/2/", usr, pw)
        self.work_log_module = WorkLogModule()

    def preloop(self):
        print("")
        self.do_get_issues("")

    def run(self):
        self.cmdloop("enter something, unsure? try help")

    def do_exit(self, args):
        return True

    def do_start(self, should_print):
        if self.issue_module.get_active_issue() is None:
            print("Set issue before continuing")
            return
        self.timer_module.start(should_print)

    def do_end(self, comment):
        current_issue = self.issue_module.get_active_issue()
        if current_issue is None:
            print("Tried to end a timing session before an active issue had been started")

        start_time, time_spent = self.timer_module.end()
        if current_issue in self.time_spent_on_issue:
            self.time_spent_on_issue[current_issue] += time_spent
        else:
            self.time_spent_on_issue[current_issue] = time_spent
        self.work_log_module.log_work(current_issue, comment, time_spent, start_time)

    def emptyline(self):
        pass

    def do_list_issues(self, a):
        self.issue_module.list_issues()

    def do_get_issues(self, a):
        self.issue_module.get_issues()

    def do_set_active_issue(self, issue):
        self.issue_module.set_active_issue(issue)

    def do_commit_work(self, a):
        self.work_log_module.push_work_log()

    def do_show_active(self, a):
        self.issue_module.show_active_issue()

    def do_show_time_spent(self, issue_key):
        if issue_key != "":
            print(self.time_spent_on_issue[issue_key])
        else:
            for k, v in self.time_spent_on_issue.items():
                print(k + "\t", v)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Enter username and password")
    else:
        m = Main(sys.argv[0], sys.argv[1])
        m.run()
