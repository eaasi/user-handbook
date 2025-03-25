import os, sys
import argparse
import time
import datetime
import polib
import argostranslate.translate

parser = argparse.ArgumentParser(description="Machine translate PO files using Argos Translate")

parser.add_argument('--input', required=True, nargs='+')
parser.add_argument('--src_lang', required=True)
parser.add_argument('--target_lang', required=True)

args = parser.parse_args()

for input_file in args.input:

        output_file = polib.POFile()

        output_file.metadata = {
                'Project-Id-Version': '1.0',
                'Report-Msgid-Bugs-To': 'EAASI',
                'POT-Creation-Date': time.strftime("%Y-%m-%d %H:%M%z"),
                'PO-Revision-Date': time.strftime("%Y-%m-%d %H:%M%z"),
                'Last-Translator': 'Argos-Translate',
                'Language-Team': 'EAASI',
                'Language': args.target_lang,
                'MIME-Version': '1.0',
                'Content-Type': 'text/plain; charset=utf-8',
                'Content-Transfer-Encoding': '8bit',
        }

        source_po = polib.pofile(input_file)

        for entry in source_po:

                translated_entry = polib.POEntry(
                        msgid=entry.msgid,
                        msgstr=argostranslate.translate.translate(entry.msgid, args.src_lang, args.target_lang)
                )
                output_file.append(translated_entry)

        output_file.save(input_file)
