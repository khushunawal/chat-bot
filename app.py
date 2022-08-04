

from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat, reflections

#Flask initialization
app = Flask(__name__)

pairs = [
    ['(hi|hello|hey|heyy)', ['hello','hi there','hayy']],
    ['my name is (.*)', ['hi %1']],
    ['(.*)(location|city|address) ?', [' Tonk Road, Jaipur, Rajasthan 302018']],
    ['(.*)(create|owner|made|god|father)(.*)?', ['khushbo did using nltk']],
    ['(.*)name', ['My name is UPBot']],
    ['(.*)contact(.*)', ['Call- XX']],
    ['(.*)food', ['i can not eat']],
    ['(.*)color', ['my favourite color is Bluish Black']],
    ['(.*)favourite actor(.*)', ['my favourite actor is Chris Hemsworth']],
    ['(.*)actress(.*)',['my favourite actress is Iman Vellani']],
    ['(.*)weather(.*)?',['it is amazing weather']],
    ["what(.*)want", ["Make me an offer I can't refuse"]],
    ["(.*)(sports|game|sport)(.*)", ["I'm a very big fan of Cricket",]],
    ["(.*)(Cricketer|Batsman)(.*)?",["Virat Kohli"]],
    ["quit",["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]],
    ["how are you(.*)?", ["I'm doing very well", "i am great!"]],
    ['(what is upflairs|tell me about upflairs|about upflairs)',['Upflairs is an upsurging edtech company with a mission to provide industry-relevant skill development programs through innovative content delivery.']],
    ['(.*)course(.*)',['1.Competitive Coding Using C++ 2. Python Scripting 3.Machine Learning With Data Science & Many more.']],
    ["(.*)",['That is nice to hear']]
    
]


chat = Chat(pairs,reflections)


@app.route("/", methods=["GET","POST"])
def chatbot_response():
    response = ''
    if request.method == 'POST':
    	msg = request.form['message']
    	response = chat.respond(msg)
    return render_template("index.html",response1 = response)

if __name__ == "__main__":
    app.run(debug=True)




