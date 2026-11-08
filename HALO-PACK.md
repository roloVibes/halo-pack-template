# HALO-PACK.md: working on the My pack pack

You are working in the folder of a Halo pack. Read this page first, then follow its loop for every change. A person
reads it the same way. The full guide is Halo's `docs/PACK-AUTHORING.md`; the contract is `docs/EXTENSION_API.md`.

## What this pack is

`my-pack` (pack.yaml: `id`), "My pack": A Halo pack started from the template

What it brings now (each part one line; pack.yaml lists them under `contributes`):

- bio `my-pack--checker` -- Pick me to check a draft against My pack's checklist and say what is missing, one line per item.
- bio `my-pack--lead` -- Pick me to plan and draft My pack's work -- I turn a request into a short plan and a first draft.
- command `/my-pack:hello` -- Say hello from My pack and what you can ask it to do
- command `/my-pack:search` -- Search the project for a word or a pattern with ripgrep (rg), through the pack's rg MCP server
- skill `my-pack:brief` -- The shape of a My pack draft -- a title, the plan in three steps at most, the draft, the open questions.
- skill `my-pack:checklist` -- The items every My pack draft is checked against, each answered ok, missing or wrong.
- lineup `my-pack--crew` -- The lead drafts My pack's work; the checker reads every draft before it is done.
- workflow `my-pack/flow` -- Draft one piece of work from a request, check it against the checklist and write one report.
- MCP server `words` -- counts the words and lines of a text file
- MCP server `rg` -- searches the project's files with ripgrep (rg), one line per match
- policy `guard` -- asked about Write, Edit
- mode `careful` -- Careful
- mode `focus` -- Focus
- Setup block `prefs` -- My pack: preferences
- Setup block `reach` -- My pack: check this machine
- Setup block `about` -- My pack: before you start
- theme `my-pack/night` -- A violet night with a green second accent
- Studio section `home` -- My pack
- fleet capability `my-pack.work` -- Drafts and checks My pack's work on a harness that runs the pack
- event `note.added`
- artifact `report`
- bundle `bundle:` -- the local model the pack keeps ready while it is on
- requirement `rg` -- searches the project's files for the pack's search command, its rg MCP server and its TODO hook

Once it is installed and enabled, `/my-pack` in a session (the terminal or Studio's Prompt panel) says what the pack
is, lists its commands, workflows and lineups, and runs its default action with what you type after it. That entry
command is `commands/my-pack.md`; keep its list true when you add or remove a part.

## The contract in one page

- **pack.yaml** is the manifest. `id` is lower-case letters, digits and single hyphens, and is the folder's name.
  `version` is semver. `halo_api: {min: "1.1", max: "1.9"}` is the extension API it is written against.
- **contributes** lists every part. A bio or lineup file that is not listed is a doctor line; a listed file that is
  not there is an install line.
- **The plugin half** lives where a Claude plugin keeps it: `commands/`, `skills/<name>/SKILL.md`,
  `hooks/hooks.json`, `.mcp.json`, `.claude-plugin/plugin.json` (its `name` is the id). Halo reads them in place,
  named `my-pack:<name>`; a hook or a server command uses `${halo_python}` (Halo's own Python) and
  `${CLAUDE_PLUGIN_ROOT}` (this folder).
- **Halo's half**: bios in `agents/*.yaml` (read as `my-pack--<name>`), lineups in `teams/*.yaml`, workflows in
  `workflows/<name>.yaml`, typed events in `events/<kind>.json`, artifact schemas in `artifacts/<name>.json`, Studio
  panels, fleet capabilities, policy hooks and modes, Setup blocks, themes, a `bundle:` block, and the tools it needs
  under `requires:`.
- **Code** imports `halo_harness.ext` and nothing else of Halo (`write_private`, `data_dir`, `publish_event`,
  `get_config`, `set_mode`, `testing`, ...).
- **Permissions**: each part that needs one (`hooks`, `mcp:<server>`, `studio-script`, `bash`, `network`,
  `home-write`) is requested in pack.yaml's `permissions`; the owner grants it with `halo pack enable my-pack --grant
  <name>`. Nothing that needs a permission runs until it is granted.

## The loop

1. Edit the files.
2. `halo pack test .` -- every check in a scratch home, one line per failure (`<file>: <what> -- <fix>`), then
   `RESULT: N checks, N passed, N failed`. Read the line, fix that file, run it again. `--json` gives the same for you
   to read. `python -m tests.pack_test` runs the same checks plus the pack's own (`tests/pack_test.py`).
3. `halo pack install . --link --project` -- once: the installed pack is this folder, so every edit shows at the next
   read with no reinstall. Then `halo pack enable my-pack --grant-all` (or only the grants you need).
4. Try it: `/my-pack` in a session, `halo --team my-pack--<lineup>` for a lineup, `halo workflow run my-pack/<name>`
   for a workflow, the pack's section in Studio.
5. `halo pack doctor` -- nothing about this pack left. Then go back to 1.

## The rules

- **Every value in pack.yaml is checked at install**, and so is every file it names. A bad value is one line that
  names the key and what it takes: read the line the check prints and change what it names.
- **No telemetry.** The pack sends nothing anywhere on its own. A tool it wraps that phones home is switched off
  (an environment variable in `.mcp.json`, a flag in the command) and the README says so.
- **No secret in a file.** A key or a token is an environment variable the owner sets; a bio names it by
  `environment.env`, a policy by `redact`. The doctor's privacy scan reads every file of the pack.
- **The owner grants permissions, and the pack asks for the least.** Request only what a part uses; say in the README
  what each grant lets the pack do.
- **A pack writes only in its own folder and its data folder** (`ext.write_private`, `ext.data_dir`: the folder
  `~/.halo/packs/.data/my-pack/`). Writing elsewhere takes the `home-write` grant.
- **Every offered action says what it does and what it costs** before it runs: a Setup check's `what`, `cost`,
  `time` and `writes`; a command's description; a workflow's `budget_usd`.
- **Plain words.** The pack describes what it does; it adds no refusal or warning wording of its own.
- **A tool the pack needs is declared, never installed**: `requires:` names it with the owner's install line for each
  OS, and the doctor says when it is missing.

## Before you share it

`halo pack doctor` clean, `halo pack test .` green, the README true to the files, the permissions the least the parts
use, `CHANGELOG.md` and `version` moved together. Halo 3.3.12.0 wrote this page.
