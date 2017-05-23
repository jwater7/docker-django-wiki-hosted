# docker-django-wiki-hosted

Project to web host an instance of [django-wiki](https://github.com/django-wiki/django-wiki) using the [jwater7/django-wiki](https://hub.docker.com/r/jwater7/django-wiki) container.

### Description

This container provides the web service exposed on port 80.  By default, the admin username is 'admin' and password is 'admin'.

The project is based on the sample site 'testproject' from [django-wiki](https://github.com/django-wiki/django-wiki).

### Usage
~~~sh
sudo docker pull jwater7/django-wiki
~~~

Example quick-start to run the wiki:
~~~sh
sudo docker run -d -p 8000:80 jwater7/django-wiki-hosted
~~~

