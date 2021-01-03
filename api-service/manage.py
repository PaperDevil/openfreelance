from Application import create_app

from settings import Base


app = create_app(Base())

if __name__ == '__main__':
    app.run()
