"""Additional functions to the class tasklib.TaskWarrior."""

from tasklib import TaskWarrior


class TasktualWarrior(TaskWarrior):
    """An enhanced version of Taskwarrior with additional functionality."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_reports(self) -> list[str]:
        """Return a list of reports.

        Executes the command `task reports` and returns the report names in a list.
        """
        tw_output = self.execute_command(["reports"])
        reports = []
        for report_line in tw_output[3:-2]:
            reports.append(report_line.split(" ")[0])
        return reports

    def get_projects(self) -> list[str]:
        """Return a list of projects or empty list.

        Executes the command `task _projects` and returns the project names in a list.
        """
        return self.execute_command(["_projects"])

    def get_tags(self) -> list[str]:
        """Return a list of tags (virtual and normal) or an empty list.

        Executes the command `task _tags` and returns the tag names in a list.
        """
        return self.execute_command(["_tags"])
