import { Badge, Box, Button, Divider, Grid, Heading, Inline, Stack, Text } from '@aurora-ds/components';
import { BellIcon, CheckCircleIcon, CommandIcon, EyeIcon } from '@aurora-ds/icons';

const features = [
  { accent: 'var(--aurora-color-primitive-blue-600)', surface: 'var(--aurora-color-primitive-blue-50)', icon: <CheckCircleIcon size={24} aria-hidden />, title: 'Built for WCAG 2.1 AA', description: 'Keyboard support, focus management, contrast, and screen-reader semantics are built in from the first component.' },
  { accent: 'var(--aurora-color-primitive-purple-600)', surface: 'var(--aurora-color-primitive-purple-50)', icon: <CommandIcon size={24} aria-hidden />, title: 'Tokens that travel', description: 'A semantic token layer keeps every product surface consistent while making theme changes predictable.' },
  { accent: 'var(--aurora-color-primitive-teal-600)', surface: 'var(--aurora-color-primitive-teal-50)', icon: <EyeIcon size={24} aria-hidden />, title: 'Clear by default', description: 'Primitives compose into interfaces that remain legible, balanced, and easy to scan at every scale.' },
  { accent: 'var(--aurora-color-primitive-orange-600)', surface: 'var(--aurora-color-primitive-orange-50)', icon: <BellIcon size={24} aria-hidden />, title: 'Documented in Storybook', description: 'Explore live examples, states, and accessibility guidance alongside the components your team ships.' },
];

export default function Home() {
  return (
    <main style={{ minHeight: '100vh', background: 'radial-gradient(circle at 0% 25%, var(--aurora-color-primitive-purple-200), transparent 30%), radial-gradient(circle at 100% 25%, var(--aurora-color-primitive-aurora-200), transparent 30%), linear-gradient(180deg, #ffffff 0%, var(--aurora-color-background-default) 12%)' }}>
      <Box as="header" style={{ background: 'rgba(255, 255, 255, 0.72)', borderBottom: '1px solid var(--aurora-color-border-default)', backdropFilter: 'blur(14px)', position: 'relative', zIndex: 1 }}>
        <Inline align="center" style={{ maxWidth: '1180px', margin: '0 auto', minHeight: '72px', padding: '0 32px' }}>
          <Inline gap={3} align="center">
            <img src="/aurora.svg" alt="Aurora DS" width={32} height={32}/>
            <Text as="span" weight="semibold" style={{ letterSpacing: '-0.02em' }}>Aurora DS</Text>
          </Inline>
          <Badge intent="brand" variant="subtle">v0.1.0</Badge>
        </Inline>
      </Box>

      <Box as="section" aria-labelledby="hero-title" style={{ margin: '0 auto', maxWidth: '1180px', padding: '112px 32px 88px' }}>
        <Stack gap={8} align="center" style={{ margin: '0 auto', maxWidth: '820px', textAlign: 'center' }}>
          <Badge intent="brand" variant="subtle">✦ A practical React design system ✦</Badge>
          <Stack gap={5} align="center">
            <Heading level={1} size="4xl" id="hero-title" style={{ color: 'var(--aurora-color-primitive-slate-900)', fontSize: 'clamp(3.4rem, 7vw, 6.5rem)', letterSpacing: '-0.065em', lineHeight: 0.94, maxWidth: '15ch' }}>
              Designed for people. Built for momentum.
            </Heading>
            <Text size="xl" muted style={{ fontSize: '1.3rem', maxWidth: '54ch' }}>Aurora gives product teams an expressive foundation of accessible React components, semantic tokens, and clear implementation guidance.</Text>
          </Stack>
          <Inline gap={3} wrap>
            <Button intent="brand" size="lg" as="a" href="/docs/getting-started">Get started</Button>
            <Button variant="outline" size="lg" as="a" href="http://localhost:6006">Browse Storybook ↗</Button>
          </Inline>
        </Stack>
      </Box>

      <Box as="section" aria-labelledby="features-title" style={{ margin: '0 auto', maxWidth: '1180px', padding: '0 32px 112px' }}>
        <Divider />
        <Stack gap={8} style={{ paddingTop: '56px' }}>
          <Stack gap={3} style={{ maxWidth: '560px' }}>
            <Text as="span" size="sm" weight="semibold" style={{ color: 'var(--aurora-color-primitive-aurora-800)', letterSpacing: '0.12em', textTransform: 'uppercase' }}>The foundation</Text>
            <Heading level={2} size="2xl" id="features-title" style={{ fontSize: 'clamp(2.2rem, 4vw, 3.5rem)', letterSpacing: '-0.045em', lineHeight: 1 }}>Everything needed to make the good path the easy path.</Heading>
          </Stack>
          <Grid columns={2} gap={6}>
            {features.map(({ accent, surface, icon, title, description }) => (
              <Box key={title} as="article" className="feature-card" style={{ '--feature-accent': accent, background: surface, border: `1px solid ${accent}`, borderRadius: 'var(--aurora-border-radius-xl)', padding: '30px', position: 'relative' } as React.CSSProperties}>
                <Stack gap={4}>
                  <Box aria-hidden className="feature-card__icon" style={{ alignItems: 'center', background: accent, borderRadius: 'var(--aurora-border-radius-lg)', color: 'white', display: 'flex', height: '46px', justifyContent: 'center', width: '46px' }}>{icon}</Box>
                  <Stack gap={2}>
                    <Heading level={3} size="lg">{title}</Heading>
                    <Text muted>{description}</Text>
                  </Stack>
                </Stack>
              </Box>
            ))}
          </Grid>
          <Box style={{ background: 'linear-gradient(115deg, var(--aurora-color-primitive-aurora-500), var(--aurora-color-primitive-purple-100))', borderRadius: 'var(--aurora-border-radius-xl)', color: 'white', marginTop: '8px', overflow: 'hidden', padding: '36px' }}>
            <Inline align="center" wrap style={{ gap: '24px', justifyContent: 'space-between', width: '100%' }}>
              <Stack gap={2} style={{ maxWidth: '620px' }}>
                <Text as="span" size="sm" weight="semibold" style={{ color: 'var(--aurora-color-primitive-slate-700)', letterSpacing: '0.1em', textTransform: 'uppercase' }}>Start with the system</Text>
                <Heading level={2} size="xl" style={{ color: 'black', letterSpacing: '-0.035em' }}>One considered language for every interface.</Heading>
              </Stack>
              <Button className="final-cta-button" size="lg" as="a" href="http://localhost:6006">Explore components</Button>
            </Inline>
          </Box>
        </Stack>
      </Box>
    </main>
  );
}
