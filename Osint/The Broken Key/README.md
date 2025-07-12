## **“The Broken Key”**

**Author:** Huzaifa Zia


### 🕵 Intro

An unassuming image leads to a strange domain — a minimal website with barely any content. But something feels off. A closer look at it reveals odd changes and fragmented information hidden in plain sight. Can you trace the trail, reconstruct what was broken, and reveal the identity encrypted deep within this web of clues?

> 🧠 *Objective*: Extract the hidden email from a split PGP public key found via OSINT trails across GitHub and Medium.

---

## 🧷 Step 1: Hidden in the Image

You're provided with an image file: `image.png`. Before diving into websites, examine the file metadata.

Use the `exiftool` or `strings` command to analyze EXIF data for hidden clues.

```bash
exiftool image.png
```

Look closely at the comment fields.

🧩 *Hidden in the metadata comment*, you'll find a GitHub Pages domain:

```
https://zaifi786.github.io/fake_check.github.io/
```

This becomes your entry point to the broader investigation.

---

## 🌐 Step 2: Starting Point – GitHub Pages

Visit the hosted site:

🔗 [https://zaifi786.github.io/fake\_check.github.io/](https://zaifi786.github.io/fake_check.github.io/)

Here, we find a bare page (or something misleadingly simple). A quick source view or hover reveals it’s hosted on GitHub, under the user:

➡ [https://github.com/zaifi786/fake\_check.github.io](https://github.com/zaifi786/fake_check.github.io)

---

## 🔍 Step 3: Digging into GitHub

Head into the repo, and look through the *commit history*.

* Open:
  🔗 [https://github.com/zaifi786/fake\_check.github.io/commits/main](https://github.com/zaifi786/fake_check.github.io/commits/main)

* Check each commit. Eventually, you’ll discover a commit (likely on `index.html`) that includes suspicious text inside the commit *diff* — not normal code.

You’ll find *the first half of a PGP public key block*, starting with:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: Keybase OpenPGP v1.0.0
...
```

📁 *Save this partial key — it’s not usable yet.*

---

## 📄 Step 4: The "About Me" Clue

From the GitHub repo or page, the player finds an “About Me” file or reference pointing to a Medium blog:

🔗 [https://medium.com/@hzia2962](https://medium.com/@hzia2962)

On this profile, there’s a blog post related to PGP, maybe titled *"Why I Use PGP"* or something similar. It appears innocuous, but…

---

## 🧠 Step 5: Hidden Paste

Inside the Medium post, there’s an *embedded link* — a phrase or hyperlink that subtly points to a paste site.

🔗 Embedded paste site: [https://paste.ee/p/uS7H7lTS](https://paste.ee/p/uS7H7lTS)

Open it and voilà: the *second half* of the PGP key block.

---

## 🛠 Step 6: Reconstruct the Full Key

Now, combine both halves of the key:

Save it as a single `.asc` file, like `key.asc`.

```bash
nano key.asc
# paste both blocks fully and save
```

The complete key starts with:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: Keybase OpenPGP v1.0.0
...
```

And ends with:

```
...
=mKWW
-----END PGP PUBLIC KEY BLOCK-----
```

---

## 🔐 Step 7: Import and Inspect with GPG

Import the key using GPG:

```bash
gpg --import key.asc
```

Then, extract key details:

```bash
gpg --list-keys
```

Or more directly:

```bash
gpg --with-colons --import-options show-only --import key.asc
```

---

## 🎯 Final Flag

The final output will contain the *email identity* embedded in the PGP key block. For example:

```
uid           [ultimate] Baba Yaga <notsoez@gmail.com>
```

✅ *Your flag is:*
**`RDX{notsoez@gmail.com}`**

---

## ✅ Challenge Recap

| Step | Action                                                                          |
| ---- | ------------------------------------------------------------------------------- |
| 🟢 1 | Extract EXIF data from `image.png` to find the GitHub Pages link                |
| 🟢 2 | Start at: [GitHub Pages site](https://zaifi786.github.io/fake_check.github.io/) |
| 🟢 3 | Visit the repo → inspect commit history                                         |
| 🟢 4 | Extract first half of PGP key                                                   |
| 🟢 5 | Visit Medium blog: [medium.com/@hzia2962](https://medium.com/@hzia2962)         |
| 🟢 6 | Find paste link: [https://paste.ee/p/uS7H7lTS](https://paste.ee/p/uS7H7lTS)     |
| 🟢 7 | Combine and import key with GPG                                                 |
| 🟢 8 | Extract email identity — *this is the final flag* 🎉                            |

---


