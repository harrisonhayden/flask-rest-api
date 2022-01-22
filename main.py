from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'idk'


video_post_args = reqparse.RequestParser()
video_post_args.add_argument(
    'name', type=str, help='Name of the video is required', required=True
)
video_post_args.add_argument(
    'likes', type=int, help='Likes on the video is required', required=True
)
video_post_args.add_argument(
    'views', type=str, help='Views of the video is required', required=True
)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument('name', type=str)
video_update_args.add_argument('likes', type=int)
video_update_args.add_argument('views', type=str)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Could not find video with that id')
        return result

    @marshal_with(resource_fields)
    def post(self, video_id):
        args = video_post_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message='Video id taken...')

        video = VideoModel(
            id=video_id, name=args['name'], views=args['views'], likes=args['likes']
        )
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Video does''nt exist, cannot update')

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.views = args['likes']

        db.session.commit()

        return result

    def delete(self, video_id):
        result = VideoModel.query.get(video_id)
        if not result:
          abort(404, message='Video doesn\'t exist, cannot delete')

        db.session.delete(result)
        db.session.commit()
        return 'Deleted video ' + str(video_id) + '!', 201


api.add_resource(Video, '/video/<int:video_id>')


if __name__ == '__main__':
    app.run(debug=True)
