import os, sys
import argparse
import time
import datetime
import polib
import argostranslate.translate

parser = argparse.ArgumentParser(description="Machine translate PO files using Argos Translate")

parser.add_argument('--input', required=True)
parser.add_argument('--src_lang', required=True)
parser.add_argument('--target_lang', required=True)
parser.add_argument('--output', required=True)

args = parser.parse_args()

input_file = polib.pofile(args.input)
from_code = args.src_lang
to_code = args.target_lang
output_file = polib.POFile()

output_file.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'ethan',
        'POT-Creation-Date': time.strftime("%Y-%m-%d %H:%M%z"),
        'PO-Revision-Date': time.strftime("%Y-%m-%d %H:%M%z"),
        'Last-Translator': 'ethan',
        'Language-Team': 'ethan',
        'Language': args.target_lang,
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
}


for entry in input_file:

        translated_entry = polib.POEntry(
                msgid=entry.msgid,
                msgstr=argostranslate.translate.translate(entry.msgid, from_code, to_code)
        )
        time.sleep(1)
        output_file.append(translated_entry)

output_file.save(args.output)
