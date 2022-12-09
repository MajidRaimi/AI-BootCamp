## Flask 

Flask is a micro web framework written in Python. It is classified as a micro-framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

### Installation

```bash
pip install Flask
```

### Start Your Project

import flask
```py
from flask import Flask
```

Create an instance of the Flask class
```py
app = Flask(__name__)
```


Run Your Project
```py
if __name__ == '__main__':
    app.run(debug=True)
```

### Routing


```py

    @app.route('/') # The route decorator is used to bind a function to a URL
    def index(): # Your function 
        return 'Hello World' # return value to the browser
```

### Get Data From The Browser 

First Method
```py
    @app.route('/<name>') # any value after ' / ' will considered as a {name} 
    def user(name): # the variable name you pulled from 'app.route'
        return f'Hello {name}' 
```

Second Method ( GET )
```py
    @app.route('/user' , methods = ['GET']) # default value of the both form and route is GET
    def user(): 
        name = request.args.get('name') # get the value of the key 'name' from the query string from HTML templates
        return f'Hello {name}' 
```

Third Method ( POST )
```py
    @app.route('/user' , methods = ['POST']) # default value of the both form and route is GET and we changed it to POST
    def user(): 
        name = request.form.get('name') # get the value of the key 'name' from the query string from HTML templates
        return f'Hello {name}' 
```

### Templates 

```py
from flask import Flask , render_template # import render_template
```
index.html file must be in 'templates' folder 
```py
    @app.route('/') 
    def index(): 
        return render_template('index.html') # render the template 
```

### Flask Jinja
Flask uses templates to expand the functionality of a web application while maintaining a simple and organized file structure. Templates are enabled using the Jinja2 template engine and allow data to be shared and processed before being turned in to content and sent back to the client.

#### Variable

```py
@app.route('/<name>')
def user(name):
    return render_template('user.html', name=name) # pass the variable name to the template
```

'{{ name }}' will display as the value you passed to the route
```html
    <h1> {{ name }} </h1> 
```

