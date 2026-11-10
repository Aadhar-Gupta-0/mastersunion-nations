# Masters Union Nations — ZERO: The World Reset

An independently maintained edition of the Masters Union Nations conference website, featuring cinematic committee pages, interactive map/navigation, registration flows and responsive CSS. Original collaborators retain credit and code provenance.

## This edition
- Stronger visible keyboard focus styles across interactive controls.
- Consistent support for \`prefers-reduced-motion\`: animations/transitions settle immediately on accessibility preference.
- A standalone media inventory and local-asset reference audit to identify missing resources and performance hotspots.
- A separate repository so changes here do not modify the original event website or its live deployment.

## Running locally

\`\`\`bash
python -m http.server 5173
python tools/site_audit.py
python -m unittest discover -s tools -p 'test_*.py'
\`\`\`

Open http://localhost:5173. API routes in \`api/\` require the correct Vercel configuration and a secure test environment.

## Audio and production safety

**Licensed / externally sourced audio recordings were intentionally excluded from this public edition pending rights confirmation.** Silent fallback may occur until appropriately licensed files are supplied. Verify the complete asset list using \`python tools/site_audit.py\`.

Never configure real Razorpay credentials in source control. This is a portfolio copy, not a second live payments/registration endpoint. Do not publish or enable payment processing without permission and a full checkout/security test.

## Credits and provenance

Originally co-developed with the Masters Union Nations team. Based on [ronitpahuja08/masters-union-nations](https://github.com/ronitpahuja08/masters-union-nations). Independently maintained for additional development and QA under \`Aadhar-Gupta-0/mastersunion-nations\`.
