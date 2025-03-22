// content.config.ts
// This file is used to define the content collections for your Astro project.

import { defineCollection } from 'astro:content';
import { docsSchema } from '@astrojs/starlight/schema';
import { z } from 'astro/zod';

const docsCollection = defineCollection({
  schema: (context) => docsSchema({
    extend: z.object({
      draft: z.boolean().optional(),
      categories: z.array(z.string()).optional(),
      tags: z.array(z.string()).optional(),
      tasks: z.array(z.object({
        id: z.string(),
        title: z.string(),
        points: z.number(),
        topics: z.array(z.string()),
      })).optional(),
    }),
  })(context),
});

export const collections = {
  docs: docsCollection,
};