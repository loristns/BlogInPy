      ____  _             _____       _____
     |  _ \| |           |_   _|     |  __ |
     | |_) | | ___   __ _  | |  _ __ | |__) |   _
     |  _ <| |/ _ \ / _` | | | | '_ \|  ___| | | |
     | |_) | | (_) | (_| |_| |_| | | | |   | |_| |
     |____/|_|\___/ \__, |_____|_| |_|_|    \__, |
                     __/ |                   __/ |
                    |___/                   |___/
                    
[![Codacy Badge](https://api.codacy.com/project/badge/grade/3a9da39de6fc49b7ad931ae6426b61cc)](https://www.codacy.com/app/lorisazerty/BlogInPy) [![Code Health](https://landscape.io/github/the-new-sky/BlogInPy/master/landscape.svg?style=flat)](https://landscape.io/github/the-new-sky/BlogInPy/master)

The smallest static blog generator ever created !

BlogInPy help you to interact with everyone freely and fastly. In 60 seconds you can have a static blog running on the web. BlogInPy is highly customisable, just add some things to templates, change CSS, add some Python-Markdown extensions and it's over !

# Why use BlogInPy

- BlogInPy do essential, no more : create and share posts around the world.

- But BlogInPy is extendable : Want comments ? Add Disqus by copying HTML code in your template !
Want maths ? Add Mathjax to Python-Markdown extensions and some javascript to template !

- BlogInPy was designed to be lighweight, portable and powerful. 


# Installation

Just clone this repository and look at the documentation.

 
# Usage

For configuring BlogInPy, open the file `config.json`, it look like that :

```json
    {
        "blog_name": "Default-blog",
        "lang": "en",
        "index": [
            "welcome.md"
        ],
        "description": "Is the default description of BlogInPy...",
        "md_plugin_list": [
            "markdown.extensions.meta",
            "markdown.extensions.align",
            "markdown.extensions.tables",
            "markdown.extensions.video",
            "markdown.extensions.smart_strong",
            "markdown.extensions.newtab",
            "markdown.extensions.toc"
        ]
    }
```

Just change `blog_name`, `description` and `lang` parameters.

The `index` parameter is the list of article in blog, don't change it here, it can be modified by using the command line interface or application.

You can add or delete some  Python-Markdown extensions by adding them in the `md_plugin_list` parameter, just never delete `markdown.extensions.meta`.


## Hello world !

To generate your first blog with BlogInPy, start `main.py` with Python 3.4 (or newer and probably Python 3.3 but not tested)...

```
$python3 main.py

          ____  _             _____       _____
         |  _ \| |           |_   _|     |  __ |
         | |_) | | ___   __ _  | |  _ __ | |__) |   _
         |  _ <| |/ _ \ / _` | | | | '_ \|  ___| | | |
         | |_) | | (_) | (_| |_| |_| | | | |   | |_| |
         |____/|_|\___/ \__, |_____|_| |_|_|    \__, |
                         __/ |                   __/ |
                        |___/                   |___/

        -- Welcome to the smallest blog generator ever --

        INFO - Article list :
        
         - welcome.md

    ACTION - What do you want to do ?

         1- Add article to index
         2- Delete article to index
         3- Generate the blog
         4- Quit
```

...And select the option 3 to generate your static blog.

Go to the `/blog/` directory, and start an HTTP server who serve all files in this directory.

You are going to get a static blog !


## Delete articles

You need to delete the default article : `welcome.md`. First, delete article from index, you can use CLI :

```
$python3 main.py index- welcome.md
```

Or you can use the application :

```
$python3 main.py

...

YOU >>> 2

...

Name of article file : welcome.md
```

Then, delete `welcome.md` to the `/article/` directory.

NOTE : If you just want not generate article in the blog, don't delete it completly, just from index.


## Add articles

First add your article in the `/article/` directory and add it from index by using CLI :

```
$python3 main.py index+ newarticle.md
```

Or you can use the application :

```
$python3 main.py

...

YOU >>> 1

...

Name of article file : newarticle.md
```

NOTE : Article require metadatas, let's see this exemple :

```
Title:  The title of your article
Filename:  filename.md
Author:  YOU

This article contains *metadatas*.
```

## TIPS

You can hack templates to change your blog !

## Me

Created with :heart: in France by **the_new_sky**.