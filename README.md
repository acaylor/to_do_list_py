# TO DO list

This is a python project that uses the Django framework to create a _very_ simple to-do list

The style of the site uses bootstrap CDN

## Development

In order to work with this project you need `python` interpreter on your system.

Install the required python packages using the `pip` python package manager:

```shell
python -m pip install -r requirements.txt
```

To run a development web server run:

```shell
python manage.py runserver
```

There is a page to register users but login has not been implemented. The Django admin page allows you to manipulate database tables:

`http://localhost:8000/admin`

The app code is in the base directory and the `to_do_list` directory is server configuration.
