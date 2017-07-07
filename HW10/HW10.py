from flask import Flask, jsonify
import datetime

app = Flask(__name__)


@app.route('/locales')
def locales():
	return jsonify('ru', 'en', 'it')

@app.route('/meta')
def meta():
	return jsonify(current_date = datetime.datetime.now().strftime('%Y-%m-%d'), 
		current_time = datetime.datetime.now().strftime('%H:%M'),
		received_headers = dict(request.headers), # не понимаю почему это словари?
		received_query_args = dict(request.args)) # не понимаю




if __name__ == '__main__':
    app.run()

