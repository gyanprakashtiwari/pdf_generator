from flask import Flask ,render_template , request ,make_response
import pdfkit

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# @app.route("/get_pdf", methods=["GET"])
# def get_pdf():
#     items = ["fb",1,2,3,"my string"]
#     rendered = render_template("new.html")
#     css = ['templates/new.css']
#     pdf = pdfkit.from_string(rendered,css=css)

#     response = make_response(pdf)
#     response.headers['Content-Type']='application/pdf'
#     response.headers['Content-Disposition']='inline;filename=report.pdf'
#     return response


@app.route("/get_pdf", methods=["GET"])
def get_pdf():
    path = "/home/gyan/Desktop/gyan1/projects/pdfApiParams/templates/"
    rendered = render_template("html.html",templates_path=path)
    css = ['templates/css.css']
    pdfkit.from_string(rendered,"output.pdf",css=css)

    return "saved pdf in current directory"




if __name__ == "__main__":
    app.run(debug=True)




