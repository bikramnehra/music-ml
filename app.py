import os
from flask import Flask
from flask import request
from flask import jsonify
from model import model


class MyServer(Flask):
    """
    need to instantiate model only once and share amongst different requests
    """
    def __init__(self, *args, **kwargs):
        super(MyServer, self).__init__(*args, **kwargs)
        self.model = model()


app = MyServer(__name__)


@app.route("/recommendations")
def recommend_songs():
    """
    entry point for getting song recommendations
    """
    songs = request.args.get('songs')
    limit = request.args.get('limit')
    output = app.model.get_recommendations(songs.split(","), limit)

    return jsonify(output)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
