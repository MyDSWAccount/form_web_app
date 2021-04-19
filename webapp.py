from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_first():
    return render_template('pigLatin.html')

@app.route("/response", methods=['GET', 'POST'])
def render_response():
    if request.method == 'POST':
         text_input = request.args['text_input']
        name_input = ""
        userId = ""
        name_input = request.args['name_input']
        if name_input != "":
            userId = name_input + "'s"
        else:
            userId = "Your"
        c = 0
        y = ""
        txt = []
        for x in text_input:
            y = y + x
            c = c + 1
            if x == " ":
                y = y[0:len(y)-1]
                txt.append(y)
                y = ""
            elif c == len(text_input):
                txt.append(y)
                y = ""
        vowel = ["a", "e", "i", "o", "u"]
        reply = ""
        for word in txt:
            if word[0].lower() in vowel:
                reply = reply + word + "yay" + " "
            else:
                reply = reply + word[1:len(word)] + word[0:1] + "ay" + " "
        return render_template('reply.html', response = reply, name = userId)
    else:
        return render_template('PigLatin.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
