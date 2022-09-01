package_path = 'f"src/{lang}/{package}"'

res_path = 'f"src/{lang}/{package}/res"'

android_manifest = """<?xml version="1.0" encoding="utf-8"?>
<manifest package="eu.kanade.tachiyomi.animeextension" />"""

build_gradle = """f'''apply plugin: 'com.android.application'
apply plugin: 'kotlin-android'

ext {{
    extName = '{source}'
    pkgNameSuffix = '{lang}.{package}'
    extClass = '.{source}'
    extVersionCode = 1
    libVersion = '13'
}}

apply from: "$rootDir/common.gradle"'''"""

AnimeHttpSource = """f'''package eu.kanade.tachiyomi.animeextension.{lang}.{package}

import eu.kanade.tachiyomi.animesource.model.AnimesPage
import eu.kanade.tachiyomi.animesource.model.AnimeFilterList
import eu.kanade.tachiyomi.animesource.model.Video
import eu.kanade.tachiyomi.animesource.model.SAnime
import eu.kanade.tachiyomi.animesource.model.SEpisode
import eu.kanade.tachiyomi.animesource.online.AnimeHttpSource
import okhttp3.Request
import okhttp3.Response

class {source}(): AnimeHttpSource() {{

    override val name = "{source}"

    override val baseUrl = ""

    override val lang = "{lang}"

    override val supportsLatest = false

    // Popular
    override fun popularAnimeParse(response: Response): AnimesPage {{
        TODO("Not yet implemented")
    }}

    override fun popularAnimeRequest(page: Int): Request {{
        TODO("Not yet implemented")
    }}

    // Episodes
    override fun episodeListParse(response: Response): List<SEpisode> {{
        TODO("Not yet implemented")
    }}

    // Video url
    override fun videoListRequest(episode: SEpisode): Request {{
        TODO("Not yet implemented")
    }}

    override fun videoListParse(response: Response): List<Video> {{
        TODO("Not yet implemented")
    }}

    // Anime details
    override fun animeDetailsParse(response: Response): SAnime {{
        TODO("Not yet implemented")
    }}

    // Search
    override fun searchAnimeParse(response: Response): AnimesPage {{
        TODO("Not yet implemented")
    }}

    override fun searchAnimeRequest(page: Int, query: String, filters: AnimeFilterList): Request {{
        TODO("Not yet implemented")
    }}

    // Latest
    override fun latestUpdatesParse(response: Response): AnimesPage {{
        TODO("Not yet implemented")
    }}

    override fun latestUpdatesRequest(page: Int): Request {{
        TODO("Not yet implemented")
    }}
}}

'''"""

ParsedAnimeHttpSouce = """f'''package eu.kanade.tachiyomi.animeextension.{lang}.{package}

import eu.kanade.tachiyomi.animesource.model.AnimeFilterList
import eu.kanade.tachiyomi.animesource.model.SAnime
import eu.kanade.tachiyomi.animesource.model.SEpisode
import eu.kanade.tachiyomi.animesource.model.Video
import eu.kanade.tachiyomi.animesource.online.ParsedAnimeHttpSource
import okhttp3.Request
import org.jsoup.nodes.Document
import org.jsoup.nodes.Element

class {source}(): ParsedAnimeHttpSource() {{

    override val name = "{source}"

    override val baseUrl = ""

    override val lang = "{lang}"

    override val supportsLatest = false

    // Popular
    override fun popularAnimeFromElement(element: Element): SAnime {{
        TODO("Not yet implemented")
    }}

    override fun popularAnimeNextPageSelector(): String? {{
        TODO("Not yet implemented")
    }}

    override fun popularAnimeRequest(page: Int): Request {{
        TODO("Not yet implemented")
    }}

    override fun popularAnimeSelector(): String {{
        TODO("Not yet implemented")
    }}
    
    // Episode
    override fun episodeFromElement(element: Element): SEpisode {{
        TODO("Not yet implemented")
    }}

    override fun episodeListSelector(): String {{
        TODO("Not yet implemented")
    }}

    override fun animeDetailsParse(document: Document): SAnime {{
        TODO("Not yet implemented")
    }}
    
    // Video url
    override fun videoFromElement(element: Element): Video {{
        TODO("Not yet implemented")
    }}

    override fun videoListSelector(): String {{
        TODO("Not yet implemented")
    }}

    override fun videoUrlParse(document: Document): String {{
        TODO("Not yet implemented")
    }}
    
    // Search
    override fun searchAnimeFromElement(element: Element): SAnime {{
        TODO("Not yet implemented")
    }}

    override fun searchAnimeNextPageSelector(): String? {{
        TODO("Not yet implemented")
    }}

    override fun searchAnimeRequest(page: Int, query: String, filters: AnimeFilterList): Request {{
        TODO("Not yet implemented")
    }}

    override fun searchAnimeSelector(): String {{
        TODO("Not yet implemented")
    }}
    
    // Latest
    override fun latestUpdatesFromElement(element: Element): SAnime {{
        TODO("Not yet implemented")
    }}

    override fun latestUpdatesNextPageSelector(): String? {{
        TODO("Not yet implemented")
    }}

    override fun latestUpdatesRequest(page: Int): Request {{
        TODO("Not yet implemented")
    }}

    override fun latestUpdatesSelector(): String {{
        TODO("Not yet implemented")
    }}
}}

'''"""
