from flask_testing import TestCase
import skel
from models import db


class SkelTestCase(TestCase):
    def create_app(self):
        skel.app.config['TESTING'] = True
        skel.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        return skel.app

    def setUp(self):
        with skel.app.app_context():
            db.create_all()

    def tearDown(self):
        with skel.app.app_context():
            db.drop_all()

    def test_load(self):
        r = self.client.post('/loads')

        self.assert200(r)

        lid = r.json['load_id']

        r = self.client.get('/loads')

        assert r.json == [{'load_id': lid}]
