import os
from dotenv import load_dotenv
from github import Github

load_dotenv()
g = Github(os.environ['GITHUB_TOKEN'])


def handler():
    # アクセス可能な全リポジトリから特定文字列を含むリポジトリを抽出
    for repo in g.get_user().get_repos():
        if os.environ['SEARCH_WORD'] in repo.name:
            initialize(repo)


def initialize(repo):

    # PRマージ後のブランチ削除を有効化
    repo.edit(
        delete_branch_on_merge=True
    )

    # ブランチ保護
    targets = ['develop', 'staging', 'main', 'master']
    for branch in repo.get_branches():
        if branch.name in targets:
            # 保護の有効化
            branch.edit_protection()
            # PRの必須化
            branch.edit_required_pull_request_reviews(
                required_approving_review_count=1,
                dismiss_stale_reviews=True
            )

    print(f'{repo.name}: 初期化完了')


if __name__ == '__main__':
    handler()
