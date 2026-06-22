from flask import Flask, render_template, jsonify, request

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

# 真正的 JWT Token 驗證 API（專題展示與安全測試使用）
@app.route('/cars', methods=['GET'])
def get_cars():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"msg": "Missing Authorization Header"}), 401
    
    # 簡單驗證 dummy token
    try:
        token_type, token = auth_header.split(" ")
        if token_type.lower() != 'bearer' or token != 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.dummy_token':
            return jsonify({"msg": "Invalid Token"}), 403
    except Exception:
        return jsonify({"msg": "Invalid Authorization Header Format"}), 400

    # 驗證通過，回傳車款數據
    return jsonify({
        "status": "success",
        "cars": [
            {"brand": "Mercedes-Benz", "model": "E-Class", "price": 4500, "stock": 3},
            {"brand": "BMW", "model": "5 Series", "price": 4800, "stock": 2},
            {"brand": "Tesla", "model": "Model 3", "price": 3800, "stock": 5}
        ]
    })

if __name__ == '__main__':
    # 依照使用者要求，運行在 port 5260 (避開 Chrome 限制的 unsafe port 526)
    app.run(host='0.0.0.0', port=5260, debug=True)

