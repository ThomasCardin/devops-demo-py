from flask import Flask

app= Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p> Hello world <p>"

# Return max value between 2 values
def max(a, b):
    if a > b:
        # for i in 10:
        #     print(i)
        return a
    else:
        return b
        
print("test")