import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
    	return ("hello, on test branch")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()