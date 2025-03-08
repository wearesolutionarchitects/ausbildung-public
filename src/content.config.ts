import { defineCollection, z } from 'astro:content'; 
import { docsSchema } from '@astrojs/starlight/schema';

// Erweitere das Schema, falls `docsSchema` die Tags nicht korrekt beinhaltet
// const extendedDocsSchema = (context: any) => (docsSchema(context) as unknown as z.ZodObject<any>).merge(z.object({
// tags: z.array(z.string()).optional(),
// }));

const docsCollection = defineCollection({
  schema: (context) => docsSchema()(context), 
});

// Debugging, um zu sehen, ob Tags richtig erfasst werden
// async function debugTags() {
//   const docs = await import('astro:content').then(({ getCollection }) => getCollection('docs'));
//   console.log("📢 Geladene Dokumente:", docs);

//   docs.forEach(doc => {
//     console.log(`📄 Dokument: ${doc.id} - Tags:`, doc.data.tags || "⚠ Keine Tags gefunden");
//   });
// }

// debugTags();

export const collections = {
  docs: docsCollection,
};