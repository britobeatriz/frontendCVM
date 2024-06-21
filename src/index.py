from flask import Flask, render_template, request, redirect
import uuid

app = Flask(__name__)

listQuestion = []
listAnswer = []

@app.route("/")
def home():
    return render_template('chat.html')

# @app.route("/chat", methods=['GET','POST'])
# def enviar():
#     question = request.form.get('chat-input')
#     questionObj = {
#         'id': str(uuid.uuid4()),
#         'question': question
#     }
#     listQuestion.append(questionObj)
#     print(listQuestion)

#     if question.__len__() <= 0:
#         return render_template('chat.html', listQuestion=listQuestion, listaAnswer=listAnswer)
    
#     answer = []
#     answerObjt = {
#         'id': str(uuid.uuid4()),
#         'answer': answer,
#         'question_id': questionObj['id']
#     }
#     listAnswer.append(answerObjt)

#     print(listAnswer)
#     print(listQuestion)
#     return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)