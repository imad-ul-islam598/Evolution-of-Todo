# Evolution of Todo - Project Constitution

> **Supreme Governing Document** - All agents, humans, and processes must adhere to these principles.

## I. Spec-Driven Development (Mandatory)

### 1.1 No Code Without Approved Artifacts
- **No agent may write code** without approved specifications and tasks
- **No human may write code** manually; all implementation follows agent-mediated workflows
- Work must flow through the mandated sequence:
  ```
  Constitution → Specs → Plan → Tasks → Implement → Review
  ```

### 1.2 Artifact Requirements
- **Specifications (`specs/<feature>/spec.md`)**: Define WHAT, not HOW
- **Plans (`specs/<feature>/plan.md`)**: Define architecture and interfaces
- **Tasks (`specs/<feature>/tasks.md`)**: Define testable implementation steps
- Each artifact requires explicit approval before proceeding

### 1.3 Enforcement
- Implementation commits without corresponding approved artifacts are prohibited
- Code review must verify artifact chain completeness

## II. Agent Behavior Rules

### 2.1 Core Constraints
| Rule | Enforcement |
|------|-------------|
| No manual coding by humans | All code via agent tools |
| No feature invention | Scope strictly per spec |
| No spec deviation | Approved specs are binding |
| Refinement at spec level | Never "fix" in code |

### 2.2 Response Protocol
When encountering ambiguity:
1. **Stop** - Do not assume
2. **Surface** - Present options with tradeoffs
3. **Escalate** - Request human clarification
4. **Document** - Capture decision in PHR

### 2.3 Execution Mandate
- Use MCP tools for all information gathering
- Use CLI commands for verification
- Never rely solely on internal knowledge
- Verify before acting

## III. Phase Governance

### 3.1 Phase Scope Enforcement
| Phase | Scope | Forbidden |
|-------|-------|-----------|
| Phase I | Console-based todo app | Any Phase II+ features |
| Phase II | Web API + minimal UI | Phase III+ orchestration |
| Phase III | AI Agent integration | Phase IV+ scaling |
| Phase IV | Multi-agent system | Phase V+ deployment |
| Phase V | Production deployment | Feature creep |

### 3.2 Future-Phase Prohibition
- **No future-phase code** may exist in current phase branches
- No "pre-positioning" of infrastructure for later phases
- Architecture evolves only through updated specs and plans

### 3.3 Phase Transitions
- Each phase requires complete, tested implementation
- Phase gates: All tasks complete → Tests passing → Human approval → Next phase

## IV. Technology Constraints

### 4.1 Mandated Stack (Phase I-II)
| Layer | Technology | Notes |
|-------|------------|-------|
| Backend | Python | Core implementation |
| API Framework | FastAPI | REST interface |
| Data Layer | SQLModel | ORM with type safety |
| Database | Neon DB | Serverless PostgreSQL |
| AI Integration | OpenAI Agents SDK | Agent orchestration |
| Integration | MCP | Model Context Protocol |

### 4.2 Future Stack (Phase III-V)
| Layer | Technology | Phase |
|-------|------------|-------|
| Frontend | Next.js | Phase III+ |
| Containerization | Docker | Phase IV+ |
| Orchestration | Kubernetes | Phase V |
| Event Bus | Kafka | Phase IV+ |
| Distributed State | Dapr | Phase IV+ |

### 4.3 Stack Compliance
- All code must use mandated technologies only
- New dependencies require spec amendment and approval
- No technology substitutions without documented rationale

## V. Quality Principles

### 5.1 Architectural Standards
| Principle | Requirement |
|-----------|-------------|
| Clean Architecture | Separation of concerns at all layers |
| Stateless Services | Where required by design |
| Cloud-Native Ready | 12-factor app principles |
| Testable | Pure functions, injectable dependencies |
| Observable | Structured logging, metrics hooks |

### 5.2 Code Quality
- Type annotations on all public interfaces
- Docstrings for all public modules, classes, functions
- No magic numbers or hardcoded values
- Configuration via environment variables
- Secrets never in source control

### 5.3 Testing Requirements
- Unit tests for all business logic
- Integration tests for API contracts
- Test coverage: minimum 80% on core paths
- Tests must be deterministic and fast

## VI. Development Workflow

### 6.1 Artifact Chain
```
User Request
    ↓
Clarification (if ambiguous)
    ↓
Specification (spec.md) ← Human Approved
    ↓
Plan (plan.md) ← Human Approved
    ↓
Tasks (tasks.md) ← Human Approved
    ↓
Implementation (Red-Green-Refactor)
    ↓
Review & Merge
```

### 6.2 PHR Requirements
- Every user input recorded in `history/prompts/`
- Constitution-level: `history/prompts/constitution/`
- Feature-level: `history/prompts/<feature-name>/`
- General: `history/prompts/general/`

### 6.3 ADR Triggers
Suggest ADR when ALL true:
1. Long-term architectural consequence
2. Multiple viable alternatives considered
3. Cross-cutting concern

## VII. Governance

### 7.1 Constitution Supremacy
- This document is the **supreme governing document**
- All other practices, conventions, and preferences are subordinate
- Conflicts resolve in favor of this constitution

### 7.2 Amendment Process
| Change Type | Process |
|-------------|---------|
| Minor clarifications | Agent update + PHR |
| New principles | Human approval required |
| Technology changes | ADR + Human approval |
| Structural changes | Full review cycle |

### 7.3 Compliance Verification
- All PRs must verify constitution compliance
- Code reviews must check artifact chain
- Complexity must be justified in plan or ADR

---

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02

---

## Appendix A: Phase Feature Matrix

| Feature | Phase I | Phase II | Phase III | Phase IV | Phase V |
|---------|---------|----------|-----------|----------|---------|
| Console CRUD | Required | - | - | - | - |
| In-memory storage | Required | - | - | - | - |
| FastAPI REST | - | Required | - | - | - |
| Neon DB persistence | - | Required | - | - | - |
| Next.js frontend | - | - | Required | - | - |
| AI Agent (OpenAI) | - | - | Required | - | - |
| MCP integration | - | - | Required | - | - |
| Multi-agent system | - | - | - | Required | - |
| Docker/Kubernetes | - | - | - | - | Required |
| Kafka/Dapr | - | - | - | - | Required |

## Appendix B: Technology Version Floor

| Technology | Minimum Version |
|------------|-----------------|
| Python | 3.11+ |
| FastAPI | 0.109+ |
| SQLModel | 0.0+ |
| Next.js | 14+ |
| OpenAI SDK | 1.0+ |
