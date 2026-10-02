"""Generate localized AKUTSTART instructions with identical campaign terms."""
import html
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / 'site'
LANGS = {'sv': 'Svenska', 'nb': 'Norsk', 'da': 'Dansk', 'en': 'English'}
APPLE = 'https://apps.apple.com/redeem?ctx=offercodes&id=6781746961&code=AKUTSTART'
PLAY = 'https://play.google.com/store/apps/details?id=se.sononordic.akutpocus'
COPY = {
'en': {
 'title': 'Two weeks of full access, free', 'language': 'Language', 'home': 'SonoNordic home',
 'intro': 'Explore AkutPOCUS with AKUTSTART: 14 days of full access free for new subscribers on the App Store and Google Play.',
 'termsTitle': 'The same offer on iPhone and Android',
 'terms': 'AKUTSTART applies to the monthly subscription and is available to new subscribers only, once per eligible store account. After 14 days, the subscription renews automatically at the local monthly price unless cancelled before renewal. In Sweden: 49 SEK/month. Other countries use the price and currency shown by the store. A valid payment method is required. Redeem by 31 October 2026, subject to remaining redemptions and store availability in your country. Apple: 500 redemptions; Google Play: 2,000. The code has no cash value and is not for resale.',
 'appleTitle': 'iPhone and iPad', 'apple': 'Install AkutPOCUS, then open the Apple redemption link below. Sign in with your Apple Account and follow the instructions. Confirm that the store shows two weeks free before accepting. Open AkutPOCUS after redemption; use Restore purchases if needed.', 'appleButton': 'Redeem AKUTSTART with Apple',
 'androidTitle': 'Android', 'android': 'Install AkutPOCUS from Google Play. Open the full-access screen and choose the monthly subscription. In Google Play’s purchase sheet, open the payment-method menu, choose Redeem code and enter AKUTSTART. Confirm that the sheet shows 14 days free before accepting. This custom code must be entered in the purchase sheet opened from the app, not on Google Play’s general redemption page or in the app’s store-review code field.', 'androidButton': 'Get AkutPOCUS on Google Play',
 'cancelTitle': 'Cancel before renewal to avoid a charge', 'cancel': 'Manage or cancel the subscription in your Apple Account or Google Play subscriptions. Follow the deadline shown by the store; we recommend cancelling at least 24 hours before renewal. Uninstalling the app does not cancel a subscription. If the store does not show the free period, do not confirm a paid purchase; contact info@sononordic.se for help.',
 'freeTitle': 'Free content remains free', 'free': 'eFAST, Lungs and thorax, and Arterial line are available without a subscription. AKUTSTART unlocks the remaining content during the offer. AkutPOCUS is an educational and reference app for healthcare professionals and medical students, in Swedish, Norwegian, Danish and English.',
 'termsLink': 'Subscription terms', 'privacyLink': 'Privacy',
},
'sv': {
 'title': 'Två veckor med full åtkomst, gratis', 'language': 'Språk', 'home': 'Till SonoNordic',
 'intro': 'Utforska AkutPOCUS med AKUTSTART: 14 dagars full åtkomst gratis för nya prenumeranter på App Store och Google Play.',
 'termsTitle': 'Samma erbjudande på iPhone och Android',
 'terms': 'AKUTSTART gäller månadsprenumerationen och endast nya prenumeranter, en gång per berättigat butikskonto. Efter 14 dagar förnyas prenumerationen automatiskt till det lokala månadspriset om den inte sägs upp före förnyelsen. I Sverige: 49 SEK/månad. I andra länder gäller priset och valutan som visas i butiken. En giltig betalningsmetod krävs. Lös in senast 31 oktober 2026, så länge inlösningar finns kvar och appen är tillgänglig i ditt land. Apple: 500 inlösningar; Google Play: 2 000. Koden saknar kontantvärde och får inte säljas vidare.',
 'appleTitle': 'iPhone och iPad', 'apple': 'Installera AkutPOCUS och öppna sedan Apples inlösningslänk nedan. Logga in med ditt Apple-konto och följ instruktionerna. Kontrollera att butiken visar två veckor gratis innan du bekräftar. Öppna AkutPOCUS efter inlösen; använd Återställ köp vid behov.', 'appleButton': 'Lös in AKUTSTART hos Apple',
 'androidTitle': 'Android', 'android': 'Installera AkutPOCUS från Google Play. Öppna sidan för full åtkomst och välj månadsprenumerationen. Öppna menyn för betalningsmetod i Google Plays köpruta, välj Lös in kod och ange AKUTSTART. Kontrollera att rutan visar 14 dagar gratis innan du bekräftar. Denna kampanjkod ska anges i köprutan som öppnas från appen, inte på Google Plays allmänna inlösningssida eller i appens kodfält för butikskontroll.', 'androidButton': 'Hämta AkutPOCUS på Google Play',
 'cancelTitle': 'Säg upp före förnyelsen för att undvika debitering', 'cancel': 'Hantera eller säg upp prenumerationen i ditt Apple-konto eller under prenumerationer i Google Play. Följ butikens tidsfrist; vi rekommenderar uppsägning minst 24 timmar före förnyelsen. Avinstallation avslutar inte prenumerationen. Om butiken inte visar gratisperioden ska du inte bekräfta ett betalköp; kontakta info@sononordic.se för hjälp.',
 'freeTitle': 'Gratisinnehållet förblir gratis', 'free': 'eFAST, Lungor och thorax samt Artärnål är tillgängliga utan prenumeration. AKUTSTART låser upp övrigt innehåll under erbjudandet. AkutPOCUS är en utbildnings- och referensapp för vårdpersonal och läkarstudenter, på svenska, norska, danska och engelska.',
 'termsLink': 'Prenumerationsvillkor', 'privacyLink': 'Integritet',
},
'nb': {
 'title': 'To uker med full tilgang, gratis', 'language': 'Språk', 'home': 'Til SonoNordic',
 'intro': 'Utforsk AkutPOCUS med AKUTSTART: 14 dager med full tilgang gratis for nye abonnenter på App Store og Google Play.',
 'termsTitle': 'Samme tilbud på iPhone og Android',
 'terms': 'AKUTSTART gjelder månedsabonnementet og bare nye abonnenter, én gang per kvalifisert butikkonto. Etter 14 dager fornyes abonnementet automatisk til lokal månedspris dersom det ikke sies opp før fornyelsen. I Sverige: 49 SEK/måned. I andre land gjelder prisen og valutaen som vises i butikken. Gyldig betalingsmåte kreves. Løs inn senest 31. oktober 2026, så lenge innløsninger gjenstår og appen er tilgjengelig i landet ditt. Apple: 500 innløsninger; Google Play: 2 000. Koden har ingen kontantverdi og skal ikke videreselges.',
 'appleTitle': 'iPhone og iPad', 'apple': 'Installer AkutPOCUS og åpne deretter Apples innløsningslenke nedenfor. Logg inn med Apple-kontoen din og følg instruksjonene. Kontroller at butikken viser to uker gratis før du bekrefter. Åpne AkutPOCUS etter innløsning; bruk Gjenopprett kjøp ved behov.', 'appleButton': 'Løs inn AKUTSTART hos Apple',
 'androidTitle': 'Android', 'android': 'Installer AkutPOCUS fra Google Play. Åpne siden for full tilgang og velg månedsabonnementet. Åpne menyen for betalingsmåte i Googles kjøpsvindu, velg Løs inn kode og skriv AKUTSTART. Kontroller at vinduet viser 14 dager gratis før du bekrefter. Denne kampanjekoden skal brukes i kjøpsvinduet som åpnes fra appen, ikke på Google Plays generelle innløsningsside eller i appens kodefelt for butikkontroll.', 'androidButton': 'Hent AkutPOCUS på Google Play',
 'cancelTitle': 'Si opp før fornyelse for å unngå belastning', 'cancel': 'Administrer eller si opp abonnementet i Apple-kontoen din eller under abonnementer i Google Play. Følg butikkens frist; vi anbefaler oppsigelse minst 24 timer før fornyelse. Avinstallasjon avslutter ikke abonnementet. Hvis butikken ikke viser gratisperioden, skal du ikke bekrefte et betalt kjøp; kontakt info@sononordic.se for hjelp.',
 'freeTitle': 'Gratisinnholdet forblir gratis', 'free': 'eFAST, Lunger og thorax samt Arteriekanyle er tilgjengelig uten abonnement. AKUTSTART åpner resten av innholdet i tilbudsperioden. AkutPOCUS er en undervisnings- og referanseapp for helsepersonell og medisinstudenter, på svensk, norsk, dansk og engelsk.',
 'termsLink': 'Abonnementsvilkår', 'privacyLink': 'Personvern',
},
'da': {
 'title': 'To uger med fuld adgang, gratis', 'language': 'Sprog', 'home': 'Til SonoNordic',
 'intro': 'Udforsk AkutPOCUS med AKUTSTART: 14 dages fuld adgang gratis for nye abonnenter på App Store og Google Play.',
 'termsTitle': 'Samme tilbud på iPhone og Android',
 'terms': 'AKUTSTART gælder månedsabonnementet og kun nye abonnenter, én gang pr. berettiget butikskonto. Efter 14 dage fornyes abonnementet automatisk til den lokale månedspris, medmindre det opsiges før fornyelsen. I Sverige: 49 SEK/måned. I andre lande gælder prisen og valutaen, der vises i butikken. En gyldig betalingsmetode kræves. Indløs senest 31. oktober 2026, så længe indløsninger er tilbage, og appen er tilgængelig i dit land. Apple: 500 indløsninger; Google Play: 2.000. Koden har ingen kontantværdi og må ikke videresælges.',
 'appleTitle': 'iPhone og iPad', 'apple': 'Installer AkutPOCUS, og åbn derefter Apples indløsningslink nedenfor. Log ind med din Apple-konto, og følg vejledningen. Kontroller, at butikken viser to uger gratis, før du bekræfter. Åbn AkutPOCUS efter indløsning; brug Gendan køb ved behov.', 'appleButton': 'Indløs AKUTSTART hos Apple',
 'androidTitle': 'Android', 'android': 'Installer AkutPOCUS fra Google Play. Åbn siden for fuld adgang, og vælg månedsabonnementet. Åbn menuen for betalingsmetode i Google Plays købsvindue, vælg Indløs kode, og skriv AKUTSTART. Kontroller, at vinduet viser 14 dage gratis, før du bekræfter. Denne kampagnekode skal bruges i købsvinduet, som åbnes fra appen, ikke på Google Plays generelle indløsningsside eller i appens kodefelt til butikskontrol.', 'androidButton': 'Hent AkutPOCUS på Google Play',
 'cancelTitle': 'Opsig før fornyelse for at undgå betaling', 'cancel': 'Administrer eller opsig abonnementet i din Apple-konto eller under abonnementer i Google Play. Følg butikkens frist; vi anbefaler opsigelse mindst 24 timer før fornyelse. Afinstallation afslutter ikke abonnementet. Hvis butikken ikke viser gratisperioden, skal du ikke bekræfte et betalt køb; kontakt info@sononordic.se for hjælp.',
 'freeTitle': 'Gratisindholdet forbliver gratis', 'free': 'eFAST, Lunger og thorax samt Arteriekanyle er tilgængelige uden abonnement. AKUTSTART åbner resten af indholdet i tilbudsperioden. AkutPOCUS er en undervisnings- og referenceapp for sundhedspersonale og medicinstuderende, på svensk, norsk, dansk og engelsk.',
 'termsLink': 'Abonnementsvilkår', 'privacyLink': 'Privatliv',
}}

def filename(kind, lang):
 return f'akutpocus-{kind}{"" if lang == "sv" else "-" + lang}.html'

def esc(s):
 return html.escape(s, quote=True)

for lang, d in COPY.items():
 nav=''.join(f'<a href="{filename("offer", code)}" lang="{code}"'+(' aria-current="page"' if code==lang else '')+f'>{label}</a>' for code,label in LANGS.items())
 starts={
'en':'Google Play: AKUTSTART starts on 2 October 2026 at 16:05 UTC (18:05 in Sweden and Norway). The Apple offer is already available.',
'sv':'Google Play: AKUTSTART börjar 2 oktober 2026 kl. 18.05 svensk tid (16.05 UTC). Apples erbjudande är redan tillgängligt.',
'nb':'Google Play: AKUTSTART starter 2. oktober 2026 kl. 18.05 norsk tid (16.05 UTC). Apple-tilbudet er allerede tilgjengelig.',
'da':'Google Play: AKUTSTART starter 2. oktober 2026 kl. 18.05 dansk tid (16.05 UTC). Apples tilbud er allerede tilgængeligt.'}
 sections=[]
 for key in ['terms','apple','android','cancel','free']:
  body=esc(d[key]).replace('info@sononordic.se','<a href="mailto:info@sononordic.se">info@sononordic.se</a>')
  button=f'<p><a class="sibling" href="{esc(APPLE if key=="apple" else PLAY)}">{esc(d[key+"Button"])} ↗</a></p>' if key in ('apple','android') else ''
  sections.append(f'<section id="{key}"><h2>{esc(d[key+"Title"])}</h2><p>{body}</p>{button}</section>')
 contents=''.join(f'<a href="#{key}">{esc(d[key+"Title"])}</a>' for key in ['terms','apple','android','cancel','free'])
 (SITE/filename('offer',lang)).write_text(f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{esc(d['intro'])}"><title>AKUTSTART — AkutPOCUS — SonoNordic</title><link rel="icon" href="logo.png"><link rel="stylesheet" href="akutpocus-legal.css"></head>
<body><header><div class="top"><a class="brand" href="./"><img src="logo.png" alt="">SonoNordic <small>AB</small></a><a class="home" href="./">{esc(d['home'])} ↗</a></div></header>
<main id="main"><div class="intro"><p class="eyebrow">AkutPOCUS · AKUTSTART</p><h1>{esc(d['title'])}</h1><nav class="languages" aria-label="{esc(d['language'])}">{nav}</nav><p class="notice">{esc(d['intro'])}</p><p id="google-start" class="notice">{esc(starts[lang])}</p></div><div class="layout"><nav class="contents" aria-label="AKUTSTART">{contents}</nav><article>{''.join(sections)}<p><a href="{filename('terms',lang)}">{esc(d['termsLink'])}</a> · <a href="{filename('privacy',lang)}">{esc(d['privacyLink'])}</a></p></article></div></main>
<footer><span>SonoNordic AB · 559586-5816</span><a href="mailto:info@sononordic.se">info@sononordic.se</a><span>© 2026 SonoNordic AB</span></footer><script>if(Date.now() >= Date.parse("2026-10-02T16:05:00Z")) document.getElementById("google-start").hidden=true;</script></body></html>''')
