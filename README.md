# delete_exif

PNG画像から指定したテキストメタデータを削除し、UUIDのファイル名で保存するPythonツールです。

## 機能

- 入力フォルダ直下の `*.png` に一致する画像を一括処理します（サブフォルダは対象外）。
- 次のテキストメタデータを削除します。
  - `Description`
  - `Software`
  - `Source`
  - `Generation time`
  - `Comment`
- 削除対象以外の文字列メタデータは保存用のデータに引き継ぎます。
- 画像ごとに `uuid.uuid4()` でファイル名を生成し、PNG形式で保存します。
- 保存先フォルダは、画像を保存する際に自動作成します。

現在の実装は、EXIFを含むすべてのメタデータの削除を保証するものではありません。

## 必要環境

- Python 3.10以上（使用しているPillowの要件）
- Pillow 12.3.0（`requirements.txt` に記載）

## セットアップ

プロジェクトのルートディレクトリで実行します。以下はmacOS / Linux向けのコマンドです。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## 使い方

1. 入力フォルダを作成します。

   ```sh
   mkdir -p tests/test_images
   ```

2. 処理したいPNG画像を `tests/test_images/` に配置します。

3. プロジェクトのルートディレクトリから実行します。

   ```sh
   .venv/bin/python src/delete_exif/main.py
   ```

処理後の画像は `tests/test_images/output/` に保存されます。元画像はそのまま残ります。

```text
tests/test_images/
├── sample.png
└── output/
    └── 550e8400-e29b-41d4-a716-446655440000.png
```

UUIDは実行のたびに生成されるため、再実行すると新しい出力ファイルが追加されます。入力フォルダが存在しない場合や、対象画像がない場合は、画像は保存されません。現在、完了件数などのメッセージは表示しません。

## 入力先・保存先の変更

`src/delete_exif/main.py` の次の指定を変更します。

```python
input_dir = project_root / "tests" / "test_images"
output_dir = input_dir / "output"
```

`project_root` は `main.py` の場所を基準に取得したプロジェクトのルートです。入力先と保存先を同じフォルダにすると、次回の実行時に出力画像も処理対象になるため、別のフォルダを指定してください。

## ファイル構成

```text
src/delete_exif/
├── main.py       # 入力先と保存先を指定し、処理を開始
├── processor.py  # PNG画像を列挙し、UUIDの出力ファイル名を生成
└── metadata.py   # メタデータを処理し、画像を保存
```

通常は `main.py` を実行してください。`processor.py` と `metadata.py` の直接実行用コードには、個別のパス指定があります。
