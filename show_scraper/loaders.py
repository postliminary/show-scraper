import time
import re
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join, Identity

def get_airday(text):
    text = text.lower()
    if (text.find("monday") > -1):
        return "mon"
    if (text.find("tuesday") > -1):
        return "tue"
    if (text.find("wednesday") > -1):
        return "wed"
    if (text.find("thursday") > -1):
        return "thr"
    if (text.find("friday") > -1):
        return "fri"
    if (text.find("saturday") > -1):
        return "sat"
    if (text.find("sunday") > -1):
        return "sun"
    return "none"

def generate_id(text):
    return re.sub("[^A-Za-z0-9]", "", text)

def cleanup_desc(text):
    tp = text.split("|")
    if (len(tp) > 1):
        return tp[-1]
    return text

class ShowLoader(ItemLoader):
    default_input_processor = MapCompose(unicode.strip)
    default_output_processor = TakeFirst()
    
    airday_in = MapCompose(get_airday)
    
    desc_in = MapCompose(cleanup_desc, unicode.strip)
    
    id_in = MapCompose(generate_id, unicode.strip)
    
    image_urls_out = Identity()

