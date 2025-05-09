from bs4 import BeautifulSoup
import requests
import streamlit as st

#command to run website on localhost
#streamlit run F:\Python\WhosYourCommander\WhosYourCommander.py

#search tags
all_tags={"+1/+1": "+1/+1", #multiple tags
          "Aristocrats": "aristocrats", #multiple tags
          "Artifacts": "synergy-artifact",
          "Combat": "combat", #multiple tags
          "Draw": "draw",
          "Enchantress": "synergy-enchantment",
          "Flicker": "flicker",
          "Group Hug": "group-hug",
          "Landfall": "landfall",
          "Mill": "mill",
          "Self Mill": "mill-self",
          "Stompy": "power-matters",
          "Storm": "cast-trigger-you",
          "Ramp": "ramp",
          "Reanimate": "reanimate",
          "Theft": "theft",
          "Typal": "typal"
        }

st.title("Who's Your Commander?")
#search box
with st.container(border = True):
    themes = st.multiselect("Themes you want to build your deck around", all_tags.keys())

#converts all themes to proper scryfall Tags, then makes the URL
url_full = ""
actual_themes=[]
for x in themes:
        actual_themes.append(all_tags[x])

#tags that need multiple tags
for x in actual_themes:
    print(x)
    if x == "+1/+1":
        url_theme = f"+(otag%3Agives-pp-counters+or+otag%3Agains-pp-counters)"
    elif x == "aristocrats":
        url_theme = f"+(otag%3Asacrifice-outlet-creature+or+otag%3Adeath-trigger)"
    elif x == "combat":
        url_theme = f"+(otag%3Aattack-trigger+or+o%3A\"combat+damage\")"
    else:
        url_theme = f"+otag%3A{x}"
    url_full = url_full + url_theme
final_url = f"https://scryfall.com/search?q=is%3Acommander+game%3Apaper+legal%3Acommander{url_full}&order=edhrec"
response = requests.get(final_url)
print(final_url)

#web scraper finds the image of the card
doc = BeautifulSoup(response.text, "html.parser")
images = doc.find_all("img")

#makes layout
col1, col2 = st.columns(2)

#displays images
col_count = 1
for image in images:
    img_src = (image['src'])
    if col_count % 2 == 1:
        with col1:
            st.image(img_src)
    if col_count %  2 == 0:
        with col2:
            st.image(img_src)
    col_count += 1