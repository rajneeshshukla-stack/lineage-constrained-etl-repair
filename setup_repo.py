import os

project_dir = "lineage-constrained-etl-repair"

dirs = [
    "config",
    "data/raw",
    "data/processed",
    "data/scenarios/01_column_addition",
    "data/scenarios/02_column_renaming",
    "data/scenarios/03_column_removal",
    "data/scenarios/04_datatype_evolution",
    "data/scenarios/05_nullability_evolution",
    "data/scenarios/06_joinkey_evolution",
    "data/scenarios/07_multiple_changes",
    "src/contracts",
    "src/lineage",
    "src/repair",
    "src/verifiers",
    "src/utils",
    "experiments",
    "docs/figures",
    "paper"
]

files = [
    "README.md", "requirements.txt", "setup.py",
    "config/default_config.yaml", "config/thresholds.yaml",
    "data/raw/README.md", "data/processed/README.md",
    "data/scenarios/01_column_addition/README.md",
    "data/scenarios/02_column_renaming/README.md",
    "data/scenarios/03_column_removal/README.md",
    "data/scenarios/04_datatype_evolution/README.md",
    "data/scenarios/05_nullability_evolution/README.md",
    "data/scenarios/06_joinkey_evolution/README.md",
    "data/scenarios/07_multiple_changes/README.md",
    "src/__init__.py", "src/contracts/__init__.py", "src/contracts/base_contract.py",
    "src/contracts/schema_contracts.py", "src/contracts/type_contracts.py",
    "src/contracts/null_contracts.py", "src/contracts/referential_contracts.py",
    "src/contracts/contract_evaluator.py", "src/lineage/__init__.py",
    "src/lineage/dag_builder.py", "src/lineage/lineage_tracker.py",
    "src/lineage/failure_localizer.py", "src/repair/__init__.py",
    "src/repair/candidate_generator.py", "src/repair/repair_ranker.py",
    "src/repair/repair_executor.py", "src/verifiers/__init__.py",
    "src/verifiers/duplicate_check.sql", "src/verifiers/referential_check.sql",
    "src/verifiers/nullability_check.sql", "src/verifiers/domain_check.sql",
    "src/verifiers/sql_verifier_runner.py", "src/utils/__init__.py",
    "src/utils/logger.py", "src/utils/metrics_calculator.py",
    "experiments/__init__.py", "experiments/run_baseline.py",
    "experiments/run_scenarios.py", "experiments/run_unconstrained_baseline.py",
    "experiments/run_ablation.py", "experiments/statistical_tests.py",
    "docs/architecture.md", "docs/figures/README.md",
    "paper/references.bib", "paper/README.md"
]

# Create all folders
for d in dirs:
    os.makedirs(os.path.join(project_dir, d), exist_ok=True)

# Create all files
for f in files:
    path = os.path.join(project_dir, f)
    if not os.path.exists(path):
        with open(path, "w") as fp:
            pass

print("Project folder structure successfully created!")