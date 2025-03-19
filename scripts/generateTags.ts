import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import fg from 'fast-glob';

async function collectTags() {
    const entries = await fg('src/**/*.{md,mdx}');
    const tags: Record<string, number> = {};

    for (const entry of entries) {
        const content = fs.readFileSync(entry, 'utf8');
        const fmMatch = content.match(/^---\n([\s\S]*?)\n---/);
        if (fmMatch) {
            const fm = fmMatch[1];
            const tagsMatch = fm.match(/tags:\s*\[(.*?)\]/s);
            if (tagsMatch) {
                const tagsArray = fm[1].split('\n').map(line => line.replace(/- /, '').trim());
                tagsArray.forEach(tag => {
                    tags[tag] = (tags[tag] || 0) + 1;
                });
            }
        }
    }

    return tags;
}

async function generateReadme() {
    const tags = await collectTags();

    let readmeContent = '# 📌 Tag Übersicht\n\n| Tag | Häufigkeit |\n| ---- | ---- |\n';

    Object.entries(tags).forEach(([tag, count]) => {
        readmeContent += `| ${tag} | ${count} |\n`;
    });

    fs.writeFileSync('README.md', readmeContent);
    console.log('README.md erfolgreich generiert!');
}

generateReadme();
