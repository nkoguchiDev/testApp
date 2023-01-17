import requests


def get_pull_info(owner: str, repo: str, pull_num: int):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {settings.GIT_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28"}
    pulls = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_num}",
        headers=headers)
    return pulls
