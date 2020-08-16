# ベースイメージを指定
FROM node:12.18.3-alpine3.9

RUN mkdir -p /code

# node.js の環境変数を定義する
# 本番環境では production
ENV NODE_ENV=development

# axiosをインストール
RUN npm install @nuxtjs/axios

# ディレクトリを移動する
WORKDIR /code

# ポート3000番を開放する
EXPOSE 3000
