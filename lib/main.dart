import 'package:flutter/material.dart';

void main() {
  runApp(const SonoNordicWebsiteApp());
}

const _background = Color(0xFF09111F);
const _surface = Color(0xFF121D2F);
const _surfaceAlt = Color(0xFF0E1728);
const _border = Color(0xFF263245);
const _textMuted = Color(0xFFB0BACB);
const _accent = Color(0xFF7E2436);
const _accentSoft = Color(0xFFB85A6D);

enum _SitePage {
  home('Home'),
  about('About'),
  support('Support'),
  privacy('Privacy Policy');

  const _SitePage(this.label);
  final String label;
}

class SonoNordicWebsiteApp extends StatelessWidget {
  const SonoNordicWebsiteApp({super.key});

  @override
  Widget build(BuildContext context) {
    final colorScheme = ColorScheme.fromSeed(
      seedColor: _accent,
      brightness: Brightness.dark,
    ).copyWith(
      surface: _surface,
      primary: _accentSoft,
      secondary: _accent,
    );

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'SonoNordic AB',
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: colorScheme,
        scaffoldBackgroundColor: _background,
        textTheme: ThemeData.dark().textTheme.apply(
              bodyColor: Colors.white,
              displayColor: Colors.white,
            ),
      ),
      home: const _WebsiteShell(),
    );
  }
}

class _WebsiteShell extends StatefulWidget {
  const _WebsiteShell();

  @override
  State<_WebsiteShell> createState() => _WebsiteShellState();
}

class _WebsiteShellState extends State<_WebsiteShell> {
  _SitePage _selectedPage = _SitePage.home;

  void _selectPage(_SitePage page) {
    setState(() {
      _selectedPage = page;
    });
  }

  @override
  Widget build(BuildContext context) {
    final isDesktop = MediaQuery.of(context).size.width >= 900;

    return Scaffold(
      drawer: isDesktop
          ? null
          : Drawer(
              backgroundColor: _surface,
              child: SafeArea(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Padding(
                      padding: EdgeInsets.fromLTRB(20, 20, 20, 12),
                      child: _BrandBlock(),
                    ),
                    const Divider(color: Colors.white12, height: 1),
                    ..._SitePage.values.map(
                      (page) => ListTile(
                        title: Text(page.label),
                        selected: _selectedPage == page,
                        selectedTileColor: Colors.white.withValues(alpha: 0.06),
                        onTap: () {
                          Navigator.of(context).pop();
                          _selectPage(page);
                        },
                      ),
                    ),
                  ],
                ),
              ),
            ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [
              Color(0xFF09111F),
              Color(0xFF0B1425),
              Color(0xFF09111F),
            ],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: Column(
            children: [
              _TopNavigationBar(
                selectedPage: _selectedPage,
                onSelectPage: _selectPage,
              ),
              Expanded(
                child: AnimatedSwitcher(
                  duration: const Duration(milliseconds: 260),
                  switchInCurve: Curves.easeOutCubic,
                  switchOutCurve: Curves.easeInCubic,
                  child: KeyedSubtree(
                    key: ValueKey(_selectedPage),
                    child: _SitePageView(page: _selectedPage),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _TopNavigationBar extends StatelessWidget {
  final _SitePage selectedPage;
  final ValueChanged<_SitePage> onSelectPage;

  const _TopNavigationBar({
    required this.selectedPage,
    required this.onSelectPage,
  });

  @override
  Widget build(BuildContext context) {
    final isDesktop = MediaQuery.of(context).size.width >= 900;

    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        color: Colors.black.withValues(alpha: 0.08),
        border: const Border(bottom: BorderSide(color: Colors.white12)),
      ),
      child: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 1180),
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
            child: Row(
              children: [
                if (!isDesktop)
                  Builder(
                    builder: (context) => IconButton(
                      onPressed: () => Scaffold.of(context).openDrawer(),
                      icon: const Icon(Icons.menu_rounded),
                    ),
                  ),
                const _BrandBlock(),
                const Spacer(),
                if (isDesktop)
                  Row(
                    children: _SitePage.values.map((page) {
                      final selected = page == selectedPage;
                      return Padding(
                        padding: const EdgeInsets.only(left: 10),
                        child: _NavChip(
                          label: page.label,
                          selected: selected,
                          onTap: () => onSelectPage(page),
                        ),
                      );
                    }).toList(),
                  ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _BrandBlock extends StatelessWidget {
  const _BrandBlock();

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Container(
          width: 48,
          height: 48,
          padding: const EdgeInsets.all(5),
          decoration: BoxDecoration(
            color: Colors.white.withValues(alpha: 0.03),
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: Colors.white10),
            boxShadow: const [
              BoxShadow(
                color: Colors.black38,
                blurRadius: 12,
                offset: Offset(0, 6),
              ),
            ],
          ),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(10),
            child: Image.asset(
              'assets/logo.png',
              fit: BoxFit.contain,
            ),
          ),
        ),
        const SizedBox(width: 12),
        const Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'SonoNordic AB',
              style: TextStyle(
                color: Colors.white,
                fontSize: 18,
                fontWeight: FontWeight.w700,
                height: 1.1,
              ),
            ),
            SizedBox(height: 2),
            Text(
              'Clinical ultrasound solutions',
              style: TextStyle(
                color: _textMuted,
                fontSize: 12,
                fontWeight: FontWeight.w500,
              ),
            ),
          ],
        ),
      ],
    );
  }
}

class _NavChip extends StatelessWidget {
  final String label;
  final bool selected;
  final VoidCallback onTap;

  const _NavChip({
    required this.label,
    required this.selected,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return InkWell(
      borderRadius: BorderRadius.circular(999),
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        curve: Curves.easeOut,
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          color: selected ? Colors.white.withValues(alpha: 0.08) : Colors.transparent,
          borderRadius: BorderRadius.circular(999),
          border: Border.all(
            color: selected ? Colors.white24 : Colors.white10,
          ),
        ),
        child: Text(
          label,
          style: TextStyle(
            color: selected ? Colors.white : _textMuted,
            fontSize: 14,
            fontWeight: FontWeight.w600,
          ),
        ),
      ),
    );
  }
}

class _SitePageView extends StatelessWidget {
  final _SitePage page;

  const _SitePageView({
    required this.page,
  });

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 28, 20, 40),
      child: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 1180),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              switch (page) {
                _SitePage.home => const _HomePage(),
                _SitePage.about => const _AboutPage(),
                _SitePage.support => const _SupportPage(),
                _SitePage.privacy => const _PrivacyPage(),
              },
              const SizedBox(height: 32),
              const _SiteFooter(),
            ],
          ),
        ),
      ),
    );
  }
}

class _HomePage extends StatelessWidget {
  const _HomePage();

  @override
  Widget build(BuildContext context) {
    final wide = MediaQuery.of(context).size.width >= 940;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        wide
            ? Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Expanded(flex: 6, child: _HeroContent()),
                  const SizedBox(width: 24),
                  Expanded(
                    flex: 5,
                    child: Column(
                      children: const [
                        _HighlightCard(
                          title: 'POCUS Tools',
                          body:
                              'Focused ultrasound tools built for physicians working in emergency and acute care settings.',
                          icon: Icons.monitor_heart_outlined,
                        ),
                        SizedBox(height: 18),
                        _HighlightCard(
                          title: 'Clinical Decision Support',
                          body:
                              'Structured digital support for consistent bedside workflows, documentation and interpretation.',
                          icon: Icons.rule_folder_outlined,
                        ),
                      ],
                    ),
                  ),
                ],
              )
            : const Column(
                children: [
                  _HeroContent(),
                  SizedBox(height: 18),
                  _HighlightCard(
                    title: 'POCUS Tools',
                    body:
                        'Focused ultrasound tools built for physicians working in emergency and acute care settings.',
                    icon: Icons.monitor_heart_outlined,
                  ),
                  SizedBox(height: 18),
                  _HighlightCard(
                    title: 'Clinical Decision Support',
                    body:
                        'Structured digital support for consistent bedside workflows, documentation and interpretation.',
                    icon: Icons.rule_folder_outlined,
                  ),
                ],
              ),
        const SizedBox(height: 28),
        wide
            ? const Row(
                children: [
                  Expanded(child: _ScreenshotPlaceholder()),
                  SizedBox(width: 18),
                  Expanded(child: _LogoShowcase()),
                ],
              )
            : const Column(
                children: [
                  _ScreenshotPlaceholder(),
                  SizedBox(height: 18),
                  _LogoShowcase(),
                ],
              ),
        const SizedBox(height: 28),
        const _SectionIntro(
          eyebrow: 'What SonoNordic Builds',
          title: 'Tools designed for bedside speed and clinical clarity.',
          body:
              'SonoNordic develops point-of-care ultrasound tools, educational resources and clinical decision support solutions for physicians working in emergency and acute care settings.',
        ),
        const SizedBox(height: 18),
        _ResponsiveCardGrid(
          items: const [
            _InfoTileData(
              title: 'Emergency Medicine Focus',
              body:
                  'Built around rapid workflows relevant to shock, dyspnea, trauma, vascular access and acute diagnostics.',
              icon: Icons.local_hospital_outlined,
            ),
            _InfoTileData(
              title: 'Education',
              body:
                  'Bedside-oriented explanations and troubleshooting content designed to support training and refreshers.',
              icon: Icons.school_outlined,
            ),
            _InfoTileData(
              title: 'Scalable Platform',
              body:
                  'A web presence and digital products that can be expanded with product pages, screenshots and company updates later.',
              icon: Icons.devices_outlined,
            ),
          ],
        ),
      ],
    );
  }
}

class _HeroContent extends StatelessWidget {
  const _HeroContent();

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(28),
      decoration: BoxDecoration(
        color: _surface,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: Colors.white12),
        boxShadow: const [
          BoxShadow(
            color: Colors.black38,
            blurRadius: 22,
            offset: Offset(0, 16),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                width: 68,
                height: 68,
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: Colors.white.withValues(alpha: 0.04),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.white12),
                ),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(14),
                  child: Image.asset(
                    'assets/logo.png',
                    fit: BoxFit.contain,
                  ),
                ),
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 8,
                  ),
                  decoration: BoxDecoration(
                    color: _accent.withValues(alpha: 0.22),
                    borderRadius: BorderRadius.circular(999),
                    border: Border.all(
                      color: _accentSoft.withValues(alpha: 0.35),
                    ),
                  ),
                  child: const Text(
                    'Clinical ultrasound solutions for healthcare professionals',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 13,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
              ),
            ],
          ),
          Container(
            margin: const EdgeInsets.only(top: 20),
            height: 1,
            color: Colors.white10,
          ),
          const SizedBox(height: 20),
          const Text(
            'SonoNordic develops POCUS tools for emergency and acute care.',
            style: TextStyle(
              color: Colors.white,
              fontSize: 42,
              fontWeight: FontWeight.w800,
              height: 1.08,
            ),
          ),
          const SizedBox(height: 16),
          const Text(
            'Digital products, educational resources and clinical decision support designed to fit real bedside workflows for physicians working under time pressure.',
            style: TextStyle(
              color: _textMuted,
              fontSize: 17,
              height: 1.6,
            ),
          ),
          const SizedBox(height: 22),
          Wrap(
            spacing: 12,
            runSpacing: 12,
            children: const [
              _MetricChip(label: 'POCUS'),
              _MetricChip(label: 'Emergency Medicine'),
              _MetricChip(label: 'Clinical Decision Support'),
            ],
          ),
          const SizedBox(height: 24),
          FilledButton.icon(
            onPressed: null,
            style: FilledButton.styleFrom(
              backgroundColor: _accent,
              disabledBackgroundColor: _accent,
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 22, vertical: 18),
              textStyle: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w700,
              ),
            ),
            icon: const Icon(Icons.arrow_forward_rounded),
            label: const Text('Learn More'),
          ),
        ],
      ),
    );
  }
}

class _AboutPage extends StatelessWidget {
  const _AboutPage();

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const _SectionIntro(
          eyebrow: 'About SonoNordic',
          title: 'Focused on practical ultrasound use in acute care.',
          body:
              'SonoNordic AB is a Swedish company focused on point-of-care ultrasound, acute care workflows, physician education and clinically useful digital support.',
        ),
        const SizedBox(height: 18),
        _ResponsiveCardGrid(
          items: const [
            _InfoTileData(
              title: 'Founded in Sweden',
              body:
                  'A Nordic company with a clear focus on clinical usability, simplicity and credibility in healthcare settings.',
              icon: Icons.flag_outlined,
            ),
            _InfoTileData(
              title: 'POCUS Focus',
              body:
                  'Dedicated to point-of-care ultrasound solutions relevant to frontline physicians and bedside decision making.',
              icon: Icons.monitor_heart_outlined,
            ),
            _InfoTileData(
              title: 'Acute Care',
              body:
                  'Designed with emergency departments and acute clinical environments in mind, where clarity and speed matter.',
              icon: Icons.bolt_outlined,
            ),
            _InfoTileData(
              title: 'Education',
              body:
                  'Supports learning, troubleshooting and structured interpretation in a format that can grow over time.',
              icon: Icons.menu_book_outlined,
            ),
            _InfoTileData(
              title: 'Clinical Support',
              body:
                  'Works toward practical tools that can help standardize documentation and reinforce pattern recognition.',
              icon: Icons.fact_check_outlined,
            ),
          ],
        ),
      ],
    );
  }
}

class _SupportPage extends StatelessWidget {
  const _SupportPage();

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const _SectionIntro(
          eyebrow: 'Support',
          title: 'Contact SonoNordic support',
          body: 'For support regarding SonoNordic products, please contact us by email.',
        ),
        const SizedBox(height: 18),
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            color: _surface,
            borderRadius: BorderRadius.circular(24),
            border: Border.all(color: Colors.white12),
          ),
          child: const Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _SupportRow(
                title: 'Email',
                value: 'info@sononordic.se',
              ),
              SizedBox(height: 18),
              _SupportRow(
                title: 'Response time',
                value: '1-3 business days',
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class _PrivacyPage extends StatelessWidget {
  const _PrivacyPage();

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const _SectionIntro(
          eyebrow: 'Privacy Policy',
          title: 'Simple privacy information for the website and app.',
          body: 'Last updated: June 2026',
        ),
        const SizedBox(height: 18),
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            color: _surface,
            borderRadius: BorderRadius.circular(24),
            border: Border.all(color: Colors.white12),
          ),
          child: const Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _PrivacyParagraph(
                text: 'SonoNordic AB respects your privacy.',
              ),
              SizedBox(height: 16),
              _PrivacyParagraph(
                text: 'The website does not collect personal information.',
              ),
              SizedBox(height: 16),
              _PrivacyParagraph(
                text: 'The POCUS application processes no patient data.',
              ),
              SizedBox(height: 16),
              _PrivacyParagraph(
                text: 'For questions contact: info@sononordic.se',
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class _SectionIntro extends StatelessWidget {
  final String eyebrow;
  final String title;
  final String body;

  const _SectionIntro({
    required this.eyebrow,
    required this.title,
    required this.body,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          eyebrow,
          style: const TextStyle(
            color: _accentSoft,
            fontSize: 13,
            fontWeight: FontWeight.w700,
            letterSpacing: 0.4,
          ),
        ),
        const SizedBox(height: 10),
        Text(
          title,
          style: const TextStyle(
            color: Colors.white,
            fontSize: 32,
            fontWeight: FontWeight.w800,
            height: 1.1,
          ),
        ),
        const SizedBox(height: 12),
        Text(
          body,
          style: const TextStyle(
            color: _textMuted,
            fontSize: 16,
            height: 1.6,
          ),
        ),
      ],
    );
  }
}

class _HighlightCard extends StatelessWidget {
  final String title;
  final String body;
  final IconData icon;

  const _HighlightCard({
    required this.title,
    required this.body,
    required this.icon,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: _surface,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.white12),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: 48,
            height: 48,
            decoration: BoxDecoration(
              color: _accent.withValues(alpha: 0.2),
              borderRadius: BorderRadius.circular(16),
            ),
            child: Icon(icon, color: Colors.white),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 20,
                    fontWeight: FontWeight.w700,
                  ),
                ),
                const SizedBox(height: 8),
                Text(
                  body,
                  style: const TextStyle(
                    color: _textMuted,
                    fontSize: 15,
                    height: 1.55,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _MetricChip extends StatelessWidget {
  final String label;

  const _MetricChip({
    required this.label,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: Colors.white.withValues(alpha: 0.05),
        borderRadius: BorderRadius.circular(999),
        border: Border.all(color: Colors.white10),
      ),
      child: Text(
        label,
        style: const TextStyle(
          color: Colors.white,
          fontSize: 13,
          fontWeight: FontWeight.w600,
        ),
      ),
    );
  }
}

class _ScreenshotPlaceholder extends StatelessWidget {
  const _ScreenshotPlaceholder();

  @override
  Widget build(BuildContext context) {
    return _PlaceholderPanel(
      title: 'App Screenshot Placeholder',
      body:
          'Replace this area with product screenshots, device mockups or a product gallery when ready.',
      icon: Icons.phone_iphone_rounded,
    );
  }
}

class _LogoShowcase extends StatelessWidget {
  const _LogoShowcase();

  @override
  Widget build(BuildContext context) {
    return _PlaceholderPanel(
      title: 'SonoNordic Brand',
      body:
          'Current company logo integrated from the existing asset library and ready to be replaced or refined later if needed.',
      child: Padding(
        padding: const EdgeInsets.all(8),
        child: Image.asset(
          'assets/logo.png',
          fit: BoxFit.contain,
        ),
      ),
    );
  }
}

class _PlaceholderPanel extends StatelessWidget {
  final String title;
  final String body;
  final IconData? icon;
  final Widget? child;

  const _PlaceholderPanel({
    required this.title,
    required this.body,
    this.icon,
    this.child,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      height: 280,
      decoration: BoxDecoration(
        color: _surfaceAlt,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(
          color: _border,
          width: 1.2,
        ),
      ),
      child: Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (child != null)
                SizedBox(height: 120, child: Center(child: child!))
              else ...[
                Icon(icon, size: 44, color: _accentSoft),
                const SizedBox(height: 14),
              ],
              Text(
                title,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 20,
                  fontWeight: FontWeight.w700,
                ),
              ),
              const SizedBox(height: 10),
              Text(
                body,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: _textMuted,
                  fontSize: 15,
                  height: 1.5,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _ResponsiveCardGrid extends StatelessWidget {
  final List<_InfoTileData> items;

  const _ResponsiveCardGrid({
    required this.items,
  });

  @override
  Widget build(BuildContext context) {
    final width = MediaQuery.of(context).size.width;
    final columns = width >= 1000
        ? 3
        : width >= 700
            ? 2
            : 1;

    return Wrap(
      spacing: 18,
      runSpacing: 18,
      children: items.map((item) {
        final tileWidth = columns == 3
            ? 360.0
            : columns == 2
                ? 520.0
                : double.infinity;

        return ConstrainedBox(
          constraints: BoxConstraints(
            maxWidth: tileWidth,
            minWidth: columns == 1 ? 0 : tileWidth,
          ),
          child: _InfoTile(data: item),
        );
      }).toList(),
    );
  }
}

class _InfoTileData {
  final String title;
  final String body;
  final IconData icon;

  const _InfoTileData({
    required this.title,
    required this.body,
    required this.icon,
  });
}

class _InfoTile extends StatelessWidget {
  final _InfoTileData data;

  const _InfoTile({
    required this.data,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(22),
      decoration: BoxDecoration(
        color: _surface,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.white12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: 46,
            height: 46,
            decoration: BoxDecoration(
              color: _accent.withValues(alpha: 0.2),
              borderRadius: BorderRadius.circular(14),
            ),
            child: Icon(data.icon, color: Colors.white),
          ),
          const SizedBox(height: 14),
          Text(
            data.title,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 19,
              fontWeight: FontWeight.w700,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            data.body,
            style: const TextStyle(
              color: _textMuted,
              fontSize: 15,
              height: 1.55,
            ),
          ),
        ],
      ),
    );
  }
}

class _SupportRow extends StatelessWidget {
  final String title;
  final String value;

  const _SupportRow({
    required this.title,
    required this.value,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          title,
          style: const TextStyle(
            color: _accentSoft,
            fontSize: 13,
            fontWeight: FontWeight.w700,
          ),
        ),
        const SizedBox(height: 6),
        Text(
          value,
          style: const TextStyle(
            color: Colors.white,
            fontSize: 19,
            fontWeight: FontWeight.w600,
          ),
        ),
      ],
    );
  }
}

class _PrivacyParagraph extends StatelessWidget {
  final String text;

  const _PrivacyParagraph({
    required this.text,
  });

  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: const TextStyle(
        color: _textMuted,
        fontSize: 16,
        height: 1.6,
      ),
    );
  }
}

class _SiteFooter extends StatelessWidget {
  const _SiteFooter();

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(22),
      decoration: BoxDecoration(
        color: _surface,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.white12),
      ),
      child: const Wrap(
        alignment: WrapAlignment.spaceBetween,
        runSpacing: 10,
        children: [
          Text(
            'SonoNordic AB',
            style: TextStyle(
              color: Colors.white,
              fontSize: 16,
              fontWeight: FontWeight.w700,
            ),
          ),
          Text(
            'info@sononordic.se',
            style: TextStyle(
              color: _textMuted,
              fontSize: 14,
              fontWeight: FontWeight.w500,
            ),
          ),
          Text(
            '© 2026 SonoNordic AB',
            style: TextStyle(
              color: _textMuted,
              fontSize: 14,
              fontWeight: FontWeight.w500,
            ),
          ),
        ],
      ),
    );
  }
}
