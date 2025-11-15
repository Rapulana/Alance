module.exports = {
  title: 'Alance — Developer Kit',
  tagline: 'Android for Quantum Computers — SDK, runtime, and examples',
  url: 'https://rapulana.github.io',
  baseUrl: '/Alance/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'static/assets/alance-logo-placeholder.svg',
  organizationName: 'Rapulana', // GitHub org/user
  projectName: 'Alance', // repo name
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          routeBasePath: '/', // serve docs at root
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/Rapulana/Alance/tree/main/website/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        }
      },
    ],
  ],
  themeConfig: {
    colorMode: {
      defaultMode: 'dark',
      disableSwitch: false,
    },
    navbar: {
      title: 'Alance',
      logo: {
        alt: 'Alance Logo',
        src: 'static/assets/alance-logo-placeholder.svg',
      },
      items: [
        { to: '/', label: 'Docs', position: 'left' },
        { to: 'examples', label: 'Examples', position: 'left' },
        { to: 'api-reference', label: 'API', position: 'left' },
        { to: 'roadmap', label: 'Roadmap', position: 'left' },
        {
          href: 'https://github.com/Rapulana/Alance',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            { label: 'Getting Started', to: 'getting-started' },
            { label: 'Examples', to: 'examples' },
            { label: 'API Reference', to: 'api-reference' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'GitHub', href: 'https://github.com/Rapulana/Alance' }
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Release Notes', to: 'release-notes' },
            { label: 'Roadmap', to: 'roadmap' }
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Alance Technologies.`,
    },
  },
};
