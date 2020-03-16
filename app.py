import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
<<<<<<< HEAD
        return "Hello, name!"
=======
        return "Hello, world.  im on this make change branch!"
>>>>>>> makeChange

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()