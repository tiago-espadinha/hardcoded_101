import type { Metadata } from 'next';
import '@aurora-ds/tokens/css';
import '@aurora-ds/tokens/theme';
import './globals.css';

export const metadata: Metadata = {
  title: 'Aurora DS — Documentation',
  description: 'Production-grade accessible React design system',
  icons: {
    icon: '/aurora.svg',
  }
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
