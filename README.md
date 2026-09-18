<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <img src="assets/banner-light.png" width="100%" alt="Adam Matthew Steinberger — Staff Software Architect & AI Automation Engineer. Status: building in the open. Contributors welcome: developers, governments and military, universities and academia.">
</picture>

# Adam Matthew Steinberger

**Staff Software Architect & AI Automation Engineer** — I build AI systems that actually work inside enterprise environments: production-grade platforms that handle real data, real security requirements, and real organizational complexity. Not just demos.

[![vibey on PyPI](https://img.shields.io/pypi/v/vibey?style=flat-square&label=vibey&color=6f42c1)](https://pypi.org/project/vibey/) [![vibey on GitHub](https://img.shields.io/badge/GitHub-the--vibey--project%2Fvibey-24292f?style=flat-square&logo=github&logoColor=white)](https://github.com/the-vibey-project/vibey) [![LinkedIn](https://img.shields.io/badge/LinkedIn-adammatthewsteinberger-0a66c2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adammatthewsteinberger/) [![Join me](https://img.shields.io/badge/Join%20me-contribute-6f42c1?style=flat-square)](https://vibewithadam.matthewsteinberger.com/join-me)

Based in Greenville, SC. I primarily develop free and open-source software, and right now that means **[vibey](https://github.com/the-vibey-project/vibey)**, the open-source conductor that turns AI coding agents into autonomous software delivery. I'm looking for developers to help build it. Greenville-remote or US-remote volunteers are welcome and encouraged to get involved at any time.

This profile speaks to three audiences, in this order: **[developers](#help-build-vibey)** · **[governments and military](#governments-and-military)** · **[universities and academia](#universities-and-academia)**.

**→ [Everything a developer needs to get started](https://vibewithadam.matthewsteinberger.com/join-me#developers)** · [Email me](mailto:adam@matthewsteinberger.com) · [Ask about Adam](https://chatwithadam.matthewsteinberger.com/) (a Claude RAG chat I built)

## Help build vibey

AI coding agents can write code. Delivery still means babysitting them: re-prompting when one loses the thread, re-explaining everything after a crash, and watching a run die at 2am because one vendor's credits ran out. vibey takes that job over. It interviews you until the spec is sharp, builds unattended across a pool of engines, and brings you back only for the decisions that are genuinely yours.

It's MIT licensed and one `uv tool install vibey` away ([PyPI](https://pypi.org/project/vibey/) · [docs](https://the-vibey-project.github.io/vibey/main/)). The whole family lives in [one repository](https://github.com/the-vibey-project/vibey): the five `*loop` engines, vibey-gh, vibey-skills, and vibey-bootstrap.

**How to get started**

1. **Set up the repository.** You need Python 3.12+, PostgreSQL, and macOS or Linux. The test suite needs no engine binaries and no paid accounts.
   ```sh
   git clone https://github.com/the-vibey-project/vibey.git && cd vibey
   uv sync --extra dev
   uv run pre-commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push
   uv run vibey-gh install
   ```
2. **Run the gates.** The same seven gates CI runs (ruff lint and format, `mypy --strict`, the tests with a 100% branch-coverage floor on each architectural layer, import-linter, bandit, pip-audit), in one command: `uv run pre-commit run --all-files --hook-stage pre-push`.
3. **Pick an issue.** Start with a [good first issue](https://github.com/the-vibey-project/vibey/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22good%20first%20issue%22), [help wanted](https://github.com/the-vibey-project/vibey/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22help%20wanted%22), or an [open bug](https://github.com/the-vibey-project/vibey/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22bug%22). Read [CONTRIBUTING.md](https://github.com/the-vibey-project/vibey/blob/develop/CONTRIBUTING.md) and the short list of [non-negotiables](https://github.com/the-vibey-project/vibey/blob/develop/CLAUDE.md) first, because the gates enforce both.
4. **Branch from `develop` and commit conventionally.** `git checkout -b feature/short-description develop`. The commit-msg hook appends the `Made-With:` provenance trailer.
5. **Open a pull request into `develop`, never `main`.** You never press Merge: once it has one approval, a green `gates` check, and a passing PR-automation gate, the merge train squash-merges it.

Where help matters most: finishing the sovereign path ([#115](https://github.com/the-vibey-project/vibey/issues/115), turning a local design into build work without a paid engine), fixing a reported bug, adding an engine, adding a skill, and improving the docs. The full walk-through, with the ten-minute user quickstart, is at **[/join-me#developers](https://vibewithadam.matthewsteinberger.com/join-me#developers)**.

## Governments and military

Governments, and armed forces most of all, adopt software under the hardest obligations. Every artifact has to be attributable, and every automated decision has to be reconstructible after the fact. Work has to continue when a vendor or a network is denied, and no capability can depend on a supplier's continued goodwill. Here is what vibey offers against those obligations. Each claim links to its source, so you can check it instead of trusting it.

- **Local models by preference, not as a fallback.** The project's governing rules make the fully local path the preferred way to run ([sub-doctrine 8.a](https://github.com/the-vibey-project/vibey/blob/develop/src/vibey_tools/gh/docs/doctrines.md)). The design interview can run entirely on a local model served by Ollama, and build work can be pinned to qwenloop, a local Qwen 2.5 Coder engine. One gap is still open: turning a local design into build work without a paid engine ([#115](https://github.com/the-vibey-project/vibey/issues/115)). → [decision record](https://github.com/the-vibey-project/vibey/blob/develop/docs/architecture/decisions/0027-sovereign-design-provider.md)
- **Built to run on your own hardware.** Your macOS or Linux hosts, your own PostgreSQL, no cloud control plane. The local engine never downloads model weights on its own. → [decision record](https://github.com/the-vibey-project/vibey/blob/develop/docs/architecture/decisions/0015-qwenloop-standby.md)
- **An append-only ledger you can audit.** Every decision, finding, and handoff is written to an append-only PostgreSQL ledger before it takes effect. A correction is a new event that supersedes the old one, so any run can be reconstructed after the fact. → [the paper](https://the-vibey-project.github.io/vibey/main/paper/)
- **Human authority is part of the structure.** Four of the six phases need an explicit, recorded human verdict before they close, and a worker never blocks while it waits. → [the paper](https://the-vibey-project.github.io/vibey/main/paper/)
- **Provenance and exact-head review.** Every source file carries a provenance header and every commit a provenance trailer, enforced by a pre-push hook and a required CI check. Every check, review, and merge is tied to the exact commit it examined, so an old approval can never pass newer code. → [vibey-gh for governments](https://github.com/the-vibey-project/vibey/blob/develop/src/vibey_tools/gh/docs/government.md)
- **Everything as code, behind the same gates.** Branch protection, pipelines, policy, and infrastructure are declared in the repository and reconciled from it. Changes pass bandit, pip-audit, strict typing, enforced layering, and a 100% branch-coverage floor on each layer. → [decision record](https://github.com/the-vibey-project/vibey/blob/develop/docs/architecture/decisions/0018-everything-as-code.md)
- **Written rules for machine agents.** vibey's agent instructions carry standing subdoctrine [SD-01](https://github.com/the-vibey-project/vibey/blob/develop/src/vibey_tools/gh/docs/sd-01-counterparties-trust-verification.md) word for word: every counterparty, whether a person, a company, or a state, starts unverified until a tangible check establishes its identity, authority, and intent.

Use official channels, and expect the same verification in return. Write from an official address to [adam@matthewsteinberger.com](mailto:adam@matthewsteinberger.com), report a security vulnerability privately as [vibey's security policy](https://github.com/the-vibey-project/vibey/blob/develop/SECURITY.md) describes (never in a public issue), and ask public questions in [GitHub Discussions](https://github.com/the-vibey-project/vibey/discussions). The full section is at **[/join-me#governments](https://vibewithadam.matthewsteinberger.com/join-me#governments)**.

*This profile claims no government or military customer, contract, clearance, accreditation, or endorsement. vibey is MIT-licensed open source: evaluate it on your own hardware, against its own gates.*

## Universities and academia

Claims about AI agents are easy to make and hard to reproduce. vibey's design is written as a research paper, its whole documentation is a book, and the code that backs both is open. Read it, cite it, teach with it, and test it.

- **The research paper.** *Ledger-Mediated Orchestration: Vendor-Independent Autonomous Software Delivery over a Pool of Coding Agents* states the ledger invariant, the queue semantics, the no-loss handoff gate, and the gate-soundness argument formally. [HTML](https://the-vibey-project.github.io/vibey/main/paper/) · [PDF](https://the-vibey-project.github.io/vibey/main/paper.pdf) · [companion paper on the exact-head release calculus](https://github.com/the-vibey-project/vibey/blob/develop/src/vibey_tools/gh/docs/paper.md)
- **The book.** Every page of the documentation, in reading order, rebuilt on every release. [PDF](https://the-vibey-project.github.io/vibey/main/book.pdf) · [EPUB](https://the-vibey-project.github.io/vibey/main/book.epub) · [print-ready HTML](https://the-vibey-project.github.io/vibey/main/book-print.html)
- **Reproducible from the repository.** The paper is typeset from Markdown in the repository. The properties it relies on are pure, deterministic code under a 100% branch-coverage floor, backed by property tests and a chaos test against a real PostgreSQL. The paper also says what it does not yet report: live runs beyond two paid engines. Independent replication is welcome.
- **Cite it.** The repository has a [CITATION.cff](https://github.com/the-vibey-project/vibey/blob/develop/CITATION.cff), so GitHub's "Cite this repository" button and citation managers can read it directly. No DOI or preprint identifier has been assigned yet.
- **Open licenses for teaching and research.** vibey is [MIT licensed](https://github.com/the-vibey-project/vibey/blob/develop/LICENSE). Use it in a course, fork it for an experiment, and publish what you find.
- **Research collaboration.** Some open questions worth a study: how the local path compares with paid engines on the same specifications, how the no-loss handoff gate behaves at scale, and live evaluation across all five engines. Propose a study, a course project, or a research partnership in [Discussions](https://github.com/the-vibey-project/vibey/discussions) or by [email](mailto:adam@matthewsteinberger.com).

The full section is at **[/join-me#academia](https://vibewithadam.matthewsteinberger.com/join-me#academia)**. *This profile claims no institutional affiliation or endorsement.*

## What I ship

Proof, not promises. Every number below is from a real engagement; client identities stay out of it.

- **[AI Governance Gateway](https://vibewithadam.matthewsteinberger.com/work/ai-governance-gateway)** — sole architect. Five model vendors (Azure AI, Anthropic, OpenAI/Codex, Cursor, Grok, Gemini) behind one policy-enforced, OpenAI-compatible API: per-project USD spend caps, multi-unit rate limiting, HMAC-signed hash-chained audit trail, no API keys in the path. Three product teams migrated onto it; their credentials retired.
- **[AI Payroll Processor](https://vibewithadam.matthewsteinberger.com/work/enterprise-ai-payroll-processor)** — co-lead. 20 microservices, four human-approved phases, 585 test modules, Terraform/Helm/GitOps on private AKS. Architecture production-ready at day 45; a junior dev trained in parallel now owns it.
- **[Identity Governance as Code](https://vibewithadam.matthewsteinberger.com/work/identity-governance-as-code)** — sole author. Two control planes reconciling tenant state from Git: a kopf operator with fully secretless multi-tenant auth and LLM-drafted PRs, and an IdP governance platform managing 40 resource kinds via six addressing patterns, human-gated destructive drift, point-in-time reversion.
- **[Multi-System Ticket Relay](https://vibewithadam.matthewsteinberger.com/work/multi-system-ticket-relay)** — sole author. N-way sync with no privileged hub: version vectors, echo suppression, a conflict engine that fails to manual hold. 653 tests, 93% coverage, import-linter-enforced pure domain, property/mutation/chaos-tested convergence.
- **[Technical Report Generation Platform](https://vibewithadam.matthewsteinberger.com/work/ai-report-generator-email-intake)** — lead. Instrument data → standards-aware deliverables: event-driven ingestion, multi-vendor parsers, deterministic analysis + LLM review, SAML 2.0 SSO, deploys that prove they rolled out.
- **[Self-Hosted RAG Chatbot](https://vibewithadam.matthewsteinberger.com/work/self-hosted-rag-chatbot)** — Mistral-7B, FAISS, vLLM, Docker. Zero external dependencies, shipped in 30 days.
- **[GodFocus Push Notifications](https://vibewithadam.matthewsteinberger.com/work/godfocus-push-notifications)** — TDD Web Push system. 159/159 tests, 85.84% coverage, 5 billable hours.

Underneath: secretless DevSecOps (OIDC workload identity across 20 CI workflows in 9 repos; SAST, SCA, IaC scanning, SBOM, keyless signing, policy admission), five formal architecture document sets, identity-governance advisory for a SOX-regulated enterprise, and the *Security-First Scrum* framework.

All 17 case studies → **[/work](https://vibewithadam.matthewsteinberger.com/work)**

## Open source — MIT, on PyPI

Everything here except clippy-pet lives in one repository, **[the-vibey-project/vibey](https://github.com/the-vibey-project/vibey)**, and ships as one PyPI distribution: `uv tool install vibey` installs the conductor, all five `*loop` engines, and the tools ([PyPI](https://pypi.org/project/vibey/) · [docs](https://the-vibey-project.github.io/vibey/main/)).

| Package | What it is | Links |
|---|---|---|
| **claudeloop** | Onion-architected autonomous Claude Code session runner. Never blocks on a human; tells an exhausted rate-limit window apart from exhausted credits and resumes across usage windows. | [source](https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_runners/claude) |
| **codexloop · cursorloop · agyloop** | The same runner, three more engines — OpenAI Codex, Cursor Agent, Google Antigravity/Gemini. Same contract, different vendor. | [codexloop](https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_runners/codex) · [cursorloop](https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_runners/cursor) · [agyloop](https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_runners/agy) |
| **qwenloop** | The same runner, fully local: Qwen 2.5 Coder 14B through llama.cpp by default or vLLM on NVIDIA. Never downloads weights on its own. | [source](https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_runners/qwen) |
| **vibey** | Queue-based, six-phase conductor for autonomous software delivery on top of the `*loop` runners: spec interview → design pass → build → review → deploy. PostgreSQL-backed. | [PyPI](https://pypi.org/project/vibey/) · [repo](https://github.com/the-vibey-project/vibey) · [docs](https://the-vibey-project.github.io/vibey/main/) |
| **vibey-gh** | Release automation for a GitHub repository, stdlib only: provenance fingerprints, derived version bumps, exact-head AI review and repair, a merge train, dual-channel releases, docs maintenance. | [source](https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_tools/gh) |
| **vibey-bootstrap** | Formerly azure-bootstrap. The Azure Functions cross-cutting layer, solved once — config ↔ App Insights bootstrap cycle, structured logging, Service Bus plumbing, scaffold CLI. Used across 17+ Azure Functions repos. | [source](https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_tools/bootstrap) |
| **vibey-skills** | Formerly vibe-engineering-skills. Claude Code plugin marketplace of Agent Skills across security, cloud, DevSecOps, AI/ML, architecture, QA and more. Every claim cites its source. | [source](https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_tools/skills) |
| **clippy-pet** | An animated paperclip pet for ChatGPT desktop and Codex CLI. Because not everything has to be serious. | [repo](https://github.com/adammatthewsteinberger/clippy-pet) |

More → **[/open-source](https://vibewithadam.matthewsteinberger.com/open-source)**

## Writing

> *"The AI is a commodity. The knowledge is the competitive asset."*

**[Novice to Navigator: Your Guide to AI Chatbots for Business](https://vibewithadam.matthewsteinberger.com/novice-to-navigator)** — plain-English, numerate, no hype. How RAG actually works, what makes chatbots succeed or fail, and how to decide whether your business is ready. The first edition's 33 chapters are free to read; the second edition is in development.

- 📖 [Read the first edition free](https://vibewithadam.matthewsteinberger.com/novice-to-navigator)
- ✅ [15-factor Chatbot Readiness Quiz](https://vibewithadam.matthewsteinberger.com/novice-to-navigator/readiness) — four pillars, ~30 minutes, before you sign a contract
- 🔔 [Get notified when the second edition ships](https://eepurl.com/jiYXCQ)

Also in development: *Engineering Influence* — see **[/books](https://vibewithadam.matthewsteinberger.com/books)**.

**Latest posts**
<!-- BLOG-POST-LIST:START -->
- [Fable 5, Mythos 5, and a 19-Day Pause: What &#39;Mythos-Class&#39; Means for Your RAG Budget](https://vibewithadam.matthewsteinberger.com/blog/claude-fable-5-mythos-5-and-what-mythos-class-means-for-rag) — Aug 14, 2026
- [Microsoft Foundry at Build 2026: What Actually Changes for Azure Architects](https://vibewithadam.matthewsteinberger.com/blog/microsoft-foundry-build-2026-what-changes-for-azure-architects) — Aug 12, 2026
- [MCP Became the REST of Agents. Here&#39;s How I&#39;d Expose a Legacy System to One Safely.](https://vibewithadam.matthewsteinberger.com/blog/mcp-became-the-rest-of-agents-safely-exposing-a-legacy-system) — Aug 10, 2026
- [Astra Solved 10 Open Math Problems for $2,000. ChatGPT Hit 1 Billion Users. Neither Changes the Advice I Give Clients.](https://vibewithadam.matthewsteinberger.com/blog/astra-1-billion-users-and-why-the-knowledge-base-is-the-moat) — Aug 5, 2026
<!-- BLOG-POST-LIST:END -->

## How I work

**Architecture before code. Juniors trained in parallel. Handoffs that hold.** I document as I build for the same reason a RAG pipeline cites its sources: an auditable trail beats a confident guess six months later. That's why the AI Payroll Processor transferred to a junior dev in 45 days instead of becoming someone's permanent second job.

- **Depth on the details that matter** — I find the one row that contradicts the other nine hundred instead of averaging it away
- **Onion Architecture and TDD by default** — 159/159 tests and 85.84% coverage on the GodFocus push system, in 5 billable hours
- **Cross-cutting concerns solved once** — `vibey-bootstrap` is the config/logging/Service Bus layer factored out of 17+ Azure Functions repos
- **Process engineering alongside the code** — Epics → Features → Stories decomposition, so the work stays legible to the people funding it

More → [my story](https://vibewithadam.matthewsteinberger.com/story) · [join me](https://vibewithadam.matthewsteinberger.com/join-me)

## Now

- Building **[vibey](https://github.com/the-vibey-project/vibey)** in the open: 1.0.0 shipped to [PyPI](https://pypi.org/project/vibey/) in September 2026, the conductor and the whole `*loop` family in one MIT-licensed distribution. I'm looking for developers to build it with me → [/join-me](https://vibewithadam.matthewsteinberger.com/join-me)
- Senior Azure & AI Development Engineer, **The Vizius Group**, Sep 2025 – Aug 2026.
- Volunteer software architect for a nonprofit AI apologetics chat platform since Apr 2026 — the AI→human live-chat relay is written up at [/work/project-excite-relay](https://vibewithadam.matthewsteinberger.com/work/project-excite-relay).
- B.A. Computer Science, Skidmore College (2012) · Certified ScrumMaster (2021)

<details>
<summary><strong>Stack at a glance</strong></summary>

- **Languages:** Python · TypeScript/NestJS · C#/.NET · React/Next.js
- **Azure:** Functions · Service Bus · App Configuration · Key Vault · Application Insights · AKS · Bicep
- **Platform:** Docker · Kubernetes · Helm · GitOps · GitHub Actions · Azure DevOps · Bitbucket
- **Data:** PostgreSQL/pgvector · MongoDB · Snowflake · Redis
- **AI:** RAG · vLLM · Ollama · FAISS · LangChain · MCP · Claude · GPT · Gemini · Mistral · LoRA fine-tuning · Grafana/Prometheus for LLM observability
- **Practice:** Onion Architecture · TDD · Scrum (CSM) · process engineering · Jira decomposition (Epics → Features → Stories)

</details>

<details>
<summary><strong>Also comfortable with…</strong></summary>

- Self-hosted services: WordPress, Listmonk/Postfix/OpenDKIM, Matrix/Element, Ghost, bare-metal Ubuntu
- Privacy-first stacks and Big-Tech alternatives (Proton, GrapheneOS, System76, Synology)
- Proof-of-Stake validator operations (ETH2/Rocketpool) and self-custody training

</details>

## Contact

[adam@matthewsteinberger.com](mailto:adam@matthewsteinberger.com) · [LinkedIn](https://www.linkedin.com/in/adammatthewsteinberger/) · [vibewithadam.matthewsteinberger.com](https://vibewithadam.matthewsteinberger.com/) · [RSS](https://vibewithadam.matthewsteinberger.com/feed.xml) · [llms.txt](https://vibewithadam.matthewsteinberger.com/llms.txt)

---

This profile is [CC BY 4.0](LICENSE) · the site behind it is open source: [adammatthewsteinberger/portfolio](https://github.com/adammatthewsteinberger/portfolio) (MIT code, CC BY 4.0 content) · [/join-me](https://vibewithadam.matthewsteinberger.com/join-me)
