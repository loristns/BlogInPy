from templite import Templite
import json
import markdown
import os.path


class Setting:

    def __init__(self):
        """
        Simple class to get BlogInPy configuration.
        """
        file = open("config.json")
        self.setting = json.loads(file.read())  # self.setting : complete object tree of config.json
        file.close()

    @property
    def get_blog_name(self):
        """
        Fastly get blog name from configuration
        """
        return self.setting['blog_name']

    @property
    def get_blog_lang(self):
        """
        Fastly get blog lang from configuration
        """
        return self.setting['lang']

    @property
    def get_blog_description(self):
        """
        Fastly get blog description from configuration
        """
        return self.setting['description']

    @property
    def get_markdown_plugin_list(self):
        """
        Fastly get markdown plugin list from configuration
        """
        return self.setting['md_plugin_list']


class Article:

    def __init__(self, markdown_file, templite_file="templates/article.html"):
        """
        Class for storing and rendering markdown article in html template

        :param markdown_file: File storing markdown article
        :param templite_file: File storing templite template
        """

        self.setting_access = Setting()

        tp_file = open(templite_file)  # Get template content
        self.template = tp_file.read()
        tp_file.close()

        art_file = open("article/%s" % markdown_file)  # Get markdown article content
        self.markdown = art_file.read()
        art_file.close()

        # Init markdown converter with configured extensions
        self.converter = markdown.Markdown(extensions=self.setting_access.get_markdown_plugin_list)

    def render(self):
        """
        Render markdown document to HTML page from template

        :return: HTML article
        """

        html_doc = self.converter.convert(self.markdown)  # Convert markdown article to HTML
        render_dict = {  # Set data for template
            "lang": self.setting_access.get_blog_lang,
            "blog_name": self.setting_access.get_blog_name,
            "description": self.setting_access.get_blog_description,
            "article_title": self.converter.Meta['title'],  # Metadata got from markdown article
            "article_author": self.converter.Meta['author'],
            "article": html_doc  # HTML article
        }

        return str(Templite(self.template).render(**render_dict))


class Timeline:

    def __init__(self, markdown_file_lst, templite_file="templates/index.html"):
        """
        Class for rendering article timeline from list of markdown document and template

        :param markdown_file_lst: List of markdown documents
        :param templite_file: File storing templite template
        """

        self.setting_access = Setting()

        tp_file = open(templite_file)  # Get template content
        self.template = tp_file.read()
        tp_file.close()

        self.markdown = []  # List containing all article content

        for markdown_file in markdown_file_lst:  # Get all article content
            art_file = open("article/%s" % markdown_file)
            self.markdown.append(art_file.read())
            art_file.close()

        # Init markdown converter with configured extensions
        self.converter = markdown.Markdown(extensions=self.setting_access.get_markdown_plugin_list)

    def render(self):
        """
        Render markdown documents to HTML page containing "timeline" from template.

        :return: HTML timeline
        """

        article_list = []  # List containing all article information
        for md_article in self.markdown:
            html_doc = self.converter.convert(md_article)  # Convert markdown article to HTML
            article_dict = {
                "title": self.converter.Meta['title'],  # Metadata got from markdown
                "author": self.converter.Meta['author'],
                "url": "%s.html" %os.path.splitext(os.path.basename(self.converter.Meta['filename'][0]))[0],
                "content": html_doc  # HTML article
            }
            article_list.append(article_dict)

        render_dict = {  # Set data for template
            "lang": self.setting_access.get_blog_lang,
            "blog_name": self.setting_access.get_blog_name,
            "description": self.setting_access.get_blog_description,
            "article_list": article_list  # List of article data
        }

        return str(Templite(self.template).render(**render_dict))


def add_article(filename):
    """
    Add article to configuration index

    :param filename: File containing article
    :return: Message of success or failure
    """

    config = Setting()

    if filename in config.setting["index"]:  # If file is already indexed
        return "File is already indexed, cannot index it."
    else:
        config.setting["index"].insert(0, filename)  # Else insert file on the top of index

        new_config = open("config.json", "w")  # And save
        new_config.write(json.dumps(config.setting, indent=2))
        new_config.close()

        return "File successfully indexed !"


def delete_article(filename):
    """
    Delete article to configuration index

    :param filename: File containing article
    :return: Message of success or failure
    """

    config = Setting()

    if filename not in config.setting["index"]:  # If file doesn't be indexed
        return "File not found in index, cannot delete it."
    else:
        config.setting["index"].pop(config.setting['index'].index(filename))  # Else delete file
        new_config = open("config.json", "w")  # And save
        new_config.write(json.dumps(config.setting, indent=2))
        new_config.close()

        return "File successfully deleted from index !"


def generate_blog():
    """
    Generate all content to create a blog from configuration index of article.
    """

    config = Setting()

    for article in config.setting['index']:  # Add article page for all article
        new_article = open("blog/%s.html" % os.path.splitext(os.path.basename(article))[0], 'w')
        new_article.write(Article(markdown_file=article).render())
        new_article.close()

    new_timeline = open("blog/index.html", 'w')  # Add timeline page
    new_timeline.write(Timeline(config.setting['index']).render())
    new_timeline.close()
