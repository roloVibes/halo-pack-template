# Halo pack template

The starting point for a [Halo Harness](https://github.com/roloVibes/Halo-Harness) pack that is known to work. It is the
folder `halo pack new my-pack --all --github` writes (Halo 3.3.12.0): one working example of every part a pack can
contribute -- agent bios, a lineup, skills, commands, hooks, an MCP server, events and artifacts, a workflow, a Studio
section, a capability bundle, a fleet note, a policy, a mode, Setup blocks, a theme and an open-source tool wrapped with
`requires:` -- plus the files that make it a project: the contract a Halo session follows (`HALO-PACK.md`), tests, a
CHANGELOG, a license and a GitHub Actions workflow that runs `halo pack test .` on Linux and Windows on every push.

## Start here

1. **Take it.** "Use this template" on GitHub (or clone it), then in the folder: `python rename.py <your-id> "<Your name>"`.
   The id is the pack's name everywhere (`/<id>` is its entry command); the script replaces `my-pack` in every file and
   deletes itself.
2. **Install Halo** if you have not: `uv tool install git+https://github.com/roloVibes/Halo-Harness@v3.3.12.0`
   (the install page: https://github.com/roloVibes/Halo-Harness/blob/master/docs/INSTALL.md).
3. **Check it works before you change anything:** `halo pack test .` -- every check runs in a scratch home of its own, with
   no model call and no network; the line `RESULT: N checks, N passed, 0 failed` is the goal from here on.
4. **Make it yours.** Keep the kinds you need and delete the rest -- a folder and its line under `contributes:` in
   `pack.yaml` go together. Each example says in its first lines what it is for. The reference for every field is
   https://github.com/roloVibes/Halo-Harness/blob/master/docs/EXTENSION_API.md and the guide is
   https://github.com/roloVibes/Halo-Harness/blob/master/docs/PACK-AUTHORING.md.
5. **Or let a Halo session do it:** `halo --team pack-author` in this folder runs the lineup Halo ships for pack work
   (an author who reads `HALO-PACK.md` first, a researcher who finds open-source tools to wrap, a reviewer who checks the
   pack against the checklist). Several sessions can work on several pack folders at once.
6. **Try it live:** `halo pack install . --link --project` (the installed pack is this folder; an edit shows at once),
   `halo pack enable <id> --grant-all`, then `/<id>` in a session.
7. **Publish.** Push to GitHub; the workflow in `.github/workflows/pack-test.yml` runs the same `halo pack test .` against
   the Halo release this template was made with (move the tag when you test a newer one). Users install it with
   `halo pack sources add https://github.com/<you>/<repo>` and `halo pack install <id>`; tag each release so
   `halo pack update` can tell them apart.

Everything below this line is the pack's own README as `halo pack new` wrote it: replace it with yours.

---

# My pack (my-pack)

A Halo pack started from the template

A Halo pack. `HALO-PACK.md` is how to work on it; this page is how to use it.

## Install

It uses these open-source tools; Halo never installs them, so install each once:

- **rg** (MIT OR Unlicense, https://github.com/BurntSushi/ripgrep): searches the project's files for the pack's search command, its rg MCP server and its TODO hook
  - windows: `winget install BurntSushi.ripgrep.MSVC`
  - linux: `sudo apt install ripgrep`
  - mac: `brew install ripgrep`

## Install from GitHub

```
halo pack sources add https://github.com/<you>/my-pack
halo pack install my-pack
halo pack enable my-pack --grant-all
```

`halo pack update` reads the repo again and says each `migrations` note first; tag each release.

## Use it

```
halo pack install ./my-pack
halo pack enable my-pack --grant-all
```

Then `/my-pack` in a session lists what it brings:

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

## Permissions

Each one runs nothing until you grant it (`halo pack enable my-pack --grant <name>`):

- `hooks`: its hooks and its policy hooks run
- `mcp:words`: its MCP server words starts
- `studio-script`: its Studio bundle panel's script runs in the page
- `mcp:rg`: its MCP server rg starts

## Files

- `.claude-plugin/plugin.json`: the Claude-plugin half's name (the pack's id)
- `.github/workflows/pack-test.yml`: GitHub Actions: halo pack test . on Linux and Windows at a pinned Halo tag
- `.gitignore`: caches and run-time data kept out of the repo
- `.mcp.json`: the MCP servers, started with Halo's own Python once their mcp:<server> grant is given
- `CHANGELOG.md`: each release of the pack, newest first
- `HALO-PACK.md`: what a Halo session (or you) follows when working on the pack: the contract, the loop, the rules
- `LICENSE`: the pack's license
- `README.md`: this page, written from pack.yaml by halo pack new
- `agents/checker.yaml`: a bio
- `agents/lead.yaml`: a bio
- `artifacts/report.json`: an artifact schema
- `commands/hello.md`: a slash command
- `commands/my-pack.md`: the entry command /my-pack: what the pack is, its parts, its default action
- `commands/search.md`: a slash command
- `events/note.added.json`: an event kind's schema
- `fleet/notes.md`: a fleet inspector line
- `hooks/hooks.json`: the hooks, loaded once the hooks grant is given
- `hooks/log_write.py`: a hook script
- `hooks/rg_todos.py`: a hook script
- `mcp/rg_server.py`: an MCP server
- `mcp/words_server.py`: an MCP server
- `pack.yaml`: the manifest: id, version, the extension API range, what it contributes, what it requests
- `policy/guard.py`: a policy hook
- `setup/about.md`: a Setup block's file
- `setup/check.py`: a Setup block's file
- `skills/brief/SKILL.md`: a skill
- `skills/checklist/SKILL.md`: a skill
- `studio/notes.md`: a Studio panel's source
- `studio/view.js`: a Studio panel's source
- `teams/crew.yaml`: a lineup
- `tests/__init__.py`: makes tests/ a package, so python -m tests.pack_test finds the pack's own
- `tests/pack_test.py`: the pack's own test: halo_harness.ext.testing's checks, then its own
- `tests/samples/artifacts/report.json`: a sample its schema is checked against by halo pack test
- `tests/samples/events/note.added.json`: a sample its schema is checked against by halo pack test
- `workflows/flow.yaml`: a workflow

## Develop it

`halo pack test .` checks every part in a scratch home; `halo pack install . --link --project` makes the installed pack this folder, so an edit shows at once; `halo pack doctor` says what is left. HALO-PACK.md has the loop and the rules.
