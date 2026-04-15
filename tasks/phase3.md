# Phase 3 — Finance Pack and Source-Linked Analysis

## Goal

Deliver a finance analysis pack that is read/analyze/draft only.

## Deliverables

- finance domain pack
- CSV/XLSX/PDF ingestion
- reconciliation assistant workflows
- source-linked report artifacts
- optional model compare mode for high-stakes outputs

## Non-goals

- accounting writes
- payments
- journal posting

## Tasks

### P3-001 Finance domain pack
- [ ] Register finance subgraph
- [ ] Bind finance retrieval and memory scopes
- [ ] Acceptance:
  - [ ] finance workflows are isolated from personal and Odoo packs

### P3-002 Spreadsheet ingestion plugin
- [ ] Add CSV/XLSX parser with typed artifact normalization
- [ ] Acceptance:
  - [ ] tabular artifacts preserve source file metadata and sheet names

### P3-003 PDF finance ingestion plugin
- [ ] Add PDF extraction flow for invoices/statements/reports
- [ ] Acceptance:
  - [ ] extracted text includes source references per page

### P3-004 Reconciliation draft workflow
- [ ] Build workflow for matching records across sources without mutating accounting truth
- [ ] Acceptance:
  - [ ] output is a draft reconciliation artifact only

### P3-005 Source-linked reporting renderer
- [ ] Add renderer that includes calculation inputs and source references
- [ ] Acceptance:
  - [ ] output includes enough metadata to trace each major figure

### P3-006 Finance risk policy
- [ ] Enforce finance write prohibition in v1
- [ ] Acceptance:
  - [ ] any attempt to invoke finance write capability is blocked at policy layer

### P3-007 Compare-mode integration
- [ ] Allow finance workflows to use manual compare or fallback-on-low-confidence via LLM gateway
- [ ] Acceptance:
  - [ ] provider comparison metadata is attached to the run

### P3-008 Finance tests
- [ ] Add tests for ingestion, reporting, blocked writes, and compare mode routing
- [ ] Acceptance:
  - [ ] green finance suite

## Exit gate

- finance pack can ingest source docs
- outputs are source-linked
- finance writes are blocked
