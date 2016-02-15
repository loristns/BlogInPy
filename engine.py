from templite import Templite
import json
import markdown
import os.path

class Setting:
    """
    Simple class to get BlogInPy configuration.
    """

    def __init__(self):
        file = open("config.json")
        self.setting = json.loads(file.read())
        file.close()

    @property
    def get_blog_name(self):
        return self.setting['blog_name']

    @property
    def get_blog_lang(self):
        return self.setting['lang']

    @property
    def get_blog_description(self):
        return self.setting['description']

    @property
    def get_markdown_plugin_list(self):
        return self.setting['md_plugin_list']


class Article:

    def __init__(self, markdown_file, templite_file="templates/article.html"):

        self.setting_access = Setting()

        tp_file = open(templite_file)
        self.template = tp_file.read()
        tp_file.close()

        file = open("article/%s" %markdown_file)
        self.markdown = file.read()
        file.close()

        self.converter = markdown.Markdown(extensions=self.setting_access.get_markdown_plugin_list)

    def render(self):

        html_doc = self.converter.convert(self.markdown)
        render_dict = {
            "lang": self.setting_access.get_blog_lang,
            "blog_name": self.setting_access.get_blog_name,
            "description": self.setting_access.get_blog_description,
            "article_title": self.converter.Meta['title'],
            "article_author": self.converter.Meta['author'],
            "article": html_doc
        }

        return str(Templite(self.template).render(**render_dict))

class Timeline:

    def __init__(self, markdown_file_lst, templite_file="templates/index.html"):

        self.setting_access = Setting()

        tp_file = open(templite_file)
        self.template = tp_file.read()
        tp_file.close()

        self.markdown = []

        for markdown_file in markdown_file_lst:
            file = open("article/%s" %markdown_file)
            self.markdown.append(file.read())
            file.close()

        self.converter = markdown.Markdown(extensions=self.setting_access.get_markdown_plugin_list)

    def render(self):

        article_list = []
        for md_article in self.markdown:
            html_doc = self.converter.convert(md_article)
            article_dict = {
                "title": self.converter.Meta['title'],
                "author": self.converter.Meta['author'],
                "url": "%s.html" %os.path.splitext(os.path.basename(self.converter.Meta['filename'][0]))[0],
                "content": html_doc
            }
            article_list.append(article_dict)

        render_dict = {
            "lang": self.setting_access.get_blog_lang,
            "blog_name": self.setting_access.get_blog_name,
            "description": self.setting_access.get_blog_description,
            "article_list": article_list
        }

        return str(Templite(self.template).render(**render_dict))

def add_article(filename):

    config = Setting()

    if filename in config.setting["index"]:
        return "File is already indexed, cannot index it."
    else:
        config.setting["index"].insert(0, filename)

        new_config = open("config.json", "w")
        new_config.write(json.dumps(config.setting["index"], indent=2))
        new_config.close()

        return "File successfully indexed !"

def delete_article(filename):

    config = Setting()

    if not filename in config.setting["index"]:
        return "File not found in index, cannot delete it."
    else:
        config.setting["index"].pop(config.setting['index'].index(filename))

        new_config = open("config.json", "w")
        new_config.write(json.dumps(config.setting['index'], indent=2))
        new_config.close()

        return "File successfully deleted from index !"

def generate_blog():

    config = Setting()

    for article in config.setting['index']:
        new_article = open("blog/%s.html" %os.path.splitext(os.path.basename(article))[0], 'w')
        new_article.write(Article(markdown_file=article).render())
        new_article.close()

    new_timeline = open("blog/index.html", 'w')
    new_timeline.write(Timeline(config.setting['index']).render())
    new_timeline.close()