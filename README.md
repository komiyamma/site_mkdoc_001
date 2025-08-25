

# mkdoc_site001
このリポジトリの構成や設定例（mkdocs など）はあくまで一例です。ご自身の用途や好みに合わせて自由に書き換えてご利用ください。
特に、`mkdocs.yml` の内容もプロジェクト例として記載しています。必要に応じて自由に編集・カスタマイズしてください。


## サイト構成テンプレートについて

## 各記事（.md）ファイルの先頭に記述できる主な項目（MkDocs標準仕様）

MkDocsでは、各Markdownファイルの先頭に「メタデータ（front matter）」を記述することで、記事ごとにタイトルや日付などの情報を持たせることができます。

### MultiMarkdownスタイルメタデータ
```markdown
Title: 記事タイトル
Date: 2025-08-26

# 記事タイトル

本文...
```

- `title` … 記事タイトル（`nav`で指定がなければこれが使われる）
- `date` … 日付（任意。テーマやテンプレートで利用可）

> ※ `summary` や `author` などは、このカスタム環境では別定義から参照されるため、front matter には記述不要です。

---

このリポジトリは、MkDocsによる静的サイトのテンプレートです。
サンプル記事やカテゴリはダミーであり、自由に差し替えてご利用ください。
記事・カテゴリの構成例や運用例を示すための雛形となっています。

## 概要

このリポジトリは、カスタマイズ重視のMkDocsサイト構築環境です。  
AI（GitHub Copilot）による自動化・独自拡張を取り入れ、以下の特徴を持ちます。

---

## 主な特徴

- **記事ごとの.memoファイルによるdescription自動化**  
	各Markdown記事と同名・同階層に`.memo`ファイルを配置し、記事のdescriptionやOGP、構造化データに自動反映します。

- **自作MkDocsプラグインのローカルパッケージ化**  
	`setup.py`を用意し、`pip install -e .`で開発・拡張が容易です。

- **日本語ナビゲーション**  
	`mkdocs.yml`の`nav`で日本語カテゴリ・記事名と英語パスを明示的に対応。

- **OGP/Twitter Card/JSON-LD自動出力**  
	`overrides/main.html`で全ページに構造化データ（Article/BreadcrumbList）を自動生成。

- **Python 3.13以降必須**  
	最新のPython環境で動作します。

- **サーバープレビューはポート6283を推奨**  
	複数プロジェクト併用時の競合を避けるため、`mkdocs serve -a 127.0.0.1:6283`を推奨。

---

## セットアップ手順

1. **Python 3.13以降をインストール**
2. **依存パッケージのインストール**
	 ```sh
	 pip install mkdocs mkdocs-material
	 pip install -e .
	 ```
3. **ビルド**
	 ```sh
	 mkdocs build
	 ```
4. **ローカルプレビュー（推奨ポート6283）**
	 ```sh
	 mkdocs serve -a 127.0.0.1:6283
	 ```
5. **公開**
	 - `site/` フォルダをWebサーバーにアップロード

---

## .memoファイル仕様

- 各記事（.md）と同じ場所・同名で拡張子だけ`.memo`にする
- 例: `docs/programming/python_intro.md` → `docs/programming/python_intro.memo`
- `.memo`の内容がdescriptionとして自動反映
- `.memo`がなければdescriptionは空欄またはデフォルト

---

## サーバーの安全なリスタート

- サイト構成や記事の大幅な変更時は、`mkdocs_restart.ps1`でサーバーを安全に再起動
- VS Codeの「タスク」から「Restart MkDocs Server」を実行可能

---

## 注意事項

- 本番公開時は`mkdocs.yml`の`site_url`を必ず実際のドメインに設定してください
- OGP/構造化データ/パンくずリストは全ページ自動生成されます
- 記事・カテゴリの日本語表示は`mkdocs.yml`の`nav`で制御します

---

このREADMEはAIによって自動生成・管理されています。
