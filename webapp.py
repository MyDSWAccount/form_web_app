from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    text_input = request.args['text_input'] 
    vowel = ["a", "e", "i", "o", "u"]
    if text_input[0].lower() in vowel:
        reply = text_input + "yay"
    else:
        reply = text_input[1:len(text_input)] + text_input[0:1] + "ay"
    return render_template('reply.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
