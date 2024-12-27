from app import app, db, User

def init_db():
    with app.app_context():
        db.create_all()

        if not User.query.filter_by(name='testuser').first():
            test_user = User(name='testuser')
            db.session.add(test_user)
            db.session.commit()

if __name__ == '__main__':
    init_db()

