// astro.config.mjs

// Import the starlight integration
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// Export the configuration
export default defineConfig({
    integrations: [
        // Starlight configuration
        starlight({
            title: 'Ausbildungs-Dokumentation',
            description: 'Dokumentation der Ausbildungsinhalte und Prüfungen',
            sidebar: [
                {
                    label: 'Prüfungen',
                    items: [{ label: 'Prüfungen', link: '/01' }],
                },
                {
                    label: 'Prüfungskatalog',
                    items: [{ label: 'Prüfungskatalog', link: '/02' }],
                },
                {
                    label: 'Projektarbeit',
                    items: [{ label: 'Projekt', link: '/03' }],
                },
            ],
        })
    ]
});
