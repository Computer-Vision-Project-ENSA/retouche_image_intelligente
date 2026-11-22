# Jira Import Guide & Translated Project Roadmap
**Project:** Intelligent Image Retouching (AI-Powered Object Removal & Generative Inpainting)  
**Jira Key:** `RDI`  
**Generated Files:**
* CSV Import File: [`jira_import_roadmap.csv`](../jira_import_roadmap.csv)
* JSON Companion File: [`jira_import_roadmap.json`](../jira_import_roadmap.json)

---

## 1. Executive Summary & English Translation of Roadmap

| Original Roadmap Phase (FR) | English Translated Epic | Issue Type | Items Count |
| :--- | :--- | :--- | :--- |
| **1- Setup DevOps tools** | **Epic 1: Setup DevOps & MLOps Infrastructure** | `Epic` | 8 Tasks/Research |
| **2- Setup Dataset** | **Epic 2: Dataset Preparation & Preprocessing** | `Epic` | 5 Tasks/Research |
| **3- Part 1 : Object Mask Generation** | **Epic 3: Part 1 - Object Mask Generation & Segmentation** | `Epic` | 4 Tasks/Research + 1 Bug |
| **4- Part 2 : Generative Inpainting** | **Epic 4: Part 2 - Generative Inpainting & Reconstruction** | `Epic` | 4 Tasks/Research + 1 Bug |
| **5- General Pipeline Evaluation** | **Epic 5: General Pipeline Evaluation & Integration** | `Epic` | 4 Tasks/Research |
| **6- Web Interface** | **Epic 6: Web Interface & Platform Deployment** | `Epic` | 2 Tasks + 1 Bug |
| **7- Rapport du projet** | **Epic 7: Project Documentation & Reporting** | `Epic` | 3 Tasks/Research |

**Total Issues Configured:** **40 issues** (7 Epics, 21 Tasks, 9 Research, 3 Bugs).

---

## 2. Issue Types Mapping

According to your Jira project configuration:
* **`Epic` (7):** Major functional tracks and milestones covering the 7 phases of the roadmap.
* **`Research` (9):** Theoretical studies, literature surveys, EDA, benchmarking experiments, metric definitions, and architecture selection.
* **`Task` (21):** Concrete implementation, configuration, engineering pipelines, optimization, and documentation activities.
* **`Bug` (3):** Identified real-world edge-case defects (e.g., mask shadow boundary leakage, inpainting seam texture discontinuity, canvas click coordinate scaling on high-DPI displays).

---

## 3. Step-by-Step Jira CSV Import Instructions

### Step 1: Open External System Import in Jira
1. Log into your Jira account.
2. In Jira Cloud:
   - Click the **Gear icon (Settings)** at the top right $\to$ **System**.
   - Under *Import and Export*, select **External System Import**.
   - Choose **CSV**.
   *(Alternatively, in team-managed projects, go to your Project $\to$ **Project Settings** or click `...` on the backlog $\to$ **Import issues**).*
3. In Jira Server / Data Center:
   - Click **Settings** $\to$ **System** $\to$ **External System Import** $\to$ **CSV**.

### Step 2: Upload the CSV File
1. Click **Choose File** and select:
   `d:\9raya\IID3\Computer Vision\Project\retouche_image_intelligente\jira_import_roadmap.csv`
2. Leave **File encoding** as `UTF-8` (the file is formatted with UTF-8 BOM for automatic recognition).
3. Leave **CSV Delimiter** as `,` (comma).
4. Click **Next**.

### Step 3: Select Project
1. Choose your target project (e.g., `Retouche d'image intelligente (RDI)`).
2. If prompted, select or confirm the project key and lead.
3. Click **Next**.

### Step 4: Map Fields
Map the CSV column headers to their corresponding Jira fields:

| CSV Column Header | Jira Target Field | Notes |
| :--- | :--- | :--- |
| `Issue ID` | **Issue Id** | Essential for parent-child linking and issue dependencies |
| `Issue Type` | **Issue Type** | Will map to Epic, Task, Research, Bug |
| `Summary` | **Summary** | Issue title |
| `Description` | **Description** | Detailed objectives, deliverables, and acceptance criteria |
| `Epic Name` | **Epic Name** | Used by Jira Software for Epics |
| `Epic Link` | **Epic Link** | Links child issues to their parent Epic |
| `Parent ID` | **Parent / Parent ID** | Used for Team-Managed / Next-Gen Jira projects |
| `Priority` | **Priority** | High, Medium, Low |
| `Labels` | **Labels** | Pre-tagged for easy filtering |
| `Outward issue link (blocks)` | **Outward issue link (blocks)** | Dependency link |
| `Inward issue link (is blocked by)` | **Inward issue link (is blocked by)** | Dependency link |

### Step 5: Map Values & Run Import
1. Confirm value mapping:
   - `Epic` $\to$ `Epic`
   - `Task` $\to$ `Task`
   - `Research` $\to$ `Research` *(if your Jira uses `Spike` or `Task` instead of `Research`, map it accordingly)*
   - `Bug` $\to$ `Bug`
2. Click **Begin Import**.
3. Jira will import all 40 elements and automatically wire the parent-child relationships and dependency links!
