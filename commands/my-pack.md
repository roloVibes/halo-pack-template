---
description: "My pack: what the pack is, its commands, workflows and lineups -- and its default action"
argument-hint: "[what to do]"
---
This is the My pack pack (my-pack 0.1.0): A Halo pack started from the template

What it brings:
- command /my-pack:hello -- Say hello from My pack and what you can ask it to do
- command /my-pack:search -- Search the project for a word or a pattern with ripgrep (rg), through the pack's rg MCP server
- lineup my-pack--crew -- The lead drafts My pack's work; the checker reads every draft before it is done.
- workflow my-pack/flow -- Draft one piece of work from a request, check it against the checklist and write one report.

If the request below is empty, show the user the list above, one line each, and stop. Otherwise: Run the pack's default action, the workflow my-pack/flow, with the request below as its input: tell the user the command (`halo workflow run my-pack/flow --input request="<the request>"`), what it costs (its budget_usd) and run it once they agree.

Request: $ARGUMENTS
