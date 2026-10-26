# Lineage-Constrained Autonomous Repair of Schema-Evolving ETL Pipelines Using Executable Data Contracts and SQL Verifiers

This repository contains the official implementation, experimental benchmarks, and dataset configurations for the paper:

> **Lineage-Constrained Autonomous Repair of Schema-Evolving ETL Pipelines Using Executable Data Contracts and SQL Verifiers**  
> **Authors:** Tejaskumar Patel, Praveen Kumar Sharma, Rajneesh Shukla  
> **ORCID:** [0009-0008-3618-192X](https://orcid.org/0009-0008-3618-192X)

---

##  Abstract

Schema modifications in source systems can cause silent semantic defects and execution failures in downstream ETL pipelines. This repository implements an autonomous, lineage-constrained pipeline repair framework that:
1. Detects schema evolution events using **Executable Data Contracts**.
2. Traces contract violations back through the **ETL Lineage Graph** to localize affected transformation subgraphs.
3. Generates and ranks candidate repairs based on contract compliance, lineage preservation, output quality, repair complexity, and downstream impact.
4. Validates candidate transformations using independent **SQL Verifiers** (checking uniqueness, referential integrity, nullability, and domain constraints) before committing.

---

##  Repository Structure

```text
├── config/                  # Thresholds and multi-objective scoring weights
├── data/                    # Baseline schemas and 70 schema-evolution scenarios
├── src/
│   ├── contracts/           # Executable data contract evaluation engine (Eq. 7-12)
│   ├── lineage/             # ETL DAG builder and failure localization (FL score)
│   ├── repair/              # Lineage-constrained repair generator and ranker (Algorithm 1)
│   ├── verifiers/           # SQL verification layer (Uniqueness, FK, Nullability, Domain)
│   └── utils/               # Metrics evaluation (CSR, SVR, RSR, LP, RP, MTTR)
├── experiments/             # Benchmark execution scripts and ablation study
├── docs/                    # Architecture diagrams and system documentation
└── paper/                   # Preprint manuscript and reference files