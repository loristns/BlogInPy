import markdown
from markdown.extensions.video import VideoExtension
from markdown.extensions.align import AlignExtension
from markdown.extensions.grid_tables import GridTableExtension
import json

def add_article(filename):

    config = open("config.json", "r")
    config_data = json.loads(config.read())
    config.close()


    if filename in config_data["index"]:
        return "File is already indexed, cannot index it."
    else:
        config_data["index"].insert(0, filename)

        config = open("config.json", "w")
        config.write(json.dumps(config_data, indent=4))
        config.close()

        return "File successfully indexed !"

def delete_article(filename):

    config = open("config.json", "r")
    config_data = json.loads(config.read())
    config.close()


    if not filename in config_data["index"]:
        return "File not found in index, cannot delete it."
    else:
        config_data["index"].pop(config_data['index'].index(filename))

        config = open("config.json", "w")
        config.write(json.dumps(config_data, indent=4))
        config.close()

        return "File successfully deleted from index !"

def generate_blog():

    template = open("template.html")
    template_data = template.read()
    template.close()

    config = open("config.json", "r")
    config_data = json.loads(config.read())
    config.close()

    article_flow = ""

    for article in config_data['index']:

        article_buffer = open("article/%s" %article)

        html_article = markdown.markdown(article_buffer.read(), extensions=[
            VideoExtension(js_support=True),
            AlignExtension(),
            GridTableExtension()])
        article_buffer.close()

        article_flow = article_flow + '<div class="box">' + html_article + '</div><br>'

    template_data = template_data.format(lang=config_data['lang'],
        blog_name=config_data['blog_name'],
        description=config_data['description'],
        content=article_flow)

    blog = open("blog/index.html", 'w')
    blog.write(template_data)
    blog.close()