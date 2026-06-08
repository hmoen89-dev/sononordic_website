import 'package:flutter_test/flutter_test.dart';
import 'package:sononordic_website/main.dart';

void main() {
  testWidgets('SonoNordic website loads home content', (tester) async {
    await tester.pumpWidget(const SonoNordicWebsiteApp());
    await tester.pumpAndSettle();

    expect(find.text('SonoNordic AB'), findsWidgets);
    expect(
      find.text('SonoNordic develops POCUS tools for emergency and acute care.'),
      findsOneWidget,
    );
  });
}
