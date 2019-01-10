import json


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WorkLogIdIncrementer(metaclass=Singleton):
    def __init__(self):
        self.current_id = 0

    def get_id(self):
        new_id = self.current_id
        self.current_id += 1
        return new_id


class WorkLogEntry():
    def __init__(self, comment, time_spent, time_started):
        self.id_generator = WorkLogIdIncrementer()
        self.log_id = self.id_generator.get_id()
        self.comment = comment
        self.time_spent = time_spent
        self.time_started = time_started


class WorkLogModule:
    def __init__(self):
        self.work_log = {}

    def log_work(self, issue_key, comment, time_spent, time_started):
        if issue_key in self.work_log:
            self.work_log[issue_key].append(WorkLogEntry(comment, time_spent, time_started))
        else:
            self.work_log[issue_key] = [WorkLogEntry(comment, time_spent, time_started)]

    def get_work_log(self):
        return self.work_log

    def get_work_log_on_issue(self, issue_key):
        if issue_key in self.work_log:
            return issue_key
        else:
            print("No work log found for issue %s" % issue_key)

    def push_work_log(self):
        for key, val in self.work_log.items():
            payload = json.dumps({
                "comment": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": val.comment
                                }
                            ]
                        }
                    ]
                },
                "visibility": {
                    "type": "group",
                    "value": "jira-developers"
                },
                "started": val.time_started,
                "timeSpentSeconds": val.time_spent
            })
