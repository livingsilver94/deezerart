# Deezerart

![Tests](https://github.com/livingsilver94/deezerart/workflows/Tests/badge.svg) ![Package](https://github.com/livingsilver94/deezerart/workflows/Package/badge.svg) ![License](https://img.shields.io/github/license/livingsilver94/deezerart?label=License)

Deezerart is a [MusicBrainz Picard](https://picard.musicbrainz.org) plugin that fetches album covers from [Deezer](https://www.deezer.com).\
Deezer provides free-to-use web APIs and good quality album covers, up to 1000⨯1000 pixels, proving itself to be superior to the other cover providers Picard currently supports.

Deezerart is thoroughly tested against multiple Python versions, spanning from 3.5 to 3.8, to ensure proper compatibility across the majority of operating systems supported by Picard.

## Build

To create an installable .zip file, run:
```bash
python setup.py mkplugin
```
A file called `deezerart.zip` will appear in the current directory. The archive can be installed via the Plugin section of the Picard options.
