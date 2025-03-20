import fs from 'fs';
import fg from 'fast-glob';
import matter from 'gray-matter';
import path from 'path';

async function collectTags() {
  const files = await fg('src/**/*.{md,mdx}', { absolute: true });

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

  let readmeContent = '# 📌 Tag-Übersicht\n\n| Tag | Häufigkeit |\n| ---- | ---- |\n';

  Object.entries(tags).forEach(([tag, count]) => {
    readmeContent += `| ${tag} | ${count} |\n`;
  });

  // An diesen Pfad wird die README.md geschrieben:
  const targetPath = path.resolve(process.cwd(), 'src', 'content', 'docs', '00', '03', 'README.md');

  console.log(`🖨️  Erstelle README.md in: ${targetPath}`);

  try {
    fs.writeFileSync(targetPath, readmeContent);
    console.log('✅ README.md erfolgreich erstellt.');
  } catch (err) {
    console.error('❌ Fehler beim Schreiben der README.md:', err);
  }
}

generateReadme();