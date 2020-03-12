from app import db, create_app

app = create_app()

if __name__ == '__main__':
    # Run this next two lines ONLY the first time for creating the data base
    # with app.app_context():
    #     db.create_all()
    app.run(host='0.0.0.0', use_reloader=False)
