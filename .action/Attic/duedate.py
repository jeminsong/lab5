
from logger import setup_logger
import subprocess
from datetime import date
from datetime import datetime

def days_late(due_date_isoformat, last_commit_isoformat):
    """Calculate the number of days late given to ISO 8601 datetime strings"""
    due_date = datetime.fromisoformat(due_date_isoformat)
    last_commit = datetime.fromisoformat(last_commit_isoformat)
    late = last_commit - due_date
    return late.days

# def last_commit_to_main_reflog(repository_path):
#     repo = git.Repo(repository_path)
#     try:
#         main = repo.heads.main
#     except AttributeError as e:
#         print(f'The repo you are working with {repository_path} does not have a main branch. Using master.')
#         main = repo.heads.master
#         # heads = repo.heads
#         # print(heads)
#         # return
#     log = main.log()
#     last_log = log[-1]
#     return last_log

def last_commit_to_main_reflog(repository_path):
    logger = setup_logger()
    cmd = f'git -C "{repository_path}" log -1 --format=%cs'
    logger.debug(cmd)
    status = True
    proc = subprocess.run(
        [cmd],
        capture_output=True,
        shell=True,
        timeout=15,
        check=False,
        text=True,
    )
    last_commit_date = '1969-01-01'
    if proc.stdout:
        last_commit_date = str(proc.stdout).rstrip("\n\r")
    if proc.stderr:
        logger.debug('stderr: %s', str(proc.stderr).rstrip("\n\r"))
    if proc.returncode != 0:
        status = False
    return (status, last_commit_date)

def seconds_since_epoch_to_isoformat(seconds):
    d = date.fromtimestamp(seconds)
    return d.isoformat()