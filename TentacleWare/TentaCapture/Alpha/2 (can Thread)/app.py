from flask import Flask, render_template, Response, abort, request
from camera import CameraStream
import cv2

import requests # 다운로드 관련

app = Flask(__name__)






@app.before_request

def limit_remote_addr(): # 접근 허용 및 금지
    
    def ReadWhiteList(): # 화이트 리스트 읽기

        try:  
            # 화이트 리스트 다운로드
            #url = 'http://ic.deexint.com/WhiteList.txt'
            #r = requests.get(url, allow_redirects=True)
            #open('WhiteList.txt', 'wb').write(r.content)
            a=1

        except:
            print("Server Down")
    
        # 화이트 리스트 읽기
        f = open("WhiteList.txt",'r')

        ip=list(range(100))

        count = 0

        while True:
            line = f.readline()
            if not line: break
            ip[count]=line.rstrip()

            count+=1

         
        f.close()

        return ip
    
    
    if request.remote_addr not in ReadWhiteList():
        abort(403)  # Forbidden
    
    


cap = CameraStream().start()


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen_frame():
    """Video streaming generator function."""
    while cap:
        frame = cap.read()
        convert = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + convert + b'\r\n') # concate frame one by one and show result


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000', threaded=True)
