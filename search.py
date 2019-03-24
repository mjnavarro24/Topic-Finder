from flask import Flask, render_template, request
import YouTube
import Reddit

KEY = 'AIzaSyB7Yn5wsbeNCfwSKVBNWeoZ-pLPE3ux78Y'


app = Flask(__name__)

@app.route('/')
def first_run():
    return render_template("index.html")
@app.route('/result', methods = ['POST', 'GET'])
def result():
    YT_result = []
    reddit_result = []
    final_result = []
    if request.method == 'POST':
        word = request.form.get("keyword")
        select = request.form.get("choices-single-defaul")
        if select == 'Reddit':
            reddit_result = Reddit.search_suball_week(word)
            
            #final_result.append('r')
             
        elif select == 'YouTube':
            YT_result = YouTube.YouTube_API(word,KEY)
            
            #final_result.append('y')

        else:
            reddit_result = Reddit.search_suball_week(word)
            YT_result = YouTube.YouTube_API(word,KEY)

        final_result.append(YT_result)
        final_result.append(reddit_result)
        return render_template("result.html",word = final_result)
#         # return render_template("result.html", word=YT_result)
#     if request.method == 'POST':
#         word_2 = request.form.get("keyword")
#         reddit_result = Reddit.search_suball_week(word_2)
#         #reddit_result = render_template("result.html", word_2 = red_stuff)
#     final_result.append(YT_result)
#    # final_result+=['\nREDDIT']
#     final_result.append(reddit_result)
#     return render_template("result.html",word = final_result)
if __name__ == "__main__":
    app.run(debug = True) 