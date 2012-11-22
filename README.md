mathdash
========

Simple web app to help children and others measure and improve mental calculation skills


Localization
------------
1. extract strings to be localized:

	$ pybabel extract -o locale/messages.pot .

2. update catalogs for each supported locale

	$ pybabel update -l fr_FR -i locale/messages.pot -d locale

3. perform translations in .po files

4. compile catalogs into .mo files.

	$ pybabel compile -d locale -f