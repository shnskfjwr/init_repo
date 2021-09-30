# init_repo

GitHubのリポジトリに対し、以下の初期設定を行うスクリプトです。

- develop、staging、main(master)ブランチの削除保護有効化&レビュー必須化
- PRがマージされた際の作業ブランチの自動削除

大量のリポジトリに1つ1つ保護設定を入れていくのが面倒だったので作成しました。

## 前提条件
- 作業端末にpipenvがインストール済みであること
- 初期設定したいリポジトリの管理者権限を持つGitHubパーソナルアクセストークンが払い出し済みであること
- 初期設定したいリポジトリのオーナーがPro、Team、Enterpriseユーザーであること

## 実行方法

```bash
# 初期インストール
export PIPENV_VENV_IN_PROJECT=true
pipenv install

# 環境変数設定
cp .env_example .env

# GITHUB_TOKENとSEARCH_WORDを設定

pipenv shell
python init_repo.py

```

