# eaasi_user_handbook

Public-facing user guide for EaaSI-flavored EaaS system and interface at https://eaasi.gitlab.io/eaasi_user_handbook

## Auto-translation note

The EaaSI team is experimenting with offering automated translations of the EaaSI User Handbook. These translations are generated using [argos-translate](https://github.com/argosopentech/argos-translate), an open-source, offline Python translation library built on neural models from the [OpenNMT](https://opennmt.net/) project.

Unfortunately the EaaSI team does not currently have the staffing capacity or language expertise to perform quality control or improve these automatically-generated translations. Pull requests to improve non-English versions of the User Handbook are welcome.

Current automatically-generated translations are based on argos-translate's compatible languages and the languages spoken at organizations who have made direct inquiries to the EaaSI platform and services in the past. Please feel free to [file a ticket](https://gitlab.com/eaasi/eaasi_user_handbook/-/issues) to request an alternative language be added to the list of options:

- English (en)
- German (de)
- Spanish (es)
- French (fr)
- Dutch (nl)
- Korean (ko)

Once changes are committed to the English version of the Handbook, steps to generate and build auto-translations for the live site:

1. Working in a local copy of the `eaasi_user_handbook` repository, navigate to the `source` directory and then run:

``$ sphinx-build -b gettext . _build/gettext``

2. Use the `sphinx-intl` module (not included by default with sphinx installations, use `pip` to install manually if missing) to generate translation files for each target language. All target languages can be specified at once as an argument list, e.g.

`` $ sphinx-intl update -p _build/gettext -l de -l es -l fr -l nl -l ko``

3. Run the `translate_po.py` script (depends on `polib` and `argostranslate` Python modules, install with `pip` first if missing) one-by-one to run Argos-Translate over translation files for each language, e.g.

`` $ python translate_po.py --input locale/de/LC_MESSAGES/*.po --src_lang en --target-lang de`` 

Note: translation may take some time. Translation script is currently designed for the Handbook authors to go language-by-language to allow the opportunity to periodically check success of the process rather than translating all languages at once and thus going a very long time (~a whole day) without feedback from the terminal, but the `translate_po.py` script could potentially be optimized to translate all directories under the `locale` directory automatically.

4. Navigate to root directory and run `make html` to generate machine-actionable .mo files from the plain-text .po translate files. (TODO: this doesn't seem right? I am not sure why the GitLab Pages build pipeline doesn't handle this, but currently I have to make sure the .mo files are updated and committed first, or else the Pages pipeline falls back to a non-updated version of the .mo files for making the html. Maybe need to un-commit the .mo files entirely so that Pages can create and use them on-the-fly?)

5. Once .po and .mo files for all desired languages have been translated, commit the updated translations to the `main` branch of the repository. GitLab Pages should automatically deploy all translated pages to the live site.