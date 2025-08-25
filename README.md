# mkdoc_site001

## 概要

- MkDocsとMaterialテーマを用いた静的サイト生成環境
- カテゴリごとにMarkdown記事を自動生成
- 設定やビルド、プレビュー、git管理までAIが自動化

## 目的

AIによるドキュメントサイト構築のやりやすさ・自動化の検証

## 環境再現手順


1. Python 3.13以降をインストール

2. 必要なパッケージをインストール（コマンド例）

	```sh
	pip install mkdocs mkdocs-material
	pip install -e .
	```

	※このリポジトリ直下で実行してください（自作プラグイン有効化のため）

3. サイトのビルド

	```sh
	mkdocs build
	```

4. ローカルプレビュー（例: ポート6283で起動）

	```sh
	mkdocs serve -a 127.0.0.1:6283
	```

5. `site/` フォルダをWebサーバーにアップロード

---

このREADMEもAIによって自動生成されています。
4. `site/` フォルダをWebサーバーにアップロード

---

このREADMEもAIによって自動生成されています。
