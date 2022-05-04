#!/usr/bin/env python3

from http import cookies
from random import randrange
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageColor
from colorthief import ColorThief
from glitch_this import ImageGlitcher
from os import listdir
import base64
import pyfiglet
import logging
import datetime
import json
import uuid
import requests

def main():
    create_metadevil_hexadomain()

def metadevil(image_file, data, output_path):
    notice_of_non_affiliation_and_disclaimer = "We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with the the domain. The name in use, as well as related names, marks, emblems, and images are registered trademarks of their respective owners."
    description = "Influenced by a random domain name using the site's layout, color palette, and metadata including cookie count and total response bytes."
    created_by = "mindrash"
    collection = "metadevil"
    collection_type = "hexadomain"
    ipfs_url = "https://ipfs.infura.io:5001"
    return_count = 1
    data_elements_len = 3

    try:
        data_elements = []
        with open(data, "r") as data_file: 
            data_line = data_file.readlines()
            data_elements = data_line[0].split(',')
            logging.info("data_elements[]: " + data)

        if (len(data_elements) == data_elements_len):
            domain = data_elements[0]
            total_bytes = data_elements[1]
            cookies = data_elements[2]
        else:
            logging.critical("data_elements[]: is empty")
            return 0

        # Influence: Base layer from screenshoot of domain
        colors = ColorThief(image_file)
        palette = colors.get_palette(color_count=10)
        img = Image.open(image_file)
        imgSmall = img.resize((16,16),resample=Image.BILINEAR)
        result = imgSmall.resize(img.size,Image.NEAREST)
        glitcher = ImageGlitcher()

        for glitch_i in range(1, 20):
            glitch_img = glitcher.glitch_image(result, 8, color_offset=True)
            img = ImageEnhance.Contrast(glitch_img).enhance(5)
            glitch_i += 1

        img = img.convert("RGBA")

        freak_ellipse_count = 0
        if randrange(0, 3) == 1:
            freak_ellipse(img, palette)
            freak_ellipse_count += 1

        # Vertical line
        # Influence: Create lines based on the second number in total bytes
        if len(data_elements) == data_elements_len:
            line_number = int(total_bytes[1])
        else:
            line_number = 10

        for line_i in range(0, line_number):
            line = Image.new('RGBA', img.size, (255,255,255,0))
            l = ImageDraw.Draw(line)
            line_x = randrange(0, 2000)
            # Influence: set the line_width to the first digit in total bytes * 10
            if len(data_elements) == data_elements_len:
                line_width = int(total_bytes[0]) * 10
            else:
                line_width = 10

            if len(palette) == 0:
                palette = (255,255,255)

            line_color = palette[randrange(0, len(palette) - 1)]
            rgb_fill = (line_color[0], line_color[1], line_color[2], 15)
            l.line((line_x,0, line_x,img.height), width=line_width, fill=rgb_fill)
            img = Image.alpha_composite(img, line)
            line_i += 1

        # Influece: Add a color line if cookies are > 10
        if int(cookies) > 10:
            line_width = 10
            line_color = palette[randrange(0, len(palette) - 1)]
            rgb_fill = (line_color[0], line_color[1], line_color[2], 65)
            l.line((line_x,0, line_x,img.height), width=line_width, fill=rgb_fill)
            img = Image.alpha_composite(img, line)
            line_i += 1            

        # Metadevil's eye
        circle_size = randrange(50, 1000)
        circle_x = randrange(40, 900)
        circle_width1 = randrange(10, 400)
        circle_width2 = randrange(1, 400)
        ellipse_box = [circle_x, circle_x, circle_size, circle_size]
        ellipse_count = 0
        draw_ellipse(img, ellipse_box, palette[randrange(0, len(palette) - 1)], width=circle_width1)
        ellipse_count += 1 
        draw_ellipse(img, ellipse_box, palette[randrange(0, len(palette) - 1)], outline='black', width=circle_width2, antialias=8)
        ellipse_count += 1 
        if (randrange(0,10) == 1):
            ellipse_box[0] = ellipse_box[0] * 10
            ellipse_box[1] = ellipse_box[1] * 10
            ellipse_box[2] = ellipse_box[2] - 200
            ellipse_box[0] = ellipse_box[3] - 200
            draw_ellipse(img, ellipse_box, palette[randrange(0, len(palette) - 1)], outline='black', width=circle_width1, antialias=8)
            ellipse_count += 1
        if (randrange(0,100) == 1):
            ellipse_box[0] = ellipse_box[0] - 300
            ellipse_box[1] = ellipse_box[1] - 300
            ellipse_box[2] = ellipse_box[2] + 400
            ellipse_box[0] = ellipse_box[3] + 400
            draw_ellipse(img, ellipse_box, palette[randrange(0, len(palette) - 1)], outline='white', width=circle_width1, antialias=8)
            ellipse_count += 1 
            ellipse_box[0] = ellipse_box[0] - 800
            ellipse_box[1] = ellipse_box[1] - 800
            ellipse_box[2] = ellipse_box[2] + 200
            ellipse_box[0] = ellipse_box[3] + 200
            draw_ellipse(img, ellipse_box, palette[randrange(0, len(palette) - 1)], outline='white', width=circle_width1, antialias=8)
            ellipse_count += 1 

        # Influence: based on the number of cookies 
        chars = "▓"
        if len(data_elements) == 3:
            char_number = int(cookies) * 10
            if char_number != 0:
                chars = chars * randrange(0, char_number)
            else:
                chars = ""
        else:
            chars = ""

        char_color = palette[randrange(0, len(palette) - 1)]
        char_x = randrange(0, 2000)
        char_y = randrange(0, 2000)
        title_font = ImageFont.truetype('Keyboard.ttf', randrange(50, 600)) # unicode unknown wins this round
        txt = Image.new('RGBA', img.size, (255,255,255,0))
        d = ImageDraw.Draw(txt)
        rgb_fill = (char_color[0], char_color[1], char_color[2], randrange(15, 45))
        d.text((char_x, char_y), chars, fill=rgb_fill, font=title_font)
        img = Image.alpha_composite(img, txt)
    
        image_uri = str(uuid.uuid4())
        image_name = image_uri + ".png"
        img.save(output_path + image_name)

        nft_name = to_base64(data_elements[0])
        data_name = image_uri + ".json"
        ipfs_url = "[[IPS_URL]]"
        nft_json = {
            "name" : nft_name,
            "description" : description,
            "image" : ipfs_url,
            "attributes" : [
                {
                    "trait_type" : "domain",
                    "value" : domain
                },
                {
                    "trait_type" : "cookies",
                    "value" : cookies
                },
                {
                    "trait_type" : "response_total_bytes",
                    "value" : total_bytes
                },
                {
                    "trait_type" : "line_number",
                    "value" : line_number
                },
                {
                    "trait_type" : "ellipse_count",
                    "value" : ellipse_count
                },
                {
                    "trait_type" : "freak_ellipse_count",
                    "value" : freak_ellipse_count
                },
                {
                    "trait_type" : "chars_number",
                    "value" : len(chars)
                },
                {
                    "trait_type" : "created_by",
                    "value" : created_by
                },
                {
                    "trait_type" : "collection",
                    "value" : collection
                },
                {
                    "trait_type" : "collection_type",
                    "value" : collection_type
                },
                {
                    "trait_type" : "non-affiliation disclaimer",
                    "value" : notice_of_non_affiliation_and_disclaimer
                },
            ]
        }

        with open(output_path + data_name, "w") as data_file:
            json.dump(nft_json, data_file, indent = 4)
    except Exception as e:
        logging.critical("Error with: " + image_file)
        logging.critical(e)
        return_count = 0

    return return_count

def to_base64(item):
    domain_bytes = item.encode('ascii')
    base64_bytes = base64.b64encode(domain_bytes)
    return str(base64_bytes.decode('ascii'))

def freak_ellipse(img, palette):
    dctx = ImageDraw.Draw(img)
    bmsz = (img.width // 16 - 10, img.height // 16 - 10)

    if randrange(0, 5) == 1:
        colors = palette
    else:
        colors = list(ImageColor.colormap.keys())

    if randrange(1, 3) % 2 == 0:
        colors.sort()

    if 1 == randrange(1, 10):
        colors.sort(reverse=True)

    for y in range(16):
        for x in range(16):
            bm = Image.new("L", bmsz)
            dctx_inner = ImageDraw.Draw(bm)
            dctx_inner.ellipse(
                [(0, 0), bm.size],
                fill=y * 16 + x
                )
            del dctx_inner

            pos = [
                ((bmsz[0] + 10) * x + 10,
                (bmsz[1] + 10) * y + 10)]
            dctx.bitmap(
                pos,
                bm,
                fill=colors[(y * 16 + x) % len(colors)])
    del dctx

def draw_ellipse(image, bounds, palette, width=1, outline='white', antialias=4):
    mask = Image.new(
        size=[int(dim * antialias) for dim in image.size],
        mode='L', color='black')
    draw = ImageDraw.Draw(mask)

    elipse_color1 = rgb_to_hex(palette)
    if (randrange(1, 3) % 2 == 0):
        elipse_color1 = "white"

    elipse_color2 = "black"
    if (randrange(1, 10) % 5 == 0):
        elipse_color1 = rgb_to_hex(palette)

    for offset, fill in (width/-2.0, elipse_color1), (width/2.0, elipse_color2):
        left, top = [(value + offset) * antialias for value in bounds[:2]]
        right, bottom = [(value - offset) * antialias for value in bounds[2:]]
        draw.ellipse([left, top, right * 2, bottom * 2], fill=fill)

    mask = mask.resize(image.size, Image.LANCZOS)
    image.paste(outline, mask=mask)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def create_metadevil_hexadomain():
    logging.basicConfig(level=logging.INFO, filename='logs/app-cmh.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.info(pyfiglet.figlet_format("metadevil"))
    console_line = "*" * 80
    logging.info(console_line)
    logging.info("Starting: " + str(datetime.datetime.now()))

    image_dir = "/Users/tlawson/projects/metadevil/metadevil-screenshots/"
    image_files = listdir(image_dir)
    output_path = "../metadevil-out/"
    collection_count = 10000
    out_count = 0
    processed_count = 0
    
    for image_file in image_files:
        if image_file.endswith(".png"):
            processed_count = metadevil(image_dir + image_file, image_dir + image_file.replace(".png", ".csv"), output_path)
            out_count += processed_count
            logging.info("Processed: " + str(out_count))
            if out_count == collection_count:
                break

    logging.info(console_line)
    logging.info("Finished: " + str(datetime.datetime.now()))

if __name__ == "__main__":
    main()