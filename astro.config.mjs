// astro.config.mjs
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import auth from 'auth-astro';

export default defineConfig({
  integrations: [starlight({
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
          { label: 'Katalog', link: '/00/readme', },
          { label: 'Themenübersicht', link: '/tags-table', attrs: { target: '_blank', rel: 'noopener noreferrer' } },
        ],
      },
      {
        label: 'Abschlussprüfungen',
        items: [
          {
            label: 'AP1 Einrichtung',
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
                  { label: 'November 2024', link: '/01/02/01/2024-november/readme' },
                  { label: 'April 2024', link: '/01/02/01/2024-april/readme' },
                  { label: 'November 2023', link: '/01/02/01/2023-november/readme' },
                  { label: 'April 2023', link: '/01/02/01/2023-april/readme' },
                  { label: 'November 2022', link: '/01/02/01/2022-november/readme' },
                ],
              },
              {
                label: '02 Entwicklung und Umsetzung',
                items: [
                  { label: 'November 2024', link: '/01/02/02/2024-november/readme' },
                  { label: 'April 2024', link: '/01/02/02/2024-april/readme' },
                  { label: 'November 2023', link: '/01/02/02/2023-november/readme' },
                  { label: 'April 2023', link: '/01/02/02/2023-april/readme' },
                  { label: 'November 2022', link: '/01/02/02/2022-november/readme' },
                ],
              },
              {
                label: '03 Wirtschafts- und Sozialkunde',
                items: [
                  { label: 'November 2024', link: '/01/02/03/2024-november/readme' },
                  { label: 'April 2024', link: '/01/02/03/2024-april/readme' },
                  { label: 'November 2023', link: '/01/02/03/2023-november/readme' },
                  { label: 'April 2023', link: '/01/02/03/2023-april/readme' },
                  { label: 'November 2022', link: '/01/02/03/2022-november/readme' },
                ],
              },
            ],
          },
        ],
      },
      {
        label: 'Projekt',
        items: [{ label: 'Projektbeschreibung', link: '/03/readme' }],
      },
      {
        label: 'Praktikum',
        items: [{ label: 'Übersicht', link: '/04/readme' }],
      },
      {
        label: 'Bürokratie',
        items: [
          { label: 'Ausbildungsnachweis', link: '/05/01/readme' },
          { label: 'Zeitnachweis', link: '/05/02/readme'},
          { label: 'Industrie- und Handelskammern', link: '' },
          { label: 'Bildungsträger', link: '' },
          { label: 'Kostenträger', link: '' },
        ],
      },
    ],
    
  }), auth()],
});