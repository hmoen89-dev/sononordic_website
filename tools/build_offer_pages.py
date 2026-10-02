"""Generate code-free instructions for recipients of privately shared campaign codes."""
import html
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / 'site'
LANGS = {'sv': 'Svenska', 'nb': 'Norsk', 'da': 'Dansk', 'en': 'English'}
APPLE = 'https://apps.apple.com/app/id6781746961'
PLAY = 'https://play.google.com/store/apps/details?id=se.sononordic.akutpocus'
COPY = {
'en': {
 'title': 'Campaign code instructions', 'language': 'Language', 'home': 'SonoNordic home',
 'intro': 'Have you received a campaign code for AkutPOCUS? Use the code shared with you in a message or at an event.',
 'termsTitle': 'The same offer on iPhone and Android',
 'terms': 'The campaign code applies to the monthly subscription and is available to new subscribers only, once per eligible store account. After 14 days, the subscription renews automatically at the local monthly price unless cancelled before renewal. In Sweden: 49 SEK/month. Other countries use the price and currency shown by the store. A valid payment method is required. Redeem by 31 October 2026, subject to remaining redemptions and store availability in your country. Apple: 500 redemptions; Google Play: 2,000. The code has no cash value and is not for resale.',
 'appleTitle': 'iPhone and iPad', 'apple': 'Install AkutPOCUS. Open the App Store, tap your account picture and choose Redeem Gift Card or Code. Enter the code you received and follow the instructions. Confirm that the store shows the offered free period before accepting. Then open AkutPOCUS; use Restore purchases if needed.', 'appleButton': 'Get AkutPOCUS on the App Store',
 'androidTitle': 'Android', 'android': 'Install AkutPOCUS from Google Play. Open the full-access screen and choose the monthly subscription. In Google Play’s purchase sheet, open the payment-method menu, choose Redeem code and enter the code you received. Confirm that the sheet shows 14 days free before accepting. This custom code must be entered in the purchase sheet opened from the app, not on Google Play’s general redemption page or in the app’s store-review code field.', 'androidButton': 'Get AkutPOCUS on Google Play',
 'cancelTitle': 'Cancel before renewal to avoid a charge', 'cancel': 'Manage or cancel the subscription in your Apple Account or Google Play subscriptions. Follow the deadline shown by the store; we recommend cancelling at least 24 hours before renewal. Uninstalling the app does not cancel a subscription. If the store does not show the free period, do not confirm a paid purchase; contact info@sononordic.se for help.',
 'freeTitle': 'Free content remains free', 'free': 'eFAST, Lungs and thorax, and Arterial line are available without a subscription. The campaign code unlocks the remaining content during the offer. AkutPOCUS is an educational and reference app for healthcare professionals and medical students, in Swedish, Norwegian, Danish and English.',
 'termsLink': 'Subscription terms', 'privacyLink': 'Privacy',
},
'sv': {
 'title': 'Instruktioner för kampanjkod', 'language': 'Språk', 'home': 'Till SonoNordic',
 'intro': 'Har du fått en kampanjkod för AkutPOCUS? Använd koden som delats med dig i ett meddelande eller vid en föreläsning.',
 'termsTitle': 'Samma erbjudande på iPhone och Android',
 'terms': 'Kampanjkoden gäller månadsprenumerationen och endast nya prenumeranter, en gång per berättigat butikskonto. Efter 14 dagar förnyas prenumerationen automatiskt till det lokala månadspriset om den inte sägs upp före förnyelsen. I Sverige: 49 SEK/månad. I andra länder gäller priset och valutan som visas i butiken. En giltig betalningsmetod krävs. Lös in senast 31 oktober 2026, så länge inlösningar finns kvar och appen är tillgänglig i ditt land. Apple: 500 inlösningar; Google Play: 2 000. Koden saknar kontantvärde och får inte säljas vidare.',
 'appleTitle': 'iPhone och iPad', 'apple': 'Installera AkutPOCUS. Öppna App Store, tryck på din kontobild och välj Lös in presentkort eller kod. Ange koden du fått och följ instruktionerna. Kontrollera att butiken visar den erbjudna gratisperioden innan du bekräftar. Öppna sedan AkutPOCUS; använd Återställ köp vid behov.', 'appleButton': 'Hämta AkutPOCUS på App Store',
 'androidTitle': 'Android', 'android': 'Installera AkutPOCUS från Google Play. Öppna sidan för full åtkomst och välj månadsprenumerationen. Öppna menyn för betalningsmetod i Google Plays köpruta, välj Lös in kod och ange koden du fått. Kontrollera att rutan visar 14 dagar gratis innan du bekräftar. Denna kampanjkod ska anges i köprutan som öppnas från appen, inte på Google Plays allmänna inlösningssida eller i appens kodfält för butikskontroll.', 'androidButton': 'Hämta AkutPOCUS på Google Play',
 'cancelTitle': 'Säg upp före förnyelsen för att undvika debitering', 'cancel': 'Hantera eller säg upp prenumerationen i ditt Apple-konto eller under prenumerationer i Google Play. Följ butikens tidsfrist; vi rekommenderar uppsägning minst 24 timmar före förnyelsen. Avinstallation avslutar inte prenumerationen. Om butiken inte visar gratisperioden ska du inte bekräfta ett betalköp; kontakta info@sononordic.se för hjälp.',
 'freeTitle': 'Gratisinnehållet förblir gratis', 'free': 'eFAST, Lungor och thorax samt Artärnål är tillgängliga utan prenumeration. Kampanjkoden låser upp övrigt innehåll under erbjudandet. AkutPOCUS är en utbildnings- och referensapp för vårdpersonal och läkarstudenter, på svenska, norska, danska och engelska.',
 'termsLink': 'Prenumerationsvillkor', 'privacyLink': 'Integritet',
},
'nb': {
 'title': 'Instruksjoner for kampanjekode', 'language': 'Språk', 'home': 'Til SonoNordic',
 'intro': 'Har du fått en kampanjekode for AkutPOCUS? Bruk koden som er delt med deg i en melding eller på et foredrag.',
 'termsTitle': 'Samme tilbud på iPhone og Android',
 'terms': 'Kampanjekoden gjelder månedsabonnementet og bare nye abonnenter, én gang per kvalifisert butikkonto. Etter 14 dager fornyes abonnementet automatisk til lokal månedspris dersom det ikke sies opp før fornyelsen. I Sverige: 49 SEK/måned. I andre land gjelder prisen og valutaen som vises i butikken. Gyldig betalingsmåte kreves. Løs inn senest 31. oktober 2026, så lenge innløsninger gjenstår og appen er tilgjengelig i landet ditt. Apple: 500 innløsninger; Google Play: 2 000. Koden har ingen kontantverdi og skal ikke videreselges.',
 'appleTitle': 'iPhone og iPad', 'apple': 'Installer AkutPOCUS. Åpne App Store, trykk på kontobildet ditt og velg Løs inn gavekort eller kode. Skriv inn koden du har fått og følg instruksjonene. Kontroller at butikken viser den tilbudte gratisperioden før du bekrefter. Åpne deretter AkutPOCUS; bruk Gjenopprett kjøp ved behov.', 'appleButton': 'Hent AkutPOCUS på App Store',
 'androidTitle': 'Android', 'android': 'Installer AkutPOCUS fra Google Play. Åpne siden for full tilgang og velg månedsabonnementet. Åpne menyen for betalingsmåte i Googles kjøpsvindu, velg Løs inn kode og skriv koden du har fått. Kontroller at vinduet viser 14 dager gratis før du bekrefter. Denne kampanjekoden skal brukes i kjøpsvinduet som åpnes fra appen, ikke på Google Plays generelle innløsningsside eller i appens kodefelt for butikkontroll.', 'androidButton': 'Hent AkutPOCUS på Google Play',
 'cancelTitle': 'Si opp før fornyelse for å unngå belastning', 'cancel': 'Administrer eller si opp abonnementet i Apple-kontoen din eller under abonnementer i Google Play. Følg butikkens frist; vi anbefaler oppsigelse minst 24 timer før fornyelse. Avinstallasjon avslutter ikke abonnementet. Hvis butikken ikke viser gratisperioden, skal du ikke bekrefte et betalt kjøp; kontakt info@sononordic.se for hjelp.',
 'freeTitle': 'Gratisinnholdet forblir gratis', 'free': 'eFAST, Lunger og thorax samt Arteriekanyle er tilgjengelig uten abonnement. Kampanjekoden åpner resten av innholdet i tilbudsperioden. AkutPOCUS er en undervisnings- og referanseapp for helsepersonell og medisinstudenter, på svensk, norsk, dansk og engelsk.',
 'termsLink': 'Abonnementsvilkår', 'privacyLink': 'Personvern',
},
'da': {
 'title': 'Vejledning til kampagnekode', 'language': 'Sprog', 'home': 'Til SonoNordic',
 'intro': 'Har du fået en kampagnekode til AkutPOCUS? Brug koden, der er delt med dig i en besked eller ved et foredrag.',
 'termsTitle': 'Samme tilbud på iPhone og Android',
 'terms': 'Kampagnekoden gælder månedsabonnementet og kun nye abonnenter, én gang pr. berettiget butikskonto. Efter 14 dage fornyes abonnementet automatisk til den lokale månedspris, medmindre det opsiges før fornyelsen. I Sverige: 49 SEK/måned. I andre lande gælder prisen og valutaen, der vises i butikken. En gyldig betalingsmetode kræves. Indløs senest 31. oktober 2026, så længe indløsninger er tilbage, og appen er tilgængelig i dit land. Apple: 500 indløsninger; Google Play: 2.000. Koden har ingen kontantværdi og må ikke videresælges.',
 'appleTitle': 'iPhone og iPad', 'apple': 'Installer AkutPOCUS. Åbn App Store, tryk på dit kontobillede, og vælg Indløs gavekort eller kode. Indtast koden, du har fået, og følg vejledningen. Kontroller, at butikken viser den tilbudte gratisperiode, før du bekræfter. Åbn derefter AkutPOCUS; brug Gendan køb ved behov.', 'appleButton': 'Hent AkutPOCUS i App Store',
 'androidTitle': 'Android', 'android': 'Installer AkutPOCUS fra Google Play. Åbn siden for fuld adgang, og vælg månedsabonnementet. Åbn menuen for betalingsmetode i Google Plays købsvindue, vælg Indløs kode, og skriv koden, du har fået. Kontroller, at vinduet viser 14 dage gratis, før du bekræfter. Denne kampagnekode skal bruges i købsvinduet, som åbnes fra appen, ikke på Google Plays generelle indløsningsside eller i appens kodefelt til butikskontrol.', 'androidButton': 'Hent AkutPOCUS på Google Play',
 'cancelTitle': 'Opsig før fornyelse for at undgå betaling', 'cancel': 'Administrer eller opsig abonnementet i din Apple-konto eller under abonnementer i Google Play. Følg butikkens frist; vi anbefaler opsigelse mindst 24 timer før fornyelse. Afinstallation afslutter ikke abonnementet. Hvis butikken ikke viser gratisperioden, skal du ikke bekræfte et betalt køb; kontakt info@sononordic.se for hjælp.',
 'freeTitle': 'Gratisindholdet forbliver gratis', 'free': 'eFAST, Lunger og thorax samt Arteriekanyle er tilgængelige uden abonnement. Kampagnekoden åbner resten af indholdet i tilbudsperioden. AkutPOCUS er en undervisnings- og referenceapp for sundhedspersonale og medicinstuderende, på svensk, norsk, dansk og engelsk.',
 'termsLink': 'Abonnementsvilkår', 'privacyLink': 'Privatliv',
}}

def filename(kind, lang):
 return f'akutpocus-{kind}{"" if lang == "sv" else "-" + lang}.html'

def esc(s):
 return html.escape(s, quote=True)

for lang, d in COPY.items():
 nav=''.join(f'<a href="{filename("offer", code)}" lang="{code}"'+(' aria-current="page"' if code==lang else '')+f'>{label}</a>' for code,label in LANGS.items())
 sections=[]
 for key in ['terms','apple','android','cancel','free']:
  body=esc(d[key]).replace('info@sononordic.se','<a href="mailto:info@sononordic.se">info@sononordic.se</a>')
  button=f'<p><a class="sibling" href="{esc(APPLE if key=="apple" else PLAY)}">{esc(d[key+"Button"])} ↗</a></p>' if key in ('apple','android') else ''
  sections.append(f'<section id="{key}"><h2>{esc(d[key+"Title"])}</h2><p>{body}</p>{button}</section>')
 contents=''.join(f'<a href="#{key}">{esc(d[key+"Title"])}</a>' for key in ['terms','apple','android','cancel','free'])
 (SITE/filename('offer',lang)).write_text(f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{esc(d['intro'])}"><meta name="robots" content="noindex"><title>{esc(d['title'])} — AkutPOCUS — SonoNordic</title><link rel="icon" href="logo.png"><link rel="stylesheet" href="akutpocus-legal.css"></head>
<body><header><div class="top"><a class="brand" href="./"><img src="logo.png" alt="">SonoNordic <small>AB</small></a><a class="home" href="./">{esc(d['home'])} ↗</a></div></header>
<main id="main"><div class="intro"><p class="eyebrow">AkutPOCUS</p><h1>{esc(d['title'])}</h1><nav class="languages" aria-label="{esc(d['language'])}">{nav}</nav><p class="notice">{esc(d['intro'])}</p></div><div class="layout"><nav class="contents" aria-label="{esc(d['title'])}">{contents}</nav><article>{''.join(sections)}<p><a href="{filename('terms',lang)}">{esc(d['termsLink'])}</a> · <a href="{filename('privacy',lang)}">{esc(d['privacyLink'])}</a></p></article></div></main>
<footer><span>SonoNordic AB · 559586-5816</span><a href="mailto:info@sononordic.se">info@sononordic.se</a><span>© 2026 SonoNordic AB</span></footer></body></html>''')
