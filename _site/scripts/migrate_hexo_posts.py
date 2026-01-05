#!/usr/bin/env python3
"""
Migrate Hexo blog posts to Jekyll format.
Converts HTML posts from old_site to markdown posts in _posts directory.
"""

import os
import re
import html
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
import subprocess

class HexoToJekyllMigrator:
    def __init__(self, old_site_path, new_posts_path):
        self.old_site_path = Path(old_site_path)
        self.new_posts_path = Path(new_posts_path)

        # Define the 4 posts to migrate (excluding hello-world and test)
        self.posts_to_migrate = [
            'Chinese-Remainder-Theorem',
            'Limit-of-Binomial-Distribution',
            'diffeqsolve',
            'Sprague-Grundy-Theorem-and-the-Game-of-Nim'
        ]

    def find_blog_posts(self):
        """Find the 4 specific blog post HTML files"""
        posts = []
        base = self.old_site_path / "2021"

        for html_file in base.rglob("index.html"):
            # Check if this is one of our target posts
            for post_slug in self.posts_to_migrate:
                if post_slug in str(html_file):
                    posts.append(html_file)
                    break

        return sorted(posts)

    def extract_metadata(self, html_path):
        """Extract title, date, tags from HTML meta tags"""
        with open(html_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'lxml')

        metadata = {}

        # Extract title
        title_tag = soup.find('meta', property='og:title')
        if title_tag:
            metadata['title'] = title_tag.get('content', '')

        # Extract date
        date_tag = soup.find('meta', property='article:published_time')
        if date_tag:
            date_str = date_tag.get('content', '')
            # Parse ISO format date
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            metadata['date_formatted'] = dt.strftime('%Y-%m-%d')
            metadata['date_obj'] = dt

        # Extract tags
        tag_tags = soup.find_all('meta', property='article:tag')
        metadata['tags'] = [tag.get('content') for tag in tag_tags if tag.get('content')]

        # Extract slug from path
        path_parts = str(html_path).split('/')
        for i, part in enumerate(path_parts):
            if part == '2021' and i + 3 < len(path_parts):
                metadata['slug'] = path_parts[i + 3]
                break

        return metadata

    def extract_post_content(self, html_path):
        """Extract content from <div class="post-body">"""
        with open(html_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'lxml')

        post_body = soup.find('div', class_='post-body')
        if not post_body:
            raise ValueError(f"No post-body found in {html_path}")

        # Get inner HTML content without the wrapper div
        return post_body.decode_contents()

    def convert_html_to_markdown(self, html_content):
        """Use pandoc to convert HTML to markdown"""
        # Pre-process: Convert MathJax span tags to proper delimiters
        # Replace <span class="math display">\[...\]</span> with $$...$$
        html_content = re.sub(
            r'<span class="math display">\\\\?\[',
            '$$',
            html_content
        )
        html_content = re.sub(
            r'\\\\?\]</span>',
            '$$',
            html_content
        )

        # Replace <span class="math inline">\(...\)</span> with $...$
        html_content = re.sub(
            r'<span class="math inline">\\\\?\(',
            '$',
            html_content
        )
        html_content = re.sub(
            r'\\\\?\)</span>',
            '$',
            html_content
        )

        try:
            result = subprocess.run(
                ['pandoc', '-f', 'html', '-t', 'markdown',
                 '--wrap=preserve'],
                input=html_content.encode('utf-8'),
                capture_output=True,
                check=True
            )

            markdown = result.stdout.decode('utf-8')

            # Clean up the markdown
            markdown = self.clean_markdown(markdown)

            return markdown

        except subprocess.CalledProcessError as e:
            print(f"Pandoc conversion failed: {e.stderr.decode('utf-8')}")
            raise

    def clean_markdown(self, markdown):
        """Clean up common conversion issues"""
        # Remove excessive newlines (more than 2)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        # Unescape HTML entities
        markdown = html.unescape(markdown)

        # Fix common HTML entities that might remain
        markdown = markdown.replace('&quot;', '"')
        markdown = markdown.replace('&#x2F;', '/')

        return markdown.strip()

    def create_jekyll_post(self, metadata, content):
        """Generate Jekyll post file with front matter"""
        # Create filename: YYYY-MM-DD-slug.md
        filename = f"{metadata['date_formatted']}-{metadata['slug']}.md"
        filepath = self.new_posts_path / filename

        # Build front matter
        front_matter = ['---']
        front_matter.append(f"title: '{metadata['title']}'")
        front_matter.append(f"date: {metadata['date_formatted']}")

        # Create permalink
        date_parts = metadata['date_formatted'].split('-')
        permalink = f"/posts/{date_parts[0]}/{date_parts[1]}/{metadata['slug'].lower()}/"
        front_matter.append(f"permalink: {permalink}")

        # Add tags if present
        if metadata.get('tags'):
            front_matter.append('tags:')
            for tag in metadata['tags']:
                front_matter.append(f"  - {tag}")

        front_matter.append('---')

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(front_matter))
            f.write('\n\n')
            f.write(content)

        print(f"Created: {filename}")
        return filepath

    def migrate_all_posts(self):
        """Main migration orchestrator"""
        print("Migrating 4 technical blog posts from Hexo to Jekyll...\n")

        # Ensure output directory exists
        self.new_posts_path.mkdir(parents=True, exist_ok=True)

        # Find posts
        posts = self.find_blog_posts()
        print(f"Found {len(posts)} posts to migrate:\n")

        migrated_count = 0

        for post_path in posts:
            try:
                # Extract metadata
                metadata = self.extract_metadata(post_path)
                print(f"Migrating: {metadata['title']}")

                # Extract content
                html_content = self.extract_post_content(post_path)

                # Convert to markdown
                markdown_content = self.convert_html_to_markdown(html_content)

                # Create Jekyll post
                self.create_jekyll_post(metadata, markdown_content)

                migrated_count += 1
                print()

            except Exception as e:
                print(f"Error migrating {post_path}: {e}\n")
                continue

        print(f"Migration complete! {migrated_count}/{len(posts)} posts successfully migrated.")
        return migrated_count

def main():
    # Set up paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    old_site_path = repo_root / "old_site"
    new_posts_path = repo_root / "_posts"

    # Create migrator and run
    migrator = HexoToJekyllMigrator(old_site_path, new_posts_path)
    migrator.migrate_all_posts()

if __name__ == "__main__":
    main()
