// astro.config.mjs
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  integrations: [
    starlight({
      head: [
        { tag: 'meta', attrs: { name: 'description', content: 'Meine Seite' } },
        { tag: 'meta', attrs: { name: 'viewport', content: 'width=device-width, initial-scale=1' } }
      ],
      title: 'Ausbildung',
      social: {
        github: 'https://github.com/devsfiae',
      },
      sidebar: [
        {
          label: 'Prüfungskatalog',
          items: [
            { label: 'Katalog', link: '/00/welcome' },
            { label: 'Themenübersicht', link: '/tags-table', attrs: { target: '_blank', rel: 'noopener noreferrer' } },
          ],
        },
        {
          label: 'Abschlussprüfungen',
          items: [
            {
              label: 'AP1',
              items: [
                // { label: 'Ablauf', link: '/01/readme' },
				        { label: 'Themen', link: '/01/01/readme' },
                { label: 'März 2025', link: '/01/01/2025-maerz/readme' },
                { label: 'September 2024', link: '/01/01/2024-september/readme' },
				{ label: 'März 2024', link: '/01/01/2024-maerz/readme' },
				{ label: 'September 2023', link: '/01/01/2023-september/readme' },
				{ label: 'März 2023', link: '/01/01/2023-maerz/readme' },
				{ label: 'September 2022', link: '/01/01/2022-september/readme' },
				{ label: 'März 2022', link: '/01/01/2022-maerz/readme' },
				{ label: 'September 2021', link: '/01/01/2021-september/readme' },
				{ label: 'März 2021', link: '/01/01/2021-maerz/readme' },
				
              ],
            },
            {
              label: 'AP2',
              items: [
                {
                  label: '01 Planung ',
                  items: [
                    { label: 'Thema 1', link: '/abschlusspruefungen/02/01/thema1' },
                    { label: 'Thema 2', link: '/abschlusspruefungen/02/thema2' },
                    { label: 'Thema 3', link: '/abschlusspruefungen/02/thema3' },
                  ],
                },
                {
                  label: '02 Entwicklung und Umsetzung',
                  items: [
                    { label: 'Thema 1', link: '/abschlusspruefungen/02/03/thema1' },
                    { label: 'Thema 2', link: '/abschlusspruefungen/02/thema2-3' },
                    { label: 'Thema 3', link: '/abschlusspruefungen/02/thema3-3' },
                  ],
                },
                {
                  label: '03 Wirtschafts- und Sozialkunde',
                  items: [
                    { label: 'Thema 1', link: '/abschlusspruefungen/02/03/thema1' },
                    { label: 'Thema 2', link: '/abschlusspruefungen/02/thema2-3' },
                    { label: 'Thema 3', link: '/abschlusspruefungen/02/thema3-3' },
                  ],
                },
              ],
            },
          ],
        },
        {
          label: 'Praktikum',
          items: [{ label: 'Übersicht', link: '/praktikum/uebersicht' }],
        },
        {
          label: 'Projekt',
          items: [{ label: 'Projektbeschreibung', link: '/projekt/projektbeschreibung' }],
        },
        {
          label: 'Bürokratie',
          items: [
            { label: 'Berichtsheft', link: '' },
            { label: 'Zeitnachweis', link: '', attrs: { target: '_blank', rel: 'noopener noreferrer' } },
            { label: 'Induestrie- und Handelskammern (79)', link: '' },
          ],
        },
      ],
      
    }),
  ],
});