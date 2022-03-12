from flask import Flask ,render_template , request ,make_response
import pdfkit

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/get_pdf", methods=["GET"])
def get_pdf():
    items = ["fb",1,2,3,"my string"]
    # rendered = render_template("index.html",name="gyan",mail="gyan@yahoo.com",items=items)
    rendered = render_template("new.html")
    css = ['templates/new.css']
    pdf = pdfkit.from_string(rendered,False,css=css)

    response = make_response(pdf)
    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition']='inline;filename=output.pdf'
    return response


if __name__ == "__main__":
    app.run(debug=True)




