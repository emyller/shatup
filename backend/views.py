from shatup import app


@app.register('/')
def main(request):
    return app.ps.jade.render('main.jade')
