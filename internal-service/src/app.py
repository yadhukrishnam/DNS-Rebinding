from flask import Flask, render_template, request, redirect

app = Flask(__name__)

status = False

@app.route('/')
def main():
    if status == False:
        result = "Disabled"
        return render_template("index.html", status=result, next="enable")
    else:
        result = "Enabled"
        return render_template("index.html", status=result, next="disable")

@app.route('/heater/enable', methods=["POST"])
def enable():
    global status
    status = True    
    print ("Heater enabled.")
    return redirect("/")

@app.route('/heater/disable', methods=["POST"])
def disable():
    global status
    status = False    
    print ("Heater disabled.")
    return redirect("/")


if __name__ == '__main__':
    app.run(port=7777, host="0.0.0.0", debug=True)
