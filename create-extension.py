import os
from time import sleep
from datas import package_path, res_path, android_manifest, build_gradle, ParsedAnimeHttpSouce, AnimeHttpSource

source = input("Enter the source name: ")
lang = input("Enter the language: ").lower()
package = source.lower()

if os.path.exists(package_path):
    print("Package already exists!")
    exit()

while True:
    os.system('cls')

    try:
        source_type = int(input(
        """
Choose the source type:
    1. AnimeHttpSource
    2. ParsedAnimeHttpSouce

Enter choice: """))
    except ValueError as e:
        print("Invalid choice: Enter number only!")
        sleep(1)
        continue

    if source_type == 1:
        source_content = AnimeHttpSource
        break
    elif source_type == 2:
        source_content = ParsedAnimeHttpSouce
        break
    else:
        print("Invalid choice!")
        sleep(1)
        continue

print(f"Working on {source} with language {lang}...")
sleep(1)

os.makedirs(f'{eval(package_path)}/src/eu/kanade/tachiyomi/animeextension/{lang}/{package}/')
os.makedirs(eval(res_path))

with open(f"{eval(package_path)}/AndroidManifest.xml", "w") as f:
    f.write(android_manifest)

with open(f"{eval(package_path)}/build.gradle", "w") as f:
    f.write(build_gradle)

with open(f"{eval(package_path)}/src/eu/kanade/tachiyomi/animeextension/{lang}/{package}/{source}.kt", "w") as f:
    f.write(eval(source_content))

sleep(1)
print("Done!")