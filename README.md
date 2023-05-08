# minutes_serverless

## 前提
- `serverless framework` がインストールされていること
- `aws cli` が構築されていること（`minutes` プロファイルが必要）

## デプロイ（関数の更新）について

```sh
serverless deploy
```

## lambda_layersについて
`AWS Lambda` の `Layer` 機能のためのディレクトリ

`Layer` を変更する場合は下記の流れで操作を行う

```sh
# requirements.txt を編集する
cd lambda_layers
pip install -r requirements.txt -t .
zip -r9 layer.zip .
# layer.zipを AWS マネジメントコンソールからアップロード
```
