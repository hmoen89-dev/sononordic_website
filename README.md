# SonoNordic website

The published website is in `site/`. Pushing to `main` deploys it to https://sononordic.se through GitHub Pages.

To preview locally, run `python3 -m http.server 8766 --directory site`.

The previous Flutter implementation is retained in `lib/` and `web/`.
The privacy page remains explicitly marked as a draft pending final review of the app release.


## AkutPOCUS app privacy and subscription terms

Publication approved by the owner on 18 September 2026. The app-specific pages are available in Swedish, Norwegian, Danish and English. Text sources are in `site/legal-content/*.json`; regenerate the eight static pages with `python3 tools/build_legal_pages.py`. Swedish entry pages are `akutpocus-privacy.html` and `akutpocus-terms.html`; other languages add `-nb`, `-da` or `-en`.

The pages work without JavaScript and retain `noindex` during launch preparation. Retention is handled manually in RevenueCat with weekly planning and deletion when due. The selected Loopia/free Gmail setup is described explicitly; consumer Gmail is not described as a processor under a SonoNordic DPA. Existing website and Clinical privacy information is separate.

## AKUTSTART launch campaign

The home page links to both stores. Campaign instructions share the same 14-day monthly-subscription offer in Swedish, Norwegian, Danish and English. Regenerate `site/akutpocus-offer*.html` with `python3 tools/build_offer_pages.py`.

Campaign redemption deadline: 31 October 2026. Apple has 500 possible redemptions; Google Play requires a minimum of 2,000. Both renew at the store's monthly price after the free period unless cancelled. Remove or replace the homepage campaign when it ends; do not reuse a Google custom code for a new campaign.

Ambassador invitations are separate: Apple offers six months without automatic renewal; Google Play offers 90 days with automatic monthly renewal unless the recipient cancels. Code values remain private and are not stored in this repository.
