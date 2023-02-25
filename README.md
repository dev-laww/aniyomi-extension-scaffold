# Aniyomi Extension Scaffold


## Usage

### Interactive mode (inputs):

```bash
$ python creator.py
Source name: Example
Source language: pt-BR
Base URL: https://example.com

Choose the source type:
    1. AnimeHttpSource / API/JSON oriented
    2. ParsedAnimeHttpSource / JSoup/CSS oriented

Enter your choice: 2

Creating src/pt/example/AndroidManifest.xml
Creating src/pt/example/build.gradle
Creating src/pt/example/src/eu/kanade/tachiyomi/animeextension/pt/example/Example.kt
Creating src/pt/example/src/eu/kanade/tachiyomi/animeextension/pt/example/ExampleUrlActivity.kt
```
### CLI-mode
```bash
$ python creator.py -n "Example" -l "en" -b "https://example.org"

Creating src/en/example/AndroidManifest.xml
Creating src/en/example/build.gradle
Creating src/en/example/src/eu/kanade/tachiyomi/animeextension/en/example/Example.kt
Creating src/en/example/src/eu/kanade/tachiyomi/animeextension/en/example/ExampleUrlActivity.kt

$ python creator.py --help
usage: creator.py [-h] [-n NAME] [-l LANG] [-b BASE_URL]
                  [-p | --parsed | --no-parsed]

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of the source
  -l LANG, --lang LANG  Language of the source
  -b BASE_URL, --base-url BASE_URL
                        Base URL of the source
  -p, --parsed, --no-parsed
                        Use ParsedAnimeHttpSource as base to the main class

```

### Mixed mode

```bash
$ python creator.py -b https://example.org --no-parsed

Source name: Example LTD
Source language: de

Creating src/de/exampleltd/AndroidManifest.xml
Creating src/de/exampleltd/build.gradle
Creating src/de/exampleltd/src/eu/kanade/tachiyomi/animeextension/de/exampleltd/ExampleLTD.kt
Creating src/de/exampleltd/src/eu/kanade/tachiyomi/animeextension/de/exampleltd/ExampleLTDUrlActivity.kt
```
