from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def maintenance():
    return render_template('maintenance.html')

@app.route('/health')
def health():
    # 備援服務的健康端點必須永遠維持正常
    return 'Healthy', 200

if __name__ == '__main__':
    # 依照使用者要求，運行在 port 5270 (配合主服務避開 unsafe port 限制)
    app.run(host='0.0.0.0', port=5270, debug=True)
