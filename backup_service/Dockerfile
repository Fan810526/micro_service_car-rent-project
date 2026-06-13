# 使用官方 Python 輕量版映像檔
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 複製依賴清單並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式代碼
COPY app.py .
COPY templates/ ./templates/

# 暴露服務使用的連接埠 (5270)
EXPOSE 5270

# 啟動應用程式
CMD ["python", "app.py"]
