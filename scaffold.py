import os
from textwrap import dedent

class Scaffold:
    def __init__(self, is_parsed: bool, name: str, lang: str, baseUrl: str):
        self.className = "".join(filter(str.isalnum, name))  # Remove special chars
        self.package = self.className.lower()
        self.is_parsed = is_parsed
        self.name = name
        self.lang = lang
        if "-" in lang:
            # en-US -> en, pt-BR -> pt
            self.short_lang = lang[: lang.find("-")]
        else:
            self.short_lang = lang

        self.baseUrl = baseUrl

        self.package_path = f"src/{self.short_lang}/{self.package}"
        self.package_id = f"{self.short_lang}.{self.package}"
        self.sources_path = f"{self.package_path}/src/eu/kanade/tachiyomi/animeextension/{self.short_lang}/{self.package}"
        self.resources_path = f"{self.package_path}/res"

    def create_dirs(self):
        try:
            os.makedirs(self.sources_path)
            os.makedirs(self.resources_path)
        except:
            pass

    def create_files(self):
        files = (
            (f"{self.package_path}/AndroidManifest.xml", self.android_manifest),
            (f"{self.package_path}/build.gradle", self.build_gradle),
            (f"{self.sources_path}/{self.className}.kt", self.default_class),
            (f"{self.sources_path}/{self.className}UrlActivity.kt", self.url_handler),
        )

        for file, content in files:
            print(f"Creating {file}")
            with open(file, "w+", encoding="utf-8") as f:
                f.write(content)

    @property
    def default_class(self):
        if self.is_parsed:
            return self.parsed_anime_http_source
        else:
            return self.anime_http_source

    @property
    def android_manifest(self) -> str:
        host = self.baseUrl.replace("https://", "", 1)
        return dedent(f"""
        <?xml version="1.0" encoding="utf-8"?>
        <manifest xmlns:android="http://schemas.android.com/apk/res/android"
            package="eu.kanade.tachiyomi.animeextension">

            <application>
                <activity
                    android:name=".{self.package_id}.{self.className}UrlActivity"
                    android:excludeFromRecents="true"
                    android:exported="true"
                    android:theme="@android:style/Theme.NoDisplay">
                    <intent-filter>
                        <action android:name="android.intent.action.VIEW" />

                        <category android:name="android.intent.category.DEFAULT" />
                        <category android:name="android.intent.category.BROWSABLE" />

                        <data
                            android:host="{host}"
                            android:pathPattern="/anime/..*"
                            android:scheme="https" />
                    </intent-filter>
                </activity>
            </application>
        </manifest>
        """[1:])

    @property
    def build_gradle(self) -> str:
        return dedent(f"""
        apply plugin: 'com.android.application'
        apply plugin: 'kotlin-android'

        ext {{
            extName = '{self.name}'
            pkgNameSuffix = '{self.package_id}'
            extClass = '.{self.className}'
            extVersionCode = 1
            libVersion = '13'
        }}

        apply from: "$rootDir/common.gradle"
        """[1:])

    @property
    def anime_http_source(self) -> str:
        return dedent(f"""
        package eu.kanade.tachiyomi.animeextension.{self.package_id}

        import eu.kanade.tachiyomi.animesource.model.AnimesPage
        import eu.kanade.tachiyomi.animesource.model.AnimeFilterList
        import eu.kanade.tachiyomi.animesource.model.Video
        import eu.kanade.tachiyomi.animesource.model.SAnime
        import eu.kanade.tachiyomi.animesource.model.SEpisode
        import eu.kanade.tachiyomi.animesource.online.AnimeHttpSource
        import okhttp3.Request
        import okhttp3.Response

        class {self.className}: AnimeHttpSource() {{

            override val name = "{self.name}"

            override val baseUrl = "{self.baseUrl}"

            override val lang = "{self.lang}"

            override val supportsLatest = false

            // ============================== Popular ===============================
            override fun popularAnimeParse(response: Response): AnimesPage {{
                TODO("Not yet implemented")
            }}

            override fun popularAnimeRequest(page: Int): Request {{
                TODO("Not yet implemented")
            }}

            // ============================== Episodes ==============================
            override fun episodeListParse(response: Response): List<SEpisode> {{
                TODO("Not yet implemented")
            }}

            // ============================ Video Links =============================
            override fun videoListRequest(episode: SEpisode): Request {{
                TODO("Not yet implemented")
            }}

            override fun videoListParse(response: Response): List<Video> {{
                TODO("Not yet implemented")
            }}

            // =========================== Anime Details ============================
            override fun animeDetailsParse(response: Response): SAnime {{
                TODO("Not yet implemented")
            }}

            // =============================== Search ===============================
            override fun searchAnimeParse(response: Response): AnimesPage {{
                TODO("Not yet implemented")
            }}

            override fun searchAnimeRequest(page: Int, query: String, filters: AnimeFilterList): Request {{
                TODO("Not yet implemented")
            }}

            // =============================== Latest ===============================
            override fun latestUpdatesParse(response: Response): AnimesPage {{
                TODO("Not yet implemented")
            }}

            override fun latestUpdatesRequest(page: Int): Request {{
                TODO("Not yet implemented")
            }}

            companion object {{
                const val PREFIX_SEARCH = "id:"
            }}

        }}

        """[1:])

    @property
    def parsed_anime_http_source(self) -> str:
        return dedent(f"""
        package eu.kanade.tachiyomi.animeextension.{self.package_id}

        import eu.kanade.tachiyomi.animesource.model.AnimeFilterList
        import eu.kanade.tachiyomi.animesource.model.SAnime
        import eu.kanade.tachiyomi.animesource.model.SEpisode
        import eu.kanade.tachiyomi.animesource.model.Video
        import eu.kanade.tachiyomi.animesource.online.ParsedAnimeHttpSource
        import okhttp3.Request
        import org.jsoup.nodes.Document
        import org.jsoup.nodes.Element

        class {self.className}: ParsedAnimeHttpSource() {{

            override val name = "{self.name}"

            override val baseUrl = "{self.baseUrl}"

            override val lang = "{self.lang}"

            override val supportsLatest = false

            // ============================== Popular ===============================
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

            // ============================== Episodes ==============================
            override fun episodeFromElement(element: Element): SEpisode {{
                TODO("Not yet implemented")
            }}

            override fun episodeListSelector(): String {{
                TODO("Not yet implemented")
            }}

            // =========================== Anime Details ============================
            override fun animeDetailsParse(document: Document): SAnime {{
                TODO("Not yet implemented")
            }}

            // ============================ Video Links =============================
            override fun videoFromElement(element: Element): Video {{
                TODO("Not yet implemented")
            }}

            override fun videoListSelector(): String {{
                TODO("Not yet implemented")
            }}

            override fun videoUrlParse(document: Document): String {{
                TODO("Not yet implemented")
            }}

            // =============================== Search ===============================
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

            // =============================== Latest ===============================
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

            companion object {{
                const val PREFIX_SEARCH = "id:"
            }}
        }}
        """[1:])

    @property
    def url_handler(self):
        return dedent(f"""
        package eu.kanade.tachiyomi.animeextension.{self.package_id}

        import android.app.Activity
        import android.content.ActivityNotFoundException
        import android.content.Intent
        import android.os.Bundle
        import android.util.Log
        import kotlin.system.exitProcess

        /**
         * Springboard that accepts {self.baseUrl}/anime/<item> intents
         * and redirects them to the main Aniyomi process.
         */
        class {self.className}UrlActivity : Activity() {{

            private val TAG = javaClass.simpleName

            override fun onCreate(savedInstanceState: Bundle?) {{
                super.onCreate(savedInstanceState)
                val pathSegments = intent?.data?.pathSegments
                if (pathSegments != null && pathSegments.size > 1) {{
                    // https://<host>/<segment 0>/<segment 1>...
                    // ex: pattern "/anime/..*" -> pathSegments[1]
                    // ex: pattern "/anime/info/..*" -> pathSegments[2]
                    // etc..
                    val item = pathSegments[1]
                    val mainIntent = Intent().apply {{
                        action = "eu.kanade.tachiyomi.ANIMESEARCH"
                        putExtra("query", "${{{self.className}.PREFIX_SEARCH}}$item")
                        putExtra("filter", packageName)
                    }}

                    try {{
                        startActivity(mainIntent)
                    }} catch (e: ActivityNotFoundException) {{
                        Log.e(TAG, e.toString())
                    }}
                }} else {{
                    Log.e(TAG, "could not parse uri from intent $intent")
                }}

                finish()
                exitProcess(0)
            }}
        }}
        """[1:])
