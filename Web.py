from flask import Flask, render_template
import test
app = Flask(__name__)


@app.route('/')
@app.route('/web')
def speedtest():
    (download, upload, packet_loss, avg_ping) = test.speedTest()
    return render_template('web.html', title='Home', download = download, upload = upload)


if __name__ == '__main__':
    app.run()
    