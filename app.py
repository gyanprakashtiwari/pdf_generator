from flask import Flask ,render_template , request ,make_response ,jsonify
import requests
import json
import pdfkit

app = Flask(__name__)

def get_data_from_api(facility_type):
    api_url = f"https://hz3tqftb8e.execute-api.ca-central-1.amazonaws.com/api/nbh/auth/{facility_type}?lng=-79.3709183&api_key=FES80v8F3r4rMQfoFT7NC4q1sthviz9077SRfatI&lat=43.7639275&client_id=9562fbc00d56cc95209b818e8f9040654cecd9f4"
    response_data = requests.get(api_url)
    return (response_data.content)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/get_pdf", methods=["GET"])
def get_pdf():
    path = "/home/gyan/Desktop/gyan1/projects/pdfApiParams/templates"
    all_types = ["bar","daycare", "healthcare","ele_school","sec_school","grocery","cafe","restaurant","walkscore"]
    # for all types of data dict/map
    all_data = {}
    try:
        for t in all_types:
            facility_type = t
            data = get_data_from_api(facility_type)
            data = json.loads(data.decode('utf-8'))
            all_data[facility_type] = data[facility_type]
        # print(all_data["ele_school"]["closest_facility"][0]["name"])
    except:
        return {"msg":"unable to get all data from api"}
    
    
    
    try:
        rendered = render_template("index.html",templates_path=path,data = all_data)
        css = ['templates/main.css']
        pdfkit.from_string(rendered,"output.pdf",css=css)
    except:
        return {"msg":"some error in generating pdf"}
       
    
    return {"msg":"pdf report generated successfully"}



if __name__ == "__main__":
    app.run(debug=True)



