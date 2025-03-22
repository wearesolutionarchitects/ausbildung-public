// content.config.ts
// This file is used to define the content collections for your Astro project.

import { defineCollection, z } from 'astro:content'; 
import { docsSchema } from '@astrojs/starlight/schema';

const docsCollection = defineCollection({
  schema: (context) => docsSchema()(context), 
});

// Define the collections for your project
export const collections = {
  docs: docsCollection,
};