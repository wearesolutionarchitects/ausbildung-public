import { defineCollection, z } from 'astro:content';

const docsCollection = defineCollection({
    schema: z.object({
        title: z.string(),
        description: z.string().optional(),
        author: z.string().optional(),
        pubDate: z.string().optional(),
    tags: z.array(z.string()).optional(),
    }),
});

export const collections = {
    docs: docsCollection,
};