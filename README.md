
# mkdoc_site001

## このリポジトリについて

AI（GitHub Copilot）によって自動構築された、カスタマイズ重視のMkDocsサイト環境です。
標準的なMkDocsと異なり、以下の独自仕様・拡張を採用しています。

---

## 標準MkDocsとの差分・独自仕様

- **.memoファイルによるdescription自動化**
	- 各記事（.md）と同じ場所・同名で拡張子だけ`.memo`にしたテキストファイルを配置
	- 例: `docs/programming/python_intro.md` → `docs/programming/python_intro.memo`
	- `.memo`の内容がdescription（構造化データ/OGP等）に自動反映
- **自作プラグインのローカルパッケージ化**
	- `pip install -e .` で有効化（`setup.py`あり）
- **カテゴリ・記事の日本語ナビゲーション**
	- `mkdocs.yml`の`nav`で日本語名と英語パスを明示的に対応
- **OGP/Twitter Card/JSON-LD自動出力**
	- `overrides/main.html`で構造化データ（Article/BreadcrumbList）を全ページ自動生成
- **Python 3.13以降必須**
- **サーバープレビューはポート6283を推奨**
- **`site_url`は本番公開時に必ず設定**

---

## 環境再現手順

1. Python 3.13以降をインストール
2. 必要なパッケージをインストール（このリポジトリ直下で実行）
	 ```sh
	 pip install mkdocs mkdocs-material
	 pip install -e .
	 ```
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

## .memoファイル仕様まとめ

- 各記事（.md）と同じ場所・同名で拡張子だけ`.memo`にする
- 例: `docs/programming/python_intro.md` → `docs/programming/python_intro.memo`
- `.memo`の内容がdescriptionとして自動反映
- `.memo`がなければdescriptionは空欄またはデフォルト

---

## その他

- OGP/構造化データ/パンくずリストは全ページ自動生成
- 記事・カテゴリの日本語表示は`mkdocs.yml`の`nav`で制御
- 本番公開時は`mkdocs.yml`の`site_url`を必ず実際のドメインに設定

---

このREADMEもAIによって自動生成されています。
