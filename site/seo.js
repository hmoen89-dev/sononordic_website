// Query-based translations share an HTML file. Set the canonical in JavaScript
// only, so the source never declares an English canonical for Swedish content.
const seoPath = location.pathname.endsWith('/support.html') ? '/support.html'
  : location.pathname.endsWith('/privacy.html') ? '/privacy.html' : '/';
const seoBase = 'https://sononordic.se' + seoPath;
const canonicalLink = document.createElement('link');
canonicalLink.rel = 'canonical';
document.head.appendChild(canonicalLink);

function setSeoLanguage(lang) {
  canonicalLink.href = seoBase + (lang === 'sv' ? '?lang=sv' : '');
}

for (const lang of ['en', 'sv', 'x-default']) {
  const alternate = document.createElement('link');
  alternate.rel = 'alternate';
  alternate.hreflang = lang;
  alternate.href = seoBase + (lang === 'sv' ? '?lang=sv' : '');
  document.head.appendChild(alternate);
}
setSeoLanguage(new URLSearchParams(location.search).get('lang'));
