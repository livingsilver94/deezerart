# Deezerart

![Tests](https://github.com/livingsilver94/deezerart/workflows/Tests/badge.svg) ![Package](https://github.com/livingsilver94/deezerart/workflows/Package/badge.svg) [![Foo](https://img.shields.io/badge/Picard-official-blue)](https://github.com/metabrainz/picard-plugins/tree/2.0/plugins/deezerart) ![License](https://img.shields.io/github/license/livingsilver94/deezerart?label=License)

Deezerart is a [MusicBrainz Picard](https://picard.musicbrainz.org) plugin that fetches album covers from [Deezer](https://www.deezer.com).\
Deezer provides free-to-use web APIs and good quality album covers, up to 1000⨯1000 pixels, proving itself to be superior to the other cover providers Picard currently supports.

Deezerart is thoroughly tested against multiple Python versions, spanning from 3.5 to 3.8, to ensure proper compatibility across the majority of operating systems supported by Picard.

Big thanks to [phw](https://github.com/phw/) for the development support.

## Build

To create an installable .zip file, run:
```bash
python setup.py mkplugin
```
A file called `deezerart.zip` will appear in the current directory. The archive can be installed via the Plugin section of the Picard options.

## Issues

Due to a bug in Picard versions older that 2.5, the cover art provider does not handle HTTP redirections. A workaround is available, but this will make Picard hang a little on slow networks, and will make it crash on Windows. So if on Windows, make sure you're running the latest release.

## This repository vs. the Picard 3rd party plugin repository

There are small differences between this code and the one merged into the official Picard plugin repository, to match Picard developers' requests.

 - The official Picard version does not support Picard versions older than 2.5 (thus, the redirection workaround is removed)
