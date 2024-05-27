from flask import Flask, render_template, request, redirect, url_for, flash
from extract_yt_cmnts import get_yt_answer
from extract_ama_cmts import get_am_answer

app = Flask(__name__)

@app.route('/')
def submit():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/youtube' , methods=['GET','POST'])
def youtube():
    if request.method == 'POST':
        youtube_link = request.form.get('link')
        video_id = youtube_link[32:]
        # flash("Generating summary....")
        summary = get_yt_answer(video_id)
        return summary
        
    return render_template('youtube.html')

@app.route('/amazon', methods=['GET','POST'])
def amazon():
    if request.method == 'POST':
        product_link = request.form.get('link')
        summary = get_am_answer(product_link)
        return summary

    return render_template('amazon.html')

if __name__ == '__main__':
    app.run(debug=True)


