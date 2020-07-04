msg_template = """Hello {name},
Thank you for visiting {website}. Enjoy!
""" # .format(name="Phil", website='philhuot.com')

def format_msg(my_name="Phil", my_website="philhuot.com"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg