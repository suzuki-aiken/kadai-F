"""
課題F: Webアプリ 簡易掲示板
Webアプリの基本的な課題です。HTTPの基本やFlaskでの書き方、ファイル入出力の知識も問われます。

要件
簡易掲示板をつくる
動作イメージ → https://simple-bbs.herokuapp.com
実際に投稿して動きを確かめてください
課題F-1: 要件の書き出し
https://simple-bbs.herokuapp.com でいくつか投稿を試し、どういう要件を備えたアプリなのかを書き出してください
課題F-2: 実装
課題F-1で書き出した要件に従って実装してください
課題F-3: 改善
自由課題です
より使い勝手のよい掲示板になるような改善をしてください
例: 機能の追加, 見た目の変更 など
以上
"""
"""
課題F-1: 要件の書き出し
　見出しがある
　入力フォームusername messageがある
    送信ボタンがある
    username messageに入力された文字列がusername:messageのように表示される
    ・username:messageのように表示される
    username messageが別サーバーに保存されている（txtデータで保存する）
    更新しても過去のusername messageを表示する
    usernameが空欄の場合　名無しさんと表示される
    messageが空欄の場合　空文字列を返す
"""
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
name_message = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', message_list=name_message)

    # if request.method == 'POST':
    #     username = request.form['username']
    #     message = request.form['message']
    #     return render_template('index.html', username=username, message=message)

    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        name_message.append(f'{username}:{message}')
        # return render_template('index.html', name_message=name_message)
        return redirect("/")  # 相対パス


if __name__ == '__main__':
    app.run(debug=True, port=5353)
