# 🕵️ Fiscal Secrets - Writeup

---

> **Name:** Fiscal Secrets  
> **Category:** Forensics  
> **Points:** 🟧 Medium  
> **Author:** Usman Ibrahim  
> **Flag Format:** `RDX{...}`

---

The NSA's Q4 financial report seems like an ordinary document, but insiders suspect something more… encrypted. Your task is to uncover hidden data within this PDF and extract the full flag.

---

## 📁 Files Provided

- `NSA_Q4_Report_Confidential.pdf`

---

## 🕵️ Walkthrough

---

### 🟠 **Step 1: Inspect the PDF for Clues**

Run `exiftool` to check for metadata and hidden hints:

```bash
exiftool NSA_Q4_Report_Confidential.pdf
```

**Output:**
```
Author   : NSA Ops
Title    : Quarterly Financial Report
Keywords : xor_key:CTF2025
Subject  : Confidential Information
```

> **Clue Found:**  
> `xor_key:CTF2025` in the Keywords field.

---

### 🟠 **Step 2: Extract Embedded Files from the PDF**

Use `pdfdetach` to extract all embedded files:

```bash
pdfdetach -saveall NSA_Q4_Report_Confidential.pdf
```

**Extracted Files:**
- `budget_report.xls` — Looks harmless but hides something.
- `hidden_data.bin` — Binary blob that’s likely encrypted.

---

### 🟠 **Step 3: Search for Flag Fragments in the Excel File**

Use `grep` to look for flag patterns:

```bash
grep -o 'RDX{[^}]*' budget_report.xls
```

**Result:**
```
RDX{Could_You
```

---

### 🟠 **Step 4: Decrypt the Hidden Binary File**

Use the XOR key found earlier to decrypt `hidden_data.bin`:

```python
# xor_decrypt.py
def xor_bytes(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

with open("hidden_data.bin", "rb") as f:
    encrypted = f.read()

key = b"CTF2025"
decrypted = xor_bytes(encrypted, key)

with open("recovered_flag.zip", "wb") as f:
    f.write(decrypted)
```

After running the script, you get `recovered_flag.zip`.

---

### 🟠 **Step 5: Extract and Decrypt the Second Flag Part**

Unzip `recovered_flag.zip` to get `part2_encrypted.bin`, then decrypt it:

```python
# decrypt_flag.py
def xor_bytes(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

with open("part2_encrypted.bin", "rb") as f:
    encrypted = f.read()

key = b"CTF2025"
decrypted = xor_bytes(encrypted, key)

print(decrypted.decode())
```

**Output:**
```
_Believe_That}
```

---

### 🏁 **Final Flag**

Combine both parts to get the full flag:

```
RDX{Could_You_Believe_That}
```

---

✅ **Flag:** `RDX{Could_You_Believe_That}`

