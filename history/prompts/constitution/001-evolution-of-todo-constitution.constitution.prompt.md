---
id: "001"
title: "Evolution of Todo Constitution"
stage: "constitution"
date: "2026-01-02"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "master"
user: "human"
command: "/sp.constitution"
labels: ["constitution","governance","spec-driven-development"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - ".specify/memory/constitution.md"
  - "history/prompts/constitution/001-evolution-of-todo-constitution.constitution.prompt.md"
tests: []
---

## Prompt

/sp.constitution

Create a single global constitution for the entire "Evolution of Todo" project

covering Phase I through Phase V.

This constitution must define:

1. Spec-Driven Development as mandatory

- No agent may write code without approved specs and tasks

- All work must follow: Constitution → Specs → Plan → Tasks → Implement

2. Agent Behavior Rules

- No manual coding by humans

- No feature invention

- No deviation from approved specifications

- Refinement must occur at spec level, not code level

3. Phase Governance

- Each phase is strictly scoped by its specification

- Future-phase features must never leak into earlier phases

- Architecture may evolve only through updated specs and plans

4. Technology Constraints

- Python for backend

- Next.js for frontend (later phases)

- FastAPI, SQLModel, Neon DB

- OpenAI Agents SDK, MCP

- Docker, Kubernetes, Kafka, Dapr (later phases)

5. Quality Principles

- Clean architecture

- Stateless services where required

- Clear separation of concerns

- Cloud-native readiness

This constitution must remain stable across all phases

and act as the supreme governing document for all agents.

## Response snapshot

Created comprehensive project constitution at `.specify/memory/constitution.md` covering:

- **Section I**: Spec-Driven Development mandate with artifact chain requirements

- **Section II**: Agent behavior rules with core constraints and response protocols

- **Section III**: Phase governance with scope enforcement and future-phase prohibition

- **Section IV**: Technology constraints (Python, FastAPI, SQLModel, Neon DB, Next.js, OpenAI SDK, MCP, Docker, Kubernetes, Kafka, Dapr)

- **Section V**: Quality principles (clean architecture, cloud-native, testing)

- **Section VI**: Development workflow with artifact chain diagram

- **Section VII**: Governance with constitution supremacy and amendment process

- **Appendix A**: Phase feature matrix showing required features per phase

- **Appendix B**: Technology version floor

## Outcome

- ✅ Impact: Created supreme governing document for "Evolution of Todo" project spanning all 5 phases
- 🧪 Tests: N/A - governance document
- 📁 Files: 1 created (`.specify/memory/constitution.md`)
- 🔁 Next prompts: Begin Phase I specification
- 🧠 Reflection: Constitution establishes clear guardrails for all future development work

## Evaluation notes (flywheel)

- Failure modes observed: "none"
- Graders run and results (PASS/FAIL): "N/A - governance document"
- Prompt variant (if applicable): "none"
- Next experiment (smallest change to try): "N/A"
