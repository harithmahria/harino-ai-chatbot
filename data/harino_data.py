# ============================================
# Harino.ai — UGC AI Studio Chatbot Data
# Alle informatie over het Harino.ai platform
# ============================================

documents = []

# ==========================================
# PLATFORM INFO — Wat is Harino.ai?
# ==========================================
platform_info = [
    "Harino.ai is een AI-gestuurd UGC (User Generated Content) video platform. Gebruikers kunnen professionele AI-gegenereerde video's maken zonder acteurs, camera's of studio's. Het platform richt zich op advertenties, productdemo's en social media content.",
    "Harino.ai maakt professionele UGC video productie toegankelijk voor iedereen via AI. Gebruikers uploaden een productfoto, beschrijven wat ze willen, en het platform genereert een professionele UGC video in ongeveer drie minuten.",
    "Harino.ai heeft meer dan 1 miljard views gegenereerd met advertenties gemaakt op het platform. Het is geschikt voor ondernemers, marketeers, agencies, e-commerce merken en content creators.",
    "Contact: Voor vragen en support, mail naar support@harino.ai. Website: https://harino.ai",
]
for text in platform_info:
    documents.append({"content": text, "category": "info"})

# ==========================================
# FEATURES — Wat kan je ermee?
# ==========================================
features = [
    "AI Avatar Ads (Creator Track): Maak advertenties met een AI avatar als presentator. Ideaal voor TikTok, Instagram Reels en landingspagina's. Schrijf een script, kies een AI actor en genereer een professionele video.",
    "UGC Style Videos (Brand Track): Maak productdemo's, creator-style testimonials en snelle advertentievariaties. De AI creëert video's met product interactie in UGC stijl.",
    "AI Video Generatie: Harino.ai gebruikt de nieuwste AI modellen voor video generatie, waaronder Sora 2 (OpenAI), Kling Pro, Veo 3 (Google), en meer. Alleen modellen die fotorealistische resultaten leveren worden geselecteerd.",
    "AI Foto Generatie: Harino.ai kan ook foto's en productbeelden genereren met Nano Banana. Gebruikers kunnen foto prompts gebruiken om visuele assets te maken voor advertenties, productcontent en social media.",
    "1000+ AI Actors: Kies uit meer dan 1000 AI acteurs met verschillende looks, leeftijden en stijlen. Je kunt ook je eigen foto uploaden om een custom AI actor te maken.",
    "Emotie controle: Volledige controle over de emoties en expressies van je AI actor in de gegenereerde video's.",
    "Multi-taal support: Genereer video's in meer dan 30 talen. Ideaal voor internationale campagnes en localisatie.",
    "UGC Editor: Schrijf een script, kies een AI actor (of upload je eigen foto), en het platform genereert automatisch een professionele UGC video.",
    "Snelle productie: Een professionele UGC video wordt in ongeveer 3 minuten gegenereerd. Geen wachttijden van dagen of weken zoals bij traditionele video productie.",
    "Platform optimalisatie: Video's zijn geoptimaliseerd voor TikTok, Instagram Reels, landingspagina's, websites en betaalde advertentiecampagnes. Verticaal kort formaat (9:16).",
]
for text in features:
    documents.append({"content": text, "category": "features"})

# ==========================================
# HOE WERKT HET?
# ==========================================
how_it_works = [
    "Stap 1 - Kies je content formaat: Selecteer of je een AI Avatar Ad wilt maken (met een presentator) of een UGC Style Video (productdemo, testimonial).",
    "Stap 2 - Kies een AI creator of actor: Kies uit 1000+ AI acteurs of upload je eigen foto om een custom AI actor te maken.",
    "Stap 3 - Schrijf je script: Schrijf het script voor je video of laat de AI een script genereren. Beschrijf wat je wilt laten zien.",
    "Stap 4 - Genereer de video: Het platform gebruikt AI modellen (Sora 2, Kling Pro, Veo 3) om je video te genereren in ongeveer 3 minuten.",
    "Stap 5 - Publiceer: Download je video en publiceer op TikTok, Instagram, je website of gebruik het in advertentiecampagnes.",
]
for text in how_it_works:
    documents.append({"content": text, "category": "info"})

# ==========================================
# PRICING — Abonnementen
# ==========================================
pricing = [
    "Harino.ai Starter Plan: 49,99 dollar per maand. Inclusief 4.000 credits per maand, toegang tot alle AI modellen, avatar ads en UGC video's, en standaard support. Automatische verlenging, op elk moment opzegbaar.",
    "Harino.ai Creator Plan (meest populair): 99 dollar per maand. Inclusief 8.000 credits per maand, alle AI modellen, priority support, en automatische verlenging. Best voor wekelijkse content en advertentie testing.",
    "Harino.ai Pro Plan: 149 dollar per maand. Inclusief 16.000 credits per maand, alle AI modellen, priority support, en automatische verlenging. Ideaal voor teams, agencies en grotere volumes.",
    "Alle plannen bevatten toegang tot alle AI modellen (Sora 2, Kling Pro, Veo 3 en meer), de volledige UGC editor, en 1000+ AI actors. Het verschil zit in het aantal credits en het support level.",
    "Credits systeem: Harino.ai werkt met een maandelijks credit systeem. Elke video generatie kost een bepaald aantal credits afhankelijk van het model en de videoduur. Credits worden elke maand vernieuwd bij je abonnement.",
]
for text in pricing:
    documents.append({"content": text, "category": "pricing"})

# ==========================================
# AI MODELLEN
# ==========================================
ai_models = [
    "Sora 2 (OpenAI): Een van de beschikbare AI video modellen op Harino.ai. Bekend om hoge kwaliteit en realistische video generatie. Onderdeel van alle abonnementen.",
    "Kling Pro: AI video generatie model beschikbaar op Harino.ai. Levert fotorealistische resultaten voor UGC content. Onderdeel van alle abonnementen.",
    "Veo 3 (Google): Google's AI video model, beschikbaar op Harino.ai. Staat bekend om natuurlijke bewegingen en hoge kwaliteit output. Onderdeel van alle abonnementen.",
    "Nano Banana: AI model voor foto generatie en beeldcreatie binnen Harino.ai. Geschikt voor het maken van productbeelden, advertentiebeelden en social media visuals.",
    "Harino.ai integreert ook andere AI modellen zoals Seedance, Hailuo, Luma en Framepack. Het team voegt nieuwe modellen toe kort na release. Alleen modellen die fotorealistische, niet van echt te onderscheiden video's produceren worden geselecteerd.",
]
for text in ai_models:
    documents.append({"content": text, "category": "features"})

# ==========================================
# USE CASES — Waarvoor gebruik je het?
# ==========================================
use_cases = [
    "E-commerce: Maak productdemo video's en UGC advertenties voor je webshop. Upload een productfoto en genereer meerdere advertentievariaties voor A/B testing.",
    "Social Media Marketing: Genereer korte, verticale video's geoptimaliseerd voor TikTok en Instagram Reels. Schaal je content productie op zonder extra kosten voor creators.",
    "Advertentie Agencies: Maak snel meerdere advertentievariaties voor klanten. Test verschillende scripts, AI actors en stijlen. Bespaar op productiekosten en doorlooptijd.",
    "Dropshipping en DTC merken: Genereer snel UGC-style content voor nieuwe producten zonder te wachten op creators. Ideaal voor snelle product launches.",
    "Internationale campagnes: Gebruik de multi-taal functie om dezelfde advertentie in 30+ talen te genereren voor internationale markten.",
    "Startups en kleine bedrijven: Professionele video content zonder het budget voor traditionele videoproductie. Begin al vanaf 49,99 dollar per maand.",
]
for text in use_cases:
    documents.append({"content": text, "category": "info"})

# ==========================================
# BEDRIJFSWAARDEN
# ==========================================
values = [
    "Innovatie: Het Harino.ai team integreert nieuwe AI modellen kort na hun release. Het platform blijft altijd up-to-date met de nieuwste AI technologie.",
    "Kwaliteit boven kwantiteit: Fotorealisme is de standaard. Alleen AI modellen die video's produceren die niet van echt te onderscheiden zijn worden geselecteerd.",
    "Transparantie: Duidelijke prijzen zonder verborgen kosten. Open communicatie over hoe de AI werkt.",
    "Toegankelijkheid: Professionele video productie is beschikbaar voor iedereen, van solo-ondernemers tot grote agencies.",
]
for text in values:
    documents.append({"content": text, "category": "info"})

# ==========================================
# FAQ — Veelgestelde vragen
# ==========================================
faq_items = [
    ("Wat is Harino.ai?", "Harino.ai is een AI-gestuurd platform waarmee je professionele UGC video's en avatar advertenties kunt maken zonder acteurs, camera's of studio's. Upload een productfoto, schrijf een script, kies een AI actor en genereer een video in ongeveer 3 minuten."),
    ("Hoe werkt het credits systeem?", "Harino.ai werkt met maandelijkse credits. Starter geeft 4.000 credits, Creator 8.000 en Pro 16.000 per maand. Elke video generatie kost credits afhankelijk van het gekozen AI model en de videoduur. Credits worden elke maand vernieuwd."),
    ("Welke AI modellen zijn beschikbaar?", "Harino.ai biedt toegang tot Sora 2 (OpenAI), Kling Pro, Veo 3 (Google), Seedance, Hailuo, Luma, Framepack en meer. Alle modellen zijn beschikbaar in elk abonnement."),
    ("Kan Harino.ai foto's genereren?", "Ja, Harino.ai kan foto's genereren met Nano Banana. Dit kan gebruikt worden voor productbeelden, advertentiebeelden en social media visuals."),
    ("Hoeveel kost Harino.ai?", "Starter plan: 49,99 dollar per maand (4.000 credits). Creator plan: 99 dollar per maand (8.000 credits). Pro plan: 149 dollar per maand (16.000 credits). Alle plannen bevatten toegang tot alle AI modellen."),
    ("Kan ik mijn abonnement opzeggen?", "Ja, je kunt je abonnement op elk moment opzeggen. Je behoudt toegang tot het einde van je huidige factureringsperiode."),
    ("In hoeveel talen kan ik video's genereren?", "Harino.ai ondersteunt meer dan 30 talen voor video generatie. Ideaal voor internationale campagnes en localisatie van content."),
    ("Kan ik mijn eigen foto uploaden als AI actor?", "Ja, je kunt je eigen foto uploaden om een custom AI actor te maken. Daarnaast kun je kiezen uit meer dan 1000 vooraf beschikbare AI acteurs."),
    ("Hoe lang duurt het om een video te genereren?", "Een professionele UGC video wordt in ongeveer 3 minuten gegenereerd, afhankelijk van het gekozen AI model en de complexiteit."),
    ("Waarvoor kan ik de video's gebruiken?", "De video's zijn geoptimaliseerd voor TikTok, Instagram Reels, landingspagina's, websites en betaalde advertentiecampagnes. Ze zijn in verticaal kort formaat (9:16)."),
    ("Wat is het verschil tussen Avatar Ads en UGC Videos?", "Avatar Ads gebruiken een AI presentator die direct in de camera praat, ideaal voor advertenties en uitleg. UGC Style Videos zijn meer productdemo's en creator-style testimonials met productinteractie."),
    ("Is er een gratis proefperiode?", "Neem contact op met support@harino.ai voor de meest actuele informatie over proefperiodes en aanbiedingen."),
    ("Hoe verschilt Harino.ai van traditionele video productie?", "Traditionele UGC video's kosten honderden euro's per video, duren dagen tot weken en vereisen acteurs en studio's. Harino.ai genereert fotorealistische video's in 3 minuten, vanaf 49,99 dollar per maand voor onbeperkt experimenteren."),
    ("Wat als ik meer credits nodig heb?", "Je kunt upgraden naar een hoger plan voor meer maandelijkse credits. Neem contact op met support@harino.ai voor custom volumes."),
    ("Voor welke platforms zijn de video's geschikt?", "De video's zijn geoptimaliseerd voor TikTok, Instagram Reels, Facebook, YouTube Shorts, landingspagina's en betaalde advertenties op Meta en TikTok Ads."),
    ("Wie gebruikt Harino.ai?", "E-commerce merken, dropshippers, social media marketeers, advertentie agencies, DTC merken, content creators, startups en kleine bedrijven."),
    ("Hoe bereik ik support?", "Stuur een email naar support@harino.ai. Creator en Pro plan gebruikers hebben priority support."),
    ("Is de kwaliteit vergelijkbaar met echte video's?", "Ja, Harino.ai selecteert alleen AI modellen die fotorealistische, van echt niet te onderscheiden video's produceren. Kwaliteit boven kwantiteit is een kernwaarde."),
    ("Kan ik de video's gebruiken voor betaalde advertenties?", "Ja, de video's zijn specifiek geoptimaliseerd voor betaalde advertenties op TikTok Ads, Meta Ads (Facebook/Instagram) en andere platforms."),
    ("What is Harino.ai?", "Harino.ai is an AI-powered UGC video platform. Create professional AI-generated videos with avatar ads and UGC-style content without actors, cameras or studios. Starting from $49.99/month."),
    ("How does the credit system work?", "Harino.ai uses monthly credits. Starter gives 4,000 credits, Creator 8,000, and Pro 16,000 per month. Each video generation costs credits based on the AI model and video length."),
    ("What AI models are available?", "Harino.ai offers Sora 2 (OpenAI), Kling Pro, Veo 3 (Google), Seedance, Hailuo, Luma, Framepack and more. All models are included in every subscription plan."),
]
for vraag, antwoord in faq_items:
    documents.append({
        "content": f"Vraag: {vraag} Antwoord: {antwoord}",
        "category": "faq"
    })

# ==========================================
# VERGELIJKING — Waarom Harino.ai?
# ==========================================
comparison = [
    "Vergelijking Harino.ai vs traditionele UGC: Traditioneel kost een UGC video 200-500 euro per stuk, duurt 3-7 dagen en vereist een creator, camera en editing. Met Harino.ai kost het vanaf 49,99 dollar per maand voor meerdere video's, duurt het 3 minuten per video en heb je geen crew nodig.",
    "Vergelijking Harino.ai vs andere AI video tools: Harino.ai onderscheidt zich door toegang tot meerdere top AI modellen (Sora 2, Kling Pro, Veo 3) in een platform, 1000+ AI actors, UGC-specifieke features, en multi-taal ondersteuning in 30+ talen.",
]
for text in comparison:
    documents.append({"content": text, "category": "info"})
