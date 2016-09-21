import click
from flask import Flask, jsonify  # type: ignore
from models import db, Load


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/ph.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/loads', methods=['POST'])
def create_load():
    load = Load()
    db.session.add(load)
    db.session.commit()

    return jsonify({'load_id': load.id})


@app.route('/loads', methods=['GET'])
def get_all_loads():
    return jsonify([l.to_dict() for l in Load.query.all()])


@app.cli.command()
def init_db():
    """Initialize the database."""
    click.echo('Init the db')
    db.create_all()
