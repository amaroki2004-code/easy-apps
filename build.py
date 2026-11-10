import os, html, json
BASE = "https://amaroki2004-code.github.io/easy-apps"   # change if repo name differs
DEV = "https://apps.apple.com/us/developer/athir-maroki/id6784476559"
APPS = [
 dict(slug="chaldean-easy", name="Chaldean Easy", id="6796100193",
  icon="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/46/57/ef/4657ef4b-5880-97ac-3ab6-9981d480e54f/AppIcon-0-0-1x_U007emarketing-0-11-0-85-220.png/512x512bb.jpg",
  tag="Learn spoken Chaldean (Soorath) the fun way", ar="",
  intro="Chaldean Easy is an app built specifically to teach spoken Chaldean (Soorath / Syriac / Assyrian) to English speakers, with real human voices, easy English transliteration, cartoon characters and bite-sized daily lessons.",
  for_="Iraqi Christian diaspora families, people reconnecting with their heritage, and anyone curious about one of the world's oldest living languages.",
  feats=["24 units covering greetings, family, food, body parts, verbs and more","Every word written in easy English letters (transliteration), so you can start speaking before learning the alphabet","Real recordings by native Chaldean speakers (male and female voices)","Games: Bubble Pop, Word Scramble, Matching Pairs, True or False and more","Flashcards, dialogues and cultural proverbs","Daily learning path with XP and streaks","Kids Mode, a grammar reference guide and a Chaldean alphabet explorer"],
  price="Unit 1 is free, no account needed. Full access is $14.99/month or $99.99/year.", kw="learn Chaldean, Soorath, Syriac, Assyrian, Neo-Aramaic, Chaldean language app",
  faq=[("Is there an app to learn spoken Chaldean?","Yes. Chaldean Easy is an iPhone app built specifically to teach spoken Chaldean Neo-Aramaic (Soorath) to English speakers. It has 24 units, recordings by native male and female Chaldean speakers, games, flashcards and a daily learning path. Unit 1 is free."),
   ("Can I learn Chaldean without reading the Aramaic alphabet?","Yes. Every word is shown in English letters (transliteration) with native audio, so you can start speaking before you learn the script. An alphabet explorer is included when you are ready."),
   ("Is Chaldean the same as Soorath, Sureth or Assyrian?","They are closely related. Soorath (also written Sureth or Soureth) is what many speakers call their spoken Neo-Aramaic. Chaldean and Assyrian speakers can usually understand each other, with differences in accent and some vocabulary by village and region. Chaldean Easy teaches the Chaldean variety."),
   ("Is Chaldean Easy good for kids?","Yes. It has a Kids Mode and game-based practice, so parents can use it to pass the family language on to their children."),
   ("How much does Chaldean Easy cost?","The app is free to download and Unit 1 is free with no account required. Full access to all 24 units is $14.99 per month or $99.99 per year."),
   ("Is Chaldean Easy available on Android?","Chaldean Easy is currently available for iPhone on the App Store.")]),
 dict(slug="america-easy-learn-english", name="America Easy – Learn English", id="6832024234",
  icon="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/38/e4/6b/38e46b7b-be9f-dcaf-7f89-eee14c126b57/AppIcon-0-0-1x_U007emarketing-0-11-0-85-220.png/512x512bb.jpg",
  tag="Practical American English for Arabic speakers", ar="أمريكا سهلة — الإنجليزية العملية للحياة في أمريكا، بالعربي",
  intro="America Easy (أمريكا سهلة) teaches Arabic speakers the American English they need in real life: the bank, the DMV, the doctor, school, renting an apartment and job interviews. The whole app, including menus, explanations and word meanings, is in Arabic.",
  for_="Arabs living in the US, and people getting ready to move there for work, study or to join family.",
  feats=["57 lessons in 8 levels, on a road trip across America from New York to Los Angeles","Real-life situations: renting an apartment, the bank, the DMV and your driver's license, jobs and job interviews, your kids' school, the doctor and pharmacy, government offices, money and bills","Spelling your name, email and address in English: \"How do you spell that?\"","Every word has a picture, clear American audio, the Arabic meaning and a pronunciation hint written in Arabic letters","Tips for the sounds Arabic speakers find hard: P, V, TH and CH","Short dialogues, quizzes, listening games, a Word Bank, Kids Mode and Sahl, your travel buddy","No account, no ads, no tracking"],
  price="Level 1 is free, plus two preview lessons from later levels. Pro unlocks all levels and games for $7.99/month or $59.99/year, with a free trial for new subscribers.", kw="learn English for Arabic speakers, تعلم الانجليزية, American English, English for life in America",
  faq=[("Is there an app to learn practical English for life in America, in Arabic?","Yes. America Easy (أمريكا سهلة) teaches Arabic speakers the English they need for daily life in the US: the bank, the DMV, the doctor and pharmacy, the kids' school, renting an apartment and job interviews. All menus and explanations are in Arabic."),
   ("Do I need to know any English to start?","No. Every word comes with a picture, American audio, the Arabic meaning and a pronunciation hint written in Arabic letters, so complete beginners can start from Level 1."),
   ("Does America Easy help with hard English sounds like P, V and TH?","Yes. It includes tips for the sounds Arabic speakers often find difficult, such as P, V, TH and CH."),
   ("How much does America Easy cost?","Level 1 and two preview lessons are free. Pro unlocks all 57 lessons for $7.99 per month or $59.99 per year, with a free trial for new subscribers.")]),
 dict(slug="learn-iraqi-arabic-easy", name="Learn Iraqi Arabic Easy", id="6807597152",
  icon="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/72/92/e6/7292e615-f125-a9d4-7687-4d64d31905bd/AppIcon-0-0-1x_U007emarketing-0-11-0-85-220.png/512x512bb.jpg",
  tag="Iraqi dialect, not textbook Arabic", ar="",
  intro="Most Arabic apps teach Modern Standard Arabic, the formal language of news and textbooks. Learn Iraqi Arabic Easy teaches the everyday Iraqi dialect spoken by family and friends, recorded by real native Iraqi speakers.",
  for_="Kids and grandkids of Iraqi immigrants, partners marrying into an Iraqi family, travelers, and anyone who got stuck on textbook Arabic.",
  feats=["800+ real Iraqi Arabic words and phrases in 65+ structured lessons","Greetings, family, food, shopping, travel, jobs, emotions, emergencies and more","Animated two-speaker conversations","Simple grammar: verb conjugation, past tense, pronouns","Flashcards, matching and fill-in-the-blank games","Cultural tips behind the words"],
  price="Free to download.", kw="Iraqi Arabic, Iraqi dialect, learn Arabic, spoken Arabic, Baghdadi"),
 dict(slug="learn-mexican-spanish-easy", name="Learn Mexican Spanish Easy", id="6811497071",
  icon="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/c4/4f/92/c44f92e4-1bc1-07e7-aff2-8d69b86b459b/AppIcon-0-0-1x_U007emarketing-0-11-0-85-220.png/512x512bb.jpg",
  tag="Speak real, everyday Mexican Spanish", ar="",
  intro="Spanish Easy gets you speaking real, everyday Mexican Spanish through short daily lessons instead of grammar drills.",
  for_="Beginners, travelers, and anyone connecting with Spanish-speaking family and friends across Mexico and the Southwest US.",
  feats=["Native-voice audio for every word and phrase, never robotic text-to-speech","Pronunciation hints so you know where the stress falls","Daily lessons: family, food, numbers, colors, the market, the restaurant and more","Games and quizzes, plus dialogues between two native speakers","Culture tips and Kids Mode","No account, no ads, no data collection"],
  price="Free to download.", kw="Mexican Spanish, learn Spanish, speak Spanish, Spanish for beginners"),
 dict(slug="german-easy-arabic-edition", name="German Easy: Arabic Edition", id="6821470658",
  icon="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/21/f9/25/21f92522-d527-5df9-cee2-73d1b1478ab5/AppIcon-0-0-1x_U007emarketing-0-11-0-85-220.png/512x512bb.jpg",
  tag="Learn German in Arabic, from zero to A1", ar="تعلّم الألمانية بالعربية — من الصفر إلى المستوى A1",
  intro="German Easy is the German course built for Arabic speakers, from zero to level A1. Every explanation and menu is in Arabic, every German word and sentence has clear German audio, and pronunciation is written in Arabic letters so you can read German from day one.",
  for_="Anyone preparing for an A1 German exam (for example for a spouse visa), newcomers to Germany, Austria and Switzerland, and students and workers who want a strong start.",
  feats=["76 lessons in 14 units covering level A1","A1 exam practice: listening, reading, writing and speaking, with Arabic explanations (our own practice material, not official exam questions)","Pronunciation written in Arabic script","Short, funny dialogues from everyday life in Germany","Journey map across Germany, unlimited flashcards and quizzes","Culture tips such as when to say du and Sie"],
  price="Unit 1 is free. German Easy Pro unlocks everything, with a 3-day free trial on the monthly plan and a 1-week free trial on the yearly plan.", kw="learn German in Arabic, German A1, تعلم الألمانية, German for Arabic speakers"),
 dict(slug="isbani-sahl-learn-spanish", name="Isbani Sahl – Learn Spanish", id="6824751092",
  icon="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/a0/77/39/a0773917-822d-71b4-a29b-9a87e821c242/AppIcon-0-0-1x_U007emarketing-0-11-0-85-220.png/512x512bb.jpg",
  tag="Learn Spanish in Arabic (Spain)", ar="إسباني سهل — تعلّم الإسبانية بالعربية",
  intro="Isbani Sahl (إسباني سهل) teaches the Spanish spoken in Spain to Arabic speakers. The whole app, including menus, explanations and word meanings, is in Arabic.",
  for_="Arabs living in or moving to Spain, travelers and students.",
  feats=["60 lessons in 11 units, from greetings and numbers to restaurants, shopping, the doctor and work","A \"Living in Spain\" unit: government offices, empadronamiento, NIE and TIE, opening a bank account","Clear help with ser vs estar, and tú vs usted","Every word has a picture, Spanish audio, Arabic audio and a pronunciation hint in Arabic letters","Dialogues, quizzes, listening games and a Word Bank","No account, no ads, no tracking"],
  price="Unit 1 is free. Pro unlocks all units and games (monthly or yearly, with a free trial for new subscribers).", kw="learn Spanish in Arabic, تعلم الإسبانية, Spanish for Arabic speakers, Spain"),
 dict(slug="watermelon-scanner", name="Watermelon Scanner", id="6784476557",
  icon="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/b5/62/0b/b5620b52-0f65-65b8-1913-37ab3c1db6a7/AppIcon-0-0-1x_U007emarketing-0-11-0-85-220.png/512x512bb.jpg",
  tag="Pick a ripe watermelon with your iPhone camera", ar="",
  intro="Watermelon Scanner uses your iPhone camera and AI to instantly score watermelon ripeness: no guessing, no tapping, no wasted melons. Point, tap, know.",
  for_="Farmers markets, grocery shopping, backyard BBQs, and anyone who wants a perfectly ripe watermelon every time.",
  feats=["Free scan: photograph a watermelon and get a Ripeness Score (0-100) based on color, field spot and skin texture, with expert tips","Pro scan ($2.99 one-time): guided 3-step analysis of overhead color, field spot photo and stem condition, with a detailed breakdown by category","Scan history: every scan is saved with its photo and score so you can compare melons","No account required, no data collected, works entirely on your device"],
  price="Free scan included. Pro scan is a $2.99 one-time purchase.", kw="watermelon ripeness, ripe watermelon, how to pick a watermelon, watermelon scanner"),
]
CSS = """:root{--teal:#1b7a72;--gold:#e6a817;--cream:#fdf8ee}*{box-sizing:border-box}body{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;background:var(--cream);color:#24312e;line-height:1.6}
header{background:linear-gradient(135deg,var(--teal),#12524c);color:#fff;text-align:center;padding:48px 20px}header h1{margin:0 0 8px;font-size:2rem}header p{max-width:620px;margin:0 auto;opacity:.95}
main{max-width:880px;margin:0 auto;padding:28px 20px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px}
.card{background:#fff;border-radius:16px;padding:18px;box-shadow:0 2px 10px rgba(0,0,0,.07)}.card img,.hero img{width:84px;height:84px;border-radius:20px}
.card h2{font-size:1.1rem;margin:10px 0 4px}.card p{margin:0 0 10px;font-size:.95rem}a{color:var(--teal)}.btn{display:inline-block;background:var(--gold);color:#24312e;padding:10px 18px;border-radius:10px;font-weight:700;text-decoration:none}
.hero{display:flex;gap:18px;align-items:center;margin-bottom:12px}.hero h1{margin:0}footer{text-align:center;padding:30px 20px;font-size:.9rem;opacity:.8}li{margin:4px 0}[dir=rtl]{text-align:right}"""
def page(title, desc, path, body, ld=None, lang="en"):
    canon = f"{BASE}/{path}"
    j = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>' if ld else ""
    return f"""<!DOCTYPE html><html lang="{lang}"{' dir="rtl"' if lang=="ar" else ""}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}">
<style>{CSS}</style>{j}</head><body>{body}<footer>&copy; 2026 Athir Maroki &middot; <a href="{DEV}">All apps on the App Store</a> &middot; <a href="{BASE}/">Home</a></footer></body></html>"""
def store(a): return f"https://apps.apple.com/us/app/id{a['id']}"
# home
cards = "".join(f"""<div class="card"><img src="{a['icon']}" alt="{html.escape(a['name'])} app icon" loading="lazy"><h2><a href="{a['slug']}.html">{html.escape(a['name'])}</a></h2><p>{html.escape(a['tag'])}</p><a class="btn" href="{store(a)}">Get on the App Store</a></div>""" for a in APPS)
home = page("Easy Language Apps by Athir Maroki — Chaldean, Iraqi Arabic, Spanish, German and Watermelon Scanner", "Fun, cartoon-style language apps with real native voices: Chaldean (Soorath), Iraqi Arabic, Mexican Spanish, German and Spanish for Arabic speakers. Free to download on iPhone and iPad.", "",
 f"""<header><h1>Easy Language Apps</h1><p>Learn to speak, not just to read. Real native voices, cartoon guides and 5-15 minute daily lessons.</p></header><main><div class="grid">{cards}</div>
<h2>Articles</h2><ul><li><a href="articles/how-many-people-speak-chaldean.html">How many people speak Chaldean? Where they live and why to learn it</a></li><li><a href="articles/practical-english-for-life-in-america-arabic.html" lang="ar" dir="rtl">الإنجليزية العملية للحياة في أمريكا (بالعربي)</a></li><li><a href="articles/english-sounds-arabic-speakers-p-v-th.html" lang="ar" dir="rtl">أصعب أصوات الإنجليزية على العرب: P و V و TH (بالعربي)</a></li><li><a href="articles/learn-german-for-beginners-arabic.html" lang="ar" dir="rtl">تعلّم الألمانية للمبتدئين حتى A1 (بالعربي)</a></li><li><a href="articles/common-iraqi-arabic-phrases.html">25 everyday Iraqi Arabic phrases</a></li><li><a href="articles/learn-chaldean-soorath.html">How to learn spoken Chaldean (Soorath)</a></li><li><a href="articles/iraqi-arabic-dialect-vs-msa.html">Iraqi Arabic dialect vs Modern Standard Arabic</a></li><li><a href="articles/learn-german-for-arabic-speakers-a1.html">Learn German for Arabic speakers: your A1 roadmap</a></li><li><a href="articles/learn-spanish-in-spain-for-arabic-speakers.html">Learn Spanish in Spain, in Arabic</a></li><li><a href="articles/mexican-spanish-for-beginners.html">Mexican Spanish for beginners</a></li><li><a href="articles/how-to-pick-a-ripe-watermelon.html">How to pick a ripe watermelon</a></li></ul></main>""",
 {"@context":"https://schema.org","@type":"Person","name":"Athir Maroki","url":BASE+"/","sameAs":[DEV]})
open("index.html","w",encoding="utf-8").write(home)
urls=[BASE+"/"]
def faq_html(a):
    if not a.get("faq"): return ""
    qa="".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(t)}</p>" for q,t in a["faq"])
    ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":t}} for q,t in a["faq"]]}
    return f'<h2>Frequently asked questions</h2>{qa}<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
for a in APPS:
    rtl = f'<p dir="rtl" lang="ar"><strong>{a["ar"]}</strong></p>' if a["ar"] else ""
    feats="".join(f"<li>{html.escape(f)}</li>" for f in a["feats"])
    body=f"""<header><h1>{html.escape(a['name'])}</h1><p>{html.escape(a['tag'])}</p></header><main><div class="hero"><img src="{a['icon']}" alt="{html.escape(a['name'])} app icon"><a class="btn" href="{store(a)}">Download on the App Store</a></div>{rtl}
<p>{html.escape(a['intro'])}</p><h2>What's inside</h2><ul>{feats}</ul><h2>Who it's for</h2><p>{html.escape(a['for_'])}</p><h2>Price</h2><p>{html.escape(a['price'])}</p>{faq_html(a)}<p><a class="btn" href="{store(a)}">Get {html.escape(a['name'])}</a></p><p><a href="{BASE}/">&larr; All apps</a></p></main>"""
    ld={"@context":"https://schema.org","@type":"MobileApplication","name":a["name"],"operatingSystem":"iOS","applicationCategory":"EducationalApplication","description":a["intro"],"url":store(a),"image":a["icon"],"author":{"@type":"Person","name":"Athir Maroki"},"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}}
    open(a["slug"]+".html","w",encoding="utf-8").write(page(f"{a['name']} — {a['tag']}", a["intro"][:155], a["slug"]+".html", body, ld)); urls.append(f"{BASE}/{a['slug']}.html")
# articles
A={x["slug"]:x for x in APPS}
def L(slug): return f'<a href="../{slug}.html">{html.escape(A[slug]["name"])}</a>'
ART=[
("learn-chaldean-soorath","How to Learn Spoken Chaldean (Soorath): A Beginner's Guide","A practical beginner's guide to learning spoken Chaldean, also called Soorath, with tips on listening, family conversation and daily practice.",
 [("Why spoken Chaldean is hard to learn","Chaldean, also called Soorath, Sureth or Chaldean Neo-Aramaic, is spoken at home by many Iraqi Christian families, but it has very few learning resources written for English speakers. Most materials focus on the written language or assume you already read the script. If your goal is to talk with your grandparents, you need audio first."),
  ("Start with listening, not reading","Spoken languages are learned through the ear. Pick a few everyday words, such as greetings and family words, and hear them from native speakers many times before worrying about spelling. Hearing both male and female voices also helps, because some forms change with the speaker."),
  ("Build a 10-minute daily habit","Short, regular practice beats long, occasional sessions. Five to fifteen minutes a day with greetings, family, food and the body is enough to start understanding simple conversations within weeks."),
  ("Practice with real dialogues","Words stick when you hear them in context. Two-speaker dialogues, such as a friendly uncle greeting a neighbor, show you how phrases are really used, and proverbs add cultural meaning."),
  ("A tool built for this","The app "+L("chaldean-easy")+" was built for exactly this: 24 units of spoken Chaldean for English speakers, recorded by native speakers, with games, flashcards, dialogues and a Kids Mode. Unit 1 is free, so you can try it before deciding.")]),
("iraqi-arabic-dialect-vs-msa","Iraqi Arabic Dialect vs Modern Standard Arabic: Which Should You Learn?","Why many learners choose the Iraqi dialect over Modern Standard Arabic if their goal is to talk with family and friends.",
 [("Two different goals","Modern Standard Arabic (MSA) is the formal language of news, books and speeches. Iraqi Arabic is the dialect people actually speak at home, at the market and with friends. If you want to talk to Iraqi relatives, the dialect is usually the better first step."),
  ("What changes in the dialect","Vocabulary, pronunciation and everyday phrases differ from MSA. Textbook Arabic can leave you understood but sounding stiff, and sometimes not understood at all in casual conversation."),
  ("How to learn the dialect","Learn from native Iraqi voices, practice short real-life phrases (greetings, family, food, shopping), and listen to conversations between two speakers so you hear the rhythm."),
  ("An app for the dialect",L("learn-iraqi-arabic-easy")+" teaches 800+ real Iraqi words and phrases across 65+ lessons, recorded by native Iraqi speakers, with dialogues, simple grammar and games. It is free to download.")]),
("learn-german-for-arabic-speakers-a1","Learn German for Arabic Speakers: Your A1 Roadmap","A roadmap for Arabic speakers learning German to level A1, with exam practice tips and pronunciation help in Arabic letters.",
 [("What A1 means","A1 is the first level of the European language framework. It covers greetings, numbers, shopping, appointments, simple forms and talking about the past in basic terms. Many people need A1 for a family visa."),
  ("Learn in your own language","Explanations in Arabic remove a big barrier. Pronunciation written in Arabic letters lets you read German aloud from day one, and Arabic translations of answers explain why each answer is right."),
  ("Practice the four exam parts","A1 exams test listening, reading, writing and speaking. Practice each part with short exercises and keep key phrases such as introductions, numbers and times ready."),
  ("The app",L("german-easy-arabic-edition")+" has 76 lessons in 14 units covering A1, A1 exam practice with Arabic explanations (its own practice material, not official exam questions), funny everyday dialogues and a journey map across Germany. Unit 1 is free and the monthly plan has a 3-day free trial.")]),
("learn-spanish-in-spain-for-arabic-speakers","Learn Spanish in Spain, in Arabic: A Guide for Newcomers","A guide for Arabic speakers moving to Spain: the Spanish you need for offices, banks, work and daily life.",
 [("The Spanish you need first","Newcomers need greetings, numbers, restaurants, transport and the doctor, plus the vocabulary of paperwork: empadronamiento, NIE and TIE, opening a bank account, phone and internet."),
  ("Two grammar traps","Ser vs estar and tú vs usted confuse many learners. Learn them with short examples, in your own language."),
  ("Learn with Arabic support",L("isbani-sahl-learn-spanish")+" (إسباني سهل) has 60 lessons in 11 units, entirely in Arabic, with a picture, Spanish audio, Arabic audio and an Arabic-letter pronunciation hint for every word. Unit 1 is free.")]),
("mexican-spanish-for-beginners","Mexican Spanish for Beginners: Speak Real, Everyday Spanish","A short beginner's guide to Mexican Spanish: pronunciation, stress and everyday vocabulary for travel and family.",
 [("Why Mexican Spanish","Mexican Spanish is spoken across Mexico and the Southwest US. Learning it helps you travel, work and connect with family and neighbors."),
  ("Watch the stress","A common beginner mistake is stressing the wrong syllable. Pronunciation hints for every new word help you get it right."),
  ("Learn by talking","Short daily lessons on family, food, numbers, colors, the market and the restaurant, plus dialogues between native speakers, build conversation faster than grammar drills."),
  ("Try it",L("learn-mexican-spanish-easy")+" uses native-voice audio for every word, games, quizzes and Kids Mode, with no account, no ads and no data collection. Free to download.")]),
("how-to-pick-a-ripe-watermelon","How to Pick a Ripe Watermelon: Color, Field Spot and Stem","Simple signs of a ripe watermelon (color, field spot, skin texture and stem) and how a phone scan can help.",
 [("Look at the color","A ripe watermelon usually has a deep, even color with a dull rather than shiny skin. Very shiny skin often means it was picked early."),
  ("Find the field spot","The field spot is the patch where the melon rested on the ground. A creamy yellow spot is a better sign than a white or pale green one."),
  ("Check the stem and texture","A dry, brownish stem and a firm, evenly textured skin suggest a melon that matured on the vine."),
  ("Let your phone help",L("watermelon-scanner")+" scores ripeness from 0 to 100 from a photo of the melon, using color, field spot and skin texture. The free scan gives an instant score and tips, and the Pro scan ($2.99 one-time) adds a guided 3-step breakdown. No account is needed and it works on your device.")]),
]
STORE_CE="https://apps.apple.com/us/app/id6796100193"
ART.insert(0,("how-many-people-speak-chaldean","How Many People Speak Chaldean? Where They Live and Why to Learn It","How many people speak Chaldean Neo-Aramaic (Soorath), where Chaldean communities live today, from the Nineveh Plains to Metro Detroit and El Cajon, and why learning the language matters now.",
 [("","<style>.t{border-collapse:collapse;width:100%;margin:12px 0;font-size:.95rem}.t th,.t td{border:1px solid #d6cfbf;padding:8px 10px;text-align:left;vertical-align:top}.t th{background:#f3ead6}.note{font-size:.88rem;opacity:.85}.appbox{background:#fff;border:2px solid var(--teal);border-radius:16px;padding:20px;margin:28px 0}.aibox{border-left:4px solid var(--gold);background:#fff;padding:12px 16px;margin:20px 0}</style>"
   "<p>Chaldean Neo-Aramaic, which most speakers simply call <strong>Soorath</strong> (also written Sureth or Soureth), is a living form of Aramaic, the language family of the ancient Near East. Today it survives mostly in families, in churches and in the diaspora, and in many homes it is slipping away within one generation. Here is what we know about how many people speak it, where they live, and why it is worth learning now.</p>"
   f"<p><strong>Want to start speaking today?</strong> <a href=\"{STORE_CE}\">Get Chaldean Easy free on the App Store</a>. Unit 1 is free.</p>"),
  ("How many people speak Chaldean?","<p>The honest answer: <strong>nobody knows exactly.</strong> No census counts Chaldean speakers, and being Chaldean is not the same as speaking Chaldean. Many Chaldeans speak Arabic at home, and many diaspora children understand some Soorath but cannot hold a conversation. The best available numbers:</p>"
   "<table class=\"t\"><tr><th>Estimate</th><th>Figure</th><th>Source</th></tr>"
   "<tr><td>Speakers of Chaldean Neo-Aramaic</td><td>about 216,000</td><td>Ethnologue (1994 figure, now very dated) [1]</td></tr>"
   "<tr><td>Members of the Chaldean Catholic Church worldwide</td><td>about 419,000</td><td>CNEWA [2]</td></tr>"
   "<tr><td>Chaldeans in the United States</td><td>more than 500,000</td><td>Chaldean News, community estimate (2020) [3]</td></tr></table>"
   "<p class=\"note\">These figures measure different things (speakers, church members, ethnic community) and come from different years, which is why they don't add up. Treat them as a range, not a precise count. Fluent speakers are certainly a smaller group than the total Chaldean population.</p>"),
  ("Where do Chaldeans live today?","<p><strong>Iraq, the homeland.</strong> Soorath is traditionally spoken in the Christian towns of the Nineveh Plains in northern Iraq, such as Telkeppe (Tel Keppe), Alqosh, Batnaya and Tesqopa, as well as in Baghdad, Mosul and the Kurdistan Region. But Iraq's Christian community has shrunk dramatically: commonly cited estimates say it fell from about <strong>1.5 million in 2003 to roughly 150,000 today</strong> [4]. Most Chaldeans now live outside Iraq.</p>"
   "<p><strong>Metro Detroit, Michigan, the largest community outside Iraq.</strong> A 2023 Walsh College survey with the Chaldean American Chamber of Commerce estimated <strong>about 183,500 Chaldeans in Metro Detroit</strong>, up from 160,000 in 2018 and 113,000 in 2008 [5]. Common areas include West Bloomfield, Sterling Heights, Farmington Hills and Commerce Township.</p>"
   "<table class=\"t\"><tr><th>Community</th><th>Estimated Chaldean population</th></tr>"
   "<tr><td>Metro Detroit, Michigan</td><td>about 183,500 (2023) [5]</td></tr>"
   "<tr><td>El Cajon / San Diego, California</td><td>about 50,000 [3]</td></tr>"
   "<tr><td>Arizona</td><td>about 15,000 [3]</td></tr>"
   "<tr><td>Australia and New Zealand</td><td>about 29,000 [2]</td></tr></table>"
   "<p>There are also communities in Chicago, Canada, Sweden, Germany and other parts of Europe, and in Jordan, Lebanon and Turkey, where many families waited as refugees.</p>"),
  ("Why learn Chaldean?","<p><strong>1. To talk with your grandparents while you still can.</strong> For many families, the grandparents are the last fluent speakers. Every conversation in Soorath is something no recording can replace.</p>"
   "<p><strong>2. Because the language is at risk.</strong> With the homeland communities scattered across the world, Soorath is passed on mainly at home. If one generation stops speaking it, the chain breaks.</p>"
   "<p><strong>3. To understand your faith and culture from the inside.</strong> Prayers, hymns, proverbs, wedding songs and family sayings carry meaning that gets lost in translation.</p>"
   "<p><strong>4. To give it to your children.</strong> Kids pick up languages fastest when they are young. Even a few hundred words and everyday phrases give them a real connection to who they are.</p>"
   "<p><strong>5. Because it is Aramaic.</strong> Soorath belongs to the same language family that was spoken across the ancient Near East for thousands of years. Few people anywhere can say they speak a living Aramaic language.</p>"),
  ("","<div class=\"appbox\"><h2 style=\"margin-top:0\">Start speaking: Chaldean Easy</h2>"
   "<p>I built <strong>Chaldean Easy</strong> for exactly this: to help English speakers, especially diaspora families and their kids, actually <em>speak</em> Chaldean, not just read translations.</p><ul>"
   "<li>24 units: greetings, family, food, verbs and more</li><li>Native Chaldean male and female voice recordings</li>"
   "<li>Every word in easy English letters (transliteration), no alphabet needed to start</li>"
   "<li>Games: Bubble Pop, Word Scramble, Matching Pairs, True or False and more</li>"
   "<li>Flashcards, dialogues, proverbs, Kids Mode and an alphabet explorer</li><li>Unit 1 is free, with no account needed</li></ul>"
   f"<a class=\"btn\" href=\"{STORE_CE}\">Download Chaldean Easy on the App Store</a></div>"
   "<div class=\"aibox\"><strong>What AI assistants say:</strong> When we asked ChatGPT and Google Gemini in November 2026 which app to use to learn to speak Chaldean, both named Chaldean Easy as their first pick. AI answers change over time and vary by question, so try it yourself.</div>"),
  ("Sources","<ol class=\"note\">"
   "<li>Ethnologue figure for Chaldean Neo-Aramaic (1994), as cited in <a href=\"https://en.wikipedia.org/wiki/Northeastern_Neo-Aramaic\">Wikipedia: Northeastern Neo-Aramaic</a>.</li>"
   "<li><a href=\"https://cnewa.org/eastern-christian-churches/the-catholic-eastern-churches/from-the-assyrian-church-of-the-east/the-chaldean-catholic-church/\">CNEWA: The Chaldean Catholic Church</a>.</li>"
   "<li><a href=\"https://chaldeannews.com/chaldeans-around-the-world/2020/6/28/chaldean-communities-in-the-american-southwest-california-arizona-nevada-and-texas\">Chaldean News: Chaldean Communities in the American Southwest (2020)</a>.</li>"
   "<li><a href=\"https://eclj.org/geopolitics/upr/christians-in-iraq-from-15-million-in-2003-to-150000-today\">ECLJ: Christians in Iraq, from 1.5 million in 2003 to 150,000 today</a>.</li>"
   "<li><a href=\"https://www.chaldeannews.com/2024-content/2024/1/1/walsh-college-survey-reveals-demographic-data-about-metro-detroit-chaldeans\">Chaldean News: Walsh College survey of Metro Detroit Chaldeans (2023)</a>.</li></ol>")]))
DATES={"how-many-people-speak-chaldean":"2026-11-09"}
# ---- Extra articles (Nov 2026) ----
TSTYLE = "<style>.t{border-collapse:collapse;width:100%;margin:12px 0;font-size:.95rem}.t th,.t td{border:1px solid #d6cfbf;padding:8px 10px;vertical-align:top}.t th{background:#f3ead6}.t td.en{direction:ltr;text-align:left;font-weight:600}.note{font-size:.88rem;opacity:.85}.appbox{background:#fff;border:2px solid var(--teal);border-radius:16px;padding:20px;margin:28px 0}.tip{border-inline-start:4px solid var(--gold);background:#fff;padding:12px 16px;margin:20px 0}</style>"

def rows(pairs, en_first=True):
    """pairs: (english, arabic) -> table rows; English cell is LTR."""
    return "".join(f'<tr><td class="en">{html.escape(e)}</td><td>{html.escape(a)}</td></tr>' for e, a in pairs)

def table_ar(pairs):
    return f'<table class="t"><tr><th>بالإنجليزية</th><th>المعنى</th></tr>{rows(pairs)}</table>'

def appbox(slug, heading, text, items, cta):
    li = "".join(f"<li>{html.escape(i)}</li>" for i in items)
    return f'<div class="appbox"><h2 style="margin-top:0">{html.escape(heading)}</h2><p>{text}</p><ul>{li}</ul><a class="btn" href="{store(A[slug])}">{html.escape(cta)}</a></div>'

A = {x["slug"]: x for x in APPS}
AM = "america-easy-learn-english"

ART.insert(1, ("practical-english-for-life-in-america-arabic",
 "الإنجليزية العملية للحياة في أمريكا: جمل تحتاجها من أول يوم",
 "أهم الجمل الإنجليزية التي يحتاجها العرب في أمريكا: البنك، الـDMV، الطبيب والصيدلية، مدرسة الأولاد، استئجار شقة، مقابلة العمل والطوارئ، مع المعنى بالعربي.",
 [("", TSTYLE +
   "<p>إذا انتقلت إلى أمريكا أو تعيش فيها حديثاً، فأنت لا تحتاج إلى قواعد معقدة في البداية. تحتاج إلى جمل قصيرة وواضحة تستخدمها في البنك، وعند الطبيب، وفي مدرسة أولادك، وفي مقابلة العمل. هذه أهم الجمل التي ستسمعها وتقولها في أول أسابيعك، مع معناها بالعربي.</p>"
   f'<p><strong>تريد أن تتدرب عليها بالصوت؟</strong> <a href="{store(A[AM])}">حمّل تطبيق أمريكا سهلة مجاناً من App Store</a>. المستوى الأول مجاني.</p>'),
  ("١. التهجئة: اسمك وإيميلك وعنوانك",
   "<p>أكثر سؤال ستسمعه في أمريكا هو كيف تكتب اسمك. تعلّم الحروف الإنجليزية بصوت عالٍ، وجهّز هذه الجمل:</p>" + table_ar([
    ("How do you spell that?", "كيف تكتب ذلك؟ (اسمك أو كلمة)"),
    ("My last name is ...", "اسم عائلتي هو ..."),
    ("Could you repeat that, please?", "هل يمكنك أن تعيد ذلك من فضلك؟"),
    ("Could you speak more slowly, please?", "هل يمكنك أن تتكلم ببطء من فضلك؟"),
    ("at / dot com", "علامة @ تُنطق \"at\" والنقطة تُنطق \"dot\""),
    ("What's your date of birth?", "ما تاريخ ميلادك؟"),
    ("What's your zip code?", "ما الرمز البريدي لعنوانك؟")])),
  ("٢. في البنك",
   table_ar([
    ("I'd like to open a checking account.", "أريد أن أفتح حساباً جارياً."),
    ("What documents do I need?", "ما الأوراق التي أحتاجها؟"),
    ("savings account", "حساب توفير"),
    ("debit card", "بطاقة السحب المرتبطة بحسابك"),
    ("I'd like to deposit this check.", "أريد أن أودع هذا الشيك."),
    ("What is the monthly fee?", "كم الرسوم الشهرية؟")])),
  ("٣. في الـDMV ورخصة القيادة",
   "<p>الـDMV (أو Secretary of State في ميشيغان) هو المكتب المسؤول عن رخص القيادة وتسجيل السيارات.</p>" + table_ar([
    ("I'd like to make an appointment.", "أريد أن أحجز موعداً."),
    ("I'm here to apply for a driver's license.", "جئت لأقدّم على رخصة قيادة."),
    ("the written test / the road test", "الامتحان النظري / امتحان القيادة العملي"),
    ("proof of address", "إثبات العنوان (مثل فاتورة باسمك)"),
    ("vision test", "فحص النظر"),
    ("Which line should I wait in?", "في أي طابور يجب أن أنتظر؟")])),
  ("٤. عند الطبيب والصيدلية",
   table_ar([
    ("I have an appointment at 10.", "عندي موعد الساعة العاشرة."),
    ("I'm a new patient.", "أنا مريض جديد."),
    ("Do you accept my insurance?", "هل تقبلون تأميني الصحي؟"),
    ("It hurts here.", "يؤلمني هنا."),
    ("I'm allergic to ...", "عندي حساسية من ..."),
    ("I'm here to pick up a prescription.", "جئت لأستلم وصفة طبية (دواء)."),
    ("How often should I take it?", "كم مرة يجب أن آخذه؟")])),
  ("٥. مدرسة الأولاد",
   table_ar([
    ("I'd like to enroll my child.", "أريد أن أسجّل ابني/ابنتي في المدرسة."),
    ("My son will be absent today.", "ابني سيغيب اليوم."),
    ("parent-teacher conference", "اجتماع الأهل مع المعلم"),
    ("What time is pick-up?", "متى موعد استلام الأطفال؟"),
    ("Does the school have ESL classes?", "هل في المدرسة صفوف إنجليزية لغير الناطقين بها؟")])),
  ("٦. استئجار شقة",
   table_ar([
    ("Is this apartment still available?", "هل هذه الشقة ما زالت متاحة؟"),
    ("How much is the rent?", "كم الإيجار؟"),
    ("lease", "عقد الإيجار"),
    ("security deposit", "التأمين (مبلغ يُدفع مقدماً)"),
    ("Are utilities included?", "هل الماء والكهرباء والغاز مشمولة؟"),
    ("landlord", "صاحب الشقة / المؤجر")])),
  ("٧. العمل ومقابلة العمل",
   table_ar([
    ("Tell me about yourself.", "حدّثني عن نفسك. (أول سؤال تقريباً في كل مقابلة)"),
    ("I have five years of experience in ...", "عندي خمس سنوات خبرة في ..."),
    ("full-time / part-time", "دوام كامل / دوام جزئي"),
    ("When can you start?", "متى يمكنك أن تبدأ؟"),
    ("I can start next Monday.", "أستطيع أن أبدأ يوم الإثنين القادم."),
    ("Do you have any questions for us?", "هل عندك أي أسئلة لنا؟")])),
  ("٨. الطوارئ",
   "<p>رقم الطوارئ في أمريكا هو <strong>911</strong> للشرطة والإسعاف والإطفاء.</p>" + table_ar([
    ("I need an ambulance.", "أحتاج سيارة إسعاف."),
    ("My address is ...", "عنواني هو ..."),
    ("There's been an accident.", "حصل حادث."),
    ("I don't speak English well. Arabic, please.", "لا أتكلم الإنجليزية جيداً. العربية من فضلك.")]) +
   "<div class=\"tip\"><strong>نصيحة:</strong> كثير من المستشفيات والمكاتب الحكومية توفّر مترجماً مجاناً. قل: <span dir=\"ltr\"><strong>I need an Arabic interpreter, please.</strong></span> (أحتاج مترجماً للعربية من فضلك.)</div>"),
  ("", appbox(AM, "تدرّب على هذه الجمل مع أمريكا سهلة",
    "بنيت تطبيق <strong>أمريكا سهلة</strong> لهذا الهدف بالضبط: الإنجليزية التي تحتاجها فعلاً في الحياة اليومية في أمريكا، وكل الشرح بالعربي.",
    ["57 درساً في 8 مستويات، في رحلة من نيويورك إلى لوس أنجلوس",
     "البنك، الـDMV، الطبيب والصيدلية، المدرسة، السكن، العمل ومقابلات العمل",
     "لكل كلمة صورة وصوت أمريكي واضح والمعنى بالعربي ونطق مكتوب بحروف عربية",
     "نصائح لأصعب الأصوات على العرب: P و V و TH و CH",
     "المستوى الأول مجاني، بلا حساب وبلا إعلانات"],
    "حمّل أمريكا سهلة من App Store") +
   "<p class=\"note\">هذا المقال لتعلّم اللغة فقط، وليس نصيحة قانونية أو مالية. المتطلبات تختلف من ولاية إلى أخرى.</p>")]))

ART.insert(2, ("english-sounds-arabic-speakers-p-v-th",
 "لماذا يصعب على العرب نطق P و V و TH و CH؟ وكيف تتدرّب عليها",
 "شرح بالعربي لأصعب أصوات الإنجليزية على المتحدثين بالعربية: P و V و TH و CH، مع كلمات للتدريب ونصائح عملية.",
 [("", TSTYLE +
   "<p>إذا قلت <span dir=\"ltr\"><strong>bark</strong></span> وأنت تقصد <span dir=\"ltr\"><strong>park</strong></span>، فأنت لست وحدك. بعض أصوات الإنجليزية غير موجودة في العربية الفصحى، فيستبدلها دماغنا بأقرب صوت يعرفه. الخبر الجيد: هذه الأخطاء معروفة ولها حلول سهلة.</p>"),
  ("صوت P (مثل park)",
   "<p>العربية ليس فيها P، لذلك نقولها غالباً B. الفرق أن P تخرج <strong>بنفخة هواء</strong> ومن دون اهتزاز في الحلق.</p>"
   "<p><strong>التمرين:</strong> ضع يدك أمام فمك وقل <span dir=\"ltr\">park</span>. يجب أن تشعر بنفخة هواء. ثم قل <span dir=\"ltr\">bark</span>: النفخة أضعف بكثير.</p>" +
   '<table class="t"><tr><th>P</th><th>B</th></tr>' + "".join(f'<tr><td class="en">{a}</td><td class="en">{b}</td></tr>' for a, b in [("park", "bark"), ("pay", "bay"), ("pill", "bill"), ("pet", "bet")]) + "</table>"),
  ("صوت V (مثل very)",
   "<p>نقولها كثيراً مثل F. الحل: ضع أسنانك العلوية على شفتك السفلى، تماماً كما تقول ف، لكن <strong>شغّل صوتك</strong> حتى تشعر باهتزاز في الشفة.</p>" +
   '<table class="t"><tr><th>V</th><th>F</th></tr>' + "".join(f'<tr><td class="en">{a}</td><td class="en">{b}</td></tr>' for a, b in [("very", "fairy"), ("van", "fan"), ("vote", "photo"), ("live", "leaf")]) + "</table>"),
  ("صوت TH: عندك ميزة",
   "<p>هنا العرب عندهم ميزة حقيقية: صوتا TH موجودان في العربية.</p><ul>"
   "<li><span dir=\"ltr\"><strong>think, three, thank you</strong></span>: مثل حرف <strong>ث</strong></li>"
   "<li><span dir=\"ltr\"><strong>this, that, mother</strong></span>: مثل حرف <strong>ذ</strong></li></ul>"
   "<p>المشكلة أن كثيراً من اللهجات تنطق ث وذ مثل س وز أو ت ود. إذا كنت تقول <span dir=\"ltr\">\"tank you\"</span> أو <span dir=\"ltr\">\"sank you\"</span>، فتذكّر فقط: <strong>ث</strong> كما في الفصحى، واللسان بين الأسنان.</p>"),
  ("صوت CH (مثل chair)",
   "<p>صوت CH هو <strong>تش</strong>. أهل العراق والخليج عندهم ميزة هنا، لأن حرف <strong>چ</strong> في لهجتهم هو نفس الصوت تقريباً (چاي). لا تخلطه مع SH (ش):</p>" +
   '<table class="t"><tr><th>CH (تش)</th><th>SH (ش)</th></tr>' + "".join(f'<tr><td class="en">{a}</td><td class="en">{b}</td></tr>' for a, b in [("chair", "share"), ("watch", "wash"), ("cheap", "sheep"), ("chip", "ship")]) + "</table>"),
  ("خطة تدريب ٥ دقائق يومياً",
   "<ol><li>اختر صوتاً واحداً فقط كل أسبوع.</li><li>اسمع الكلمة من متحدث أمريكي ثم كرّرها بصوت عالٍ ٥ مرات.</li>"
   "<li>سجّل صوتك على الهاتف وقارنه بالأصل.</li><li>استخدم الكلمة في جملة حقيقية في نفس اليوم.</li></ol>"),
  ("", appbox(AM, "تدرّب بالصوت مع أمريكا سهلة",
    "تطبيق <strong>أمريكا سهلة</strong> فيه نصائح خاصة بالأصوات الصعبة على العرب، ولكل كلمة صوت أمريكي واضح ونطق مكتوب بحروف عربية.",
    ["57 درساً للحياة اليومية في أمريكا", "صوت أمريكي واضح لكل كلمة", "نصائح لأصوات P و V و TH و CH", "المستوى الأول مجاني"],
    "حمّل أمريكا سهلة من App Store"))]))

ART.insert(3, ("learn-german-for-beginners-arabic",
 "تعلّم اللغة الألمانية للمبتدئين بالعربي: خطة واضحة للوصول إلى المستوى A1",
 "دليل بالعربي لتعلّم الألمانية من الصفر حتى المستوى A1: ما هو A1، أصعب الأصوات، أول كلمات تحتاجها، وأقسام امتحان A1 الأربعة.",
 [("", TSTYLE +
   "<p>سواء كنت تستعد للسفر إلى ألمانيا أو النمسا أو سويسرا، أو تحتاج شهادة A1 لملفّك، فالبداية الصحيحة توفّر عليك أشهراً. هذا دليل بسيط بالعربي لأول خطواتك.</p>"
   f'<p><strong>تريد أن تبدأ اليوم؟</strong> <a href="{store(A["german-easy-arabic-edition"])}">حمّل ألماني سهل مجاناً من App Store</a>. الوحدة الأولى مجانية.</p>'),
  ("ما هو المستوى A1؟",
   "<p>A1 هو أول مستوى في الإطار الأوروبي للغات. في هذا المستوى تستطيع أن تعرّف بنفسك، وتسأل وتجيب عن أشياء بسيطة مثل العنوان والعمل والعائلة، وتفهم جملاً قصيرة في التسوّق والمواعيد. في كثير من الحالات يُطلب A1 من الأزواج والزوجات في ملفات لمّ الشمل، لذلك تحقّق دائماً من المتطلبات الرسمية الخاصة بحالتك.</p>"),
  ("أول كلمات وجمل تحتاجها",
   '<table class="t"><tr><th>بالألمانية</th><th>المعنى</th></tr>' + rows([
    ("Hallo / Guten Tag", "مرحباً / نهارك سعيد"),
    ("Danke / Bitte", "شكراً / من فضلك أو عفواً"),
    ("Entschuldigung", "عفواً، لو سمحت"),
    ("Ich heiße ...", "اسمي ..."),
    ("Ich komme aus ...", "أنا من ..."),
    ("Wie geht's?", "كيف حالك؟"),
    ("Ich verstehe nicht.", "لا أفهم."),
    ("Sprechen Sie langsam, bitte.", "تكلّم ببطء من فضلك.")]) + "</table>"),
  ("أصوات تحتاج انتباهاً",
   "<ul><li><strong>ü و ö و ä</strong>: أصوات غير موجودة في العربية. استمع إليها كثيراً قبل أن تحاول نطقها.</li>"
   "<li><strong>ch</strong>: في كلمة <span dir=\"ltr\">Ich</span> صوت خفيف قريب من الهمس، وفي <span dir=\"ltr\">Buch</span> قريب من <strong>خ</strong>.</li>"
   "<li><strong>r</strong>: الألمانية غالباً تنطقها من الحلق، قريبة من <strong>غ</strong> خفيفة.</li>"
   "<li><strong>w</strong>: تُنطق مثل V الإنجليزية، فـ<span dir=\"ltr\">Wasser</span> تبدأ بصوت \"ڤ\".</li></ul>"),
  ("أقسام امتحان A1 الأربعة",
   "<ul><li><strong>Hören</strong>: الاستماع</li><li><strong>Lesen</strong>: القراءة</li><li><strong>Schreiben</strong>: الكتابة (مثل تعبئة استمارة أو رسالة قصيرة)</li><li><strong>Sprechen</strong>: المحادثة (تعريف بالنفس وأسئلة بسيطة)</li></ul>"
   "<p>تدرّب على الأقسام الأربعة كلها، ولا تترك المحادثة للنهاية.</p>"),
  ("خطة ١٥ دقيقة يومياً",
   "<ol><li>٥ دقائق: كلمات جديدة مع الصوت.</li><li>٥ دقائق: حوار قصير، اسمعه ثم كرّره.</li><li>٥ دقائق: مراجعة البطاقات والاختبارات القصيرة.</li></ol><p>الاستمرار يومياً أهم من الساعات الطويلة مرة في الأسبوع.</p>"),
  ("", appbox("german-easy-arabic-edition", "ابدأ مع ألماني سهل",
    "تطبيق <strong>ألماني سهل</strong> مصمّم للعرب: كل الشرح والقوائم بالعربي، ولكل كلمة صوت ألماني واضح، والنطق مكتوب بحروف عربية.",
    ["76 درساً في 14 وحدة حتى المستوى A1",
     "تدريب على أقسام امتحان A1 مع شرح بالعربي (مواد تدريبية خاصة بالتطبيق، وليست أسئلة امتحان رسمية)",
     "حوارات قصيرة ومضحكة من الحياة اليومية في ألمانيا",
     "الوحدة الأولى مجانية"],
    "حمّل ألماني سهل من App Store"))]))

ART.insert(4, ("common-iraqi-arabic-phrases",
 "25 Everyday Iraqi Arabic Phrases (with Pronunciation)",
 "25 common Iraqi Arabic phrases with Arabic script, easy pronunciation and English meaning, for heritage learners, spouses and travelers.",
 [("", TSTYLE +
   "<p>Iraqi Arabic sounds very different from the Modern Standard Arabic taught in most courses. If you want to talk with Iraqi family and friends, start with the phrases people actually use every day. Pronunciation below follows the Baghdadi dialect; accents vary by city and family.</p>"
   f'<p><strong>Want to hear them spoken?</strong> <a href="{store(A["learn-iraqi-arabic-easy"])}">Get Learn Iraqi Arabic Easy on the App Store</a>, with native Iraqi voices.</p>'),
  ("Greetings and small talk",
   '<table class="t"><tr><th>Iraqi Arabic</th><th>Say it</th><th>Meaning</th></tr>' + "".join(f'<tr><td dir="rtl" lang="ar">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in [
    ("شلونك؟", "shlonak? (to a man) / shlonich? (to a woman)", "How are you?"),
    ("زين، الحمد لله", "zein, il-hamdu lillah", "Good, thank God"),
    ("شكو ماكو؟", "shaku maku?", "What's new? What's going on?"),
    ("ماكو شي", "maku shi", "Nothing much"),
    ("هلا والله", "hala wallah", "Hey, welcome! (warm greeting)"),
    ("الله وياك", "allah wiyak", "Goodbye (God be with you)"),
    ("تسلم", "tislam", "Thanks (bless you)"),
    ("عيوني", "eyooni", "My dear (literally \"my eyes\")")]) + "</table>"),
  ("Everyday words you'll hear constantly",
   '<table class="t"><tr><th>Iraqi Arabic</th><th>Say it</th><th>Meaning</th></tr>' + "".join(f'<tr><td dir="rtl" lang="ar">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in [
    ("اكو / ماكو", "aku / maku", "There is / there isn't"),
    ("شنو؟", "shinu?", "What?"),
    ("وين؟", "wein?", "Where?"),
    ("هسه", "hessa", "Now"),
    ("باچر", "bachir", "Tomorrow"),
    ("هواية", "hwaya", "A lot, very"),
    ("خوش", "khosh", "Good, nice"),
    ("أريد", "arid", "I want"),
    ("يللا", "yalla", "Come on, let's go")]) + "</table>"),
  ("At the table",
   '<table class="t"><tr><th>Iraqi Arabic</th><th>Say it</th><th>Meaning</th></tr>' + "".join(f'<tr><td dir="rtl" lang="ar">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in [
    ("تمن", "timman", "Rice"),
    ("خبز", "khubuz", "Bread"),
    ("ماي", "mai", "Water"),
    ("چاي", "chai", "Tea"),
    ("بالعافية", "bil-afya", "Enjoy your meal / to your health"),
    ("شبعت", "shbaat", "I'm full"),
    ("طيب هواية", "tayyib hwaya", "Very tasty"),
    ("كافي", "kafi", "Enough, that's enough")]) + "</table>"
   "<p class=\"note\">Iraqi Arabic uses the letter چ (ch) and گ (g), which don't exist in standard Arabic: <em>chai</em> (tea) and <em>bachir</em> (tomorrow) use the ch sound.</p>"),
  ("", appbox("learn-iraqi-arabic-easy", "Keep going with Learn Iraqi Arabic Easy",
    "<strong>Learn Iraqi Arabic Easy</strong> teaches the dialect your family actually speaks, recorded by native Iraqi speakers.",
    ["800+ real Iraqi Arabic words and phrases in 65+ lessons", "Animated two-speaker conversations", "Simple grammar: verbs, past tense, pronouns", "Flashcards, matching and fill-in-the-blank games"],
    "Get Learn Iraqi Arabic Easy on the App Store"))]))

LANG = {"practical-english-for-life-in-america-arabic": "ar", "english-sounds-arabic-speakers-p-v-th": "ar", "learn-german-for-beginners-arabic": "ar"}
for _s in ["practical-english-for-life-in-america-arabic", "english-sounds-arabic-speakers-p-v-th", "learn-german-for-beginners-arabic", "common-iraqi-arabic-phrases"]:
    DATES[_s] = "2026-11-09"

for slug,title,desc,secs in ART:
    b="".join((f"<h2>{html.escape(h)}</h2>" if h else "")+(t if t.startswith(("<p","<div","<style","<table","<ol","<ul")) else f"<p>{t}</p>") for h,t in secs)
    lg=LANG.get(slug,"en")
    back="&larr; All apps" if lg=="en" else "كل التطبيقات &larr;"
    body=f"<header><h1>{html.escape(title)}</h1></header><main>{b}<p><a href=\"../index.html\">{back}</a></p></main>"
    os.makedirs("articles",exist_ok=True)
    p=page(title,desc,f"articles/{slug}.html",body,{"@context":"https://schema.org","@type":"Article","headline":title,"author":{"@type":"Person","name":"Athir Maroki"},"datePublished":DATES.get(slug,"2026-11-01")},lang=lg)
    p=p.replace('href="../index.html"','href="../index.html"').replace(f'<a href="{BASE}/">Home</a>',f'<a href="{BASE}/">Home</a>')
    open(f"articles/{slug}.html","w",encoding="utf-8").write(p); urls.append(f"{BASE}/articles/{slug}.html")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{u}</loc></url>" for u in urls)+"</urlset>")
llms=["# Easy Language Apps by Athir Maroki","","> Independent iPhone apps for learning spoken languages, especially heritage languages of Iraqi and Arabic-speaking families. Native-speaker audio, games and short daily lessons.","","## Apps",""]
llms+=[f"- [{a['name']}]({BASE}/{a['slug']}.html): {a['intro']} App Store: {store(a)}" for a in APPS]
llms+=["","## Guides",""]+[f"- [{t}]({BASE}/articles/{s}.html): {d}" for s,t,d,_ in ART]
llms+=["","## Developer","","- Athir Maroki, independent developer, Michigan, USA",f"- All apps: {DEV}",""]
open("llms.txt","w",encoding="utf-8").write("\n".join(llms))
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("built", len(urls), "pages")
