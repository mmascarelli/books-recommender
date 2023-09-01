from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

top50 = pd.read_pickle(open('/Users/matt/Desktop/books-project/app/top50.pkl','rb'))
matrix = pd.read_pickle(open('/Users/matt/Desktop/books-project/app/matrix.pkl','rb'))
ss = pd.read_pickle(open('/Users/matt/Desktop/books-project/app/ss.pkl','rb'))
books = pd.read_pickle(open('/Users/matt/Desktop/books-project/app/books.pkl','rb'))

app = Flask(__name__)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(top50['title'].values),
                           author= list(top50['name'].values),
                           image = list(top50['image_url'].values),
                           rating = list(top50['avg_rating'].values),
                           num_ratings = list(top50['ratings_count'].values)
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(matrix.index == user_input)[0][0]
    similar_books = sorted(list(enumerate(ss[index])), key=lambda x:x[1], reverse=True)[1:51]
    
    book_list = []
    for i in similar_books:
        book = []
        temp_df = books[books['title'] == matrix.index[i[0]]]
        book.extend(list(temp_df.drop_duplicates('title')['title'].values))
        book.extend(list(temp_df.drop_duplicates('title')['name'].values))
        book.extend(list(temp_df.drop_duplicates('title')['image_url'].values))
        book_list.append(book)
    return render_template('recommend.html', data=book_list)

if __name__ == '__main__':
    app.run(debug=True)