import fs from 'fs';
import fg from 'fast-glob';
import matter from 'gray-matter';
import path from 'path';

async function collectTags() {
  const files = await fg('src/content/docs/01/01/**/*.{md,mdx}', { absolute: true });

  const tags: Record<string, number> = {};

  files.forEach((filePath) => {
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    const { data } = matter(fileContent);

    if (data.tags && Array.isArray(data.tags)) {
      data.tags.forEach((tag: string) => {
        tags[tag] = (tags[tag] || 0) + 1;
      });
    }
  });

  return tags;
}

async function generateReadme() {
  const tags = await collectTags();

  const yamlHeader = `---
title: Themen
pubDate: 2025-03-22
meta:
  - name: "description"
    content: "Themen"
  - name: "author"
    content: "Heiko Fanieng"
  - property: "og:title"
    content: "Prüfungen"
  - property: "og:description"
    content: "Themen"
  - http-equiv: "content-language"
    content: "de"
---

`;

  let readmeContent = `${yamlHeader}
## 📌 Themen-Übersicht

### AP 1

| Thema | Häufigkeit |
| ---- | ---- |
`;

Object.entries(tags)
.sort(([, a], [, b]) => b - a)
.forEach(([tag, count]) => {
  readmeContent += `| ${tag} | ${count} |\n`;
});

  const targetPath = path.resolve(process.cwd(), 'src', 'content', 'docs', '00', '03', 'README.md');

  console.log(`🖨️  Erstelle README.md in: ${targetPath}`);

  try {
    fs.writeFileSync(targetPath, readmeContent);
    console.log('✅ README.md erfolgreich mit YAML-Header erstellt.');
  } catch (err) {
    console.error('❌ Fehler beim Schreiben der README.md:', err);
  }
}

generateReadme();
