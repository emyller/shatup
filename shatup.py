#!/usr/bin/env python
import muffin


app = muffin.Application('shatup', CONFIG='backend.settings')


if __name__ == '__main__':
    from backend.views import *
    app.manage()
