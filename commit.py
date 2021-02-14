from github import Github
import random
def multiple_commits(event,context):
    num_commits =  random.randint(0,12)
    g = Github("personal_access_token")
    repo = g.get_repo("repo_url")
    contents = repo.get_contents("README.md")
    for _ in range(num_commits):
        repo.update_file(contents.path, "lambda",\
             "lambda", contents.sha, branch="master")