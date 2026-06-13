from flask import Flask, render_template, jsonify

app = Flask(__name__)

# 全域變數用於模擬服務健康狀態
is_healthy = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    global is_healthy
    if is_healthy:
        return 'Healthy', 200
    else:
        return 'Unhealthy - Service Crashed', 500

@app.route('/crash', methods=['POST', 'GET'])
def crash():
    global is_healthy
    is_healthy = False
    return jsonify({
        'status': 'crashed',
        'message': '主服務（功能 2）已觸發崩潰！/health 端點現在開始回傳 500 錯誤。'
    })

if __name__ == '__main__':
    # 依照使用者要求，運行在 port 5260 (避開 Chrome 限制的 unsafe port 526)
    app.run(host='0.0.0.0', port=5260, debug=True)
