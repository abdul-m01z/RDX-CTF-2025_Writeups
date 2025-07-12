## 📂 LogQuest - Writeup

**Author**:Usman Ibrahim
**Category**: Forensics  
**Difficulty**: Medium 
**File**: `LogQuest.evtx`  
**Flag Format**: `RDX{...}`

## 📝 Description

> **“Log files tell stories—if you know how to read them.”**

On **June 19, 2025**, a series of suspicious account activities occurred on a Windows system. Several accounts were created, passwords were reset, and some users were deleted—multiple times. It's your job to comb through the provided Windows Security Event Logs and reconstruct the timeline.

Your task is to investigate the security logs to answer key forensic questions and generate a flag.

---

## 📁 Files Provided

* **`LogQuest.evtx`**
  Windows Security Event Log file containing 1 day’s worth of user-related activity.

You can open this `.evtx` file using:

* **Windows Event Viewer**
  `Right-click > Open Saved Log`
* **PowerShell**

  ```powershell
  Get-WinEvent -Path "LogQuest.evtx"
  ```


## 🧠 Questions

1. **Which two accounts were created first on 6/19/2025?**
2. **LogAdmin changed which account password on 6/19/2025?**
3. **Whose account was deleted two times on 6/19/2025?**
4. **How many overall users are present in the system, including deleted users on 6/19/2025?**

---

## 🛠️ Event Log Analysis (Step-by-Step)

To solve this challenge, you need to understand the meaning behind specific **Windows Security Event IDs**:

| Event ID | Description                             |
| -------- | --------------------------------------- |
| **4720** | A user account was created              |
| **4724** | An attempt was made to reset a password |
| **4726** | A user account was deleted              |
| **4738** | A user account was changed              |

### 📌 Step 1: Load the `.evtx` file

* Open `LogQuest.evtx` using **Event Viewer** or tools like **EvtxECmd**, **Chainsaw**, or **Kape**.
* Filter by `Event ID` to isolate relevant events.

---

## 🔍 Answer Walkthrough

### 🔹 Q1: Which two accounts were created first on 6/19/2025?

* **Event ID to use**: `4720`
* Sort the `4720` events by **Time Created**.
* You will find two accounts created early on:

  * `rahim_drag`
  * `Moiz_Don`

✅ **Answer**: `rahim_drag_Moiz_Don`

---

### 🔹 Q2: LogAdmin changed which account password on 6/19/2025?

* **Event ID to use**: `4724`
* Look for entries where the **SubjectUserName** is `LogAdmin`.
* Identify the **TargetUserName**—this is the account whose password was reset.

✅ **Answer**: `Moiz_Don`

---

### 🔹 Q3: Whose account was deleted two times on 6/19/2025?

* **Event ID to use**: `4726`
* Scan for duplicate `TargetUserName` entries.
* `Moiz_Don` appears **twice**, indicating multiple deletions.

✅ **Answer**: `Moiz_Don`

---

### 🔹 Q4: How many overall users are present in the system, including deleted users?

* Use a combination of `4720` (created users), `4726` (deleted), and others like `4722`, `4738`, etc.
* Include:

  * Users who were **created**
  * Users who were **deleted**
  * The **administrator** or any user performing the actions (e.g., `LogAdmin`)

From the logs:

* `rahim_drag`
* `Moiz_Don`
* `LogAdmin`
* `Zaifi`

✅ **Answer**: `4`

---

## 🏁 Flag Format

> Submit the answers in the following format:

```
RDX{<Q1_answer>_<Q2_answer>_<Q3_answer>_<Q4_answer>}
```

### 🧩 Final Flag:

```
RDX{rahim_drag_Moiz_Don_Moiz_Don_Moiz_Don_4}
```

---

## 📚 Summary

| Question              | Answer                   |
| --------------------- | ------------------------ |
| Created accounts      | `rahim_drag`, `Moiz_Don` |
| Password reset target | `Moiz_Don`               |
| Deleted account twice | `Moiz_Don`               |
| Total users           | `4`                      |

---