#!/usr/bin/env python
import muffin


app = muffin.Application('shatup', CONFIG='backend.settings')


@app.register('/')
def main(request):
    return app.ps.jade.render('main.jade')


if __name__ == '__main__':
    app.manage()
