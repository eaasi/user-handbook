# EAASI_user_handbook

Exclusive user guide for EAASI Research Alliance members, published to https://EAASI-user-handbook.readthedocs-hosted.com

## Building and contributing to the Handbook

The EAASI User Handbook relies on the following underlying projects/components:
- [reStructuredText](https://docutils.sourceforge.io/rst.html) - plaintext markup language (similar to Markdown, but with different syntax and features), for writing documentation
- [Sphinx](https://www.sphinx-doc.org/en/master/) - Python-based documentation and static site generator, for converting RST into HTML (or other formats like PDF or EPUB if desired)
- [Read the Docs](https://about.readthedocs.com/?ref=readthedocs.org) - documentation hosting platform with integrated support for Sphinx and GitHub
- [GitHub](https://github.com/EAASI/user-handbook) - this repository, for version control
- argos-translate - for experiments with automatically-generated translation into languages other than English, see more [below](#auto-translation-note)

Files for editing the Handbook documentation itself are nested in the `source` directory:
- `_static`: static web assets (logos/thumbnails, some minor custom CSS)
- `_templates`: some RTD configuration for the flyout menu, **do not edit**
- `api`: source RST files for "API Documentation" section of the Handbook (Next Gen EAASI-only)
- `configuration`: source RST files for "Making and Sharing Environments" section of the Handbook
- `guide`: source RST files for "User Guide" section of the Handbook
- `images`: image files for all pages (currently v2021.10-only, but will be added to Next Gen once available)
- `locale`: files related to auto-translate experiments, can be ignored
- `overview`: source RST files for "Overview" section of the Handbook
- `resources`: source RST files for "More Help" section of the Handbook
- `conf.py`: Sphinx configuration file; marked up in-line to hopefully include necessary/helpful details where changed from Sphinx's defaults, but should remain unedited
- `index.rst`: Sphinx configuration file for generating Handbook's table-of-contents and sidebar navigation
- `translate_po.py`: script related to auto-translate experiments, can be ignored

The top-level directory of this repository contains license info, as well as configuration files necessary for Read the Docs to automatically build and deploy the generated documentation to https://EAASI-user-handbook.readthedocs-hosted.com (`.readthedocs.yaml`).

### Deployment

There are two versions of the EAASI User Handbook being actively deployed and hosted on Read the Docs, in parallel. The default, "main" branch of the GitHub repository is configured in the Read the Docs account settings to deploy to https://eaasi-user-handbook.readthedocs-hosted.com/en/latest/, and is intended to document behavior and the look of "Next Gen EAASI", which is still under active development.

The "v2021-10" branch of this GitHub repository is configured in Read the Docs to deploy to https://eaasi-user-handbook.readthedocs-hosted.com/en/v2021-10/, and is intended to document behavior and the look of the legacy, v2021.10 version of the EAASI platform that is (as of 10-30-2025) still in use on hosted.eaasi.cloud (for Yale use only) and spn-eaasi.cloud (hosted by Notch8 as an exclusive benefit to U.S.-based members of the EAASI Research Alliance). Since this is the only version in active use, Read the Docs is also configured to route the top-level https://EAASI-user-handbook.readthedocs-hosted.com URL to the v2021-10 branch/version by default.

Any changes committed or merged to one of these two branches in GitHub should automatically trigger Read the Docs to rebuild and upload the changes to the relevant branch of the live documentation. Any new branches (or new commits to those new branches) in GitHub will not change the live documentation unless configured in the Read the Docs project settings.

### Previewing changes

A downside of editing files directly in GitHub is that there is no ability to fully preview changes to the whole Handbook before the documentation is generated and deployed to the live site (GitHub renders RST files in its "Preview" features, but this only works for individual pages, and will not render Sphinx-specific features or the RTD theming, etc.). For this reason editors may wish to edit and build the Handbook locally in order to "preview" changes before committing to the `main` or `v2021-10` branches of the repo.

There are lots of options for local tools and workflows for accomplishing this depending on your host system and text/source editor of choice. The main things to keep in mind:

- You *must* at least install Sphinx, **any and all Sphinx extensions** specified in the `conf.py` file, and the `sphinx-rtd-theme` package to build and preview the site properly. This is probably best handled with Python (also necessary) and its native package manager `pip`, but there is further guidance and options [here](https://www.sphinx-doc.org/en/master/usage/installation.html).
- Build files generated for local preview should not be committed to the GitHub repository; the RTD workflow is set up to build the documentation on-the-fly before deploying it to the live site, and pre-built files may interfere with RTD's build processes. Usual/common build directories (at the top-level of the repo, and at `source/_build`) are included in the `.gitignore` file to help avoid accidental commits.
- To align local versions of Python, Sphinx, Python modules, etc. with that used in the configured RTD workflow, check `.readthedocs.yaml` and `requirements.txt`

### Guidance for contributing

The EAASI team welcomes contributions or suggestions to the EAASI User Handbook from the community. If you have access to the private GitHub repository, please feel free to file a ticket in the [Issue tracker](https://github.com/EAASI/user-handbook/issues) if you have a question or comment for what we could improve about the Handbook; if you would like to directly contribute text or code, please commit your changes to a new branch, then submit a Pull Request with the `main` or `v2021-10` branch (as relevant) as the target. The Handbook maintainer (currently the Senior Software Preservation and Emulation Technologist at Yale) will review and merge or discuss further edits if need be!

## Auto-translation experiments

**The following instructions have not yet been edited to adjust to the RTD workflow; auto-translated versions of the Handbook are currently not building/publishing correctly**

The EAASI team is experimenting with offering automated translations of the EAASI User Handbook. These translations are generated using [argos-translate](https://github.com/argosopentech/argos-translate), an open-source, offline Python translation library built on neural models from the [OpenNMT](https://opennmt.net/) project.

Unfortunately the EAASI team does not currently have the staffing capacity or language expertise to perform quality control or improve these automatically-generated translations. Pull requests to improve non-English versions of the User Handbook are welcome.

Current automatically-generated translations are based on argos-translate's compatible languages and the languages spoken at organizations who have made direct inquiries to the EAASI platform and services in the past. Please feel free to [file a ticket](https://gitlab.com/EAASI/EAASI_user_handbook/-/issues) to request an alternative language be added to the list of options:

- English (en)
- German (de)
- Spanish (es)
- French (fr)
- Dutch (nl)
- Korean (ko)

Once changes are committed to the English version of the Handbook, steps to generate and build auto-translations for the live site:

1. Working in a local copy of the `user-handbook` repository, navigate to the `source` directory and then run:

``$ sphinx-build -b gettext . _build/gettext``

2. Use the `sphinx-intl` module (not included by default with sphinx installations, use `pip` to install manually if missing) to generate translation files for each target language. All target languages can be specified at once as an argument list, e.g.

`` $ sphinx-intl update -p _build/gettext -l de -l es -l fr -l nl -l ko``

3. Run the `translate_po.py` script (depends on `polib` and `argostranslate` Python modules, install with `pip` first if missing) one-by-one to run Argos-Translate over translation files for each language, e.g.

`` $ python translate_po.py --input locale/de/LC_MESSAGES/*.po --src_lang en --target-lang de`` 

Note: translation may take some time. Translation script is currently designed for the Handbook authors to go language-by-language to allow the opportunity to periodically check success of the process rather than translating all languages at once and thus going a very long time (~a whole day) without feedback from the terminal, but the `translate_po.py` script could potentially be optimized to translate all directories under the `locale` directory automatically.

4. Navigate to root directory and run `make html` to generate machine-actionable .mo files from the plain-text .po translate files. (TODO: this doesn't seem right? I am not sure why the RTD build pipeline doesn't handle this, but currently I have to make sure the .mo files are updated and committed first, or else the RTD pipeline falls back to a non-updated version of the .mo files for making the html. Maybe need to un-commit the .mo files entirely so that Pages can create and use them on-the-fly?)

5. Once .po and .mo files for all desired languages have been translated, commit the updated translations to the `main` branch of the repository. GitLab Pages should automatically deploy all translated pages to the live site.

## Copyright

The EAASI User Handbook is distributed under the [CC Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. Copyright (c) Yale University (unless otherwise noted).
