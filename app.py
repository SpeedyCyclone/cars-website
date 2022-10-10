from flask import Flask,request,send_file,redirect,make_response
app = Flask(__name__)
import os,json

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
    args=dict(request.args)
    if path=="" or path=="/":
        if request.cookies.get('user')!=None:
            return open("index.html").read().replace("Login",request.cookies.get('user'))
        return open("index.html").read()
    if path=="user":
        if request.cookies.get('user')!=None:
            return request.cookies.get('user')
        return redirect("/login")
    if path=="about":
        if request.cookies.get('user')!=None:
            return open("about.html").read().replace("Login",request.cookies.get('user'))
        return open("about.html").read()
    if path=="login":
        return open("auth.html").read()
    if path=="auth":
        if args["id"] in os.listdir("users"):
            if json.loads(open("users/"+args["id"]).read())["key"]==args["key"]:
                resp=make_response('<meta http-equiv="refresh" content="0.01; URL=http://127.0.0.1:5000/" />')
                resp.set_cookie("user",args["id"])
                resp.set_cookie("key",args["key"])
                return resp
            else:
                open("users/"+args["id"]).write(json.dumps({"key":args["key"]}))
                resp=make_response('<meta http-equiv="refresh" content="0.01; URL=http://127.0.0.1:5000/" />')
                resp.set_cookie("user",args["id"])
                resp.set_cookie("key",args["key"])
                return resp
        return redirect("/login")
    if path[0]=="/":
        path=path[1:]
    print(path)
    if os.path.exists(path):
        print(path)
        return send_file(path)
    return open("error.html").read()