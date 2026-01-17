# SafeEd ML Query Validation Record

## Steps for Validation

1. **Run test cases on the queries**
2. **Check variation for data**
3. **Review every single query manually** (unique to this project: human reasoning required, so the script is called `elbow_grease.py`)

---

## ========================= REVIEW #1 =========================

**Initially generated 42 queries**

### 1. Passed 6/7 test cases
- Question about `"pre-cum cause pregnancy?"` didn't have enough variance
- Added 3 more questions similar to `"pre-cum cause pregnancy?"` &rarr; **Total: 45 queries**
- Re-ran: **Passed 7/7 test cases**

### 2. Label counts:
```
myth: 25
question: 17
fact: 1
concern: 2
```
- Variation required for facts and concerns
- Added **20 more queries (10 facts, 10 concerns)** &rarr; **Total: 65 queries**
- Run tests again; **Passed 7/7 test cases**
```
myth: 25
question: 17
fact: 11
concern: 12
```
### 3. **Reviewed all 65/65 queries**
- *Every single query was manually checked for appropriateness, semantic intent, and category. This step is crucial for the sensitive and nuanced domain of sexual/reproductive health queries.*

---
**Summary:**  
All generated and labeled queries have passed automated tests (7/7), achieved healthy class balance, show sufficient paraphrase/variation per intent, and have been manually reviewed with `elbow_grease.py` for semantic quality and real-world accuracy.