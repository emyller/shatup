ShatUp!
=======

This is yet another chat system.

It is intended solely to explore bleeding edge software pieces like the Python
3 asyncio module and web components.


Installing
----------

First, make sure your system meet the following requirements:

- Node.js installed
- bower installed (`npm install bower`)
- A Python 3.5 virtualenv activated (`my_env` used as an example)

That said, you should make the first-run configuring:

	(my_env)$ make config

From now on, ~~all you have to do~~ we expect that the following is enough:

	(my_env)$ make run

Of course, if you ever want to deploy this into a production server, you should
read the `Makefile` and do things separately and [most likely] with different
configuration values (see below).


Settings
--------

The following environment variables can be set in order to properly set up your
ShatUp instance:

- `DEBUG`: Yeah, debug mode. "True" or "False". Defaults to `False`.
- `REDIS_URL`: 12factor-like URL pointing to your Redis database. Defaults to
  `redis://localhost/0`.


Testing
-------

Grab a cup of coffee and run the following:

	(my_env)$ py.test

That's it.
