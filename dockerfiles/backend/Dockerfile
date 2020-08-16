FROM python:3.8
# 標準入出力・標準エラー出力はバッファリングなし
ENV PYTHONUNBUFFERED 1
# mkdirコマンドの実行
RUN mkdir /code
# 作業ディレクトリの設定
WORKDIR /code
# requirements.txtを/codeに追加する
COPY requirements.txt ./
# Pythonのパッケージ管理ツールのpipを最新にする
RUN pip install --upgrade pip==20.2.2
# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install -r requirements.txt
# ローカルのディレクトリを/codeに追加する
COPY . /code
