from flask import Flask,request,send_file,redirect,make_response
app = Flask(__name__)
import os,json

lorem_ipsum="""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
"""

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
    args=dict(request.args)
    if path=="" or path=="/":
        if request.cookies.get('user')!=None:
            return open("home.html").read().replace("Login",request.cookies.get('user'))
        return open("home.html").read()
    if path=="about":
        if request.cookies.get('user')!=None:
            return open("about.html").read().replace("Login",request.cookies.get('user'))   
        return open("about.html").read()
    if path=="products":
        if request.cookies.get('user')!=None:
            return open("products.html").read().replace("Login",request.cookies.get('user'))   
        return open("products.html").read()
    if path=="contact":
        if request.cookies.get('user')!=None:
            return open("contact.html").read().replace("Login",request.cookies.get('user'))   
        return open("contact.html").read()
    if path=="login":
        return open("auth.html").read()
    if path=="auth":
        if args["id"] in os.listdir("users"):
            if json.loads(open("users/"+args["id"]).read())["key"]==args["key"]:
                resp=make_response('<meta http-equiv="refresh" content="0.01; URL=http://127.0.0.1:5000/" />')
                resp.set_cookie("user",args["id"])
                resp.set_cookie("key",args["key"])
                return resp
        return redirect("/login")
    if path=="reg":
        if args["id"] not in os.listdir("users"):
            open("users/"+args["id"],"a").write(json.dumps({"key":args["key"]}))
            resp=make_response('<meta http-equiv="refresh" content="0.01; URL=http://127.0.0.1:5000/" />')
            resp.set_cookie("user",args["id"])
            resp.set_cookie("key",args["key"])
            return resp
    if path=="signup":
        return send_file("reg.html")
    if path=="product":
        car=args["car"]
        data=json.loads(open("cars/"+car).read())
        toreturn=open("productprofile.html").read().replace("{car_img}",data["image"]).replace("{data1}",lorem_ipsum).replace("{data2}",lorem_ipsum).replace("{price}",str(data["price"])).replace("{car_name}",data["name"])
        if request.cookies.get('user')!=None:
            return toreturn.replace("Login",request.cookies.get('user')) 
        return toreturn
    if path=="user":
        if request.cookies.get('user') in os.listdir("users"):
            if json.loads(open("users/"+request.cookies.get('user')).read())["key"]==request.cookies.get('key'):
                return open("profile.html").read().replace("name_",request.cookies.get('user'))
        return redirect("/login")
    if path[0]=="/":
        path=path[1:]
    if os.path.exists(path):
        return send_file(path)
    return open("error.html").read()