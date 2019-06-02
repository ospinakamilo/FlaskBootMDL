# FlaskBootMDL
A Flask project template that includes Bootsrap and Material Design Lite along other assets

#### Setup the project
This project uses **caos** as dependency manager so follow the instructions avaiable at https://github.com/ospinakamilo/caos
to install it.

Once you have installed **caos** you can proceed to clone the project
~~~
git clone https://github.com/ospinakamilo/FlaskBootMDL.git
~~~

In the main folder of the project open a terminal and run the following command to create a virtual environment:
~~~
caos prepare
~~~

Update the virtual environment dependencies with the content of the **caos.json** file:
~~~
caos update
~~~

To start the project in **Development** mode you can use the following command:

~~~
caos run
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
