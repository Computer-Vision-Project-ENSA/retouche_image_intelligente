# Datasets Documentation: Object Segmentation & Inpainting

This document describes, compares, and evaluates all datasets in `ml/data/docs/` for our project: **Suppression Intelligente d'Objets (Intelligent Object Removal)**.

---

## 1. Project Context & Pipeline

Our goal is to erase unwanted objects from photos cleanly. The system works in two stages:

```
                  ┌──────────────────────┐
                  │     Input Image      │
                  └──────────┬───────────┘
                             │
                             ▼
              [Stage 1: Interactive Segmentation]
                  Model: SAM (Segment Anything)
                  User clicks on an object ──> Binary Mask
                             │
                             ▼
                  [Stage 2: Image Inpainting]
                  Model: LaMa (or OpenCV Telea baseline)
                  Fills the masked area ──> Clean Image
                             │
                             ▼
                  ┌──────────────────────┐
                  │    Restored Image    │
                  └──────────────────────┘
```

---

## 2. Comparison Tables

### Table 1: Field / Column Availability Across Datasets

This table shows which fields/metadata each dataset contains (`✓` = present, `✗` = absent):

| Dataset | `image` | `image_id` | `width` / `height` | `bbox` | `category` / `label` | `segmentation` (poly/RLE) | `mask` (image) | `area` | `target_img` | `instruction` | `point_coords` | `stability_score` | `neg_category_ids` | `coco_url` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **COCO** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ *(derived)* | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| **LVIS** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ *(derived)* | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| **MagicBrush** | ✓ *(source_img)* | ✓ *(img_id)* | ✗ *(in PIL)* | ✗ | ✗ | ✗ | ✓ *(mask_img)* | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| **Open Images** | ✓ *(filepath)* | ✓ *(id)* | ✓ | ✓ | ✓ | ✓ | ✗ *(derived)* | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ *(neg_labels)* | ✗ |
| **PIPE_Mask** | ✗ *(mask only)* | ✓ *(img_id)* | ✗ *(fixed 512)* | ✗ | ✗ | ✗ | ✓ *(mask)* | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Places2** | ✓ | ✗ *(filename)* | ✗ *(in PIL)* | ✗ | ✓ *(scene)* | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **SA-1B** | ✓ | ✓ | ✓ | ✓ | ✗ *(class-agnostic)* | ✓ *(RLE)* | ✗ *(derived)* | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ | ✗ |

---

### Table 2: Source URLs, Full Dataset Download & Size Comparison

| Dataset | Source Used for Analysis (URL) | Where to Get Full Dataset Later (URL) | Full Dataset Size |
| :--- | :--- | :--- | :--- |
| **COCO (2017)** | Hugging Face: [`detection-datasets/coco`](https://huggingface.co/datasets/detection-datasets/coco) & FiftyOne `coco-2017` | Official COCO Page: [https://cocodataset.org/#download](https://cocodataset.org/#download) | **~27 GB** compressed (~118k train + 5k val + 41k test images = ~164k images; annotations ~241 MB) |
| **LVIS (v1.0)** | Local validation JSON: `lvis_v1_val.json` + COCO image URLs | Official LVIS Page: [https://www.lvisdataset.org/dataset](https://www.lvisdataset.org/dataset) | **~21 GB** total (~180 MB compressed JSON annotations + ~20 GB shared COCO 2017 train/val images) |
| **MagicBrush** | Hugging Face: [`osunlp/MagicBrush`](https://huggingface.co/datasets/osunlp/MagicBrush) | Hugging Face: [https://huggingface.co/datasets/osunlp/MagicBrush](https://huggingface.co/datasets/osunlp/MagicBrush) & [GitHub](https://github.com/OSU-NLP-Group/MagicBrush) | **~10.5 GB** compressed (~10,388 editing turns with source image, mask, instruction, target image) |
| **Open Images (v7)** | FiftyOne Zoo: `open-images-v7` validation sample | Google Open Images: [https://storage.googleapis.com/openimages/web/index.html](https://storage.googleapis.com/openimages/web/index.html) | **~500 GB to 1 TB** for full 9M images; validation split alone is **~12 GB** (41,620 images); masks zip is **~10 GB** |
| **PIPE_Mask** | Hugging Face: [`paint-by-inpaint/PIPE_Masks`](https://huggingface.co/datasets/paint-by-inpaint/PIPE_Masks) | Hugging Face: [https://huggingface.co/datasets/paint-by-inpaint/PIPE_Masks](https://huggingface.co/datasets/paint-by-inpaint/PIPE_Masks) | **~4 GB** download (888,230 binary inpainting masks in Parquet format) |
| **Places2** | MIT CSAIL Server: [`val_large.tar`](http://data.csail.mit.edu/places/places365/val_large.tar) + [`filelists`](http://data.csail.mit.edu/places/places365/filelist_places365-standard.tar) | Official MIT Places2 Page: [http://places2.cs.ailab.mit.edu/download.html](http://places2.cs.ailab.mit.edu/download.html) | **~120 GB** for Places365-Standard High-Res (1.8M images: ~105 GB train + ~14 GB val); **~26 GB** for 256x256; **>400 GB** for full Places2 challenge |
| **SA-1B** | Hugging Face: [`hdtech/SA-1B`](https://huggingface.co/datasets/hdtech/SA-1B) (streaming `train`) | Official Meta AI Portal: [https://ai.meta.com/datasets/segment-anything/](https://ai.meta.com/datasets/segment-anything/) or [Hugging Face](https://huggingface.co/datasets/hdtech/SA-1B) | **~10 to 11 Terabytes (TB)** across 1,000 tar shards (11M images, 1.1B masks; ~10–11 GB per shard) |

---

### Table 3: Pipeline Role, Strengths & Limitations

| Dataset | Role in Our Pipeline | Pipeline Stage | Key Strength | Main Limitation |
| :--- | :--- | :--- | :--- | :--- |
| **COCO** | Standard benchmark | Segmentation (SAM) | Easy to stream, lightweight, standard 80 classes. | Only 80 common classes; polygon masks can be coarse. |
| **LVIS** | Long-tail stress test | Segmentation (SAM) | 1,203 categories, high-precision object boundaries. | Large JSON annotation file (~350 MB validation). |
| **MagicBrush** | Ground-truth benchmark | End-to-End Pipeline | Contains paired `(source, mask, target)` before/after photos. | Limited to ~10k samples; edits vary in scope. |
| **Open Images** | Diversity evaluation | Segmentation & Inpainting | Huge scale, rich real-life scene diversity. | Very large dataset; requires selective filtering via FiftyOne. |
| **PIPE_Mask** | Realistic mask supply | Inpainting (LaMa / Telea) | 888k ready-to-use realistic object masks. | Masks only; must link to parent images for full context. |
| **Places2** | Scene texture benchmark | Inpainting (LaMa) | Academic gold standard for inpainting evaluation. | Scene backgrounds only; does not provide object masks. |
| **SA-1B** | Reference foundation | Segmentation (SAM) | Unmatched quality and volume of masks with click points. | Massive download size (>10 TB); class-agnostic only. |

---

## 3. Detailed Dataset Descriptions

### 1. COCO (Common Objects in Context)
- **Source Used for Analysis:** Hugging Face [`detection-datasets/coco`](https://huggingface.co/datasets/detection-datasets/coco) (streaming train split) & FiftyOne `coco-2017`.
- **Where to Get Full Dataset Later:** [https://cocodataset.org/#download](https://cocodataset.org/#download) (Train 19 GB, Val 1 GB, Annotations 241 MB).
- **Full Dataset Size:** ~27 GB compressed (~164k images total).
- **Description:** The most popular computer vision benchmark for object detection and instance segmentation.
- **Key Columns:** `image_id`, `image`, `width`, `height`, `objects` (`bbox_id`, `category`, `bbox`, `area`).
- **Verdict for Project:** **Essential.** Fast to stream and prototype. Perfect for verifying that SAM generates sharp masks on standard everyday objects (person, car, animal, furniture).

---

### 2. LVIS (Large Vocabulary Instance Segmentation)
- **Source Used for Analysis:** Local validation JSON (`lvis_v1_val.json`) from LVIS v1.0 paired with COCO image URLs.
- **Where to Get Full Dataset Later:** [https://www.lvisdataset.org/dataset](https://www.lvisdataset.org/dataset) (Annotations: train ~150 MB, val ~30 MB; Images: shared with COCO 2017).
- **Full Dataset Size:** ~21 GB total (annotations ~180 MB compressed + COCO train/val images ~20 GB).
- **Description:** An extension of COCO that re-annotates images with 1,203 categories in a long-tail distribution (rare `r`, common `c`, frequent `f`).
- **Key Tables:** `images` (metadata, URLs), `annotations` (`bbox` `[x, y, w, h]`, `area`, `segmentation` polygons), `categories` (names, synsets, frequency).
- **Verdict for Project:** **Highly Recommended.** Tests SAM's zero-shot segmentation on rare, complex, and small objects with detailed polygon boundaries.

---

### 3. MagicBrush
- **Source Used for Analysis:** Hugging Face [`osunlp/MagicBrush`](https://huggingface.co/datasets/osunlp/MagicBrush) (streaming `dev` split).
- **Where to Get Full Dataset Later:** [https://huggingface.co/datasets/osunlp/MagicBrush](https://huggingface.co/datasets/osunlp/MagicBrush) & [GitHub](https://github.com/OSU-NLP-Group/MagicBrush).
- **Full Dataset Size:** ~10.5 GB compressed (10,388 editing pairs).
- **Description:** The first real-world dataset specifically designed for instruction-guided image editing with local modifications.
- **Key Columns:** `source_img` (original), `mask_img` (binary edit area), `instruction` (text prompt), `target_img` (ground-truth edited photo).
- **Verdict for Project:** **Top Choice for End-to-End Evaluation.** Because it provides both the input photo and the true edited result photo, we can directly compute image fidelity metrics (PSNR, SSIM, LPIPS) on our inpainting outputs.

---

### 4. Open Images (v7)
- **Source Used for Analysis:** FiftyOne Dataset Zoo (`open-images-v7`, validation split sample).
- **Where to Get Full Dataset Later:** [https://storage.googleapis.com/openimages/web/index.html](https://storage.googleapis.com/openimages/web/index.html) or via FiftyOne `foz.load_zoo_dataset("open-images-v7")`.
- **Full Dataset Size:** ~500 GB to 1 TB for full 9M images; validation split alone is ~12 GB (41,620 images); segmentation masks zip is ~10 GB.
- **Description:** Google's massive dataset with 9 million images, 16M bounding boxes, and 2.8M segmentation masks across 350+ object classes.
- **Key Fields:** `filepath`, `ground_truth` (bboxes), `segmentations` (polygons/bitmaps), `positive_labels`, `negative_labels`.
- **Verdict for Project:** **Optional / Secondary.** Great for finding challenging test cases across complex scenes, but too large for everyday prototyping.

---

### 5. PIPE_Mask (Paint-by-Inpaint Masks)
- **Source Used for Analysis:** Hugging Face [`paint-by-inpaint/PIPE_Masks`](https://huggingface.co/datasets/paint-by-inpaint/PIPE_Masks).
- **Where to Get Full Dataset Later:** [https://huggingface.co/datasets/paint-by-inpaint/PIPE_Masks](https://huggingface.co/datasets/paint-by-inpaint/PIPE_Masks).
- **Full Dataset Size:** ~4 GB (888,230 binary inpainting masks in Parquet format).
- **Description:** A dedicated collection of 888,230 binary inpainting masks derived from COCO (25.9%) and Open Images (74.1%).
- **Key Columns:** `mask` ($512 \times 512$ grayscale image), `target_img_dataset` (`'COCO'` or `'OpenImages'`), `img_id`, `ann_id`.
- **Verdict for Project:** **Very Useful for Inpainting Testing.** Provides realistic object-shaped masks to test LaMa or OpenCV Telea inpainting without having to generate masks manually.

---

### 6. Places2
- **Source Used for Analysis:** MIT CSAIL Server: [`val_large.tar`](http://data.csail.mit.edu/places/places365/val_large.tar) and category lists [`filelist_places365-standard.tar`](http://data.csail.mit.edu/places/places365/filelist_places365-standard.tar).
- **Where to Get Full Dataset Later:** [http://places2.cs.ailab.mit.edu/download.html](http://places2.cs.ailab.mit.edu/download.html).
- **Full Dataset Size:** Places365-Standard High-Res: ~120 GB (~105 GB train + ~14 GB val, 1.8M images); Places365-Standard 256x256: ~26 GB; Full Places2 Challenge: >400 GB (10M images).
- **Description:** Over 10 million scene photographs (indoor and outdoor) across 400+ scene categories (kitchen, office, street, nature, etc.).
- **Key Fields:** `image` (high-resolution photo), `label` (scene category name).
- **Verdict for Project:** **Inpainting Benchmark Standard.** The LaMa paper and other deep inpainting models use Places2 scenes to prove they can reconstruct complex natural backgrounds and textures.

---

### 7. SA-1B (Segment Anything 1-Billion)
- **Source Used for Analysis:** Hugging Face mirror [`hdtech/SA-1B`](https://huggingface.co/datasets/hdtech/SA-1B) (streaming `train` split).
- **Where to Get Full Dataset Later:** [https://ai.meta.com/datasets/segment-anything/](https://ai.meta.com/datasets/segment-anything/) or [https://huggingface.co/datasets/hdtech/SA-1B](https://huggingface.co/datasets/hdtech/SA-1B).
- **Full Dataset Size:** **~10 to 11 Terabytes (TB)** across 1,000 tar shards (11M images, 1.1B masks; ~10–11 GB per shard).
- **Description:** The massive dataset created by Meta AI to train SAM, containing 11 million licensed images and 1.1 billion class-agnostic masks with click point prompts.
- **Key Fields:** `image`, `annotations` (`bbox`, `area`, `segmentation` RLE, `point_coords`, `stability_score`).
- **Verdict for Project:** **Reference Model Origin.** We do not need to download the full 10 TB dataset. It serves as the reference foundation explaining SAM's zero-shot click-segmentation performance.

---

## 4. Final Recommendations for Our Project

1. **For Segmentation Validation (SAM):**
   - Use **COCO** for baseline testing on standard everyday objects (people, vehicles, furniture).
   - Use **LVIS** to test challenging, small, and fine-grained objects with complex silhouettes.

2. **For Inpainting Evaluation (LaMa vs. Telea):**
   - Use **PIPE_Mask** paired with COCO images to test inpainting on realistic object holes.
   - Use **Places2** sample scenes to test background texture restoration on complex natural scenes.

3. **For End-to-End System Evaluation (SAM + Inpainting):**
   - Use **MagicBrush** samples that have object removal instructions. We can run our full pipeline on `source_img` and directly compare our inpainting output against `target_img` using PSNR and SSIM.
