from flask import Flask, jsonify, render_template, url_for, request
import random

def create_app(test_config=None):
    app = Flask(__name__)

    board = [
        '', '', '',
        '', '', '',
        '', '', ''
    ]
    counter = 0

    @app.route('/', methods=['GET'])
    def hello():
        global board
        global counter

        board = [
            '', '', '',
            '', '', '',
            '', '', ''
        ]
        counter = 0
        #print(board)
        return render_template('index.html', board = board, turn = random.choice(['X', 'O']))
        
    @app.route('/', methods=['POST'])
    def play():
        global board
        global counter
        json = request.json
        player = json['player']
        index = json['index']

        board[int(index)] = player
        #print(board)
        counter += 1
        data = {
            'winner': check(board)
        }
        if counter == 9 and data['winner'] == -1:
            data['winner'] = -2
            #print('end')
        return jsonify(data)


    def check(board):
        lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for line in lines:
            if(board[line[0]] == board[line[1]] == board[line[2]] and (board[line[2]] == 'X' or board[line[2]] == 'O')):
                return board[line[0]]
        return -1


    return app