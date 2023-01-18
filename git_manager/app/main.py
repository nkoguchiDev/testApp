import requests


class Settings:
    GIT_API_ENDPOINT: str = "https://api.github.com"
    GIT_API_TOKEN: str = ""
    GIT_API_HEADERS: dict = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GIT_API_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28"}


settings = Settings()


def get_pull_info(owner: str, repo: str, pull_num: int) -> list:
    pulls = requests.get(
        f"{settings.GIT_API_ENDPOINT}/repos/{owner}/{repo}/pulls/{pull_num}",
        headers=settings.GIT_API_HEADERS)
    return pulls.json()


def get_pull_file_diff(owner: str, repo: str, pull_num: int) -> list:
    pulls = requests.get(
        f"{settings.GIT_API_ENDPOINT}/repos/{owner}/{repo}/pulls/{pull_num}/files",
        headers=settings.GIT_API_HEADERS)
    return pulls.json()
