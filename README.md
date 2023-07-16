# このリポジトリの使い方
- クローンしてください
- VSCodeで開いてdevcontainerの拡張を使ってコンテナで再度開くを押してください
- コンテナ内で `poetry run streamlit run streamlit_app.py` を実行してください

# モジュールの追加方法
新しくモジュールを追加したい場合は下記のようにコンテナ内でコマンドを打ってください。poetry.lockが更新されます。

```
poetry add hogehoge
```
一度モジュールを追加したら特に何もする必要はありません。
再度コンテナを開くとpoetry.lockを参照してモジュールが自動でインストールされます