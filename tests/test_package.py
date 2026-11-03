"""Package integrity checks without third-party runtime dependencies."""
from pathlib import Path
import json
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'game-design-skill'
REFERENCES = SKILL / 'references'
BUNDLE = ROOT.parent / 'refrences' / 'game-design-skills-bundle-master'

LENS_SECTIONS = ['When to use', 'Gather', 'Checks', 'Common problems', 'Fix menu', 'Reporting notes']
REPORT_SECTIONS = ['Summary', 'Findings by lens', 'Priority issues', 'Minimal-fix recommendations', 'Next steps']
HOST_SPECIFIC = ['Claude Code', 'Codex', 'AskUserQuestion', 'TodoWrite', 'Task tool', 'mcp__', 'slash command']


def strip_code(text):
    return re.sub(r'```.*?```', '', text, flags=re.S)


def links(text):
    return [link for link in re.findall(r'\]\(([^)]+)\)', strip_code(text))
            if '://' not in link and not link.startswith('#')]


def headings(text, level):
    return re.findall(r'^' + '#' * level + r' (.+)$', strip_code(text), re.M)


def shingles(text, size=10):
    words = re.findall(r"[a-z0-9']+", text.lower())
    return {' '.join(words[i:i + size]) for i in range(len(words) - size + 1)}


class FrontmatterTests(unittest.TestCase):
    def test_portable_frontmatter(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        self.assertIsNotNone(match)
        fields = dict(line.split(': ', 1) for line in match[1].splitlines())
        self.assertEqual(set(fields), {'name', 'description', 'license'})
        self.assertEqual(fields['name'], 'game-design-skill')
        self.assertEqual(fields['name'], SKILL.name)
        self.assertRegex(fields['name'], r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
        self.assertEqual(fields['license'], 'MIT')
        self.assertTrue(0 < len(fields['description']) <= 1024)
        self.assertIn('Use when', fields['description'])
        self.assertNotIn('[TODO', text)


class ReferenceTests(unittest.TestCase):
    def test_every_lens_file_is_routed_from_skill(self):
        linked = {Path(link).name for link in links((SKILL / 'SKILL.md').read_text(encoding='utf-8'))
                  if link.startswith('references/')}
        present = {path.name for path in REFERENCES.glob('*.md')}
        self.assertEqual(linked, present)
        self.assertEqual(len(present), 9)

    def test_relative_markdown_links_resolve(self):
        for path in ROOT.rglob('*.md'):
            for link in links(path.read_text(encoding='utf-8')):
                self.assertTrue((path.parent / link.split('#')[0]).exists(), (str(path), link))

    def test_lens_files_share_one_structure(self):
        for path in REFERENCES.glob('*.md'):
            text = path.read_text(encoding='utf-8')
            self.assertEqual(len(headings(text, 1)), 1, path.name)
            self.assertEqual(headings(text, 2), LENS_SECTIONS, path.name)

    def test_reading_budget(self):
        self.assertLess(len((SKILL / 'SKILL.md').read_text(encoding='utf-8').split()), 1600)
        for path in REFERENCES.glob('*.md'):
            self.assertLess(len(path.read_text(encoding='utf-8').split()), 1200, path.name)


class ReportFormatTests(unittest.TestCase):
    def test_skill_defines_report_and_ratings(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        template = re.search(r'```markdown\n(.*?)```', text, re.S)
        self.assertIsNotNone(template)
        self.assertEqual([h for h in headings(template[1], 2) if h != 'Deliverable'], REPORT_SECTIONS)
        for label in ('P1 Critical', 'P2 Major', 'P3 Minor', 'Observed', 'Inferred', 'Assumed'):
            self.assertIn(label, text)

    def test_examples_follow_report_format(self):
        examples = sorted((ROOT / 'docs' / 'examples').glob('*.md'))
        self.assertTrue(examples, 'At least one recorded example is required')
        for path in examples:
            text = path.read_text(encoding='utf-8')
            self.assertIn('Trial record', text, path.name)
            found = [h for h in headings(text, 2) if h in REPORT_SECTIONS]
            self.assertEqual(found, REPORT_SECTIONS, path.name)


class PortabilityTests(unittest.TestCase):
    def test_skill_text_is_host_neutral(self):
        for path in SKILL.rglob('*.md'):
            text = path.read_text(encoding='utf-8')
            for term in HOST_SPECIFIC:
                self.assertNotIn(term, text, (path.name, term))

    def test_skill_has_no_personal_dependencies(self):
        for path in SKILL.rglob('*'):
            if path.is_file() and path.suffix in {'.md', '.yaml'}:
                text = path.read_text(encoding='utf-8')
                for term in ('/Users/', '/root/', 'ANTHROPIC_API_KEY', 'OPENAI_API_KEY'):
                    self.assertNotIn(term, text, str(path))

    @unittest.skipUnless(BUNDLE.is_dir(), 'reference bundle not present')
    def test_no_long_passages_shared_with_reference_bundle(self):
        bundle = set()
        for path in BUNDLE.rglob('*.md'):
            bundle |= shingles(path.read_text(encoding='utf-8', errors='ignore'))
        ours = list(SKILL.rglob('*.md')) + [ROOT / 'README.md'] + list((ROOT / 'docs').rglob('*.md'))
        for path in ours:
            shared = shingles(path.read_text(encoding='utf-8')) & bundle
            self.assertFalse(shared, (path.name, sorted(shared)[:3]))


class PluginTests(unittest.TestCase):
    def test_plugin_manifests(self):
        plugin = json.loads((ROOT / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        self.assertEqual(plugin['name'], 'game-design-skill')
        self.assertRegex(plugin['version'], r'^\d+\.\d+\.\d+$')
        self.assertEqual(plugin['license'], 'MIT')
        self.assertTrue(plugin['description'])
        for path in plugin['skills']:
            self.assertTrue((ROOT / path / 'SKILL.md').is_file(), path)
        self.assertEqual(len(market['plugins']), 1)
        self.assertEqual(market['plugins'][0]['name'], plugin['name'])
        self.assertTrue((ROOT / market['plugins'][0]['source'] / '.claude-plugin/plugin.json').is_file())
        self.assertTrue(market['owner']['name'])

    def test_plugin_urls_match_release_repository(self):
        plugin = json.loads((ROOT / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        release = (ROOT / '.github/workflows/release.yml').read_text(encoding='utf-8')
        repo = re.search(r"github\.repository == '([^']+)'", release)[1]
        self.assertEqual(plugin['repository'], 'https://github.com/' + repo)
        self.assertEqual(plugin['homepage'], 'https://github.com/' + repo + '#readme')

    def test_license_travels_with_standalone_skill(self):
        root_license = (ROOT / 'LICENSE').read_text(encoding='utf-8')
        self.assertEqual((SKILL / 'LICENSE').read_text(encoding='utf-8'), root_license)
        self.assertIn('MIT License', root_license)
        self.assertIn('Copyright (c) 2026 Kristian Rolando Limantara', root_license)

    def test_contributor_entrypoints(self):
        claude = (ROOT / 'CLAUDE.md').read_text(encoding='utf-8')
        self.assertEqual(claude.splitlines()[0], '@AGENTS.md')
        for name in ('AGENTS.md', 'HANDOFF.md', 'README.md'):
            self.assertTrue((ROOT / name).is_file(), name)
        handoff = (ROOT / 'HANDOFF.md').read_text(encoding='utf-8')
        self.assertIn('- format: cross-agent-handoff/1', handoff)


class RepositoryTests(unittest.TestCase):
    def test_release_notes_match_manifest_version(self):
        version = json.loads((ROOT / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))['version']
        self.assertTrue((ROOT / 'docs' / 'releases' / ('v' + version + '.md')).is_file(), version)

    def test_workflows_run_the_suite_and_guard_releases(self):
        command = 'python -m unittest discover -s tests -v'
        ci = (ROOT / '.github/workflows/ci.yml').read_text(encoding='utf-8')
        release = (ROOT / '.github/workflows/release.yml').read_text(encoding='utf-8')
        self.assertIn(command, ci)
        self.assertIn(command, release)
        self.assertIn("assert tag == 'v' + version", release)
        guard = re.search(r"github\.repository == '([^']+)'", release)
        self.assertIsNotNone(guard)
        self.assertIn(guard[1], (ROOT / 'README.md').read_text(encoding='utf-8'))

    def test_file_map_paths_exist(self):
        text = (ROOT / 'docs' / 'file-map.md').read_text(encoding='utf-8')
        paths = [p for p in re.findall(r'^\| ([^ |]+) \|', text, re.M) if p not in ('Path', '---')]
        self.assertTrue(paths)
        for path in paths:
            self.assertTrue(list(ROOT.glob(path)), path)

    def test_readme_artwork_is_self_contained(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        assets = sorted((ROOT / 'docs' / 'assets').glob('*.svg'))
        self.assertTrue(assets)
        for path in assets:
            text = path.read_text(encoding='utf-8')
            root = ET.fromstring(text)
            self.assertEqual(root.tag, '{http://www.w3.org/2000/svg}svg', path.name)
            self.assertIsNotNone(root.find('{http://www.w3.org/2000/svg}title'), path.name)
            self.assertIsNotNone(root.find('{http://www.w3.org/2000/svg}desc'), path.name)
            for banned in ('<script', '<image', '<foreignObject', 'href="http', '@import', 'url(http'):
                self.assertNotIn(banned, text, (path.name, banned))
            ids = re.findall(r'\bid="([^"]+)"', text)
            self.assertEqual(len(ids), len(set(ids)), path.name)
            self.assertIn('docs/assets/' + path.name, readme, path.name)

    def test_local_artifacts_are_ignored(self):
        ignored = (ROOT / '.gitignore').read_text(encoding='utf-8').splitlines()
        for pattern in ('__pycache__/', '*.pyc', '.DS_Store'):
            self.assertIn(pattern, ignored)


if __name__ == '__main__':
    unittest.main(verbosity=2)
