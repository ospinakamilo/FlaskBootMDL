# Flask Start Template
A Flask project template that includes Bootsrap and Material Design Lite along other assets

#### Setup the project
This project uses **caos** as dependency manager so follow the instructions available at https://github.com/caotic-co/caos
to install it.

Install **caos** dependency manager:
~~~
$ pip install caos==2.0.3
~~~

Once you have installed **caos** you can proceed to clone the project
~~~
$ git clone https://github.com/ospinakamilo/FlaskStartTemplate.git
~~~

In the main folder of the project open a terminal and run the following command to create a virtual environment:
~~~
$ caos init
~~~

Update the virtual environment dependencies with the content of the **caos.yml** file:
~~~
$ caos update
~~~

To start the project in **Development** mode you can use the following command:

~~~
$ caos run development
~~~

To start the project in **Debug** mode use the following command:
~~~
caos run debug
~~~

To start the project in a **Production** environment run:
~~~
caos run production
~~~

#### Configure Ports and Addresses
By default development mode always uses **127.0.0.1:8080** as the main configuration but some further configuration is
available for the **Debug** and **Production** modes under the file **config.py** located in the root of the project.

```python
"""Edit here the host and port for the DEBUG and PRODUCTION environments"""

environments_config_dict = {
    "DEBUG":{
        "host":"127.0.0.1",
        "port":"8080"
    },
    "PRODUCTION":{
        "port":"8080"
    }
}
```
