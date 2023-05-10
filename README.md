# minutes_serverless

## 概要
文字起こししたYouTube動画の全文検索サービス

## 前提
- `serverless framework` がインストールされていること
- `aws cli` が構築されていること（`minutes` プロファイルが必要）

## デプロイ（関数の更新）について

```sh
serverless deploy
```

## pythonディレクトリについて
`AWS Lambda` の `Layer` 機能のためのディレクトリ

`Layer` を変更する場合は下記の流れで操作を行う

```sh
docker build . -t lambda-layer:python3.9
docker container run -it --name "test" lambda-layer:python3.9
pip3 install -t /python boto3==1.26.90 pydub yt-dlp pycryptodome
zip -r /dist/layer.zip /python

# コンテナ抜ける
docker cp [CONTAINER ID]:/dist/pandas.zip ./
# 生成された layer.zip をAWS マネジメントコンソールからアップロード
```
