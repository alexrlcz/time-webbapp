from flask import Flask
from datetime import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/')
def show_time():
    tz_name = os.environ.get('TZ', 'UTC')
    try:
        tz = pytz.timezone(tz_name)
    except:
        tz = pytz.UTC
    
    now = datetime.now(tz)
    return f"""
    <html>
    <body style="font-family: Arial; text-align: center; margin-top: 50px;">
        <h1>Current Time in tara mea</h1>
        <p style="font-size: 2em;">⏰ {now.strftime('%H:%M:%S')}</p>
        <p style="font-size: 1.2em;">📍 {tz_name}</p>
        <p style="color: #666;">{now.strftime('%A, %B %d, %Y')}</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
