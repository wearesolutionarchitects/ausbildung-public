// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Mysteryland.biz',
			social: {
				github: 'https://github.com/devsfiae',
			},
			sidebar: [
				{
					label: 'Prüfungskatalog',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Katalog', slug: '00/welcome' },
					],
				},
				{
					label: 'Abschlussprüfungen',
					autogenerate: { directory: '01' },
				},
				{
					label: 'Praktikum',
					autogenerate: { directory: '02' },
				},
				{
					label: 'Projekt',
					autogenerate: { directory: '03' },
				},
			],
		}),
	],
});
