# minutes_serverless

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
# requirements.txt を編集する
docker run --rm -v $(pwd):/var/task amazon/aws-sam-cli-build-image-python3.9:latest \
pip install -r requirements.txt -t python/lib/python3.9/site-packages/
zip -r layer.zip python
# 生成された layer.zip をAWS マネジメントコンソールからアップロード
```
