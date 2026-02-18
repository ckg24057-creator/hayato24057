FROM python:3.11-slim
WORKDIR /oimo
# 依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# プロジェクトファイルのコピー
COPY . .