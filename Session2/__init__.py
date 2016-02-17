from flask import Flask, make_response, jsonify, request, abort, render_template, redirect
from models import db, Links

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		if 'link' in request.form:
			link = Links.query.filter_by(original=request.form['link']).first()
			if link:
				pass
			else:
				link = Links(request.form['link'])
				db.session.add(link)
				db.session.commit()

			return render_template('index.html', link_name=str(link.id))

		else:
			return "WHAT"
	else:
		return "GET OUTTA HERE"

@app.route("/<id>", methods=['GET'])
def goto(id):
	url = Links.query.filter_by(id=id).first()
	if url is None:
		return "Not a URL!"
	else:
		return redirect(url.original)


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
